print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("Yes, you can ride")
    age = int(input("What is your age? "))
    ticket = (input("How many tickets would you like?"))
    tickets = int(ticket)
    bill = 0
    if age <= 12:
        bill = 5
        print("Child tickes are £5 ")
    elif age <= 18:
        bill = 7
        print("Youth tickets are £7 ")
    else:
        bill = 12
        print("Adult tickets are £12 ")
    ticket_bill = tickets * bill
    # print(ticket_bill)

    wants_photo = input("Do you want a photo? Answer Y or N: ")
    if wants_photo == "Y":
        ticket_bill += 3
        print("Photo costs £3")

    print(f"Your total ticket price is £{ticket_bill}")

else:
    print("Sorry you cannot ride")
