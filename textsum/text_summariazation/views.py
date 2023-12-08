from django.shortcuts import render
from .models import TextGeneration
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from django.http import HttpResponse

def generate_text(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')

        # Ensure that user_input is not empty before proceeding
        if not user_input:
            return HttpResponse('User input cannot be empty.')

        # Load Pegasus model and tokenizer
        model_name = 'google/pegasus-xsum'
        model = PegasusForConditionalGeneration.from_pretrained(model_name)
        tokenizer = PegasusTokenizer.from_pretrained(model_name)

        # Tokenize and generate output
        inputs = tokenizer(user_input, return_tensors='pt', max_length=1024,truncation=True)

        # Adjust min_length and max_length to control the length of the generated summary
        min_length = 100  # Adjust the value as needed
        max_length = 500  # Adjust the value as needed

        summary_ids = model.generate(**inputs, min_length=min_length, max_length=max_length)

        generated_output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        # Save user input and generated output to the database
        TextGeneration.objects.create(user_input=user_input, generated_output=generated_output)

        return render(request, 'output.html',
                      {'user_input': user_input, 'generated_output': generated_output})

    return render(request, 'input.html')
