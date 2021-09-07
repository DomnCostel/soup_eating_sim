from time import sleep
import os

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
#vars
soupeaten = False
souppoisoned = True
toomuchsalt = False
saltiness = 0
hotel = "trivago"
#actions
def eatsoup():
    global soupeaten
    soupeaten = True
def addsalt():
    try:
        global saltiness
        global souppoisoned
        global toomuchsalt
        howmuch = int(input("How much shakes?\n"))
        print("You added " + str(howmuch) + " salt shakes.")
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
    print("U were dumb, the soup was poisoned, like all soup is, so u ded now")
    print("You ascend into the Eternal Sea, and there you meet Crab God and become a crab and rave.")
    print("ENDING 1/?: POISON DEATH")
def saltylife():
    print("The soup was poisoned, like all soup is. HOWEVER, the magik power of salt neutralized poison, so u still alive.")
    print("ENDING 2/?: STILL ALIVE (and salty)")
def toosalty():
    print("You added too much salt. The original poison was neutralized, but you died of dehydration/sodium poisoning/whatever")
    print("You ascend into the Eternal Sea, and there you meet Crab God and become a crab and rave.")
    print("ENDING 3/?: TOO SALTY")
#game
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
