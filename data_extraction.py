import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from app.db.models import Disease, Symptom
from app.db import get_db, init_db


init_db()
db_gen = get_db()
db = next(db_gen)