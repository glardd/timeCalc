import math

def timeconverter(time,speed):
    hour = time[0:2]
    minute = time[2:4]
    seconds = time[4:6]

    hour = float(hour) * 3600
    minute = float(minute) * 60
    seconds = float(seconds)
    #     print(hour)
    #     print(minute)
    #     print(seconds)

    finalseconds = hour + minute + seconds

    #     print (finalseconds)
    finaltime = finalseconds / speed
    #     print(finaltime)

    finalhour = math.floor(finaltime / 3600)
    #     print(finalhour)
    finalminute = math.floor(finaltime % 3600 / 60)
    #     print(finalminute)
    finalseconds = math.floor(finaltime % 3600 % 60)
    #     print(finalseconds)
    print('{}:{}:{} '.format(finalhour, finalminute, finalseconds))
    return '{}{}{} '.format(finalhour, finalminute, finalseconds)

