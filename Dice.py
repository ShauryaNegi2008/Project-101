import random

response = input('If you want to roll the dice press y else press n to exit : ')

def Dice(response):
 if(response=='y'):
  no=random.randint(1,6)
  if(no==1):
   print("[-----]")
   print("[     ]")
   print("[  0  ]")
   print("[     ]")
   print("[-----]")
  if(no==2):
   print("[-----]")
   print("[     ]")
   print("[ 0 0 ]")
   print("[     ]")
   print("[-----]")
  if(no==3):
   print("[-----]")
   print("[     ]")
   print("[0 0 0]")
   print("[     ]")
   print("[-----]")
  if(no==4):
   print("[-----]")
   print("[0   0]")
   print("[     ]")
   print("[0   0]")
   print("[-----]")
  if(no==5):
    print("[-----]")
    print("[0   0]")
    print("[  0  ]")
    print("[0   0]")
    print("[-----]")
  if(no==6):
   print("[-----]")
   print("[0   0]")
   print("[0   0]")
   print("[0   0]")
   print("[-----]")
 
  response2=input("To roll dice agian, press y else to exit press n : ")
  if(response2=='y'):
   Dice(response2)
  else:
   print('You have been exited')
 else:print('You have been exited')

Dice(response)
