import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Enter stock details (type 'done' to finish)\n")

while True:
    stock = input("Enter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.\n")
        continue

    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity

# Save to CSV
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price", "Total Value"])

    print("\n📊 Portfolio Summary")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        total_investment += value
        writer.writerow([stock, qty, stock_prices[stock], value])
        print(f"{stock}: {qty} × ₹{stock_prices[stock]} = ₹{value}")

    writer.writerow(["Total Investment", "", "", total_investment])

print(f"\n💰 Total Investment Value: ₹{total_investment}")
print("📁 Data saved to portfolio.csv")
