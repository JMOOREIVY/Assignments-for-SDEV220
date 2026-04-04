#James Moore   
#SDEV220-50P
#Module 3 Programming Assignment - Lists and Functions

#7.4 Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
things = ["mozzarella", "cinderella", "salmonella"]

#7.5 Capitalize the element in things that refers to a person and then print the list. 
things[1] = things[1].capitalize()
print(things)
#Did it change the element in the list? Yes, because Cinderella is the only person in the list, and the 1 is where the Cinderella is on on the list

#7.6 Make the cheesy element of things all uppercase and then print the list.
things[0] = things[0].upper()
print(things)
#The cheesy element is mozerella as in mozarella cheese, so it will now print as MOZZARELLA

#7.7 Delete the disease element from things, collect your Nobel Prize, and print the list.
del things[2] #deletes salmonella from the list
print("Nobel Prize Collected") #Since we now completely eliminated the disease
print(things)


#9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].

def good(): #Defines the function and what will be delivered 
    return ["Harry", "Ron", "Hermione"]

#9.2 Define a generator function called get_odds() that returns the odd numbers from range(10). 
def get_odds():
    for number in range(10):
        if number % 2 != 0:
            yield number

# Use a for loop to find and print the third value returned.
count = 1 
for number in get_odds():
    if count == 3:
        print(number)
        break
    count += 1
