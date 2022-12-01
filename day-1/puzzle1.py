with open("day-1/data.txt", "r") as file:
    data = file.read()
    calories = {}
    elfid = 1
    for elf in data.split("\n\n"):
        total = 0
        for item in elf.split("\n"):
            total += int(item)
        calories["Elf " + str(elfid)] = str(total)
        elfid += 1
    print(str(max(calories, key=calories.get)) + " has the most calories, with " + calories[max(calories, key=calories.get)] + " in total.")