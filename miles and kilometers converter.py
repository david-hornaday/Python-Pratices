# David Hornaday

def start_screen():
    print()
    print("===========================")
    print("   Select a conversion")
    print("1: miles to Kilometers")
    print("2: Kilometers to miles")
    print("3: Exit Program")
    print("===========================")
    print()


def to_kilometers():
    get_miles = float(input("How many Miles do you wish to convert to Kilometers: "))
    print("Enter a number to convert")
    kilometers = get_miles * 1.609
    print()
    print(f"{get_miles} miles is {round(kilometers, 2)} Kilometers")
    print()


def to_miles():
    get_kilo = float(input("How many Kilometers do you wish to convert to Miles: "))
    miles = get_kilo * 0.6214
    print()
    print(f"{get_kilo} kilometers is {round(miles, 2)} miles")


def main():
    print()
    print("\tWELOCME")
    print("What Do You Wish to Convert")
    start_screen()

    while True:
        try:

            select = input("Your Selection: ")
            if select == "1":
                to_kilometers()
                again = input("Do you want to convert another value (y/n): ").lower()
                try:
                    if again != "y":
                        print("Goodbye")
                        break
                except ValueError:
                    print("Enter y or n")

            if select == "2":
                to_miles()
                loop = input("Do you want to convert another value (y/n): ").lower()
                try:
                    if loop != "y":
                        print("Goodbye")
                        break
                except ValueError:
                    print("Enter y or n")

            if select == "3":
                print("Goodbye")
                break
            else:
                print("Enter a number from the selection")
        except ValueError:
            print("Enter a number from the selection")
        start_screen()


if __name__ == "__main__":
    main()
