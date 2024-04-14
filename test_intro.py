import unittest
from intro import (diseases, symptoms, get_input, intro, identify_disease)

class TestDiseaseIdentification(unittest.TestCase):

    def test_diseases(self):
        self.assertIsInstance(diseases, dict)
        self.assertGreater(len(diseases), 0)

    def test_symptoms(self):
        self.assertIsInstance(symptoms, list)
        self.assertGreater(len(symptoms), 0)

    def test_get_input(self):
        prompt = "Welcome to Dr. Chat! We help you identify possible diseases you might be suffering from based on the symptoms you are having.\n\nTo get started, please choose the symptoms you have from the list below:\n1. dry cough\n2. fever\n3. runny nose\n4. fatigue\n5. sore throat\n6. muscle aches\n7. cough\n8. shortness of breath\n9. mild fever\n10. loss of taste or smell\n11. sneezing\n12. lack of appetite\n13. headache\n14. vomiting\n15. thirst\n16. diarrhea\n17. irritability\n18. low blood pressure\n19. stomach ache\n20. weakness"
        expected_input = {symptoms[0], symptoms[1], symptoms[2]}
        actual_input = get_input(prompt)
        self.assertIsInstance(actual_input, set)
        self.assertEqual(actual_input, expected_input)
        self.assertIsInstance(list(actual_input)[0], str)
        # self.assertTrue(all(symptom.isdigit() for symptom in actual_input))

    def test_identify_disease(self):
        # Test for a specific case
        user_symptoms = {symptoms[1], symptoms[6], symptoms[2]}
        expected_output = "Influenza"
        self.assertEqual(identify_disease(user_symptoms)[1], expected_output)


if __name__ == '__main__':
    unittest.main()

