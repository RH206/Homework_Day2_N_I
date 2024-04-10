#Lesson_2_1_b. Nested Decisions: The Adventure Game

#Task 1: Code Correction 
#You are provided with a Python script that is supposed to guide a 
# user through an adventure game, but it has some errors. Identify and fix them.

place = input("Choose a place forest or cave? ")

if place == 'forest':
    action = input("climb a tree or cross a river?")
    if action == 'climb a tree':
        print("You found a bird's nest!")
    if action == 'cross a river':
        print("You found a boat!")
if place == 'cave':
    print("You find a hidden treasure!")

#Task 2:Setting the Scene
#Based on the corrected code from Task 1, expand the game. 
# If the user chooses "cave", ask them if they want to "light a torch" 
# or "proceed in the dark", and provide outcomes for each decision.

if place == 'cave':
    action = input("Do you want to light a torch?")
    if action == 'yes':
        print("You illumanate a new path to discover even more treasure!")
    if action == 'no':
        print("In the darkness you hear a growl and are eaten by a bear!") 
#Task 3:Default Path
#If the user makes an invalid choice at any point, use the "pass" statement for now. 
# Later, you can enhance this to provide feedback or a different branch of the story.

pass