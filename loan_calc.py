def main():
    print ("Welcome to the loan payment calculator!\n")
    prince = get_prince()
    an_rate = get_an()
    years = get_years()
    month_pay = calc_month_pay(prince, an_rate, years)
    dis_res(prince, an_rate, years, month_pay)

def get_prince():
    while True:
        prince = float(input("\nEnter the loan's principal amount($): "))
        if prince >= 0:
            return prince
        else:
            print ("Error, try again.")

def get_an():
    while True:
        an_rate = float(input ("\nEnter the loan's anual intrest rate(in %. ex. 5.0 = 5%): "))
        if an_rate >= 0:
            return an_rate
        else:
            print ("Error, try again.")

def get_years():
    while True:
        years = int(input("\nEnter the loan term in years: "))
        if years >= 0:
            return years
        else:
            print ("Error, try again.")

def calc_month_pay(prince, an_rate, years):
    month_rate = an_rate / 12 / 100
    pay_num = years * 12
    month_pay = (prince * month_rate) / (1 - (1 + month_rate)^(-pay_num))
    return month_pay

def dis_res(prince, an_rate, years, month_pay):
    total_pay = years * 12
    total_am = month_pay * total_pay
    print ("Loan Payment Summary:")
    print (f"\nLoan Principal: ${prince:.2f}")
    print (f"\nLoan Anual Intrest: {an_rate:.1f}%")
    print (f"\nLoan Term: {years} years")
    print (f"\nLoan Monthly Payment: ${month_pay:.2f}")
    print (f"\nLoan total payment: ${total_am:.2f}")

main()