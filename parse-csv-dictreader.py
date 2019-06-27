import csv

# script ini menggunakan fungsi Dictreader dan Dictwriter
# penggunaan untuk DictReader sama dengan reader
# tapi untuk DictWriter, kita harus mempersiapkan fieldnames terlebih dahulu
# bertujuan untuk menampung header
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('names-dict.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
