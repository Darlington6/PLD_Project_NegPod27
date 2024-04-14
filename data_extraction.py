import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from app.db.models import Disease, Symptom
from app.db import get_db, init_db


init_db()
db_gen = get_db()
db = next(db_gen)

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
             "content": '''As a medical specialist, your task is to identify and list symptoms from a provided text describing a medical condition or illness. Your response should consist solely of the symptoms, formatted as a comma-separated list on a single line. Ensure that no extra sentences or unrelated details are included. If the text does not explicitly mention any symptoms, provide a list of five common symptoms associated with the condition described.
