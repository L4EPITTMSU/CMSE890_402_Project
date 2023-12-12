import unittest
import os
import numpy as np
from contour.py import load_data_contour, plot_contour, plot_save  # contour.py is the actual name of my script


class TestContourPlottingScript(unittest.TestCase):
    def test_load_data_contour_valid(self):
        # Assuming having a valid data file 'data.dat'
        data = load_data_contour('data.dat')
        self.assertIsInstance(data, np.ndarray)

    def test_plot_contour(self):
        # Test contour plotting with a sample data
        data = np.array([[0, 0, 0, 1], [1, 1, 1, 2], [2, 2, 4, 3]])
        try:
            plot_contour(data, 'Test Plot', 'viridis', 'test_contour_plot.png')
        except Exception as e:
            self.fail(f"plot_contour raised an exception: {e}")

    def test_plot_save_contour(self):
        # Test plot save function for contour
        try:
            plot_save('test_contour_plot.png')
            self.assertTrue(os.path.exists('test_contour_plot.png'))
            os.remove('test_contour_plot.png')  # Clean up after test
        except Exception as e:
            self.fail(f"plot_save raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()


