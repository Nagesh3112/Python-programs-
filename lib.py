text = input("Enter the number of days late: ")
num = ""
for ch in text:
    if ch.isdigit():
        num = num + ch
if num == "":
    print("Please enter a number")
else:
    days = int(num)

    if days == 0:
        print("No fine")
    elif days <= 5:
        print("Fine = Rs. 0.50")
    elif days <= 10:
        print("Fine = Rs. 1.00")
    elif days <= 30:
        print("Fine = Rs. 5.00")
    else:
        print("Membership cancelled")