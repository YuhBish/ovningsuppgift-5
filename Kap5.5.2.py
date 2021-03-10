import datetime

dt=datetime.datetime.now()
d=dt.date()
dtext=str(d)

print("Vad är ditt personummer? I formatet ÅÅMMDDXXXX ")
persnmr=input("")
birthdate=(persnmr[2:6])
month=(dt.month)
dtext1=dtext[5]
dtext2=dtext[6]
dtext3=dtext[8]
dtext4=dtext[9]
dtext0=dtext1+dtext2+dtext3+dtext4 

if dtext0 == birthdate:
    print("Grattis på födelsedagen!")
else:
    print("Hejdå")