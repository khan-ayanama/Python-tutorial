# write to file
# 'w', 'a', 'r+'

# w method should be used when file is empty and will create a file automatically
# with open('file2.txt', 'w') as f:
#     f.write('hello')


# a --> append method
# with open('file2.txt', 'a') as f:
#     f.write('New line is added')

# r+ method --> it does not create file unlike others
with open('file3.txt', 'r+') as f:
    f.seek(len(f.read()))
    f.write('2nd time New line is added')
