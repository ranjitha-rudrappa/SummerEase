# # utils.py
#
# from PyPDF2 import PdfReader
# import requests
#
# def extract_text_from_pdf(pdf_file):
#     with open(pdf_file, 'rb') as file:
#         pdf_reader = PdfReader(file)
#         text = ''
#         for page_num in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_num]
#             text += page.extract_text()
#         return text
#
# def summarize_pdf_api(pdf_path, pages_to_summarize, api_url, api_token):
#     text = extract_text_from_pdf(pdf_path)
#
#     # Adjust the API call as needed
#     headers = {"Authorization": f"Bearer {api_token}"}
#     max_length = 700  # Adjust as needed
#
#     response = requests.post(api_url, headers=headers, json={
#         "inputs": text,
#         "parameters": {"min_length": max_length // 4, "max_length": max_length},
#     })
#
#     if response.status_code == 200:
#         return response.json()[0]["summary_text"]
#     else:
#         raise Exception(f"Error in API response: {response.text}")
