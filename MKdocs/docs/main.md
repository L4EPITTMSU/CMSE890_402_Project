::: functions.main



#Main Function

The main function serves as the entry point for a script that loads data from two files, creates a plot, and saves it to a specified location.



## Parameters

- input_file1 (str): The path to the first input file from which data will be loaded.

- input_file2 (str): The path to the second input file from which data will be loaded.

- output_file (str): The path where the generated plot will be saved.

## Returns

- None: This function does not return a value. It orchestrates the process of data loading, plotting, and saving the plot.

Usage

The function is intended to be used as the main executable of a Python script. It can be invoked with command line arguments representing the file paths.


## Example


if __name__ == "__main__":

    input_file1 = sys.argv[1]

    input_file2 = sys.argv[2]

    output_file = sys.argv[3]

    main(input_file1, input_file2, output_file)
