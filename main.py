import pyperclip
from datetime import datetime
from time import sleep

last_copied_data = ''

def dateAndTime():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S\t:\t")

def log_data_copied(log_date_and_time):
    with open("log.txt", "a") as f:
        f.write(str(log_date_and_time) + pyperclip.paste()+'\n')

if __name__ == '__main__':
    while True:
        if last_copied_data == pyperclip.paste():
            # print("True")
            pass
        else:
            # print("False")
            last_copied_data = pyperclip.paste()
            log_date_and_time = dateAndTime()
            log_data_copied(log_date_and_time)
