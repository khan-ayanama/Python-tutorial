from csv import DictWriter

with open('file4.csv', 'w', newline='') as f:
    csv_writer = DictWriter(f, fieldnames=['firstname', 'lastname', 'age'])
    csv_writer.writeheader()

    # writerow
    # csv_writer.writerow({
    #     'firstname': 'Ayan',
    #     'lastname': 'Khan',
    #     'age': 20
    # })
    # csv_writer.writerow({
    #     'firstname': 'Jameel',
    #     'lastname': 'Khan',
    #     'age': 20
    # })
    # csv_writer.writerow({
    #     'firstname': 'Naeem',
    #     'lastname': 'Khan',
    #     'age': 20
    # })

    # writerows ---> [dict,dict,dict]
    csv_writer.writerows([
        {
            'firstname': 'Ayan',
            'lastname': 'Khan',
            'age': 20
        },
        {
            'firstname': 'Jameel',
            'lastname': 'Khan',
            'age': 20
        },
        {
            'firstname': 'Naeem',
            'lastname': 'Khan',
            'age': 20
        }
    ])
