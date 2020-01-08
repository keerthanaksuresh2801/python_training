import sys

date=input("Enter the date: ")
dd,mm,yy=date.split('/')

t_date=7
t_month=1
t_year=2020
dd=int(dd)
mm=int(mm)
yy=int(yy)


if (yy>t_year):
    print("Sorry ,cannot check for a future date.")
    sys.exit(0)
elif ((yy==2020) and (mm>t_month)):
    print("Sorry ,cannot check for a future date..")
    sys.exit(0)
elif (yy==t_year and mm== t_month and dd> t_date):
    print("Sorry ,cannot check for a future date.")
    sys.exit(0)


if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max1=31
elif(mm==4 or mm==6 or mm==9 or mm==11):
    max1=30
elif(yy%4==0 and yy%100!=0 or yy%400==0):
    max1=29
else:
    max1=28
   
if(mm<1 or mm>12):
    print("Date is invalid.")
elif(dd<1 or dd>max1):
    print("Date is invalid.")
else:
    print("Date is Valid")