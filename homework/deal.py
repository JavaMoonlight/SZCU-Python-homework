def deal(num):
    deal = list(range(2,11))
    deal.extend("JQKA")
    color = ("clubs", "spades", "hearts", "diamonds")
    card = [(m,n) for m in deal  for n in color]
    card += ["SunJoker","MoonJoker"]
    if num*5 > len(card) or num < 0:
        print("please enter again")
    elif num == 0:
        print("No output")
    else:
        for i in range(0,num*5,5):
            print(card[i:i+5])

def main():
    print("Please enter：")
    num = int(input())
    deal(num)
main()