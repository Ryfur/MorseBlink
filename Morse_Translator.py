from gpiozero import LED
from time import sleep
from random import uniform

red = LED(17)

#Create a translation key from alpha to morse
key = {"A" : ".-", "B" : "-...", "C" : "-.-.",
       "D" : "-..", "E" : ".", "F" : "..-.",
       "G" : "--.", "H" : "....", "I" : "..",
       "J" : ".---", "K" : "-.-", "L" : ".-..",
       "M" : "--", "N" : "-.", "O" : "---",
       "P" : ".--.", "Q" : "--.-", "R" : ".-.",
       "S" : "...", "T" : "-", "U" : "..-",
       "V" : "...-", "W" : ".--", "X" : "-..-",
       "Y" : "-.--", "Z" : "--..", "0" : "-----",
       "1" : ".----", "2" : "..---", "3" : "...--",
       "4" : "....-", "5" : ".....", "6" : "-....",
       "7" : "--...", "8" : "---..", "9" : "----.", " " : " "}

#function to flash LED after finding appropriate length in dictionary
def morse(letter):
    for u in key[letter]:
        if u == ".":
            red.blink(speed, speed, 1)
            sleep(speed*2)
        elif u == "-":
            red.blink(speed*3, speed, 1)
            sleep(speed*4)
        else:
            sleep(speed*5)
        
#User inputs
print("""Welcome to the Morse Translator App.

This app will translate English phrases into Morse, just watch the cool LED!

""")

#Speed Input
while True:
    s = input("""Enter speed of Morse
(Fast, Medium, or Slow?):  """)

    if s.upper() == "FAST":
        speed = 0.1
        break
    elif s.upper() == "MEDIUM":
        speed = 0.25
        break
    elif s.upper() == "SLOW":
        speed = 0.5
        break
    else:
        print("Invalid Input. Try again.")

#Phrase Input
while True:
    english = input("\nNow enter a phrase you'd like to see in Morse or type Quit to exit:  ")
    
    if english.upper() == "QUIT":
        break
    else:
#loop to tranlate input phrase
        for l in english:
            morse(l.upper())
            sleep(speed*2)
                        
print("\nHope that was fun! Thanks!")