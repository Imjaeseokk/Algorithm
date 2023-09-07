n = int(input())

cards = [i for i in range(1,n+1)]

while len(cards) > 1:
    if len(cards)%2:
        temp = [cards[-1]]
        temp.extend(cards[1::2])
        cards = temp
    else:
        cards = cards[1::2]
print(cards[0])
