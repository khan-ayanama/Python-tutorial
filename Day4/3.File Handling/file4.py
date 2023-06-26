# copy the file ---> read and write simultaneously

with open('file2.txt', 'r') as rf:
    with open('file4.txt', 'w') as wf:
        wf.write(rf.read())
