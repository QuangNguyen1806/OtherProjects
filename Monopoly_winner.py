# In a game of Monopoly, this calculates the ultimate winner.

num_players = 0
while num_players <= 0:
    num_players = int(input("How many players played this round? "))
    if num_players <= 0:
        print("Invalid input. Please enter a positive, non-zero integer.")

winner = 0
max_assets = -1
current_player_assets = 0

for i in range(num_players):
    player_number = i + 1

    done = True
    while done:
        asset_input = input("Enter the value of a property/asset, or DONE to finish: ")

        if asset_input == "DONE" or asset_input == "done":
            done = False
            print("Player", player_number, "has", current_player_assets, "dollars")
        else:
            asset_value = float(asset_input)
            if asset_value >= 0:
                current_player_assets += asset_value
            else:
                print("Invalid input. Please enter a non-negative numerical value.")

    if current_player_assets > max_assets:
        max_assets = current_player_assets
        winner = i

    current_player_assets = 0

print("Congratulations, player", winner + 1, "! You won with $", max_assets, ".")
