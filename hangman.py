#Imports
import random

#Opening
print("Welcome to Hangman , i am guessing you already know the rules of this popular game so not spending time explaining .")
print("Still if someone doesnt , they can go watch https://www.youtube.com/watch?v=cGOeiQfjYPk , this is inherently hangman but vs ai .")
print()
print("Starting the game")
print()

#Hangman versions
hangmans = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
            "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 

#Word Bank and choice 
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

word = random.choice(words)

#Predefined Variables
_choice = []
i = 0
hangman = 0
#Start
chars = len(word)
for m in range(chars):
    _choice.append("_")
    
print("Word Chosen by the ai : ",_choice)
print("Current hangman progress :- ")
print(hangmans[0])
print()
while("_" in _choice):
    while (hangman < 6 ):
        choice = ""
        choice = input("Choose your character : ")
        index = word.rfind(choice)
        if(index != -1):
            print("Your guess was correct !")
            print()
            _choice.insert(index+1,choice)
            _choice.pop(index)
            print("Current hangman progress :-")
            print(hangmans[hangman])
            print()
            print("Current word progress :-",_choice)
        elif(index == -1):
            print("Your guess was wrong !")
            hangman += 1
            print("Current hangman progress :-")
            print(hangmans[hangman])
            print()
            print("Current word progress :-",_choice)
        if(hangman == 6):
            break
    if(hangman == 6):
        break

print("████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗    ███████╗ ██████╗ ██████╗     ██████╗ ██╗      █████╗ ██╗   ██╗██╗███╗   ██╗ ██████╗")
print("╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██║████╗  ██║██╔════╝") 
print("   ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗    █████╗  ██║   ██║██████╔╝    ██████╔╝██║     ███████║ ╚████╔╝ ██║██╔██╗ ██║██║  ███╗")
print("   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║    ██╔══╝  ██║   ██║██╔══██╗    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██║██║╚██╗██║██║   ██║")
print("   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║    ██║     ╚██████╔╝██║  ██║    ██║     ███████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝")
print("   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ")
                                                                                                                                           