from time import sleep
import os
import sys
try:
    from pygame import mixer
except:
    print("You don't have pygame installed, musik and sounds will not play. To install it open a command line\nand type \'python -m pip install pygame\' on windows, and 'pip3 install pygame' on unix-like OSes")
cwd = os.getcwd()

varspy = os.path.join(cwd, "data/vars.py")
datadir = os.path.join(cwd, "data")
try:
    os.mkdir(datadir)
except:
    pass
if os.path.exists(varspy):
    sys.path.append(datadir)
    from vars import *
else:
    f = open(varspy, 'w')
    f.write("""
GotEnd1 = False
GotEnd2 = False
GotEnd3 = False
GotEnd4 = False
ReleasedSaltman = False
ReleasedSoupman = False
""")
    f.close()
    sys.path.append(datadir)
    from vars import *

#art
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
spoon = """
   (‾‾‾‾)
  (      )
 (        )
(          )
 (        )
  (      )
   (    )
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
     ‾‾
"""
soupnsalt = """
_________________________________________________________
|                                                        |
|     _____                   ____                       |
|    ( . . )                 ( ' ' )                     |
|     ( / )                   ( ~ )     |                |
|___   ‾|‾‾  __          __    ‾|‾‾ ____|                |
|   \‾‾‾‾‾‾‾/  |        |  |‾‾‾‾‾‾‾‾|                    |
|    |  S   |  |       |   | S      |                    |
|    |      |  |      |    | /‾\/‾\ |                    |
|    \_____/               |/      \|			 |
|      | |                 ‾‾|‾‾‾|‾‾‾‾   	         |
|      | |                   |   |			 |
|                           			         |
|  5oupman likes         5alt 3an makes it        	 |
|   to soup                   salty 		         |
|                             				 |
|             Summon them today                          |
|               Dont get poisoned!               	 |
|                             				 |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
soupman = """
    Soupman
     _____
    ( . . )
     ( / )
___   ‾|‾‾  __
   \‾‾‾‾‾‾‾/  |
    |  S   |  |
    |      |  |
    \_____/
      | |
      | |
"""
saltman = """
      Saltman
        ____
       ( ' ' )
        ( ~ )     |
   __    ‾|‾‾ ____|
  |  |‾‾‾‾‾‾‾‾|
 |   | S      |
|    | /‾\/‾\ |
     |/      \|
     ‾‾|‾‾‾|‾‾‾‾
       |   |
"""
logo = """
        _________________________________________________________________
        |  ____   ___  _   _ ____    _____    _  _____ ___ _   _  ____  |
        | / ___| / _ \| | | |  _ \  | ____|  / \|_   _|_ _| \ | |/ ___| |
        | \___ \| | | | | | | |_) | |  _|   / _ \ | |  | ||  \| | |  _  |
        |  ___) | |_| | |_| |  __/  | |___ / ___ \| |  | || |\  | |_| | |
        | |____/ \___/ \___/|_|     |_____/_/   \_\_| |___|_| \_|\____| |
        |                                                               |
        |       ____ ___ __  __ _   _ _        _  _____ ___  ____       |
        |      / ___|_ _|  \/  | | | | |      / \|_   _/ _ \|  _ \      |
        |      \___ \| || |\/| | | | | |     / _ \ | || | | | |_) |     |
        |       ___) | || |  | | |_| | |___ / ___ \| || |_| |  _ <      |
        |      |____/___|_|  |_|\___/|_____/_/   \_\_| \___/|_| \_\     |
        |                                                               |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                                       ____
                                       |  |
                                       |  |
                                       |  |
     _____                             |  |                            ____
    ( . . )                            |  |                           ( ' ' )
     ( / )                             |  |                            ( ~ )     |
___   ‾|‾‾  __                         |  |                       __    ‾|‾‾ ____|
   \‾‾‾‾‾‾‾/  | \                     _|__|_                   / |  |‾‾‾‾‾‾‾‾|
    |  S   |  |  \                   (      )                 / |   | S      |
    |      |  |   \                 (        )               / |    | /‾\/‾\ |
    \_____/        \                (        )              /       |/      \|
      | |           \                (      )              /        ‾‾|‾‾‾|‾‾‾‾
      | |            \                (    )              /           |   |
                     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
#vars and lists
SpoonUpgrade = False
if GotEnd1:
    if GotEnd2:
        if GotEnd3:
            SpoonUpgrade = True
soupeaten = False
souppoisoned = True
toomuchsalt = False
saltiness = 0
soupiness = 0
nicenumbers = ["69", "420"]
breakout = False
hotel = "trivago"
#actions
def eatsoup():
    global soupeaten
    print("You ate the soup.")
    mixer.Channel(1).play(mixer.Sound('sound/soup eating.wav'))
    sleep(3)
    soupeaten = True
def addsalt():
    try:
        global GotEnd1
        global GotEnd2
        global GotEnd3
        global GotEnd4
        global ReleasedSaltman
        global ReleasedSaltman
        global saltiness
        global souppoisoned
        global toomuchsalt
        global SpoonUpgrade
        global breakout
        howmuch = int(input("How much shakes?\n"))
        print("You added " + str(howmuch) + " salt shakes.")
        mixer.Channel(1).play(mixer.Sound('sound/salt shake.wav'))
        sleep(5)
        print("Now stir it")
        stir = 0
        while stir != "stir":
            stir = input(">")
            if stir == "stir":
                print("You stirred the soup.")
                mixer.Channel(1).play(mixer.Sound('sound/stir.wav'))
                sleep(6)
            else:
                print("idiot just stir it")
        saltiness += howmuch
        if saltiness > 9:
            souppoisoned = False
            if saltiness > 19:
                toomuchsalt = True
        if ReleasedSaltman == False:
            if saltiness == 53:
                if SpoonUpgrade:
                    print("Your spoon becomes comically large and you want to bonk yourself with it, so you do.")
                    print("A very salty (not in a bad way) individual comes out of your skull, which is now cracked.")
                    mixer.music.stop()
                    mixer.music.unload()
                    mixer.music.load("sound/Man of Salt.wav")
                    mixer.music.play(-1)
                    print(saltman)
                    print("hi thank you for releasing me")
                    if ReleasedSoupman == False:
                        print("dont forget to also release soupman")
                    ReleasedSaltman = True
                    f = open(varspy, 'w')
                    f.write("GotEnd1 = " + str(GotEnd1))
                    f.close()
                    f = open(varspy, 'a')
                    f.write("\nGotEnd2 = " + str(GotEnd2))
                    f.write("\nGotEnd3 = " + str(GotEnd3))
                    f.write("\nGotEnd4 = " + str(GotEnd4))
                    f.write("\nReleasedSaltman = " + str(ReleasedSaltman))
                    f.write("\nReleasedSoupman = " + str(ReleasedSoupman))
                    f.close()
                    sleep(8)
                    mixer.music.stop()
                    mixer.music.unload()
                    mixer.music.load("sound/normal days.wav")
                    mixer.music.play(-1)
        else:
            if GotEnd4:
                if saltiness == 53:
                    if SpoonUpgrade:
                        breakout = True
    except:
        print("i asked for a number dumbass")
def lookundertable():
    global soupnsalt
    global SpoonUpgrade
    print("There is an engraving under the table. It says:")
    if SpoonUpgrade:
        print(soupnsalt)
    else:
        print("Salt you not, live you shall not.\nSalt you too much, live you not much.\nSalt you just right, live without fright.")
def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")
#endings
def deathbypoison():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global ReleasedSaltman
    global ReleasedSaltman
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load("sound/cruel soup cruel life.wav")
    mixer.music.play(-1)
    mixer.Channel(1).play(mixer.Sound('sound/dying.wav'))
    print("U were dumb, the soup was poisoned, like all soup is, so u ded now")
    print("You ascend into the Eternal Sea, and there you meet Crab God and become a crab and rave.")
    print("ENDING 1/?: POISON DEATH")
    if GotEnd1 == False:
        GotEnd1 = True
        f = open(varspy, 'w')
        f.write("GotEnd1 = " + str(GotEnd1))
        f.close()
        f = open(varspy, 'a')
        f.write("\nGotEnd2 = " + str(GotEnd2))
        f.write("\nGotEnd3 = " + str(GotEnd3))
        f.write("\nGotEnd4 = " + str(GotEnd4))
        f.write("\nReleasedSaltman = " + str(ReleasedSaltman))
        f.write("\nReleasedSoupman = " + str(ReleasedSoupman))
        f.close()
def saltylife():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global ReleasedSaltman
    global ReleasedSaltman
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load("sound/Alive but salty.wav")
    mixer.music.play(-1)
    print("The soup was poisoned, like all soup is. HOWEVER, the magik power of salt neutralized poison, so u still alive.")
    print("ENDING 2/?: STILL ALIVE (and salty)")
    if GotEnd2 == False:
        GotEnd2 = True
        f = open(varspy, 'w')
        f.write("GotEnd1 = " + str(GotEnd1))
        f.close()
        f = open(varspy, 'a')
        f.write("\nGotEnd2 = " + str(GotEnd2))
        f.write("\nGotEnd3 = " + str(GotEnd3))
        f.write("\nGotEnd4 = " + str(GotEnd4))
        f.write("\nReleasedSaltman = " + str(ReleasedSaltman))
        f.write("\nReleasedSoupman = " + str(ReleasedSoupman))
        f.close()
def toosalty():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global ReleasedSaltman
    global ReleasedSaltman
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load("sound/Life is salty.wav")
    mixer.music.play(-1)
    mixer.Channel(1).play(mixer.Sound('sound/dying.wav'))
    print("You added too much salt. The original poison was neutralized, but you died of dehydration/sodium poisoning/whatever")
    res = [sub for sub in nicenumbers if sub in str(saltiness)]
    if res:
        print("nice salt amount btw")
    print("You ascend into the Eternal Sea, and there you meet Crab God and become a crab and rave.")
    print("ENDING 3/?: TOO SALTY")
    if GotEnd3 == False:
        GotEnd3 = True
        f = open(varspy, 'w')
        f.write("GotEnd1 = " + str(GotEnd1))
        f.close()
        f = open(varspy, 'a')
        f.write("\nGotEnd2 = " + str(GotEnd2))
        f.write("\nGotEnd3 = " + str(GotEnd3))
        f.write("\nGotEnd4 = " + str(GotEnd4))
        f.write("\nReleasedSaltman = " + str(ReleasedSaltman))
        f.write("\nReleasedSoupman = " + str(ReleasedSoupman))
        f.close()
def ascend():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global ReleasedSaltman
    global ReleasedSaltman
    if ReleasedSaltman:
        if ReleasedSoupman:
            print("Having broken the loop of soup, You ascend into a safe place with the help of Saltman and Soupman's powers.")
            print("ENDING 4/?: LOOP BROKEN")
            if GotEnd4 == False:
                GotEnd4 = True
                f = open(varspy, 'w')
                f.write("GotEnd1 = " + str(GotEnd1))
                f.close()
                f = open(varspy, 'a')
                f.write("\nGotEnd2 = " + str(GotEnd2))
                f.write("\nGotEnd3 = " + str(GotEnd3))
                f.write("\nGotEnd4 = " + str(GotEnd4))
                f.write("\nReleasedSaltman = " + str(ReleasedSaltman))
                f.write("\nReleasedSoupman = " + str(ReleasedSoupman))
                f.close()


#dicts
soupyanswers = {
"eat soup": eatsoup,
"eat": eatsoup,
"eat the soup": eatsoup,
"add salt": addsalt,
"look under table": lookundertable
}
#game
def loopofsoup():
    global soup
    global salt
    global spoon
    global SpoonUpgrade
    global soupiness
    global soupnsalt
    global soupyanswers
    global soupman
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global ReleasedSaltman
    global ReleasedSoupman
    global saltiness
    global souppoisoned
    global toomuchsalt
    global breakout
    clear()
    mixer.init()
    mixer.music.load('sound/normal days.wav')
    mixer.music.play(-1)
    print("You find yourself surrounded by invisible walls, in a dark void™. You are sitting on a chair, a bowl of soup on the \ntable in front of you.")
    print(soup)
    print("Next to it is a salt shaker.")
    print(salt)
    print("There is also a spoon.")
    if SpoonUpgrade:
        print("It seems to be glowing faintly.")
        if GotEnd4 == False:
            print("You feel the urge to look under the table.")
    print(spoon)
    #loop of soup
    while soupeaten == False:
        print("What would you like to do?")
        print("Your options: eat soup, add salt, soup, look under table")
        answer = input(">")
        if answer not in soupyanswers:
            if answer == "soup":
                print("s̸̟̄̕o̶̤̬̅u̸͙͍̾p̵̫͂̚")
                soupiness += 1
                if ReleasedSoupman == False:
                    if soupiness == 5:
                        if SpoonUpgrade == True:
                            print("Your spoon becomes comically large and you want to bonk yourself with it, so you do.")
                            print("A very soupy individual comes out of your skull, which is now cracked.")
                            mixer.music.stop()
                            mixer.music.unload()
                            mixer.music.load("sound/Can you eat him with a spoon.wav")
                            mixer.music.play(-1)
                            print(soupman)
                            print("hi thank you for releasing me")
                            if ReleasedSaltman == False:
                                print("dont forget to also release saltman")
                            ReleasedSoupman = True
                            f = open(varspy, 'w')
                            f.write("GotEnd1 = " + str(GotEnd1))
                            f.close()
                            f = open(varspy, 'a')
                            f.write("\nGotEnd2 = " + str(GotEnd2))
                            f.write("\nGotEnd3 = " + str(GotEnd3))
                            f.write("\nGotEnd4 = " + str(GotEnd4))
                            f.write("\nReleasedSaltman = " + str(ReleasedSaltman))
                            f.write("\nReleasedSoupman = " + str(ReleasedSoupman))
                            f.close()
                            sleep(8)
                            mixer.music.stop()
                            mixer.music.unload()
                            mixer.music.load("sound/normal days.wav")
                            mixer.music.play(-1)
                else:
                    if GotEnd4:
                        breakout = True

            else:
                print("not an option dumdum")
        else:
            action = soupyanswers[answer]
            action()
        if GotEnd4 == False:
            if ReleasedSaltman:
                if ReleasedSoupman:
                    breakout = True

        if breakout:
            mixer.music.stop()
            mixer.music.unload()
            mixer.music.load("sound/Salty Soup.wav")
            mixer.music.play(-1)
            print("The powers of Saltman and Soupman have broken you out of the Loop of Soup!")
            break
    #the moment of truth
    if soupeaten:
        if souppoisoned:
            deathbypoison()
        elif toomuchsalt:
            toosalty()
        else:
            saltylife()
        sleep(10)
        mixer.music.stop()
        mixer.music.unload()
        mixer.music.load("sound/normal days.wav")
        mixer.music.play(-1)
        if GotEnd4:
            clear()
            mainmenu()
    else:
        if ReleasedSaltman:
            if ReleasedSoupman:
                print("Type \"ascend\" to ascend.")
                ascension = 0
                while ascension != "ascend":
                    ascension = input(">")
                    if ascension == "ascend":
                        ascend()
                        sleep(10)
                        clear()
                        mainmenu()
#main menu
def mainmenu():
    global soup
    global salt
    global spoon
    global SpoonUpgrade
    global soupiness
    global soupnsalt
    global soupyanswers
    global soupman
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global ReleasedSaltman
    global ReleasedSaltman
    global saltiness
    global souppoisoned
    global toomuchsalt
    global logo
    global soupeaten
    soupiness = 0
    saltiness = 0
    breakout = False
    toosalty = False
    souppoisoned = True
    soupeaten = False
    clear()
    try:
        mixer.init()
    except:
        pass
    try:
        mixer.music.stop()
        mixer.music.unload()
    except:
        pass
    mixer.music.load("sound/You can rest here, soupy traveler.wav")
    mixer.music.play(-1)
    print(logo)
    command = 0
    while True:
        print("What would you like to do? Commands: start game, view endings, exit")
        command = input(">")
        if command == "start game":
            break
        elif command == "view endings":
            print("Ending 1: " + str(GotEnd1))
            print("Ending 2: " + str(GotEnd2))
            print("Ending 3: " + str(GotEnd3))
            print("Ending 4: " + str(GotEnd4))
            print("More endings coming soon™")
        elif command == "exit":
            break
        else:
            print("This isnt a command")
    if command == "start game":
        loopofsoup()
#start game
if GotEnd4:
    mainmenu()
else:
    loopofsoup()
