# Python Vending Machine Simulation

productCodes = [101, 102, 103, 104, 105]
products = ["Coke", "Pepsi", "Fanta", "Sprite", "Water"]
prices = [50, 60, 55, 40, 20]
currency = [100, 50, 10, 1]
balance = 0

print("Welcome to the Vending Machine!")
print("Product Codes:")
for i in range(5):
    print(f"{productCodes[i]} - {products[i]} ({prices[i]} rupees)")

while True:
    try:
        amount = int(input("Enter amount (in rupees): "))
        if amount < 0:
            print("Invalid amount. Please enter a positive value.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    balance += amount
    print(f"Balance: {balance} rupees")

    while True:
        try:
            productCode = int(input("Enter product code (or 0 to terminate): "))
            if productCode == 0:
                break

            if productCode not in productCodes:
                print("Invalid product code. Please enter a valid code.")
                continue

            index = productCodes.index(productCode)
            if balance < prices[index]:
                print("Insufficient balance. Please add more money or select another product.")
                break

            balance -= prices[index]
            print(f"Purchased: {products[index]}")
            print(f"Balance: {balance} rupees")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

    if productCode == 0:
        break

print("Thank you for using the Vending Machine!")
print("Withdrawal:")
for i in range(4):
    count = balance // currency[i]
    if count > 0:
        print(f"{count} x {currency[i]} rupees")
    balance %= currency[i]
