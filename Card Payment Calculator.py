import time

allocated_funds = float(
    input("How much money are you setting aside to pay off your credit cards? "))
# allocated_funds = 500
apple_card_balance = float(
    input("How much is left to pay on the Apple Card? "))
# apple_card_balance = 800
discover_card_balance = float(
    input("How much is left to pay on the Discover Card? "))
# discover_card_balance = 300
total_balance = apple_card_balance + discover_card_balance

apple_payment = allocated_funds * (apple_card_balance / total_balance)
discover_payment = allocated_funds * (discover_card_balance / total_balance)
print("Working", end="", flush=True)
for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)

print(
    f"You'll be paying ${apple_payment:.2f} towards your Apple Card and ${discover_payment:.2f} for the Discover Card.")
