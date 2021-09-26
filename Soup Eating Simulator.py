from time import sleep
import os
import sys
try:
    from pygame import mixer
except:
    print("You don't have pygame installed, musik and sounds will not play. To install it open a command line\nand type \'python -m pip install pygame\' on windows, and 'pip3 install pygame' on unix-like OSes")
    sleep(5)

cwd = os.getcwd()
datadir = os.path.join(cwd, "data")
varspy = os.path.join(datadir, "vars.py")
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
GotEnd5 = False
GotEnd6 = False
ReleasedSaltman = False
ReleasedSoupman = False
GotFork = False
GotBread = False
GotGarlic = False
GotSaltSphere = False
GotSoupSphere = False
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
fork = """
|   |    |
|   |    |
|   |    |
|   |    |
‾‾‾‾|‾‾‾‾‾
    |
    |
    |
    |
    |
    |
    |
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
forkysoup = False
garlicsoup = False
garlicbread = False
saltiness = 0
soupiness = 0
nicenumbers = ["69", "420"]
breakout = False
hotel = "trivago"
#actions
def save():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    f = open(varspy, 'w')
    f.write("GotEnd1 = " + str(GotEnd1))
    f.close()
    f = open(varspy, 'a')
    f.write("\nGotEnd2 = " + str(GotEnd2))
    f.write("\nGotEnd3 = " + str(GotEnd3))
    f.write("\nGotEnd4 = " + str(GotEnd4))
    f.write("\nGotEnd5 = " + str(GotEnd5))
    f.write("\nGotEnd6 = " + str(GotEnd6))
    f.write("\nReleasedSaltman = " + str(ReleasedSaltman))
    f.write("\nReleasedSoupman = " + str(ReleasedSoupman))
    f.write("\nGotFork = " + str(GotFork))
    f.write("\nGotBread = " + str(GotBread))
    f.write("\nGotGarlic = " + str(GotGarlic))
    f.write("\nGotSaltSphere = " + str(GotSaltSphere))
    f.write("\nGotSoupSphere = " + str(GotSoupSphere))
    f.close()
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
        global GotEnd5
        global GotEnd6
        global ReleasedSaltman
        global ReleasedSaltman
        global GotFork
        global GotSaltSphere
        global GotSoupSphere
        global GotBread
        global GotGarlic
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
                    print("at last, i am free from the brainy™ and bony™ prison that is your mortal head")
                    if ReleasedSoupman == False:
                        print("dont forget to also release soupman")
                    ReleasedSaltman = True
                    save()
                    sleep(8)
                    mixer.music.stop()
                    mixer.music.unload()
                    mixer.music.load("sound/normal days.wav")
                    mixer.music.play(-1)
        else:
            if GotEnd4:
                if saltiness == 53:
                    if GotSaltSphere:
                        breakout = True
                    else:
                        if forkysoup:
                            print("dumbass your fork melted so we'll just give you ending 4 instead")
                            breakout = True
                        else:
                            print("Your fork's pointy parts start glowing so you do the logical thing: stab yourself in the forehead with it.")
                            print("You don't bleed from the wound, but a strange liquid that doesn't seem to be affected by gravity pours out of it and becomes a sphere.")
                            print("The wound closes itself instantly after.")
                            mixer.Channel(1).play(mixer.Sound('sound/pickup.wav'))
                            print("(You have obtained the Salty Sphere! Saltman would probably like to see it.)")
                            GotSaltSphere = True
                            save()
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
def eatsoupwithfork():
    global forkysoup
    print("You attempt to eat soup with the fork. It melts, now you have a forky soup.")
    forkysoup = True
def addgarlic():
    global garlicsoup
    mixer.Channel(1).play(mixer.Sound('sound/garlic.wav'))
    print("You added garlic to the soup. You feel a sense of dread.")
    mixer.music.stop()
    mixer.music.unload()
    garlicsoup = True
    sleep(3)
def addbread():
    global souppoisoned
    global toomuchsalt
    print("You added bread to the soup.")
    if souppoisoned:
        print("It dissolved from the poison")
    elif toomuchsalt:
        print("It dissolved from the salt")
    else:
        print("This is a major improvement.")
    print("The slice of bread on the table reappeared.")
def eatbread():
    print("You ate the bread. You enjoyed it, but other than that and it reappearing on the table, nothing happened.")
def eatgarlic():
    print("You ate the garlic. It tasted like it should be put on bread, not eaten raw. The clove of garlic on the table reappeared.")
def makegarlicbread():
    global garlicbread
    print("You repeatedly slammed the slice of bread with the clove of garlic. Magically, they turned into garlic bread.")
    mixer.Channel(1).play(mixer.Sound('sound/pickup.wav'))
    garlicbread = True
def eatgarlicbread():
    global garlicbread
    if garlicbread:
        print("It tastes like heaven. It feels like heaven. You feel like you are in heaven. \nActually, while enjoying the garlic bread, you transcended into the Eternal Sea (which is heaven) without dying.")
        print("You meet Crab God.")
        print("\"Oh, it's you again. Someone wanted to talk to you.\", he says, as he transfers you to two crabs.")
        print("The crabs are the devs of this game. I, Cirilaron, the lead programmer, and Domncostel, the lead art designer and sound composer.")
        print("We tell you about the planned updates: Bepis update and kitchen minigame")
        print("After that you return back to the table. This is not an ending.")
        garlicbread = False
    else:
        print("you don't have any, idiot")
#endings
def deathbypoison():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
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
        save()
def saltylife():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load("sound/Alive but salty.wav")
    mixer.music.play(-1)
    print("The soup was poisoned, like all soup is. HOWEVER, the magik power of salt neutralized poison, so u still alive.")
    print("ENDING 2/?: ALIVE BUT SALTY")
    if GotEnd2 == False:
        GotEnd2 = True
        save()
def toosalty():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
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
        save()
def ascend():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    if ReleasedSaltman:
        if ReleasedSoupman:
            print("Having broken the loop of soup, You ascend into a safe place with the help of Saltman and Soupman's powers.")
            print("ENDING 4/?: LOOP BROKEN")
            if GotEnd4 == False:
                GotEnd4 = True
                save()
def silverpoisoning():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load("sound/A Silver End.wav")
    mixer.music.play(-1)
    mixer.Channel(1).play(mixer.Sound('sound/dying.wav'))
    print("You died of silver poisoning because you ate the fork, which got mixed in the soup.")
    print("You ascend into the Eternal Sea, and there you meet Crab God and become a crab and rave.")
    print("ENDING 5/?: Forky Death")
    if GotEnd5 == False:
        GotEnd5 = True
        save()
def necksnap():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    mixer.music.load("sound/No.wav")
    mixer.music.play(-1)
    mixer.Channel(1).play(mixer.Sound('sound/neck snapping.wav'))
    print("Suddenly, i (the lead programmer, Cirilaron) appear behind you and snap your neck because i disagree with what you just did.")
    print("You ascend into the Eternal Sea, and there you meet Crab God and become a crab and rave.")
    print("ENDING 6/?: NECK SNAP")
    if GotEnd6 == False:
        GotEnd6 = True
        save()

#dicts
soupyanswers = {
"eat soup": eatsoup,
"eat": eatsoup,
"eat the soup": eatsoup,
"add salt": addsalt,
"look under table": lookundertable
}
if GotFork:
    soupyanswers["eat soup with fork"] = eatsoupwithfork
if GotBread:
    soupyanswers["add bread"] = addbread
    soupyanswers["eat bread"] = eatbread
if GotGarlic:
    soupyanswers["add garlic"] = addgarlic
    soupyanswers["eat garlic"] = eatgarlic
if GotBread and GotGarlic:
    soupyanswers["make garlic bread"] = makegarlicbread
    soupyanswers["eat garlic bread"] = eatgarlicbread
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
    global saltman
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSoupman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    global forkysoup
    global saltiness
    global souppoisoned
    global toomuchsalt
    global breakout
    global fork
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
    if GotFork:
        print("The fork you got from Saltman and Soupman is also here.")
        print(fork)
    if GotGarlic:
        print("You have some garlic in your left pocket, so you put it on the table.")
    if GotBread:
        print("You have some bread in your right pocket, so you put it on the table.")
    #loop of soup
    while soupeaten == False:
        print("What would you like to do?")
        options = "eat soup, add salt, soup, look under table"
        if GotFork:
            options = options + ", eat soup with fork"
        if GotBread:
            options = options + ", add bread, eat bread"
        if GotGarlic:
            options = options + ", add garlic, eat garlic"
        if GotBread and GotGarlic:
            options = options + ", make garlic bread, eat garlic bread"
        print("Your options: " + options)
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
                            print("Finally, the cranial jail that is your mortal skull has been broken.")
                            if ReleasedSaltman == False:
                                print("dont forget to also release saltman")
                            ReleasedSoupman = True
                            save()
                            sleep(8)
                            mixer.music.stop()
                            mixer.music.unload()
                            mixer.music.load("sound/normal days.wav")
                            mixer.music.play(-1)
                else:
                    if GotEnd4:
                        if soupiness == 5:
                            if GotSoupSphere:
                                breakout = True
                            else:
                                if forkysoup:
                                    print("dumbass your fork melted so we'll just get you ending 4 instead")
                                    breakout = True
                                else:
                                    print("Your fork's pointy parts start glowing so you do the logical thing: stab yourself in the forehead with it.")
                                    print("You don't bleed from the wound, but a strange liquid that doesn't seem to be affected by gravity pours out of it and becomes a sphere.")
                                    print("The wound closes itself instantly after.")
                                    mixer.Channel(1).play(mixer.Sound('sound/pickup.wav'))
                                    print("(You have obtained the Soupy Sphere! Soupman would probably like to see it.)")
                                    GotSoupSphere = True
                                    save()

            else:
                print("not an option dumdum")
        else:
            action = soupyanswers[answer]
            action()
        if garlicsoup:
            break
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
        if forkysoup:
            silverpoisoning()
        elif souppoisoned:
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
        if garlicsoup:
            necksnap()
            sleep(10)
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
    global saltman
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSoupman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    global forkysoup
    global saltiness
    global souppoisoned
    global toomuchsalt
    global garlicsoup
    global logo
    global soupeaten
    global breakout
    soupiness = 0
    saltiness = 0
    breakout = False
    toomuchsalt = False
    souppoisoned = True
    forkysoup = False
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
        print("What would you like to do? Commands: start game, view endings, kitchen, exit")
        command = input(">")
        if command == "start game":
            break
        elif command == "view endings":
            print("Ending 1: " + str(GotEnd1))
            print("Ending 2: " + str(GotEnd2))
            print("Ending 3: " + str(GotEnd3))
            print("Ending 4: " + str(GotEnd4))
            print("Ending 5: " + str(GotEnd5))
            print("Ending 6: " + str(GotEnd6))
            print("More endings coming soon™")
        elif command == "kitchen":
            print("You enter the kitchen. You cannot interact with it, for now. Soupman and Saltman are also here.")
            while True:
                print("What would you like to do? Commands: leave kitchen, talk")
                kommand = input(">")
                if kommand == "leave kitchen":
                    break
                elif kommand == "talk":
                    if GotFork:
                        if GotSaltSphere:
                            if GotBread:
                                print("It seems Saltman is too busy to talk")
                            else:
                                print("Saltman: Hey, there it is! The sphere of salt! Here, have this piece of bread as a thanks.")
                                sleep(3)
                                mixer.Channel(1).play(mixer.Sound('sound/pickup.wav'))
                                print("You have obtained the bread!")
                                GotBread = True
                                soupyanswers["add bread"] = addbread
                                soupyanswers["eat bread"] = eatbread
                                save()
                                sleep(3)
                        else:
                            print("Saltman: Add 53 salt shakes to the soup.")
                        if GotSoupSphere:
                            if GotGarlic:
                                print("It seems Soupman is too busy to talk.")
                            else:
                                print("Soupman: The sphere of soup! Can't believe i forgot it. Here, have this garlic clove as a thanks.")
                                sleep(3)
                                mixer.Channel(1).play(mixer.Sound('sound/pickup.wav'))
                                print("You have obtained the garlic!")
                                GotGarlic = True
                                soupyanswers["add garlic"] = addgarlic
                                soupyanswers["eat garlic"] = eatgarlic
                                save()
                                sleep(3)
                        else:
                            print("Soupman: Say soup 5 times.")
                    else:
                        print("Saltman: Hey, we are currenty making this kitchen usable to mortals")
                        sleep(3)
                        print("Soupman: We forgot some stuff we need in your head tho")
                        sleep(3)
                        print("Saltman: Can you do the stuff you did to summon us again?")
                        sleep(3)
                        print("Soupman: But with this fork.")
                        sleep(1)
                        mixer.Channel(1).play(mixer.Sound('sound/pickup.wav'))
                        print("You have obtained the fork!")
                        GotFork = True
                        soupyanswers["eat soup with fork"] = eatsoupwithfork
                        save()
                        sleep(3)
                if GotBread and GotGarlic:
                    soupyanswers["make garlic bread"] = makegarlicbread
                    soupyanswers["eat garlic bread"] = eatgarlicbread
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
