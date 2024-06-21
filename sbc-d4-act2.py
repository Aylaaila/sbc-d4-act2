import random 

# Get user inputs and convert them to a tuple
user_numbers = tuple(int(input(f"{x} number: ")) for x in ["First", "Second", "Third"])

# Fixed lottery numbers
lottery_numbers = (4, 5, 6)

# Display user numbers and lottery results
print("Your numbers are:", user_numbers)
print("Result:", lottery_numbers)

# Determine win or lose
if user_numbers == lottery_numbers:
    print("Win")
elif all(num in lottery_numbers for num in user_numbers) and len(set(user_numbers)) == 3:
    print("Win")
else:
    print("Lose")