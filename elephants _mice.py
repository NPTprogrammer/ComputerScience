"""
Title: mice_and_elephants.py

Description: The user is asked if they will be entering pounds or kilograms into
             the conversion calculator

            The user is then asked to enter a weight in numerals

            The number is printed in its  equivelent animal weights

            Weights are:

                elephants (Loxodonta africana) (weight is the average value of
                the bull elephant weight range)
                    4050 kg

                house mice (Mus musculus) 
                    42 g

                conversion of 1 lb to a kiolgram
                
                    0.45359237

Author: Nathan Tonning

Date: February 25, 2023

License: CC-BY Nathan Tonning

LIKE, SHARE, SUBSCRIBE!
"""

ELEPHANT = 4050000 #mass in grams
MOUSE = 42 #mass in grams
CONV_LB_KG =  0.45359237 #the equivalent kg to one lb

def main():
    print("Hello! (^_^) ") 
    print("  This program accepts a weight or mass and prints the corresponding")
    print("  number of elephant and mouse weights that are contained in the")
    print("  given value.")
    print()
    print(f"  For the record: one elephant weighs {ELEPHANT / 1000} kg")
    print(f"  one mouse weighs {MOUSE / 1000} kg")
    print(f"  which means that one elephant weighs as much as approximately")
    print(f"  {ELEPHANT // MOUSE} mice")
    print()
    
    choices = ["#","lb","kg","k"] #The sequence of values is important in this
                                  #list; do not alter
    choice = ""

    value = 0.0

    while(choice != "q"):
        print("\tUnit of choice: [# or lb for pound, kg for kilogram]")
        print("\tq to quit")
        choice = str(input("> "))

        if(choice in choices):
            if(choice in choices[0:2]):
                print("You chose pounds!")

                #Get the value and convert to grams
                value = float(input("Enter weight in lbs > ")) * CONV_LB_KG * 1000
                    
            elif(choice in choices[2:]):
                print("You chose kilograms!")

                #Convert value to grams
                value = float(input("Enter weight in kg > ")) * 1000

            print("Putting mice and elephants on the scale... o~o")
            print()

            print("Results")
            print("Your weight in equivalent elephants and mice is:")

            print(int(value // ELEPHANT),"elephant/s")
            print(int(value % ELEPHANT // MOUSE), "mouse/mice")
            

            print()
            print("Want to play again? 0_0")
            print()

        elif(choice == "q"):
            print("Good bye! \^O^/")


if __name__ == "__main__": main()

