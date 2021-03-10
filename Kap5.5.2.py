import datetime
import math

dt=datetime.datetime.now()

print("Vad är ditt personummer? I formatet ÅÅMMDDXXXX ")
persnmr=input("")
birthdateM=(persnmr[2] + persnmr[3])
birthdateD=(persnmr[4] + persnmr[5])
month=(dt.month)

if month>10:
    print("0"+(month))
else:
    print("k")