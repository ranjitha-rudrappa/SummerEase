# summarization/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import TextSummarization
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from transformers import pipeline, BartTokenizer, BartForConditionalGeneration
from googletrans import Translator
from .forms import SummarizationForm

def generate_summary(request):
    if request.method == 'POST':
        form = SummarizationForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            #
            # # Generate summary using Pegasus model
            # model_name = 'google/pegasus-xsum'
            # model = PegasusForConditionalGeneration.from_pretrained(model_name)
            # tokenizer = PegasusTokenizer.from_pretrained(model_name)
            # inputs = tokenizer(input_text, return_tensors='pt', max_length=1024, truncation=True)
            # summary_ids = model.generate(**inputs)
            # generated_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

            model_name = "facebook/bart-large-cnn"
            tokenizer = BartTokenizer.from_pretrained(model_name)
            model = BartForConditionalGeneration.from_pretrained(model_name)

            # Tokenize input text
            inputs = tokenizer(input_text, return_tensors="pt", max_length=2048, truncation=True)

            # Generate summary
            summary_ids = model.generate(inputs["input_ids"], max_length=500, min_length=200, length_penalty=2.0,
                                         num_beams=4, early_stopping=True)
            generated_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

            # Translate the generated summary if a language is selected
            translation_language = form.cleaned_data['translation_language']
            translated_summary = translate_text(generated_summary, translation_language) if translation_language else None

            # Save input text, generated summary, and translation to the database
            TextSummarization.objects.create(
                input_text=input_text,
                generated_summary=generated_summary,
                translated_summary=translated_summary
            )

            return render(request, 'output.html', {
                'input_text': input_text,
                'generated_summary': generated_summary,
                'translated_summary': translated_summary,
            })

    else:
        form = SummarizationForm()

    return render(request, 'input.html', {'form': form})


def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

