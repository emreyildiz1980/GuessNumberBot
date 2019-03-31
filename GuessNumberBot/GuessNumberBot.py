import random

turn = "First" 
guessednumber = 0


def guessnumber(param1,param2):
    guessednumber = random.randint(param1,param2)
    
    print(turn,' guess is', guessednumber)
    return guessednumber
    
try:
    turn1 = guessnumber(3,7)
    print("Tuttuğunuz sayı büyükse (1), Küçük ise (2), Tam isabet ise (3) Giriniz !")
    guessing = int(input())
    turn = "Second"
    if (guessing == 3):
       print("İşte Bu kadar Basit :)")
       pass
    elif(guessing == 1):
       print("Hmmmm")
       turn2 = guessnumber(turn1 + 1 , 10)
       print("Tuttuğunuz sayı büyükse (1), Küçük ise (2), Tam isabet ise (3) Giriniz !")
       guessing2 = int(input())
       pass
    elif(guessing == 2):
       print("Hmmmm")
       turn2 = guessnumber(0, (turn1 - 1))
       print("Tuttuğunuz sayı büyükse (1), Küçük ise (2), Tam isabet ise (3) Giriniz !")
       guessing2 = int(input())
       pass
    pass
except :
        print("Yanlış bilgi veriyorsunuz !")
        print("Bir tuşa basıp çıkınız...")
        exit(self,code)
        guessing3 = 0
        pass



turn="Third"

try:
    if (guessing2 == 3):
       print("İşte Bu kadar Basit :)")
       pass
    elif(guessing2 == 1):
        if (guessing==1):
           print("Hmmmm")
           turn3 = guessnumber(turn2 + 1 , 10)
           print("Tuttuğunuz sayı büyükse (1), Küçük ise (2), Tam isabet ise (3) Giriniz !")
           guessing3 = int(input())
           pass
        elif (guessing==2):
           print("Hmmmm")
           turn3 = guessnumber(turn2 + 1 , turn1-1)
           print("Tuttuğunuz sayı büyükse (1), Küçük ise (2), Tam isabet ise (3) Giriniz !")
           guessing3 = int(input())
           pass
    
        pass

    elif(guessing2 == 2):
        if (guessing==1):
          print("Hmmmm")
          turn2 = guessnumber((turn1 + 1), (turn2 - 1))
          print("Tuttuğunuz sayı büyükse (1), Küçük ise (2), Tam isabet ise (3) Giriniz !")
          guessing3 = int(input())
          pass
        elif (guessing==2):
          print("Hmmmm")
          turn2 = guessnumber(0, (turn2 - 1))
          print("Tuttuğunuz sayı büyükse (1), Küçük ise (2), Tam isabet ise (3) Giriniz !")
          guessing3 = int(input())
          pass 
        pass
except :
    print("Yanlış bilgi veriyorsunuz !")
    print("Bir tuşa basıp çıkınız...")
    guessing3 = 0
    pass



if (guessing3 == 3):
    print("Bu iş bu kadar basit :)")
    pass
else:
    print("Upps, Bir daha oynayabilir miyiz?")
    input()
    pass





