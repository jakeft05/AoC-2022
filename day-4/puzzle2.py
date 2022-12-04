with open("day-4/data.txt", "r") as file:
    overlaps = 0
    for pair in file.read().split("\n"):
        elfA = pair.split(",")[0].split("-")
        elfB = pair.split(",")[1].split("-")
        if int(elfA[0]) <= int(elfB[0]) and int(elfA[1]) >= int(elfB[0]):
            overlaps += 1
        elif int(elfA[0]) <= int(elfB[1]) and int(elfA[1]) >= int(elfB[1]):
            overlaps += 1
        elif int(elfB[0]) <= int(elfA[0]) and int(elfB[1]) >= int(elfA[0]):
            overlaps += 1
        elif int(elfB[0]) <= int(elfA[1]) and int(elfB[1]) >= int(elfA[1]):
            overlaps += 1
    print("Total overlaps: " + str(overlaps))