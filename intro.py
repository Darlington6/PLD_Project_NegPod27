from sqlalchemy import text
from sqlalchemy.orm import Session
from db.models import Disease, Symptom
from db import get_db, init_db
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

init_db()
db_gen = get_db()
db = next(db_gen)

client = OpenAI(
    api_key=os.getenv("OAI_API_KEY")
)

symptoms = db.query(Symptom).all()


def intro():
    numbered_symptoms = ''.join(f"{index}. {symptom.name}\n" for index, symptom in enumerate(symptoms, start=1))
    welcome = f"""Welcome to Dr. Chat! We help you identify possible diseases you might be suffering from based on 
    the symptoms you are having.

To get started, please choose the symptoms you have from the list below:
{numbered_symptoms}"""
    symptom = get_input(welcome)
    message = identify_disease(symptom)

    print('\n\n')
    print(message)


def get_disease_symptom_counts(db_session: Session, symptom_ids):
    query = text("""SELECT ds.disease_id, COUNT(ds.symptom_id) AS symptom_count
FROM disease_symptoms ds
WHERE ds.symptom_id = ANY (:symptom_ids)
GROUP BY ds.disease_id
ORDER BY symptom_count DESC;
""")
    results = db_session.execute(query,  {"symptom_ids": symptom_ids}).all()
    return results


def identify_disease(user_symptoms):
    symptom_ids = [symptom.id for symptom in user_symptoms]
    diseases_counts = get_disease_symptom_counts(db, symptom_ids)
    highest_count = diseases_counts[0]

    disease = db.query(Disease).filter_by(id=highest_count.disease_id).first().name
    message = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system",
             "content": f'''You are a medical specialist. Based on the data provided, the patient has exhibited the 
                 following symptoms: "{",".join([symptom.name for symptom in user_symptoms])}". It is likely that 
                 they are suffering from {disease}. Your task is to provide inform them of their condition, offer 
                 personalized advice and recommended actions to help reduce the severity of the disease or aid in 
                 recovery. Include in your response:

    Suggested lifestyle changes. Dietary modifications. Precautionary steps to take. Indications for when to seek 
    immediate medical attention. Conclude your recommendations with a disclaimer: "Please consult with a physician to 
    obtain a formal diagnosis and a tailored treatment plan. The advice provided here is for informational purposes only 
    and is not a substitute for professional medical consultation. We are not liable for any harm that may arise from 
    following these recommendations without proper medical supervision.'''},
            {"role": "user",
             "content": f'The user has shown these symptoms "{",".join([symptom.name for symptom in user_symptoms])}" '
                        f'and we have found that they are likely to have this condition {disease}.'}
        ]
    )

    return message.choices[0].message.content


# User Validation
def get_input(prompt):
    valid = False
    syms = []
    print(prompt)
    while not valid:
        try:
            user_input = input('Your response should be symptom numbers separated by comma: ')
            user_input = [int(i) for i in user_input.split(",")]
            user_input = set(user_input)
            for _id in user_input:
                sym = db.query(Symptom).filter_by(id=_id).first()
                if not sym:
                    raise ValueError(f"No symptom with id {_id}")
                syms.append(sym)
            valid = True
            break
        except:
            print('Please enter valid inputs and try again')
            pass
    return syms


if __name__ == "__main__":
    intro()
