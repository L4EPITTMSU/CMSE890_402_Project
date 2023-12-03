# plot_tke.py
# import sys
# import numpy as np
# import matplotlib.pyplot as plt

# def load_data(filepath):
    # return np.loadtxt(filepath)

# def plot_data(x, y, output_path):
    # plt.plot(x, y, 'm', markersize=12, label='case 1', linewidth=1)
    # plt.xlabel('X', fontsize=10, fontweight='bold')
    # plt.ylabel('TKE', fontsize=10, fontweight='bold')
    # plt.xlim(0.0,4.0*np.pi)
    # plt.ylim(0,0.5)
    # plt.legend()
    # plt.title('t= 5.0', fontsize=10, fontweight='bold')
    # plt.savefig(output_path)

# def main(input_file, output_file):
    # data = load_data(input_file)
    # x = data[:,0]
    # y = data[:,1]
    # plot_data(x, y, output_file)

# if __name__ == "__main__":
    # input_file = sys.argv[1]
    # output_file = sys.argv[2]
    # main(input_file, output_file)
    
       
import sys
import numpy as np
import matplotlib.pyplot as plt

def load_data(filepath):
    return np.loadtxt(filepath)
    

def plot_data(x, y, label, color):
    plt.plot(x, y, color, markersize=12, label=label, linewidth=1)
    

def main(input_file1, input_file2,output_file):
    # Load data from both files
    data1 = load_data(input_file1)
    data2 = load_data(input_file2)

    # Plot data from the first file
    plot_data(data1[:, 0], data1[:, 1], 'case 1', 'm')

    # Plot data from the second file
    plot_data(data2[:, 0], data2[:, 1], 'case 2', 'b')
    
    
    # Setting the labels and title
    plt.xlabel('X', fontsize=10, fontweight='bold')
    plt.ylabel('TKE', fontsize=10, fontweight='bold')
    plt.xlim(0, 4*np.pi)
    plt.ylim(0,3)
    plt.legend()
    plt.title('t= 5.0', fontsize=10, fontweight='bold')

    # Save the plot
    plt.savefig(output_file)

if __name__ == "__main__":
    input_file1 = sys.argv[1]
    input_file2 = sys.argv[2]
    output_file = sys.argv[3]
    main(input_file1, input_file2,output_file)
