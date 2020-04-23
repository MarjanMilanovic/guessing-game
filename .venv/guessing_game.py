import random

yes_list = ["yes", "yea", "yup", "da", "yeah", "y", "mhm", "aha", "dap"]


def main():
    num = random.randint(0, 11)
    print("I'm thinking of a number between 1 and 10. Can you guess it?")
    user_input = input()

    try:
        user_input.isdigit()
        while num != user_input:
            if int(user_input) <= num:
                print("That number is to low.")
                user_input = float(input())
            else:
                print("That number is to high.")
                user_input = float(input())
        print(f"The number I was thinking about is: {num}.")
    except ValueError:
        print(f"{user_input} is not a number.\nWould you like to start again?")
        user_input = input()
        if user_input.lower() in yes_list:
            main()
        else:
            print("Thank you for playing. See ya around.")


main()
