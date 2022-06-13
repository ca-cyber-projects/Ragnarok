#Finance program
#Author: Christian Atkins
#Date: Monday, June 6th 2022

#import math

#compound interest rate
def funct():
 
    print("Compound Interest Calculator")
    #get variables
    p = int(input('Principal: '))
    r = float(input('Interest rate: '))
    n = int(input('Number of times interest applied per time period: '))
    t = int(input('Number of time periods elapsed: '))

    #change interest rate to percent
    i = r*.01

    #compount interest formula
    a = p*(1+(i/n))**(n*t)

    print("----------------------------------------------")
    print("Total Owed: $", round(a, 2))
    print("Principal $", p)
    print("Interest: $", round(a-p, 2))
    print("Interest Rate:", i, "%")
    return

#ROI
def funct2():

    print("ROI Calculator")
    #get input
    i = float(input("Initial Value of Investment: "))
    f = float(input("Final Value of Investment: "))
    c = float(input("Cost of Investment: "))

    #calculate roi % and $
    roi = ((f-i)/c)*100
    ROI = f-c

    print("----------------------------------------------------")
    print("Your ROI:", round(roi, 2), "% or $", round(ROI, 2))
    return

#net worth
def funct3():

    print("Net Worth Calculator")
    a = float(input("Enter Assets: "))
    l = float(input("Enter Liabilities: "))
    n = a - l
    print("----------------------------------------------------")
    print("Your net worth is: $", round(n, 2))
    return

#mortgage
def funct4():

    print("Mortgage Calculator")
    h = float((input("Enter House Value: ")))
    d = float((input("Down Payment Percent: ")))
    d = d * 0.01
    
    i = float((input("Enter Interest Rate: ")))
    i = i * 0.01
    l = h - (h*d)
    t = l * (1+i)
    print("----------------------------------------------------")
    print("Your loan amount is: $", round(l, 2))
    print("Your total interest paid is: $", round(l, 2))
    print("Your loan plus interest is: ", round(t, 2))
    return

#dividend caldulator
def funct5():

    print("Dividend Payout Calculator")
    price = float((input("Enter Stock Price: ")))
    eps = float((input("Enter Earnings Per Share: ")))
    print(eps)
    shares = float((input("Enter Number of Shares You Own: ")))
    payout = price / eps
    print("----------------------------------------------------")
    print("You can expect $", round(payout, 2), "in dividends")
    return

#rule of 72
def funct6():

    print("Rule of 72 Calculator")
    r = float(input("Enter your rate of return: "))
    rule = 72/(r)
    print("----------------------------------------------------")
    print("It will take ", round(rule, 2), "years to double your money")


#true rich formula
def funct7():

    print("True Rich Formula")
    e = float(input("Enter your total yearly expenses (budgeted and all others): "))
    tr = e * 25
    print("----------------------------------------------------")
    print("To be truly rich, you will need $", round(tr, 2), " invested at an average 4% return.")


#True cost of stuff
def funct8():

    print("True Cost of Stuff Calculator")
    name = str(input("Enter the item name: "))
    print("Enter the cost of", name, ": ")
    i = float(input())
    a = i /.04
    print("----------------------------------------------------")
    print("In order for your investments to pay for", name, "you will need $", round(a, 2), "invested (assuming a 4% rate of return)")

def main():
    #select which program to run
    print("Select calculator:")
    print("1: Compound Interest - Total owed for investments, loans, credit cards, etc.")
    print("2: Return on Investment - How much will your investment generate?")
    print("3: Net Worth - How much money am I worth?")
    print("4: Mortgage - Calculate the payments on a mortgage")
    print("5: Dividend Payout - How much money will I recieve in dividends?")
    print("6: Rule of 72 - How long does it take to double your money?")
    print("7: True Rich Formula - How much do you need invested to live (at your current lifestyle) forever?")
    print("8: True Cost of Stuff - How much do you need invested for in order to pay for stuff with your investments?")
    x = input("> ")
    print("----------------------------------------------------")
    match x:
        case "1":
            funct()
        case "2":
            funct2()
        case "3":
            funct3()
        case "4":
            funct4()
        case "5":
            funct5()
        case "6":
            funct6()
        case "7":
            funct7()
        case "8":
            funct8()

main()
