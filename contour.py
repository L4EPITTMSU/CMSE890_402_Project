import sys
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import pandas as pd
    
def load_data_contour(filepath):
    try:
        # Load data using Pandas
        df = pd.read_csv(filepath, sep="\s+", skiprows=3, names=['x', 'y', 'z', 'f'])
#        df = pd.read_csv(filepath, delimiter=' ', skiprows=3, usecols=[0,1,3],names=['X', 'Y', 'Z'])
        return df.to_numpy()
    except ValueError as e:
        print("Error processing file:", filepath)
        print(e)
        raise
        
               
def plot_contour(data, title, cmap, output_file):
    # Extracting x, y, and z values
    x, y, z = data[:, 0], data[:, 1], data[:, 3]
    
    # Prepare grid
    xi = np.linspace(0, 6*np.pi, 500)
    yi = np.linspace(0, 2*np.pi, 500)
    xi, yi = np.meshgrid(xi, yi)

    # Interpolate
    zi = griddata((x, y), z, (xi, yi), method='cubic')
    
    # Generate a contour plot
    plt.figure(figsize=(10, 5))
    contour = plt.contourf(xi, yi, zi, 100, cmap=cmap)

    # Generate a colorbar and add a title
    plt.colorbar(contour)
    plt.title(title, fontsize=10, fontweight='bold')
    
    plot_save(output_file)

def plot_save(output_file):
    # Save the plot
    plt.savefig(output_file, dpi=300, format='png', bbox_inches='tight')
    plt.close()

def main(input_file1, input_file2, output_file1, output_file2):
    # Load data from both files
    data1 = load_data_contour(input_file1)
    data2 = load_data_contour(input_file2)

    # Plot data from the other files
    plot_contour(data1, 'non-reactive', 'gist_rainbow', output_file1)
    plot_contour(data2, 'reactive', 'hsv', output_file2)
    

if __name__ == "__main__":
    input_file1 = sys.argv[1]
    input_file2 = sys.argv[2]
    output_file1 = sys.argv[3]
    output_file2 = sys.argv[4]
    main(input_file1,input_file2, output_file1,output_file2)
