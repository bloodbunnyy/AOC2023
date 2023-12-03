# AOC 2023

# ----------------------------
# PART 1
# ----------------------------

# Elf's cubes
elf_red = 12
elf_green = 13
elf_blue = 14
valid_game_ids = []


with open("puzz2.txt", 'r') as file:
    for line in file:
        parts = line.split(':')  # splits line into 2 parts (game id, and sets)
        game_id_text = parts[0]  # holds ("Game" + ID)
        game_id = game_id_text.replace('Game', '').strip()  # Holds just ID

        # takes the second part of parts, and splits by ';' to separate into single sets
        game_sets = parts[1].split(';')

        is_game_valid = True

        # Goes through each set of the current game (current line)
        for set_ in game_sets:
            blue_count = 0
            red_count = 0
            green_count = 0

            # splits set into individual colour cube components
            components = set_.split(',')

            # Count the cubes of each colour
            for component in components:
                # splits the component ('5 red') into number and colour
                component_parts = component.strip().split()
                # If the component part has 2 parts (colour and number) then we initialise these 2 parts as colour_count and colour.
                # We then run through if statements, for e.g. if blue, we update our blue_count variable by adding the 'colour_count' ('7' blue) in the set
                if len(component_parts) == 2:
                    colour_count, colour = component_parts
                    if colour == 'blue':
                        blue_count += int(colour_count)
                    elif colour == 'red':
                        red_count += int(colour_count)
                    elif colour == 'green':
                        green_count += int(colour_count)

            # Check if the set is valid
            if blue_count > elf_blue or red_count > elf_red or green_count > elf_green:
                is_game_valid = False
                break  # Break out of the loop as this game is invalid

        # If the game is valid, add its ID to the list
        if is_game_valid:
            valid_game_ids.append(game_id)


# Print the IDs of valid games
print("Valid Game IDs:", valid_game_ids)
total_sum = sum(int(game_id) for game_id in valid_game_ids)
print("Total sum of valid game IDs:", total_sum)


# ----------------------------
# PART 2
# ----------------------------

# Initialising Elf's cubes
elf_red = 12
elf_green = 13
elf_blue = 14

total_powers = 0

with open("puzz2.txt", 'r') as file:
    for line in file:
        parts = line.split(':')  # splits line into 2 parts (game id, and rest)
        game_id_text = parts[0]  # holds ("Game" + ID)
        game_id = game_id_text.replace('Game', '').strip()  # Holds just ID

        # takes the second split of parts and splits this by ';' to create single sets
        game_sets = parts[1].split(';')

        # Initialises maximum count variables
        max_blue_count = 0
        max_red_count = 0
        max_green_count = 0

        for set_ in game_sets:
            blue_count = 0
            red_count = 0
            green_count = 0

            components = set_.split(',')

            # Count the cubes of each colour
            for component in components:
                component_parts = component.strip().split()
                if len(component_parts) == 2:
                    colour_count, colour = component_parts
                    if colour == 'blue':
                        blue_count += int(colour_count)
                    elif colour == 'red':
                        red_count += int(colour_count)
                    elif colour == 'green':
                        green_count += int(colour_count)

            # After a set has been processed, we update the maximum count variables
            # max function compares the current set's colour cube count (blue_count) with the current highest count found so far (max_blue_count)
            # Max function returns the larger of 2 values passed to it
            max_blue_count = max(blue_count, max_blue_count)
            max_red_count = max(red_count, max_red_count)
            max_green_count = max(green_count, max_green_count)

        # Calculates the maximum counts of EACH colour for the current game and stores value in 'power'
        power = max_blue_count * max_red_count * max_green_count
        # Adds 'power' to 'total_powers' variable, accumulating the total values after each game
        total_powers += power

print(f"New sum of valid game IDs: {total_powers}")
