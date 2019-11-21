import math
def timecalc4():
    x = 0
    finalseconds = 0
    finalsecondsupdate = 0
    while True:
        print('Enter Data for Time ' + str(x))
        timeInput = input('time in format HHMMSS:')

        # hour = input('Enter Hour: ')
        # min = input('Enter minutes:  ')
        # sec = input('Enter seconds:  ')
        timeInput = str(timeInput)
        print(timeInput)
        print()

        hour = timeInput[0:2]
        minute = timeInput[2:4]
        seconds = timeInput[4:]

        hour = float(hour) * 3600
        minute = float(minute) * 60
        seconds = float(seconds)

        finalseconds = hour + minute + seconds
        finalsecondsupdate += finalseconds

        finalhour = math.floor(finalsecondsupdate / 3600)
        finalminute = math.floor(finalsecondsupdate % 3600 / 60)
        finalseconds = math.floor(finalsecondsupdate % 3600 % 60)

        print('Current total time is {}:{}:{}'.format(finalhour, finalminute, finalseconds))
        print('time in seconds is {}'.format(finalsecondsupdate))
        print()
        x = x + 1
        end = input('COntinue? N to exit.')
        if end == 'N' or end == 'n':
            break
        print()
    print('Total Time is {}:{}:{}\n'.format(finalhour, finalminute, finalseconds))

    speed = input('select speed \n')
    speed = float(speed)

    finaltime = finalsecondsupdate / speed
    #     print(finaltime)

    finalhour = math.floor(finaltime / 3600)
    #     print(finalhour)
    finalminute = math.floor(finaltime % 3600 / 60)
    #     print(finalminute)
    finalseconds = math.floor(finaltime % 3600 % 60)

    return print('Total Time is with calculated speed is {}:{}:{}\n'.format(finalhour, finalminute, finalseconds))

