# hangman 
# this is the introduction
intro=input("hi. you are playing a harry potter themed hangman. what is your name? ")
print("hello " + intro +".")
# if you dont input people, places, and general, it will ask you to input again
def fun():
  modes=input("please select your mode. the modes are: people, places, and general. ")
  if (modes!="people" and modes!="places" and modes!="general"):
    print("do it again ")
    fun()
# what mode do you wanna play-general, people, places
  elif modes =="people":
    print("Okay, you have selected the mode people. you have 9 chances to be wrong")
  elif modes==("places"):
    print("Ok you have selected the mode places. You have 9 chances to be wrong")
  elif modes==("general"):
    print("Ok you have selected the mode general. You have 9 chances to be wrong")

fun()

# THIS IS PEOPLE MODE
# this will chose a random person from the list below 
import random

# these are variables 
chances=9
guesses=[]
win=0
guess=''
repeat=0

# this is the list of possibilities that you would have to find
people=["harry potter", "hermione granger", "ron weasley", "hagrid", "nagini", "draco malfoy", "dumbledore", "dobby", "james potter", "sirius black", "sorting hat", "luna lovegood", "bellatrix lestrange", "neville longbottom", "lupin", "tonks"]
x = random.randint(0, len(people)-1)
secretname=people[x]
print(secretname)
# this prints the dashes for the number of letter in secretname everytime you guess, and if you get letters correct, it replaces the dash with a letter
progress = ""
for letter in secretname:
  progress = "_ " + progress
  print("_ ")
#this tells you to start guessing
while win==0:
  letter_in_person =input("Okay, now please guess the letters of the name of the person you have "+str(chances)+" chances ")
  if letter_in_person in guesses:
    print("you already guessed this")

  else:
    repeat = 0
# this says that if a letter you guess is used multiple times in secretname, your guess will count for all of the times it is in the secretname
  for x in range(len(secretname)):
    if secretname[x] == letter_in_person:
      repeat+=1
      progress = progress[:x*2] + secretname[x] + progress[x*2 + 1:]

# this is if your guess is one of the letters in the secretname, then it will print the letter
  if letter_in_person in secretname:
    print(letter_in_person)

# else you lose a chance if it isn't one of the letters 
  else:
    chances -= 1
    print("sorry, that is not one of the letters in the name. you have "+str(chances)+" more chances. ")

  print(progress)

# this puts your correct guess in a list  
for x in range(repeat):
    guesses.append(letter_in_person)

# if the amount of correct guess is equal to the letters in the secretname, then win=1 meaning you won
  if len(secretname)==len(guesses):
    win=1
    print("great job, you got it!")
# you lose if you run out of chances and then win=2
  if chances==0:
    win=2
    print('sorry, you ran out of chances. you lose')
