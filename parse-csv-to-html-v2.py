import csv

# Tutorial dari https://youtu.be/bkpLhQd6YQM
html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # we don't want headers or first line 
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p>The are currently {len(names)} public contributors. Thank you!</p>'
html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'
# Membuat file patrons html
with open('patrons.html', 'w') as html_file:
    html_file.write(html_output)
# Menampilkan output dari file html ke layar
print(html_output)