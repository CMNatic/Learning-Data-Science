import csv


# Open original file
with open('datasets/original_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file) # expects values to be seperated by commas, etc

# Print for each line in csv file to console
#    for line in csv_reader:
#        print(line)

# Example of using indexes to print out specific csv file
#    for line in csv_reader:
#        print(line[2])

# Create a new file, and replace seperator ',' with '-' or "\t" for tabs
    with open('datasets/new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)
