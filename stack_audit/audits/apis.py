import json

from audits.forms import SmartContractForm
import openai
import requests
from django.conf import settings


openai.api_key = settings.OPENAI_API_KEY

def get_source_from_hiro_api(form: SmartContractForm):
    url = f"https://api.mainnet.hiro.so/extended/v1/contract/{form.contract}"

    payload = {}
    headers = {
        'Accept': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.load(response.content)["source_code"]


def get_response_from_openai(source: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Explain this clarity contract in lay-man terms:{source}"}
        ]
    )
    return response['choices'][0]['message']['content']

print('hell')