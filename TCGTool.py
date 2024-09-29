class TCGTOOL:
    def __init__(self):
        print("Welcome To Jerome's TCGTOOL")
        self.items = []

    def add_item(self):
        item_name = input("Enter Item Name: ")
        item_price = float(input("Enter Item Price: "))
        coupon = input("Did You Have A Coupon (y/n): ").lower()
        discount = 0

        if coupon == 'y':
            discount = float(input("Enter Discount Percentage: "))

        discount_amount = item_price * (discount / 100)
        final_price = item_price - discount_amount + 2.98
        tax_price = final_price * 1.1

        sell = input("Are You Planning To Sell This Item (y/n): ").lower()
        profit_marketplace = 0
        profit_margin = 0

        if sell == 'y':
            marketplace = input("Which Marketplace (f/e): ").lower()
            sell_price = float(input("Enter Sell Price: $"))
            if marketplace == 'f':
                profit_marketplace = sell_price - tax_price
            elif marketplace == 'e':
                profit_marketplace = (sell_price - tax_price) * 0.85
            profit_margin = (profit_marketplace / tax_price) * 100
        else:
            sell_price = 0

        item_summary = {
            'item': item_name,
            'price': item_price,
            'discount': discount,
            'discount_amount': discount_amount,
            'final_price': final_price,
            'tax_price': tax_price,
            'sell_price': sell_price,
            'profit_marketplace': profit_marketplace,
            'profit_margin': profit_margin
        }

        self.items.append(item_summary)

    def calculate_totals(self):
        total_final_price = sum(item['final_price'] for item in self.items)
        total_tax_price = sum(item['tax_price'] for item in self.items)
        total_profit_marketplace = sum(item['profit_marketplace'] for item in self.items)
        return total_final_price, total_tax_price, total_profit_marketplace

    def display_summary(self):
        for item in self.items:
            print(f"\nItem: {item['item']}")
            print(f"Original Price: ${item['price']:.2f}")
            print(f"Discount: {item['discount']:.2f}%")
            print("Price Breakdown:")
            print(f"Item Price: ${item['price']:.2f}")
            print("Buyee Purchase Fee: $2.98")
            print(f"Discount Amount: ${item['discount_amount']:.2f}")
            print(f"Discount Price: ${item['price']:.2f} * {item['discount']:.2f}% = ${item['price'] - item['discount_amount']:.2f}")
            print(f"Final Price Before Tax: ${item['final_price']:.2f}")
            print(f"Final Price Including Tax: (${item['price'] - item['discount_amount']:.2f} + $2.98) * 1.1 = ${item['tax_price']:.2f}")
            if item['sell_price'] > 0:
                print(f"Sell Price: ${item['sell_price']:.2f}")
                print(f"Profit on Sale: ${item['profit_marketplace']:.2f}")
                print(f"Profit Margin: {item['profit_margin']:.2f}%")

        total_final_price, total_tax_price, total_profit_marketplace = self.calculate_totals()
        total_tax_price_with_shipping = total_tax_price + 40  # Adding $40 for shipping
        total_profit_after_shipping = total_profit_marketplace - 40  # Subtracting $40 for shipping from total profit
        total_profit_margin = (total_profit_after_shipping / total_tax_price_with_shipping) * 100 if total_tax_price_with_shipping != 0 else 0

        print(f"\nTotal Final Price Before Tax: ${total_final_price:.2f}")
        print(f"Total Final Price Including Tax: ${total_tax_price:.2f}")
        print(f"Total Final Price Including Tax and Shipping ($40): ${total_tax_price_with_shipping:.2f}")
        print(f"Total Profit on All Sales After Shipping: ${total_profit_after_shipping:.2f}")
        print(f"Total Profit Margin: {total_profit_margin:.2f}%\n")

class Capital:
    @staticmethod
    def capitalize_all(text):
        return text.upper()

class Description:
    @staticmethod
    def title():
        pname = input("Enter The Card Name: ")
        pseries = input("Enter The Series (Abbreviation Eg 'XY'): ")
        pset = input("Enter The Series Set Name: ")
        pnum = input("Enter The Card Number: ")
        pcondition = input("Enter The Card's Condition (Abbreviation Eg 'NM'): ")

        series_full_name = Description.expansion(pseries)

        print(f"\n{pname} {pnum} From {pset} [{pcondition}]\n")
        print(f"\033[1m{pname.upper()} {pnum.upper()} FROM POKEMON {series_full_name.upper()} {pset.upper()} [{pcondition.upper()}]\033[0m\n")

        Description.condition(pcondition)
        Description.condition1(pcondition)

    @staticmethod
    def expansion(pseries):
        series_map = {
            'SV': 'Scarlet And Violet',
            'sv': 'Scarlet And Violet',
            'SS': 'Sword And Shield',
            'ss': 'Sword And Shield',
            'SM': 'Sun And Moon',
            'sm': 'Sun And Moon',
            'XY': 'X And Y',
            'xy': 'X And Y',
            'BW': 'Black And White',
            'bw': 'Black And White'
        }
        return series_map.get(pseries, 'Unknown Series')

    @staticmethod
    def condition(pcondition):
        condition_map = {
            'nm': 'NEAR MINT CONDITION',
            'lp': 'LOW PLAYED CONDITION',
            'mp': 'MODERATELY PLAYED CONDITION',
            'hp': 'HEAVY PLAYED CONDITION',
            'dmg': 'DAMAGED CONDITION'
        }
        print(f"-{condition_map.get(pcondition.lower(), 'UNKNOWN CONDITION')}")

    @staticmethod
    def condition1(pcondition):
        if pcondition.lower() in ['nm', 'lp']:
            print("-PACK FRESH")
            print("-NEVER PLAYED")
        print("-WILL BE SHIPPED WITH A PENNY SLEEVE, TOP LOADER AND TEAM BAG")

class Welcome:
    def print_help_guide(self):
        help_guide = """
        Help Guide For Jerome’s TCG Tool

        Capitalize Tool (1):
        A Simple Tool To Capitalize Text

        Buyee Purchase Tool (2):
        A Tool Designed To Assist When Buying Items Off The Buyee Marketplaces
        - Calculates Final Purchase Prices Including Multiple Fees For Multiple Items
        - Calculates Profit Item(s) As Well As Profit Margins On Multiple Platforms
        - Shipping Is Calculated At $40 Per Order As An Estimated Constant From Past Orders
        - Note All Final Calculations Are An Estimation As Fees May Change
        - Fees Are Also Based In AUD Off Current Yen Conversion Rates
        
        Ebay Listing Format Tool (3):
        A Tool Designed To Simplify And Enhance The Process When Creating An Ebay Listing

        Help Guide (4):
        A Help Guide Designed To Assist Users When Using Jerome’s TCG Tool

        Exit (5):
        Used To Exit The Application

        Jerome’s TCG Tool Is Specifically Designed For Pokemon TCG But Can Also Be Used For Other TCG’S
        """
        print(help_guide)

    def user(self):
        while True:
            print("Press '1' For Capitalize Tool")
            print("Press '2' For Buyee Buy Tool")
            print("Press '3' For Ebay Listing Format Tool")
            print("Press '4' For Help Guide")
            print("Press '5' To Exit")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    user_input = input("Enter Text To Be Capitalized: ")
                    result = Capital.capitalize_all(user_input)
                    print(result)
                elif choice == 2:
                    tcg_tool = TCGTOOL()
                    while True:
                        tcg_tool.add_item()
                        another = input("Do you want to add another item? (y/n): ").lower()
                        if another != 'y':
                            break
                    tcg_tool.display_summary()
                elif choice == 3:
                    Description.title()
                elif choice == 4:
                    self.print_help_guide()
                elif choice == 5:
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

welcome = Welcome()
welcome.user()
