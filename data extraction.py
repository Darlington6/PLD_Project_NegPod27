import requests
from bs4 import BeautifulSoup
from openai import OpenAI

client = OpenAI(
    api_key='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'
)

origin = 'https://www.nhsinform.scot/illnesses-and-conditions/a-to-z/'
page = requests.get(origin)

soup = BeautifulSoup(page.content, 'html.parser')

diseases = soup.select('.az_list_indivisual > ul > li > a')

for disease in diseases:
    link = disease.get('href')
    disease_page = requests.get(link)
    disease_soup = BeautifulSoup(disease_page.content, 'html.parser')
    whole_page = disease_soup.text

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a medical specialist. You will be provided with text containing information about a medical condition or illness, and your responsibility is to capture different symptoms of that condition of illness, and your response should only be a list of symptoms separated by commas on a single line. Don't add any additional sentences or information.. If no symptoms are present in the text, generate five symptoms that can be seen from patients of that illness."},
            {"role": "user",
             "content": f'{whole_page}'}
        ]
    )
    symptoms = completion.choices[0].message.content.split(',')
    print(disease.text, '\n', symptoms)
    break
