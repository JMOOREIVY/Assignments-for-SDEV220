#James Moore SDEV220-50P Module 2 Programming Assignment - Loops and Conditionals

#4.1 Choose a number between 1 and 10 and assign it to the variable secret. 
# Then, select another number between 1 and 10 and assign it to the variable guess. 
# Next, write the conditional tests (if, else, and elif) to print the string 'too low' if guess is less than secret,
#  'too high' if greater than secret, and 'just right' if equal to secret.

secret = 2
guess = 6
if guess < secret:
    print("Too Low")
elif guess > secret:
    print("Too High")
else:
    print("Just Right")

#4.2 Assign True or False to the variables small and green. 
# Write some if/else statements to print which of these matches those choices: cherry, pea, watermelon, pumpkin.

small = True
green = True

if small:
    if green:
        print("Pea")
    else:
        print("Cherry")
else:
    if green:
        print("Watermelon")
    else:
        print("Pumpkin")

#6.1 Use a for loop to print the values of the list [3, 2, 1, 0].

number = [3, 2, 1, 0]

for x in numbers: 
    print(x)

#6.2 Assign the value 7 to the variable guess_me, and the value 1 to the variable number. 
# Write a while loop that compares number with guess_me. Print 'too low' if number is less than guess me. 
# If number equals guess_me, print 'found it!' and then exit the loop. 
# If number is greater than guess_me, print 'oops' and then exit the loop. 
# Increment number at the end of the loop.

guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("Too Low")
    elif number == guess_me:
        print("Found It!")
        break
    else:
        print("OOPS")
        break
    number += 1


#6.3 Assign the value 5 to the variable guess_me. Use a for loop to iterate a variable called number over range(10). 
# If number is less than guess_me, print 'too low'. If it equals guess_me, print found it! and then break out of the for loop. 
# If number is greater than guess_me, print 'oops' and then exit the loop.

guess_me = 5 

for number in range(10):
    if number < guess_me:
        print("Too Low")
    elif number == guess_me:
        print("Found it!")
        break
    else:
        print("OOPS")
        break 
