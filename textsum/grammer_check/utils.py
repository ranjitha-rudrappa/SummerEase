# text_checker/utils.py

import requests


def check_text_with_language_tool(text):
    language_tool_api_url = "https://languagetool.org/api/v2/check"
    data = {"text": text, "language": "en-US"}

    response = requests.post(language_tool_api_url, data=data)
    return response.json()
