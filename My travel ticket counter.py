# My Travel Ticket Counter

# Step 1: Store travel booking details
destination1 = "Paris"
destination2 = "Tokyo"

price1 = 850.0
price2 = 950.0

# Step 2: Display booking information
print("Destination 1:", destination1)
print("Destination 2:", destination2)
print("Price 1:", price1)
print("Price 2:", price2)

# Step 3: Calculate total ticket cost
total_cost = price1 + price2
print("\nTotal Ticket Cost:", total_cost)

# Step 4: Compare ticket prices
if price1 > price2:
    print(destination1, "is more expensive.")
elif price1 < price2:
    print(destination2, "is more expensive.")
else:
    print("Both tickets cost the same.")

# Step 5: Work with text
print("\nFormatted Destinations:")
print("Your first trip is to", destination1.upper())
print("Your second trip is to", destination2.lower())

# Step 6: Swap two ticket prices
print("\nSwapping ticket prices...")
price1, price2 = price
