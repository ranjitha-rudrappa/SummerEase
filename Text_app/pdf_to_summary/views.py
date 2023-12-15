# views.py
import requests
from PyPDF2 import PdfReader
from django.shortcuts import render
from .forms import PdfForm
from .models import PdfDocument


def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text


def summarize_pdf_api(pdf_path, pages_to_summarize, api_url, api_token):
    #API call for summarization
    headers = {"Authorization": f"Bearer {api_token}"}
    data = extract_text_from_pdf(pdf_path)
    max_length = 700 # Adjust as needed

    response = requests.post(api_url, headers=headers, json={
        "inputs": data,
        "parameters": {"min_length": max_length // 4, "max_length": max_length},
    })

    if response.status_code == 200:
        return response.json()[0]["summary_text"]
    else:
        raise Exception(f"Error in API response: {response.text}")


def summarize(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            pages_to_summarize = form.cleaned_data['pages_to_summarize']

            try:
                #API call for summarization
                api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
                api_token = "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"

                # Save the PDF file and update the PdfDocument model
                pdf_document = PdfDocument(pdf_file=pdf_file, pages_to_summarize=pages_to_summarize)
                pdf_document.save()

                pdf_path = pdf_document.pdf_file.path

                # Make API call for summarization
                summarized_text = summarize_pdf_api(pdf_path, pages_to_summarize, api_url, api_token)

                pdf_document.summarized_text = summarized_text
                pdf_document.save()

                return render(request, 'summary.html', {'pdf_document': pdf_document})

            except Exception as e:
                # Handle exceptions, e.g., API call failure, invalid PDF, etc.
                error_message = f"Error processing PDF: {str(e)}"
                return render(request, 'input.html', {'form': form, 'error_message': error_message})

    else:
        form = PdfForm()

    return render(request, 'input.html', {'form': form})
