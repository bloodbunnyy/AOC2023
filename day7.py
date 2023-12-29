# AOC 2023

# ----------------------
# PART 1
# ----------------------

hands = []


card_strength = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
                 '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


def comparing_cards(hand, card_strength):
    card_counts = {card: hand.count(card) for card in set(hand)} # Count the occurrences of each card
  
    # Creates a sorted list of (card, count) tuples, sorted primarily by count (descending), then by card strength (descending)
    sorted_card_counts = sorted(
        card_counts.items(), key=lambda item: (-item[1], -card_strength[item[0]]))

    # Determine the hand type
    if sorted_card_counts[0][1] == 5:
        hand_type = "Five of a Kind"
    elif sorted_card_counts[0][1] == 4:
        hand_type = "Four of a Kind"
    elif sorted_card_counts[0][1] == 3: # Full-house OR Three of a Kind
        if sorted_card_counts[1][1] == 2: 
            hand_type = "Full House"
        else: 
            hand_type = "Three of a Kind"
    elif sorted_card_counts[0][1] == 2:
        if sorted_card_counts[1][1] == 2: 
            hand_type = "Two Pair"
        else:  
            hand_type = "One Pair"
    else:
        hand_type = "High Card"

    # Map each card to its strength, maintaining the original order
    comparison_key = [card_strength[card] for card in hand]

    # Assign numeric values to each hand type (higher is better)
    hand_rank_values = {
        "Five of a Kind": 8,
        "Four of a Kind": 7,
        "Full House": 6,
        "Three of a Kind": 5,
        "Two Pair": 4,
        "One Pair": 3,
        "High Card": 2
    }

    hand_rank_value = hand_rank_values[hand_type] # Dictionary to store numerical value determined by hand_rank_values that correspond to hand_type for each hand
    composite_key = (hand_rank_value, comparison_key) # A tuple to hold the numberical hand_rank_value and comparison_key list of each card to sort hands by type and strength

    return (hand_type, composite_key)


def calculate_bids(hands):
    process_hands = [(hand, int(bid)) for hand, bid in hands]
    hand_ranking = sorted(process_hands, key=lambda x: comparing_cards(
        x[0], card_strength)[1], reverse=False)

    total_winnings = 0
  
    for rank, (hand, bid) in enumerate(hand_ranking, start=1):
        hand_type, _ = comparing_cards(hand, card_strength)
        contribution = rank * bid
        total_winnings += contribution
        # print(f"Rank: {rank}, Hand: {hand}, Hand Type: {hand_type}, Bid: {bid}, Contribution: {contribution}, Running Total: {total_winnings}")

    return total_winnings


with open("7camelcards.txt", 'r') as file:
    for line in file:
        parts = line.strip().split(' ')
        cards = parts[0]
        bids = parts[1]

        hands.append([cards, bids])

total_winnings = calculate_bids(hands)
print(f"Total winnings: {total_winnings}")


# ----------------------
# PART 2
# ----------------------

# * J = Joker - Weakest cars, no more Jacks, can be used as a wildcard

hands = []


card_strength = {'A': 13, 'K': 12, 'Q': 11, 'T': 10, '9': 9, '8': 8,
                 '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}


def comparing_cards(hand, card_strength):
    # Initialize hand_type to "High Card" as a default
    hand_type = "High Card"

    joker_count = hand.count('J')
    hand_no_jokers = ''.join(card for card in hand if card != 'J')

    # Count occurrences of each non-joker card
    card_counts = {card: hand_no_jokers.count(
        card) for card in set(hand_no_jokers)}
    sorted_card_counts = sorted(
        card_counts.items(), key=lambda item: (-item[1], -card_strength[item[0]]))

    # Determine the hand type
    if joker_count > 0:  # If the hand consists only of jokers
        if joker_count == len(hand):
            hand_type = "Five of a Kind"  # All cards are Jokers
        else:
            sorted_jcard_counts = [(card, count + joker_count)
                                   for card, count in card_counts.items()]
            sorted_jcard_counts.sort(
                key=lambda item: (-item[1], -card_strength[item[0]]))

            if sorted_jcard_counts[0][1] >= 5:
                hand_type = "Five of a Kind"
            elif sorted_jcard_counts[0][1] >= 4:
                hand_type = "Four of a Kind"
            elif sorted_jcard_counts[0][1] == 3:
                if len(sorted_jcard_counts) > 1 and sorted_card_counts[1][1] >= 2:
                    hand_type = "Full House"
                else:
                    hand_type = "Three of a Kind"
            elif len(sorted_jcard_counts) > 1 and sorted_jcard_counts[0][1] == 2 and sorted_card_counts[1][1] == 2:
                hand_type = "Two Pair"
            elif sorted_jcard_counts[0][1] == 2:
                hand_type = "One Pair"
            else:
                hand_type = "High Card"

    else:  # hands without jokers
        if len(sorted_card_counts) > 0:
            if sorted_card_counts[0][1] == 5:
                hand_type = "Five of a Kind"
            if sorted_card_counts[0][1] == 4:
                hand_type = "Four of a Kind"
            elif sorted_card_counts[0][1] == 3:
                if len(sorted_card_counts) > 1 and sorted_card_counts[1][1] == 2:
                    hand_type = "Full House"
                else:
                    hand_type = "Three of a Kind"
            elif sorted_card_counts[0][1] == 2:
                if len(sorted_card_counts) > 1 and sorted_card_counts[1][1] == 2:
                    hand_type = "Two Pair"
                else:
                    hand_type = "One Pair"

    comparison_key = [card_strength[card]
                      if card != 'J' else -1 for card in hand]

    hand_rank_values = {
        "Five of a Kind": 8,
        "Four of a Kind": 7,
        "Full House": 6,
        "Three of a Kind": 5,
        "Two Pair": 4,
        "One Pair": 3,
        "High Card": 2
    }

    hand_rank_value = hand_rank_values[hand_type]
    composite_key = (hand_rank_value, comparison_key)

    return (hand_type, composite_key)


def calculate_bids(hands):
    process_hands = [(hand, int(bid)) for hand, bid in hands]
    hand_ranking = sorted(process_hands, key=lambda x: comparing_cards(
        x[0], card_strength)[1], reverse=False)

    total_winnings = 0
    for rank, (hand, bid) in enumerate(hand_ranking, start=1):
        hand_type, _ = comparing_cards(hand, card_strength)
        contribution = rank * bid
        total_winnings += contribution
        # print(f"Rank: {rank}, Hand: {hand}, Hand Type: {hand_type}, Bid: {bid}, Contribution: {contribution}, Running Total: {total_winnings}")

    return total_winnings


with open("7camelcards.txt", 'r') as file:
    for line in file:
        parts = line.strip().split(' ')
        cards = parts[0]
        bids = parts[1]

        hands.append([cards, bids])

total_winnings = calculate_bids(hands)
print(f"Total winnings: {total_winnings}")
