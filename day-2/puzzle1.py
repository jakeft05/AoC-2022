with open("day-2/data.txt","r") as file:
    data = file.read()
    score = 0
    outcomes = {"A Y":8,"A X":4, "A Z":3, "B Y":5, "B X":1, "B Z":9, "C Y":2, "C X":7, "C Z":6}
    for round in data.split("\n"):
        score += outcomes[round]
    print("Total Score: " + str(score))