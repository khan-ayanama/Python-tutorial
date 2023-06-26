from csv import writer

with open('file3.csv', 'w', newline='') as f:
    csv_writer = writer(f)
    # methods - write row, write rows
    # csv_writer.writerow(['name', 'country'])
    # csv_writer.writerow(['Ayan', 'INDIA'])
    # csv_writer.writerow(['Jameel', 'INDIA'])

    # with writerows
    csv_writer.writerows([['name', 'country'], [
                         'Ayan', 'INDIA'], ['Jameel', 'INDIA']])
