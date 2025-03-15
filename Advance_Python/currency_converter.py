class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def convert_to_dollars(self, amount_rupees):
        return amount_rupees / self.exchange_rate

    def convert_to_rupees(self, amount_dollars):
        return amount_dollars * self.exchange_rate

# Example Usage
exchange_rate =float(input("Enter the rate of rupees in 1 Dollar: "))
converter = CurrencyConverter(exchange_rate)

print("Choose Conversion:")
print("1. Rupees to Dollars")
print("2. Dollars to Rupees")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    amount_rupees = float(input("Enter the amount in Rupees: "))
    converted_amount_dollars = converter.convert_to_dollars(amount_rupees)
    print(f'{amount_rupees} INR is equal to {converted_amount_dollars:.2f} USD')

elif choice == 2:
    amount_dollars = float(input("Enter the amount in Dollars: "))
    converted_amount_rupees = converter.convert_to_rupees(amount_dollars)
    print(f'{amount_dollars} USD is equal to {converted_amount_rupees:.2f} INR')

else:
    print("Invalid choice. Please choose 1 or 2.")
