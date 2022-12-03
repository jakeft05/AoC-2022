with open("day-2/data.txt","r") as file:
    data = file.read()
    score = 0
    outcomes = {"A Y":4,"A X":3, "A Z":8, "B Y":5, "B X":1, "B Z":9, "C Y":6, "C X":2, "C Z":7}
    for round in data.split("\n"):
        score += outcomes[round]
    print("Total Score: " + str(score))