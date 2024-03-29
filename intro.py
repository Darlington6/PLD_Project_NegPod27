def intro():
    welcome = f"""
Welcome to Dr. Chat! We help you identify possible diseases you might be suffering from based on the symptoms you are having.
To get started, please choose the symptoms you have from the list below:
{''.join(f"{index}. {symptom}\n" for index, symptom in enumerate(symptoms, start=1))}
Your response should be symptom numbers separated by comma: 
"""
    symptom = input(welcome)
    symptom = [int(i) for i in symptom.split(",")]
    print(f"You have selected {symptom}")

if __name__ == "__main__":
    intro()


diseases ={
   'malaria':{'high fever', 'headache', 'lack of appetite' },
    "Influenza": {"fever", "cough", "sore throat", "muscle aches", "fatigue"},
    "Common Cold": {"runny nose", "sneezing", "sore throat", "cough", "mild fever"},
    "COVID-19": {"fever", "dry cough", "shortness of breath", "fatigue", "loss of taste or smell"}
}

symptoms ={'dry cough', 'fever', 'runny nose', 'fatigue', 'sore throat', 'muscle aches', 'cough', 'shortness of breath', 'mild fever', 'loss of taste or smell', 'sneezing', 'lack of appetite', 'headache'}

def identify_disease(user_symptoms):
    score =0
    disease = disease['malaria']
    for key in diseases.keys():
        Intersection = diseases[key].intersection(user_symptoms)
        if new_Score > score:
            disease = key
            score =  new_Score
    message = f'''it is likely that you have {disease} disease. Please know that this is not a professional doctor, so you should not rely solely on this information. This application was developed for educational purposes only. Thank you for using our application'''

	return message
