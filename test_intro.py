import unittest
from intro import (diseases, symptoms, get_input, intro, identify_disease)

class TestDiseaseIdentification(unittest.TestCase):

    def test_diseases(self):
        self.assertIsInstance(diseases, dict)
        self.assertGreater(len(diseases), 0)

    def test_symptoms(self):
        self.assertIsInstance(symptoms, list)
        self.assertGreater(len(symptoms), 0)
