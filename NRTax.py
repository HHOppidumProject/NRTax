# Nova Roma tax calc

def calculate():
    tax = 0
    salary = float(input("How much money do you earn in dollars? "))
    takehome = salary

    if takehome >= 15000:
        tax += round(((takehome-15000)*0.25), 2)
        takehome = takehome - tax
        if takehome >= 25000:
            tax += round(((takehome-25000)*0.275), 2)
            takehome = takehome - round(((takehome-25000)*0.275), 2)
            if takehome >= 35000:
                tax += round(((takehome-35000)*0.3), 2)
                takehome = takehome - round(((takehome-35000)*0.3), 2)
                if takehome >= 40000:
                    tax += round(((takehome-40000)*0.4), 2)
                    takehome = takehome - round(((takehome-40000)*0.4), 2)
                    if takehome >= 70000:
                        tax += round(((takehome-70000)*0.5), 2)
                        takehome = takehome - round(((takehome-70000)*0.5), 2)
                        if takehome >= 100000:
                            tax += round(((takehome-100000)), 2)
                            takehome = takehome - round(((takehome - 100000)), 2)

    print("You take home: $"+str(round(takehome, 2)), "per annum")
    print("You pay in tax: $"+str(tax), "per annum")
    print()
    print("You take home: $"+str(round(takehome/12 , 2)), "per month")
    print("You pay $"+str(round(tax/12, 2)), "in taxes per month")

while input("Would you like to quit? [y/n] ").lower() != "y":
    calculate()
