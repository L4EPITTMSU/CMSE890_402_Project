import unittest
import os
import numpy as np
from plot_tke.py import load_data, plot_data, plot_save  # plot_tke.py is the actual name of my script

class TestPlottingScript(unittest.TestCase):
    def test_load_data_valid(self):
        # Assuming a valid data file 'data.dat'
        data = load_data('data.dat')
        self.assertIsInstance(data, np.ndarray)
        
    def test_plot_data(self):
        # Simple test for plotting function
        x = np.array([0, 1, 2, 3, 4])
        y = np.array([0, 1, 4, 9, 16])
        try:
            plot_data(x, y, 'test', 'r')
        except Exception as e:
            self.fail(f"plot_data raised an exception: {e}")
            
    def test_plot_save(self):
        # Test plot save function
        try:
            plot_save('test_plot.png')
            self.assertTrue(os.path.exists('test_plot.png'))
            os.remove('test_plot.png')  # Clean up after test
        except Exception as e:
            self.fail(f"plot_save raised an exception: {e}")

if __name__ == '__main__':

    unittest.main()


