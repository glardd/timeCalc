from timeconv3 import timeconverter
from timecalc4 import timecalc4


while True:
    choose = input("Choose option \n1: Time Calculator \n2: Time Converter\n")
    if choose == '1':
        timecalc4()
    elif choose == '2':
        time = str(input("Please input time in HHMMSS format"))
        speed = float(input("Please enter speed"))
        print(speed)
        timeconverter(time, speed)
    else:
        print("Invalid choice. Please choose again")

