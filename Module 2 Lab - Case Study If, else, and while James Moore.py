#James Moore
#FileName: Module 2 Lab - Cast Study If, else, and while James Moore.py
#This app tests whether student are elligible for honors based upong their GPA 

def main():
    #Welcome message
    print("Welcome to Student GPA Tester. This program will check you students GPA and see if they are eligible for the Dean's List or the Honor Roll." \
    "(Enter 'ZZZ' for the student's last name to quit)")

    while True: 
        #Request and acquire student's Last name
        last_name = input("\nPlease enter a student's last name: ")

        #End process if 'ZZZ' is entered as the last name
        if last_name.upper() == 'ZZZ' :
            break

        #Request and acquire student's first name
        first_name = input("Please enter that student's first name: ")

        #Request and acquire student's GPA as a float
        try:
            gpa = float(input(f"Please enter the GPA for {first_name} {last_name}: "))
        except ValueError:
            print("Input is invalid! Please enter the student's GPA as a number only!")
            continue

        status = "No Honors"

        #Test if GPA qualifies for the Dean's list (3.5 or higher)
        if gpa >= 3.5:
            status = "Dean's List"
            print(f"***** {first_name} {last_name} qualifies for the Dean's List! *****")

        #Test if GPA qualifies for the Honor Roll (3.25 or higher)
        elif gpa >= 3.25:
            status = "Honor Roll"
            print(f"*** {first_name} {last_name} qualifies for the Honor Roll! ***")

        else:
            print(f"{first_name} {last_name} does not qualify for honors this term.")

if __name__ == "__main__":
    main()