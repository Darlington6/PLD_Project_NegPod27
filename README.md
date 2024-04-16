# PLD_Project_NegPod_27

## Getting Started

To run this project on your local machine, follow these steps:

1. **Clone the Repository**: Use the following command to clone this repository to your PC:
```bash
git clone git@github.com:Darlington6/PLD_Project_NegPod27.git
```

2. **Navigate to the Directory**: Move to the root directory of the cloned repository:
```bash
cd PLD_Project_NegPod27
```

3. **Run the Script**: Execute the `intro.py` script to begin the user journey:
```bash
python3 intro.py
```

Additionally, ensure you set up the database and define the `DB_URI` environment variable in a dotenv file. You can find the database dump in the `\diseases` file. Remember to configure other necessary environment variables as well.

## Usage Guidelines

Once you've started the project, follow these guidelines to interact with the chatbot:

1. Upon running `intro.py`, you'll receive an introductory statement and a list of symptoms.
2. Choose from the listed symptoms by entering their corresponding numbers, separated by commas.
3. Based on your selected symptoms, the chatbot will suggest possible diseases.
4. You'll then receive a follow-up statement providing recommendations based on the identified disease.

Thank you for using our application!
