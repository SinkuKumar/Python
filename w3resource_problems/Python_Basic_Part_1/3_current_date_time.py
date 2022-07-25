"""
3. Write a Python program to display the current date and time.
"""
import datetime

current_date_time = datetime.datetime.now()
print(current_date_time.strftime("%Y-%m-%d %H:%M:%S"))