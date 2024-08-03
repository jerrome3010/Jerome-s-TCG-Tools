class TCGTOOL:
    def __init__(self):
        print("Welcome To Jerome's TCGTOOL")
        self.item = input("Enter Item Name: ")
        self.price = float(input("Enter Item Price: "))
        self.coupon = input("Did You Have A Coupon (y/n): ").lower()
        self.discount = 0

        if self.coupon == 'y':
            self.discount = float(input("Enter Discount Percentage: "))

        self.discount_amount = self.price * (self.discount / 100)

    def calculate_final_price(self):
        final_price = self.price - self.discount_amount + 2.98
        tax_price = final_price * 1.1
        return final_price, tax_price

    def display_summary(self):
        final_price, final_price_including_tax = self.calculate_final_price()
        print(f"Item: {self.item}")
        print(f"Original Price: ${self.price:.2f}")
        print(f"Discount: {self.discount:.2f}%")
        print("Price Breakdown:")
        print(f"Item Price: ${self.price:.2f}")
        print("Buyee Purchase Fee: $2.98")
        print(f"Discount Amount: ${self.discount_amount:.2f}")
        print(f"Discount Price: ${self.price:.2f} * {self.discount:.2f}% = ${self.price - self.discount_amount:.2f}")
        print(f"Final Price Before Tax: ${final_price:.2f}")
        print(f"Final Price Including Tax: (${self.price - self.discount_amount:.2f} + $2.98) * 1.1 = ${final_price_including_tax:.2f}")

        self.sell = input("Are You Planning To Sell (y/n): ").lower()

        if self.sell == 'y':
            self.marketplace = input("Which Marketplace (f/e): ").lower()

            if self.marketplace == 'f':
                self.marketplace_price = float(input("Enter Sell Price: $"))
                self.profit_marketplace = self.marketplace_price - final_price_including_tax
                profit_margin = (self.profit_marketplace / final_price_including_tax) * 100
                print(f"Profit on Final Sale Price: ${self.profit_marketplace:.2f}")
                print(f"Profit Margin: {profit_margin:.2f}%")

            elif self.marketplace == 'e':
                self.marketplace_price = float(input("Enter Sell Price: $"))
                self.profit_marketplace = (self.marketplace_price - final_price_including_tax) * 0.85
                profit_margin = (self.profit_marketplace / final_price_including_tax) * 100
                print(f"Profit after 15% Fee on Final Sale Price: ${self.profit_marketplace:.2f}")
                print(f"Profit Margin: {profit_margin:.2f}%")
            else:
                print("Invalid marketplace choice. Exiting.")

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

        # Call the condition method
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
            'BW': 'Black And White',
            'bw': 'Black And White'
        }
        return series_map.get(pseries, 'Unknown Series')

    @staticmethod
    def condition(pcondition):
        if pcondition in ['nm', 'NM']:
            print("-NEAR MINT CONDITION")
        elif pcondition in ['lp', 'LP']:
            print("-LOW PLAYED CONDITION")
        elif pcondition in ['mp', 'MP']:
            print("-MODERATELY PLAYED CONDITION")
        elif pcondition in ['hp', 'HP']:
            print("-HEAVY PLAYED CONDITION")
        elif pcondition in ['dmg', 'DMG']:
            print("-DAMAGED CONDITION")

    @staticmethod
    def condition1(pcondition):
        if pcondition in ['nm', 'NM', 'lp', 'LP']:
            print("-PACK FRESH")
            print("-NEVER PLAYED")
            print("-WILL BE SHIPPED WITH A PENNY SLEEVE, TOP LOADER AND TEAM BAG")
        else:
            print("-WILL BE SHIPPED WITH A PENNY SLEEVE, TOP LOADER AND TEAM BAG")

class Welcome:
    def print_help_guide(self):
        help_guide = """
        Help Guide For Jerome’s TCG Tool

        Capitalize Tool (1):
        A Simple Tool To Capitalize Text

        Buyee Purchase Tool (2):
        A Tool Designed To Assist When Buying Items Off The Buyee Marketplaces
        - Calculates Final Purchase Prices Including Multiple Fees
        - Calculates Profit As Well As Profit Margins On Multiple Platforms
        - As Of Now Shipping Incorporated And I Am Working On Adding Support For Multiple Items
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
                x = int(input("Enter your choice: "))

                if x == 1:
                    user_input = input("Enter Text To Be Capitalized: ")
                    result = Capital.capitalize_all(user_input)
                    print(result)
                elif x == 2:
                    pokemon_cli = TCGTOOL()
                    pokemon_cli.display_summary()
                elif x == 3:
                    Description.title()
                elif x == 4:
                    self.print_help_guide()
                elif x == 5:
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

welcome = Welcome()
welcome.user()
