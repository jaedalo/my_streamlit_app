
import streamlit as st

st.title("Credit Card Payment Calculator")
allocated_funds = st.number_input("How much money are you setting aside to pay off your credit cards? ", min_value = 0.0, value = 0.0)

apple_card_balance = st.number_input("How much is left to pay on the Apple Card? ", min_value = 0.0, value = 0.0)

discover_card_balance = st.number_input("How much is left to pay on the Discover Card? ", min_value = 0.0, value = 0.0)

if st.button("Calculate"):
    total_balance = apple_card_balance + discover_card_balance

    if total_balance <= 0:
        st.warning("Enter atleast one non-zero balance.")
    else:
        apple_payment = allocated_funds * (apple_card_balance / total_balance)
        discover_payment = allocated_funds * (discover_card_balance / total_balance)

        st.success(f"Pay ${apple_payment:.2f} to your Apple Card")
        st.success(f"Pay ${discover_payment:.2f} to your Discover Card")
#apple_payment = allocated_funds * (apple_card_balance / total_balance)
#discover_payment = allocated_funds * (discover_card_balance / total_balance)
#print("Working", end="", flush=True)
#for _ in range(3):
 #   time.sleep(0.5)
  #  print(".", end="", flush=True)

#print(
#    f"You'll be paying ${apple_payment:.2f} towards your Apple Card and ${discover_payment:.2f} for the Discover Card.")
