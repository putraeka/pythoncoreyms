import csv

# Buka file names.csv - read menggunakan csv module csv.reader
# Buka file baru dengan nama new-names.csv - mode write dengan mengcopy file names.csv tapi delimiter diganti
# menggunakan tand (-)
# for loop untuk menulis semua data ke vfile baru menggunakan fungsi csv writerow
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    with open ('new-names-tab.csv', 'w') as new_csv:
        csv_writer = csv.writer(new_csv, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

    # next(csv_reader)
    # for line in csv_reader:
    #     print(line[2])
