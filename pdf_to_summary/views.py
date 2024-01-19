# views.py
import pyttsx3
import requests
from PyPDF2 import PdfReader
from django.http import JsonResponse
from django.shortcuts import render
from googletrans import Translator

# from .forms import PdfForm
from .models import PdfDocument


# def extract_text_from_pdf(pdf_file):
#     with open(pdf_file, 'rb') as file:
#         pdf_reader = PdfReader(file)
#         text = ''
#         for page_num in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_num]
#             text += page.extract_text()
#         return text
#
#
# def summarize_pdf_api(pdf_path, pages_to_summarize, api_url, api_token):
#     #API call for summarization
#     headers = {"Authorization": f"Bearer {api_token}"}
#     data = extract_text_from_pdf(pdf_path)
#     max_length = 700 # Adjust as needed
#
#     response = requests.post(api_url, headers=headers, json={
#         "inputs": data,
#         "parameters": {"min_length": max_length // 4, "max_length": max_length},
#     })
#
#     if response.status_code == 200:
#         return response.json()[0]["summary_text"]
#     else:
#         raise Exception(f"Error in API response: {response.text}")

def summarize_pdf_api(pdf_path, pages_to_summarize, api_url, api_token):
    # API call for summarization
    headers = {"Authorization": f"Bearer {api_token}"}

    # Extract text only from the specified page
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = pdf_reader.pages[int(pages_to_summarize) - 1].extract_text()

    max_length = 700  # Adjust as needed

    response = requests.post(api_url, headers=headers, json={
        "inputs": text,
        "parameters": {"min_length": max_length // 4, "max_length": max_length},
    })

    if response.status_code == 200:
        return response.json()[0]["summary_text"]
    else:
        raise Exception(f"Error in API response: {response.text}")

# views.py

from django.http import JsonResponse
from django.shortcuts import render
from .models import PdfDocument
# from .utils import summarize_pdf_api

def summarize(request):
    if request.method == 'POST' and request.FILES.get('file-input'):
        pdf_file = request.FILES['file-input']
        pages_to_summarize = request.POST.get('maxL', None)

        try:
            api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
            api_token = "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"

            pdf_document = PdfDocument(pdf_file=pdf_file, pages_to_summarize=pages_to_summarize)
            pdf_document.save()

            pdf_path = pdf_document.pdf_file.path

            summarized_text = summarize_pdf_api(pdf_path, pages_to_summarize, api_url, api_token)

            pdf_document.summarized_text = summarized_text
            pdf_document.save()
            request.session['text_for_speech'] = summarized_text
            request.session['summarized_text'] = summarized_text

            return render(request, 'input.html', {'result': summarized_text})

        except Exception as e:
            error_message = f"Error processing PDF: {str(e)}"
            return render(request, 'input.html', {'error_message': error_message})

    return render(request, 'input.html')

def texttospeech1(request):
    rate = 150
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    text = request.session.get('text_for_speech', '')
    # Use the engine to speak the given text audio
    engine.say(text)
    # Wait for the speech to finish
    engine.runAndWait()
    return render(request, 'input.html', {"result": text})


def language_translator1(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language, src='en')
    return translation.text

def translate_summary1(request):
    # Ensure 'summarized_text' is present in the session
    summarized_text = request.session.get('summarized_text', '')

    if summarized_text:
        # Get the target language from the request parameters or use 'hi' as default
        target_language = request.GET.get('target_language', 'hi')

        # If summarized_text is not None, proceed with translation
        translated_text = language_translator1(summarized_text, target_language)

        # Set the translated text to a new session key
        request.session['translated_text'] = translated_text

        return render(request, 'input.html', {"input": summarized_text, "result": translated_text})
    else:
        # If 'summarized_text' is not present, handle accordingly
        return render(request, 'input.html', {"result": "Summarized text not found in session"})




# def summarize(request):
#     if request.method == 'POST':
#         form = PdfForm(request.POST, request.FILES)
#         if form.is_valid():
#             pdf_file = form.cleaned_data['pdf_file']
#             pages_to_summarize = form.cleaned_data['pages_to_summarize']
#
#             try:
#                 #API call for summarization
#                 api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
#                 api_token = "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"
#
#                 # Save the PDF file and update the PdfDocument model
#                 pdf_document = PdfDocument(pdf_file=pdf_file, pages_to_summarize=pages_to_summarize)
#                 pdf_document.save()
#
#                 pdf_path = pdf_document.pdf_file.path
#
#                 # Make API call for summarization
#                 summarized_text = summarize_pdf_api(pdf_path, pages_to_summarize, api_url, api_token)
#
#                 pdf_document.summarized_text = summarized_text
#                 pdf_document.save()
#
#                 return render(request, 'input.html')
#
#             except Exception as e:
#                 # Handle exceptions, e.g., API call failure, invalid PDF, etc.
#                 error_message = f"Error processing PDF: {str(e)}"
#                 return render(request, 'input.html', {'form': form, 'error_message': error_message})
#
#     else:
#         form = PdfForm()
#
#     return render(request, 'input.html', {'result': form})
