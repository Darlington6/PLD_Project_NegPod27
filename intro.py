from sqlalchemy import func
from db.models import Disease, Symptom, disease_symptoms
from db import get_db, init_db

init_db()
db_gen = get_db()
db = get_db()

diseases = {
    'Malaria': {'high fever', 'headache', 'lack of appetite'},
    "Influenza": {"fever", "cough", "sore throat", "muscle aches", "fatigue"},
    "Common Cold": {"runny nose", "sneezing", "sore throat", "cough", "mild fever"},
    "COVID-19": {"fever", "dry cough", "shortness of breath", "fatigue", "loss of taste or smell"},
    "Cholera": {"vomiting", "thirst", "diarrhea", "irritability", "low blood pressure"},
    "Chicken pox": {"headache", "lack of appetite", "sore throat", "stomach ache"},
    "Typhoid Fever": {"fever", "weakness", "stomach pain", "headache", "lack of appetite"}
}

symptoms = db.query(Symptom).all()


def intro():
    numbered_symptoms = ''.join(f"{index}. {symptom.name}\n" for index, symptom in enumerate(symptoms, start=1))
    welcome = f"""Welcome to Dr. Chat! We help you identify possible diseases you might be suffering from based on 
    the symptoms you are having.

To get started, please choose the symptoms you have from the list below:
{numbered_symptoms}"""
    symptom = get_input(welcome)
    message = identify_disease(symptom)
    print(message)


def get_disease_symptom_counts(db_session, symptom_ids):
    query = (
        db_session.query(
            disease_symptoms.c.disease_id,
            func.count(disease_symptoms.c.symptom_id)
        )
        .filter(disease_symptoms.c.symptom_id.in_(symptom_ids))
        .group_by(disease_symptoms.c.disease_id)
        .order_by(func.count(disease_symptoms.c.symptom_id).desc())
    )
    results = query.all()
    return results


def identify_disease(user_symptoms):
    diseases_counts = get_disease_symptom_counts(db, user_symptoms)
    print(diseases_counts)
    message = f'''
It is likely that you have {diseases_counts[0].name} disease.

Please know that this is not a professional doctor, so you should not rely solely on this information. This 
application was developed for educational purposes only.

Thank you for using our application.'''

    return message


# User Validation
def get_input(prompt):
    valid = False
    user_input = {}
    print(prompt)
    while not valid:
        try:
            user_input = input('Your response should be symptom numbers separated by comma: ')
            user_input = [int(i) for i in user_input.split(",")]
            user_input = [symptoms[i - 1] for i in user_input]
            user_input = set(user_input)
            valid = True
            break
        except:
            print('Please enter valid inputs and try again')
            pass
    return user_input


if __name__ == "__main__":
    intro()
