from time import *
while(True):
  print()
  sleep(0.075)
  print()
  sleep(0.075)
  for f in range(5,25,5):
    print(" "*(25-int(f/2)+50)+"$"*(int(f))+" "*(25-int(f))+"$"*(int(f))) 
    sleep(0.075)
  print(" "*(13+51)+"$"*48)
  sleep(0.075)
  print(" "*(13+51)+"$"*48)
  sleep(0.075)
  for i in range(1,25,2):
    #if(i==11 or i==5 or i==7 or i==9):
    if(i==1):
       print(" "*(13+i+50)+"$"*(19-(i))+"************"+"$"*(19-(i)),"\n",end = "")
    elif(i>2 and i<12):
       print(" "*(13+i+50)+"$"*(19-(i))+"*I Love You*"+"$"*(19-(i)),"\n",end = "")
    elif(i==13):
       print(" "*(13+i+50)+"$"*(19-(i))+"************"+"$"*(19-(i)),"\n",end = "")
    else:
      print(" "*(13+i+50)+"$"*(50-(i*2)),"\n",end = "")
    sleep(0.075)
  print()
  sleep(0.075)
  print()
  sleep(0.075)
