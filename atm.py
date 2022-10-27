from os import curdir
from tkinter import W
from unittest import expectedFailure
from cardHolder import cardHolder

def print_menu():
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Pay for mobile phone")
    print("5. Exit")

def deposit(cardHolder):
    try:
        deposit = float(input("How much $$ would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Your new balance is: ", str(cardHolder.get_balance()))
    except:
        print("Invalid input")

def withdraw(cardHolder):
    try:
        withdraw = float(input("How much $$ would you like to withdraw"))
        if (cardHolder.get_balance() < withdraw):
            print("Not enough money")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("You're good to go! Thank you")
    except:
        print("Invalid input")

def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance(), "$")

def pay_for_phone(cardHolder):
    try:
        phone = int(input("Type your phone number: "))
        pay_for_phone = float(input("How much money would you like to pay for your phone?"))
        if (cardHolder.get_balance() < pay_for_phone):
            print("Not enough money")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - pay_for_phone)
            print("Operation finished successfully! You paid ", pay_for_phone, "$ for phone number: ", phone)
    except:
        print("Invalid input")


if __name__ == "__main__":
    current_user = cardHolder("", "", "", "", "")

    ### Create a repo of cardholders

    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("4278320021135321", 1234, "Ikromjon", "Akhmadjonov", 0))
    list_of_cardHolders.append(cardHolder("8600490487880809", 2003, "Ikromjon", "Akhmadjonov", 0))

    ### Promt user for devit card number
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if (len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card num not recognised. Please try again")    
        except:
            print("Card num not recognised. Please try again")

## Promt for PIN
while True:
    try:
        userPin = int(input("Please enter your pin: ").strip())
        if(current_user.get_pin() == userPin):
            break
        else:
            print("Invalid PIN")
    except:
        print("invalid PIN")

## Print options
print("Welcome ", current_user.get_firstName(), " :)")
option = 0
while (option != 5):
    print_menu()
    try:
        option = int(input())
    except:
        print("Invalid input. Please try again.")

    if (option == 1):
        deposit(current_user)
    elif (option == 2):
        withdraw(current_user)
    elif (option == 3):
        check_balance(current_user)
    elif (option == 4):
        pay_for_phone(current_user)
    elif (option == 5):
        break
    else:
        open = 0

print("Thank you. Have a nice day")