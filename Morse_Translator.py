from gpiozero import LED
from time import sleep
from random import uniform

red = LED(17)
amber = LED(27)
green = LED(22)

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

#function for traffic light
def traffic(c):
    green.blink(15,13,c)
    sleep(15)
    amber.blink(3,25,c)
    sleep(3)
    red.blink(10,18,c)

#disco function
def disco():
    red.blink(uniform(0.1,1), uniform(0.1,1))
    amber.blink(uniform(0.1,1),uniform(0.1,1))
    green.blink(uniform(0.1,1),uniform(0.1,1))

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

This app will translate English phrases into Morse, just watch the cool LED!""")

sleep(2)

#Phrase Input
while True:
    english = input("""\nNow enter a phrase you'd like to see in Morse Code
OR type Traffic for signals
OR type Disco for a party
OR type Quit to exit:  """)
    
    if english.upper() == "QUIT":
        break
    elif english.upper() == "TRAFFIC":
        cycles = int(input("Enter # of cycles you want to see: "))
        traffic(cycles)
    elif english.upper() == "DISCO":
        disco()
        print("\n\nTHIS PARTY NEVER STOPS!!!\n")
    else:
        #Speed Input
        while True:
            s = input("""\n\nEnter speed of Morse
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
                print("\nInvalid Input. Try again.")
        
#loop to tranlate input phrase
        for l in english:
            morse(l.upper())
            sleep(speed*2)
                        
print("\nHope that was fun! Thanks!")
