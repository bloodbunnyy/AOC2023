# # AOC 2023 Day 4

# # ----------------------------
# # PART 1
# # ----------------------------
total_points = 0

with open("4scratchcards.txt", 'r') as file:
    for line in file:
        winning_numbers = []
        my_numbers = []

        numbers = line.strip().split('|')
        part1 = numbers[0]
        part2 = numbers[1]
        nums = part1.strip().split(':')[1].split(' ')
        win_nums = part2.split(' ')

        for win_num in win_nums:
            if win_num.isdigit():
                winning_numbers.append(win_num)

        line_total = 0

        for my_num in nums:
            if my_num in winning_numbers:
                my_numbers.append(my_num)
                if len(my_numbers) == 1:
                    line_total += 1
                else:
                    line_total = line_total * 2
        total_points += line_total

print(total_points)

# ? ----------------------------
# ? PART 2
# ? ----------------------------


card_copies = {}
cards_to_process = deque()
last_card_id = 0  # track highest card ID encountered
card_matches = {}  # store number of matches for each card

with open("4scratchcards.txt", 'r') as file:
    for line in file:
        winning_numbers = []
        my_numbers = []

        numbers = line.strip().split('|')
        part1 = numbers[0]  # ID and player nums
        part2 = numbers[1]  # winning nums
        my_nums = part1.strip().split(':')
        nums = my_nums[1].split(' ')  # holds individual player nums
        win_nums = part2.split(' ')  # holds individual winning nums
        card_id = my_nums[0].strip()  # stores 'card' + ID #
        card_id = int(card_id.split()[1])  # stores just ID # as int
        last_card_id = max(last_card_id, card_id)

        # creates player nums and winning nums by filtering digits from parts
        winning_numbers = [num for num in my_nums[1].split() if num.isdigit()]
        my_numbers = [num for num in part2.split() if num.isdigit()]

        # Counts how many player numbers are in winning numbers
        matches = sum(num in winning_numbers for num in my_numbers)
        # card_matches dict updates with number of matches of current card
        card_matches[card_id] = matches

        # Initial instances set to 1
        cards_to_process.append((card_id, matches, 1))

# takes a card from left of queue, updates 'card_copies' for current card by adding # of instances
while cards_to_process:
    current_card, matches, instances = cards_to_process.popleft()
    card_copies[current_card] = card_copies.get(current_card, 0) + instances

    # Check if current card matches -> loops through matches
    if matches > 0:
        for i in range(1, matches + 1):
            next_card = current_card + i  # calculates next card ID
            if next_card <= last_card_id:  # checks if next card is NOT greater than last_card_id
                # Use the stored matches for the next card
                # gets # of matches for 'next_card'
                next_matches = card_matches[next_card]
                # adds this card to 'card_to_process'
                cards_to_process.append((next_card, next_matches, 1))


total_cards = sum(card_copies.values())
print(f"Total number of scratchcards: {total_cards}")
