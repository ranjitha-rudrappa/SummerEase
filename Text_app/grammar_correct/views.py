# views.py
from django.shortcuts import render
from language_tool_python import LanguageTool


def grammar_check(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')

        # Initialize LanguageTool
        tool = LanguageTool('en-US')

        # Perform grammar check
        matches = tool.check(input_text)

        # Get corrected text
        corrected_text = tool.correct(input_text)

        context = {
            'input_text': input_text,
            'matches': matches,
            'corrected_text': corrected_text,
        }

        return render(request, 'result.html', context)

    return render(request, 'form.html')
