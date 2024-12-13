#Adventofcode2401


#ownerproof-4802690-1734126430-4bc67d45e89d

#Need to compare lists from csv file.  Taking the smallest number in collem a and finding the distance from the smallest number in column b and then doing the same thing for each number going up , afterwards add all the answer together


import csv
import math
from collections import Counter


'''def historical_data(csv_file):  #Read the CSV file
    column_a = []
    column_b = []

#Read CSV File
    with open(csv_file, mode ='r') as file:
     reader = csv.DictReader(file)
     for row in reader:
        #Appends values to the lists to ensure they are integers
        column_a.append(int(row['A']))
        column_b.append(int(row['B']))

#sort the columns
    a_sorted = sorted(column_a)
    b_sorted = sorted(column_b)

#calculate the differences and sum them
    total_difference= 0
    for a, b in zip(a_sorted, b_sorted):
    total_difference += abs(a - b)
    return total_difference


'''



def calculate_differences(csv_file):
    column_a = []
    column_b = []

    # Read the CSV file
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Append values to the lists, converting them to integers
            column_a.append(int(row['A']))
            column_b.append(int(row['B']))

    # Sort the columns
    '''a_sorted = sorted(column_a)
    b_sorted = sorted(column_b)

    # Calculate the differences and sum them
    total_difference = 0
    for a, b in zip(a_sorted, b_sorted):
        difference = abs(a - b)
        total_difference += difference

    return total_difference '''
    #Count Occurances
    count_b = Counter(column_b)

    total_matches = 0
    for number in set(column_a):
        if number in count_b:
            total_matches += number * count_b[number]
    return total_matches

# Example usage
if __name__ == "__main__":
    csv_file = 'adc1.csv'  # Replace with your CSV file path
    result = calculate_differences(csv_file)
    print(f"The total sum of differences is: {result}")