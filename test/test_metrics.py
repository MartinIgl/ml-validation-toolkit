import unittest
import sys
import os

# Ajuste de ruta
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ml_validation.metrics import calculate_accuracy, calculate_precision, calculate_recall, calculate_f1

class TestMetrics(unittest.TestCase):  # <--- Necesario para unittest

    def test_calculate_accuracy(self):
        y_true = [1, 0, 1, 1]
        y_pred = [1, 0, 0, 1]
        self.assertEqual(calculate_accuracy(y_true, y_pred), 0.75)

    def test_calculate_precision(self):
        y_true = [1, 0, 1, 1]
        y_pred = [1, 0, 0, 1]
        self.assertEqual(calculate_precision(y_true, y_pred), 1.0)

    def test_calculate_recall(self):
        y_true = [1, 0, 1, 1]
        y_pred = [1, 0, 0, 1]
        self.assertAlmostEqual(calculate_recall(y_true, y_pred), 2/3)

    def test_calculate_f1(self):
        y_true = [1, 0, 1, 1]
        y_pred = [1, 0, 0, 1]
        self.assertAlmostEqual(calculate_f1(y_true, y_pred), 0.8)

    def test_different_lengths_accuracy(self):
        with self.assertRaises(ValueError):
            calculate_accuracy([1, 0, 1], [1, 0])
            
    # Repetir bloque with self.assertRaises... para las otras funciones

if __name__ == '__main__':
    unittest.main()