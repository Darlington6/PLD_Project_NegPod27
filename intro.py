def intro():
    welcome = """
Welcome to Dr. Chat! We help you identify possible diseases you might be suffering from based on the symptoms you are having.
To get started, please choose the symptoms you have from the list below:
1. A
2. B
Your response should be symptom numbers separated by comma: 
"""
    symptom = input(welcome)
    symptom = [int(i) for i in symptom.split(",")]
    print(f"You have selected {symptom}")

if __name__ == "__main__":
    intro()

