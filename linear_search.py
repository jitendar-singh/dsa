def linear_search(cards , query) -> int:
    position = 0
    while True:
        if cards[position] == query:
            return position
        position+=1

        if position == len(cards):
            return -1

if __name__ == "__main__":
    cards = [99,87,67,55,44,32,20,18,9,6,5,3,2,0]
    print(linear_search(cards, 180))
