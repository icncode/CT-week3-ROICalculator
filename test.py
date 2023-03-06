import os

# Create class for ROI
class ROI_Calculator:
    total_monthly_income = 0
    total_monthly_expenses = 0
    total_monthly_cash_flow = 0
    
    # Create constructor for ROI
    def __init__(self):
        self.income = None
        self.expenses = None
        self.cash_flow = None
        self.cash_ROI = None

    # Calculates the income with the given parameters
    def calc_income(self, rental, laundry, storage, misc):
        total_monthly_income = rental + laundry + storage + misc
        self.income = total_monthly_income

    # Calculates the total expenses with the given parameters
    def calc_expenses(self, tax, insurance, utilites, hoa, snow, vacancy, repairs, capEx, management, morgage):
        total_monthly_expenses = tax + insurance + utilites + hoa + snow + vacancy + repairs + capEx + management + morgage
        self.expenses = total_monthly_expenses

    # Calculates the total cash flow with the given parameters
    def calc_cash_flow(self):
        total_monthly_cash_flow = self.income - self.expenses
        self.cash_flow = total_monthly_cash_flow

    # Calculates the cash-on-cash Return On Investment (ROI), returns percentage
    def calc_cash_ROI(self, down_payment, closing_costs, rehab, misc):
        # Gets annual cash flow from monthly
        annual_cash_flow = self.cash_flow * 12
        self.annual_cash = annual_cash_flow 
        # Sums everything in total investments
        total_investment = down_payment + closing_costs + rehab + misc
        self.investment = total_investment
        # Calculates annual return cash-on-cash (ROI)
        if self.investment == 0:
            self.ROI = 0
        else:
            cash_ROI = (self.annual_cash / self.investment)* 100
            self.ROI = cash_ROI


def run_ROI():
    choice = '2'
    change = 'y'
    # Greeting user
    os.system('cls') # Clears the terminal
    print("Hello, welcome to the Rental Income Calculator!\nPlease enter all values without commas, symbols, or currencies.\n")
    calc = ROI_Calculator()
    # Keep looping until user enters 1
    while choice != '1':           
        
        # Calculating income
        # Keep looping until user does not want to change values
        while change != 'n':
            try: # If no errors, continue to break
                rental = float(input("What is your monthly rental income? "))
                laundry = float(input("What is your laundry income? "))
                storage = float(input("What is your storage income? "))
                misc = float(input("What are your miscellaneous incomes? "))
                change = input("Would you like to change your entries? (y/n) ").strip(' es').lower()
            except ValueError:
                os.system('cls') # Clears the terminal
                print("Please enter only a number.")
                continue # Restart loop
            break # Exit loop
        change = 'y'
        # Adding all income and returning total
        calc.calc_income(rental, laundry, storage, misc)
        os.system('cls') # Clears the terminal
        print(f"\nMonthly income: ${calc.income:.2f}\n")

        change = 'y' # Reset change to loop through while for wrong entries
        # Calculate expenses
        while change != 'n':
            try: # If no errors, continue to break
                tax = float(input("What is the monthly tax cost on the rental property? "))
                utilites = float(input("What are the utilities costs? "))
                insurance = float(input("What are the insurance costs? "))
                hoa = float(input("What are the Home Ownership Assistance costs? "))
                snow = float(input("What costs are associated with snow and lawn care? "))
                vacancy = float(input("What are the vacancy costs? "))
                repairs = float(input("What are the repairs costs? "))
                capEx = float(input("What are the capital expenses? "))
                management = float(input("What are the management costs? "))
                morgage = float(input("What are the morgage costs? "))
                change = input("Would you like to change your entries? (y/n) ").strip(' es').lower()
            except ValueError:
                os.system('cls') # Clears the terminal
                print("Please enter only a number.")
                continue # Restart loop
            break # Exit loop
        # Adding all expenses and returning total
        calc.calc_expenses(tax, insurance, utilites, hoa, snow, vacancy, repairs, capEx, management, morgage)
        os.system('cls') # Clears the terminal
        print(f"Monthly expense: ${calc.expenses}")
        
        # Calculate cash flow
        calc.calc_cash_flow()
        print(f"\nMonthly cash flow: ${calc.cash_flow:.2f}\n")

        change = 'y' # Reset change to loop through while for wrong entries
        # Calculate cash-on-cash Return On Investment (ROI)
        while change!= 'n':
            try: # If no errors, continue to break
                down_payment = float(input("What is your down payment? "))
                closing_costs = float(input("What is your closing costs? "))
                rehab = float(input("What is your rehababilitation costs? "))
                misc = float(input("What is your miscelleanous costs? "))
                change = input("Would you like to change your entries? (y/n) ").lower().strip(' es')
            except ValueError:
                os.system('cls') # Clears the terminal
                print("Please enter only a number.")
                continue # Restart loop
            break # Exit loop   
        calc.calc_cash_ROI(down_payment, closing_costs, rehab, misc)
        os.system('cls') # Clears the terminal
        print(f"\nAnnual Cash Flow: ${calc.annual_cash}\nTotal Investment: ${calc.investment}\n________________________________________\nCash-On-Cash Return On Investment: {calc.ROI:.2f}%\n")

        while choice != '1':
            # Ask user if they want to continue
            choice = input("""\n(1) quit
(2) restart the program
(3) reveiew results

Would you like to do? """)
            if choice == '1':
                break
            elif choice == '2':
                calc = ROI_Calculator()
                os.system('cls') # Clears the terminal 
                break
            elif choice == '3':
                view = '8'
                os.system('cls') # Clears the terminal
                while view != '1':
                    view = input("""\n(1) return to last menu
(2) monthly income
(3) monthly expenses
(4) monthly cash flow
(5) annual cash flow
(6) total investment
(7) monthly cash-on-cash ROI

What would you like to see? """)
                    if view == '2':
                        print(f"\nMonthly income: ${calc.income:.2f}\n")
                    elif view == '3':
                        print(f"\nMonthly expenses: ${calc.expenses:.2f}\n")
                    elif view == '4':
                        print(f"\nMonthly cash flow: ${calc.cash_flow:.2f}\n")
                    elif view == '5':
                        print(f"\nAnnual cash flow: ${calc.annual_cash:.2f}\n")
                    elif view == '6':
                        print(f"\nTotal investment: ${calc.investment:.2f}\n")
                    elif view == '7':
                        print(f"\nMonthly cash-on-cash ROI: ${calc.ROI:.2f}%\n")
                    else:
                        os.system('cls') # Clears the terminal
                        print("Please enter a valid option.")
            else:
                os.system('cls') # Clears the terminal
                print("Please enter a valid option.")
            
        os.system('cls') # Clears the terminal            
                          
run_ROI()

