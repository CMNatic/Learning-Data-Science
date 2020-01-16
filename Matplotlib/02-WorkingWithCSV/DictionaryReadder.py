import csv

# Using Dictionary Read
# All values are now stored in an ordered dictionary
# Field names are now keys for each of the values
# E.g. to print out email address you'd have to print out the 2nd index
# But now you can print out the email of the line

# with open('datasets/original_names.csv', 'r') as csv_file:
#    csv_reader = csv.DictReader(csv_file)

#    for line in csv_reader:
#        print(line['email'])

# Now using Dictionary Write

#with open('datasets/original_names.csv', 'r') as csv_file:
#    csv_reader = csv.DictReader(csv_file)


#with open('datasets/new_names_csv_writer.csv', 'w') as new_file:
#    fieldnames = ['first_name', 'last_name', 'email']

#    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

#    csv_writer.writeheader()

#    for line in csv_reader:
#        csv_writer.writerow(line)
# We have to provide field names of the file

