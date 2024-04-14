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
