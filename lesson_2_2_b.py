#Task 1: Code Correction

#You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.



attendees = input("Enter number of attendees: ")
if attendees > '100':
    venue = ("large hall") 
else: 
    venue =  "conference room"
print(venue)

#Task 2: Catering Choices

#Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers" using an inline if else statement.

print("Do you want vegetarian food?")
choice = input("Yes or No?")
if choice == 'Yes':  
    print("I recommend 'Veggie Delight Centers'")
if choice == 'No':
    print("I recommend 'Gourmet Meals Caterers")