scores_dict = {
    "inboundcancel": [50, 30, 20],
    "inboundtransfersale": [7, 6, 3, 3, 3, 3, 3, 10, 3, 2, 2, 2, 2, 2, 2, 2, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 6],
    "inboundmoveinsale": [7, 6, 3, 3, 3, 3, 3, 2, 3, 10, 2, 2, 2, 2, 2, 2, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 6],
    "inboundretention": [4, 4, 4, 4, 10, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6],
    "inboundsmssale": [8, 8, 8, 8, 8, 8, 8, 8, 10, 8, 8, 8, 2]
}


print(scores_dict.get("inboundretention"))
print(len(scores_dict.get("inboundretention")))
print(sum(scores_dict.get("inboundretention")))


# import random

# numbers = [random.randint(1, 4) for _ in range(28)]
# numbers.append(100 - sum(numbers))
# random.shuffle(numbers)

# print(numbers)