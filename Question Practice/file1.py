# 1.Write a Python program to find out what version of Python you are using

# import sys
# print(sys.version)
# print(sys.version_info)

# 2. Write a Python program to display the current date and time.

# import datetime
# print(datetime.datetime.now())

# 3.Write a Python program that prints the calendar for a given month and year.

# import calendar
# y = int(input("input the year "))
# m = int(input("input the month "))
# print(calendar.month(y, m))

# 4.Write a Python program to calculate the number of days between two dates.

# from datetime import date

# f_date = date(2023, 6, 16)
# l_date = date(2002, 10, 15)
# delta = f_date - l_date
# print(delta.days)

# 5.Write a Python program to check whether a file exists.

# import os.path
# print(os.path.isfile('file1.py'))

# 6.Write a Python program to print without a newline or space.

# for i in range(0, 10):
#     print('*', end="")
# print("\n")
