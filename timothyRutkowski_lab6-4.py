# Timothy Rutkowski 04/11/2024 timothyRutkowski_lab6-4.py

# This program will average the numbers from the exceptionNumbers.txt file.
# If non-numeric data is detected, the program will notify the user of the error
# but continue to average the readable numeric data.
# If the file is not readable, the program will display an IOError message.

# The Main Function of the program
def main():
    try:
        # Open the file for reading
        num_file = open('exceptionNumbers.txt', 'r')

        # List to store numeric data from the file
        num_list = []
        for line in num_file:
            # Attempt to convert each line to a float and add to numbers list
            try:
                num_value = float(line.strip())
                num_list.append(num_value)
            except ValueError:
                # Value error for non-numeric data
                print(f"Error: Non-numeric data '{line.strip()}' found in the file.")
        
        # Close the file
        num_file.close()

        if num_list:
            # Calculate and display the average of numbers in file
            average = calc_average(num_list)
            print(f'Average of numbers in the file: {average}')

    except IOError:
        # Display IOError if file is not readable
        print('Error reading the file.')
        
# Function to calculate the average of the list of numbers
def calc_average(num_list):
    total = sum(num_list)
    return total / len(num_list)

# Call the Main Function
if __name__ == '__main__':
    main()
