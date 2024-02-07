# from django.http import HttpResponse
# from django.shortcuts import render
# from text.models import TextSummary
# from text.models import PdfDocument
# def history(request):
#     history = TextSummary.objects.filter(user1=request.session.get('user_id'))
#     print(history[0].input_text)
#     # return HttpResponse("<h1>dfgergv</h1>")
#     # history = PdfDocument.objects.filter(user1=request.session.get('user_id'))
#     return render(request, 'history.html', {'history': history}) 
#     # return TextSummary(history[0].input_text)

# from itertools import chain
# from django.shortcuts import render
# from text.models import TextSummary
# from pdf_to_summary.models import PdfDocument

# def history(request):
#     text_summaries = TextSummary.objects.filter(user1=request.session.get('user_id'))
#     pdf_documents = PdfDocument.objects.filter(user1=request.session.get('user_id'))
    
    # Combine both querysets into a single iterable
    # combined_history = chain(text_summaries, pdf_documents)
    # print(combined_h istory)
    # return render(request, 'history.html', {'history': combined_history})


# from django.shortcuts import render
# from text.models import TextSummary
# from pdf_to_summary.models import PdfDocument

# def history(request):
#     # Retrieve TextSummary objects
#     text_summaries = TextSummary.objects.filter(user1=request.session.get('user_id'))

#     # Retrieve PdfDocument objects
#     pdf_documents = PdfDocument.objects.filter(user1=request.session.get('user_id'))

#     # Combine both querysets into a single list
#     history_list = list(text_summaries) + list(pdf_documents)

#     # Print all retrieved history
#     for item in history_list:
#         print(item)  # Adjust this based on the fields you want to print

#     # Return the history to a template for rendering if needed
#     return render(request, 'history.html', {'history': history_list})



from django.shortcuts import render
from text.models import TextSummary
from pdf_to_summary.models import PdfDocument
from grammar_correct.models import GrammarCheck


def history(request):
    # Retrieve TextSummary objects
    text_summaries = TextSummary.objects.filter(user1=request.session.get('user_id'))

    # Retrieve PdfDocument objects
    pdf_documents = PdfDocument.objects.filter(user1=request.session.get('user_id'))

    # Return both types of objects to the template
    grammars = GrammarCheck.objects.filter(user1=request.session.get('user_id'))

    return render(request, 'history.html', {'text_summaries': text_summaries, 'pdf_documents': pdf_documents, 'grammars':grammars})
