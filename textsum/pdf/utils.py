# # pdf_summarizer/utils.py
#
# from PyPDF2 import PdfReader
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer
#
#
# def summarize_pdf(pdf_path, pages_to_summarize):
#     pdf_reader = PdfReader(pdf_path)
#     summarized_text = ''
#
#     for page_num in pages_to_summarize.split(','):
#         try:
#             page_num = int(page_num.strip())
#             if 1 <= page_num <= len(pdf_reader.pages):
#                 page_text = pdf_reader.pages[page_num - 1].extract_text()
#                 parser = PlaintextParser.from_string(page_text, Tokenizer('english'))
#
#                 # Calculate sentences_count based on text length (adjust as needed)
#                 sentences_count = max(1, min(len(page_text.split('.')), 10))
#
#                 summarizer = LsaSummarizer()
#                 summary = summarizer(parser.document, sentences_count=sentences_count)
#                 summarized_text += ' '.join(map(str, summary)) + '\n\n'
#         except ValueError:
#             pass
#
#     return summarized_text.strip()

# pdf_summarizer/utils.py

# from PyPDF2 import PdfReader
# from transformers import BartForConditionalGeneration, BartTokenizer
# import torch
#
# def summarize_pdf(pdf_path, pages_to_summarize):
#     pdf_reader = PdfReader(pdf_path)
#     summarized_text = ''
#
#     # Load the BART model and tokenizer
#     model_name = 'facebook/bart-large-cnn'
#     tokenizer = BartTokenizer.from_pretrained(model_name)
#     model = BartForConditionalGeneration.from_pretrained(model_name)
#
#     for page_num in pages_to_summarize.split(','):
#         try:
#             page_num = int(page_num.strip())
#             if 1 <= page_num <= len(pdf_reader.pages):
#                 page_text = pdf_reader.pages[page_num - 1].extract_text()
#
#                 # Tokenize and generate abstractive summary
#                 inputs = tokenizer(page_text, return_tensors="pt", max_length=1024, truncation=True)
#                 summary_ids = model.generate(inputs['input_ids'], max_length=500, num_beams=4, length_penalty=5.0,
#                                              early_stopping=True)
#                 summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#
#                 summarized_text += summary + '\n\n'
#         except ValueError:
#             pass
#
#     return summarized_text.strip()

import requests

def summarize_pdf_api(data, max_length, api_url, api_token):
    headers = {"Authorization": f"Bearer {api_token}"}

    # Make API call for summarization
    payload = {
        "inputs": data,
        "parameters": {"min_length": max_length // 4, "max_length": max_length},
    }
    response = requests.post(api_url, headers=headers, json=payload)
    result = response.json()

    return result["summary_text"]



