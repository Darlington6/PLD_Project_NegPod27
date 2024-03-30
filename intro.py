diseases = {
    'Malaria': {'high fever', 'headache', 'lack of appetite'},
    "Influenza": {"fever", "cough", "sore throat", "muscle aches", "fatigue"},
    "Common Cold": {"runny nose", "sneezing", "sore throat", "cough", "mild fever"},
    "COVID-19": {"fever", "dry cough", "shortness of breath", "fatigue", "loss of taste or smell"},
    "Cholera": {"vomiting", "thirst", "diarrhea", "irritability", "low blood pressure"},
    "Chicken pox": {"headache", "lost of appetite", "sore throat", "stomach ache"}
}

symptoms = ['dry cough', 'fever', 'runny nose', 'fatigue', 'sore throat', 'muscle aches', 'cough',
            'shortness of breath', 'mild fever', 'loss of taste or smell', 'sneezing', 'lack of appetite', 'headache']


def intro():
    numbered_symptoms = ''.join(f"{index}. {symptom}\n" for index, symptom in enumerate(symptoms, start=1))
    welcome = f"""Welcome to Dr. Chat! We help you identify possible diseases you might be suffering from based on the symptoms you are having.

To get started, please choose the symptoms you have from the list below:
{numbered_symptoms}"""
    symptom = get_input(welcome)
    message = identify_disease(symptom)
    print(message)


def identify_disease(user_symptoms):
    score = 0
    disease = diseases['malaria']
    for key in diseases.keys():
        intersection = diseases[key].intersection(user_symptoms)
        new_score = len(intersection)
        if new_score > score:
            disease = key
            score = new_score
    message = f'''
It is likely that you have {disease} disease.

Please know that this is not a professional doctor, so you should not rely solely on this information. This application was developed for educational purposes only.

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
