from time import sleep

#ingridients 
soup = """
 \##############/
  \____________/"""
salt= """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣶⣦⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣾⣿⣿⡿⠟⠋⣡⣽⡳⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⠛⢿⣷⣴⣿⣷⡹⣿⣿⣞⣆⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠴⣾⣿⡿⢋⣉⣿⣿⠻⣿⣷⡈⢿⣿⣿⣿⣷⡘⣿⣿⡞⡄
⠀⠀⠀⠀⠀⠀⢸⡟⠳⣮⢻⣧⡘⠿⣿⣿⡸⠝⢿⣿⡌⠟⣉⣬⣿⣿⣿⣿⡇⠇
⠀⠀⠀⠀⠀⠀⢸⠀⠀⠈⠷⡹⣿⣶⡄⠹⣧⠰⣦⣹⣿⣾⣿⣿⣿⣿⣿⢿⡇⡀
⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠱⡹⣿⠋⣰⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⠿⠚⢡⠃
⠀⠀⠀⠀⠀⠀⠘⡀⣽⣦⠀⠀⢱⢹⣿⣿⡿⠟⠋⢹⣻⡽⠿⠛⢉⠠⠔⠊⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠱⡈⠇⠡⠀⠀⡆⣿⣟⣠⠴⠚⠉⣀⠤⠒⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠤⡀⠀⠑⣌⠂⠀⢀⣇⠇⠉⣀⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⠊⠁⠀⠈⠰⢄⠈⠙⠿⠻⠞⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣊⡁⠀⠀⠀⠀⠀⠀⠗⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠒⠁⠒⠒⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

#list of soupy answers
soupyanswers = ["eat soup", "eat", "eat the soup", "soup", "add salt"]
soupyanswerswithnosoup = ["eat soup", "eat", "eat the soup"]

#soupy functions
 def eatsoup():
  print("U were dumb, the soup was poisoned, like all soup is, so u ded now"

 def die():
  print("You die a soupy death, and ascend into the Eternal Sea, and meet Crab God, and rave.")
  print("                                     THE END.(end 1 of ?)                           ")
  e1=True
 def live():
  print("The soup was initially poisoned, like all soup is, but the salt neutralized it however the salt was poisoned so you died")
  print("                                                THE END.(end 2 of ?)                                                    ")
  e2=True
 def saltydeath():
  print("you ate way too much salt and died a salty death. you ascend into the Eternal sea, meet Crab God, and rave till the end of time")
  print("                                                   THE END.(end 3 of ?)                                                        ")
  e3= True
 def SaltMan():
  print("You put so much salt that you became Salt Man, nothing can hurt Salt Man, so you survived the poisoned soup")
  print("                                       THE END.(end 4 of ?)                                                ")
  e4= True   
 def secret():
  print("You cannot avoid death meanie")
  print("     THE END.(end 5 of 5)    ")
#the eating
print("Eat the soup.")
print(soup)
answer1 = 0
soupeaten = False

while answer1 not in soupyanswerswithnosoup: #loop of soup
  answer1 = input(">")

  if answer1 not in soupyanswers:
    print("Not an option you dumdum")
  else:
    if answer1 == "soup":
      print("soup") #soup
      if answer1 =="add salt":
      print(salt)
      salty=int(input("how many salt shakes dumbass?"))
        if salty <= 9:
        eatsoup()
        die()
        if salty >=9 and salty <=19:
        live()
        if salty >=20 and salty != 53:
        saltydeath()
        if salty = 53:
        
        else:
         print("you dummy dum, im just asking for a number, is that too hard for you?") 
       else:
         soupeaten = True
if e1= True and e2=True and e3=True 
#soupy death
if soupeaten:
  eatsoup() #consumption
  print("say \"die\" to ascend")
  answer2 = 0

  while answer2 != "die": #loop of soup 2: dead boogaloo
    answer2 = input(">")

    if answer2 != "die":
      print("Not an option you dumdum")
    else:
      die() #very dead
      sleep(3)
