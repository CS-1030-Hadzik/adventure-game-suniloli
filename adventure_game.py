print("Welcome to the Adventure Game!")
print("Your journey begins here...")
player_name = input("What is your name, adventurer? ")
print("Welcome, " + player_name + "! Your journey begins now.")
print(f"Welcome, {player_name}! Your journey begins now.")
starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(starting_area)
decision = input("Do you wish to take the path? (yes or no): ").lower()
if decision == "yes":
    print(f"Brave choice, {player_name}! You step onto the path and venture forward.")
elif decision == "no":
    print(player_name + ", you decide to wait. Perhaps courage will find you later.")
else:
    print("Confused, you stand still, unsure of what to do.")