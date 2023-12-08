# text_checker/views.py

from django.shortcuts import render
from .forms import TextCheckForm
from .utils import check_text_with_language_tool


def check_text(request):
    if request.method == 'POST':
        form = TextCheckForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']

            # Check text using LanguageTool API
            response_json = check_text_with_language_tool(input_text)

            # Extract information about errors
            errors = response_json.get('matches', [])

            # Underline errors in the input text
            for error in errors:
                error_length = error['length']
                start = error['offset']
                end = start + error_length
                input_text = input_text[:start] + f'<u>{input_text[start:end]}</u>' + input_text[end:]

            context = {'form': form, 'input_text': input_text, 'errors': errors}
            return render(request, 'text.html', context)
    else:
        form = TextCheckForm()

    return render(request, 'text.html', {'form': form})
