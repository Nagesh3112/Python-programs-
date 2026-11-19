amt=int(input("Enter the amount to be withdrawn in hundereds:"))
hundred = amt // 100
amt = amt % 100
fifty = amt // 50
amt = amt % 50
tens =amt // 10
amt = amt % 10
print("Number of 100 rupees note :",hundred)
print("Number of 50 rupees note  :",fifty)
print("Number of 10 rupees note :",tens)