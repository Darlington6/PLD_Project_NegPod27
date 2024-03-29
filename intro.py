diseases ={
   'malaria':{'high fever', 'headache', 'lack of appetite' },
    "Influenza": {"fever", "cough", "sore throat", "muscle aches", "fatigue"},
    "Common Cold": {"runny nose", "sneezing", "sore throat", "cough", "mild fever"},
    "COVID-19": {"fever", "dry cough", "shortness of breath", "fatigue", "loss of taste or smell"}
}

symptoms =['dry cough', 'fever', 'runny nose', 'fatigue', 'sore throat', 'muscle aches', 'cough',
           'shortness of breath', 'mild fever', 'loss of taste or smell', 'sneezing', 'lack of appetite', 'headache']


def intro():
    numbered_symptoms = ''.join(f"{index}. {symptom}\n" for index, symptom in enumerate(symptoms, start=1))
    welcome = f"""Welcome to Dr. Chat! We help you identify possible diseases you might be suffering from based on the symptoms you are having.

To get started, please choose the symptoms you have from the list below:
{numbered_symptoms}
Your response should be symptom numbers separated by comma: """
    symptom = input(welcome)
    symptom = [int(i) for i in symptom.split(",")]
    symptom = [symptoms[i-1] for i in symptom]
    symptom = set(symptom)
    message = identify_disease(symptom)
    print(message)


def identify_disease(user_symptoms):
    score =0
    disease = diseases['malaria']
    for key in diseases.keys():
        intersection = diseases[key].intersection(user_symptoms)
        new_score = len(intersection)
        if new_score > score:
            disease = key
            score =  new_score
    message = f'''it is likely that you have {disease} disease.

Please know that this is not a professional doctor, so you should not rely solely on this information. This application was developed for educational purposes only.

Thank you for using our application.'''

    return message


if __name__ == "__main__":
    intro()