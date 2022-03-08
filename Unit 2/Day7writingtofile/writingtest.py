import csv

with open('writetest.txt', "w") as file_out:
    file_out.write("hey\n")
    file_out.write("hey")

l = ['woow','wew','dewdew']
with open('writetest.txt', 'w') as file_out:
    writer = csv.writer(file_out)
    writer.writerow(l)

print(l)