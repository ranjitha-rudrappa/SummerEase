# pdf_summarizer/views.py

from django.shortcuts import render
from .forms import PdfForm
from .models import PdfDocument
from .utils import summarize_pdf


def summarize(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            pages_to_summarize = form.cleaned_data['pages_to_summarize']

            # Save the PDF file to the server
            pdf_document = PdfDocument(pdf_file=pdf_file)
            pdf_document.save()

            # Get the path to the saved PDF file
            pdf_path = pdf_document.pdf_file.path

            # Summarize the specified pages
            summarized_text = summarize_pdf(pdf_path, pages_to_summarize)

            # Update the PdfDocument model with the summarized text
            pdf_document.summarized_text = summarized_text
            pdf_document.pages_to_summarize = pages_to_summarize
            pdf_document.save()

            return render(request, 'summary.html', {'pdf_document': pdf_document})

    else:
        form = PdfForm()

    return render(request, 'input.html', {'form': form})
