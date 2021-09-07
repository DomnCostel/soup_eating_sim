from time import sleep
import os
from pygame import mixer

#ingridients
soup = """
 \##############/
  \____________/"""
salt= """
_________________
|                |
|                |
|       S        |
|       A        |
|       L        |
|       T        |
|                |
|                |
‾‾‾(           )‾‾
    (         )
     ‾‾‾‾‾‾‾‾‾
      .   .. .
       .  .  ..
      . . .   . .
"""
#vars and lists
soupeaten = False
souppoisoned = True
toomuchsalt = False
saltiness = 0
nicenumbers = ["69", "420"]
hotel = "trivago"
#actions
def eatsoup():
    global soupeaten
    print("You ate the soup.")
    mixer.Channel(1).play(mixer.Sound('soup eating.wav'))
    sleep(3)
    soupeaten = True
def addsalt():
    try:
        global saltiness
        global souppoisoned
        global toomuchsalt
        howmuch = int(input("How much shakes?\n"))
        print("You added " + str(howmuch) + " salt shakes.")
        mixer.Channel(1).play(mixer.Sound('salt shake.wav'))
        sleep(5)
        saltiness += howmuch
        if saltiness > 9:
            souppoisoned = False
            if saltiness > 19:
                toomuchsalt = True
    except:
        print("i asked for a number dumbass")
#dicts
soupyanswers = {
"eat soup": eatsoup,
"eat": eatsoup,
"eat the soup": eatsoup,
"add salt": addsalt
}
#endings
def deathbypoison():
    mixer.Channel(1).play(mixer.Sound('dying.wav'))
    print("U were dumb, the soup was poisoned, like all soup is, so u ded now")
    print("You ascend into the Eternal Sea, and there you meet Crab God and become a crab and rave.")
    print("ENDING 1/?: POISON DEATH")
def saltylife():
    print("The soup was poisoned, like all soup is. HOWEVER, the magik power of salt neutralized poison, so u still alive.")
    print("ENDING 2/?: STILL ALIVE (and salty)")
def toosalty():
    mixer.Channel(1).play(mixer.Sound('dying.wav'))
    print("You added too much salt. The original poison was neutralized, but you died of dehydration/sodium poisoning/whatever")
    res = [sub for sub in nicenumbers if sub in str(saltiness)]
    if res:
        print("nice salt amount btw")
    print("You ascend into the Eternal Sea, and there you meet Crab God and become a crab and rave.")
    print("ENDING 3/?: TOO SALTY")
#game
mixer.init()
mixer.music.load('soundtrack.wav')
mixer.music.play(-1)
print("You find yourself surrounded by invisible walls, in a dark void™. You are sitting on a chair, a bowl of soup on the \ntable in front of you.")
print(soup)
print("Next to it is a salt shaker.")
print(salt)
#loop of soup
while soupeaten == False:
    print("What would you like to do?")
    print("Your options: eat soup, add salt")
    answer = input(">")
    if answer not in soupyanswers:
        if answer == "soup":
            print("s̸̟̄̕o̶̤̬̅u̸͙͍̾p̵̫͂̚")
        else:
            print("not an option dumdum")
    else:
        action = soupyanswers[answer]
        action()
#the moment of truth
if soupeaten:
    if souppoisoned:
        deathbypoison()
    elif toomuchsalt:
        toosalty()
    else:
        saltylife()
sleep(10)
