with open("day-3/data.txt", "r") as file:
    items = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    priorities = 0
    for rucksack in file.read().split("\n"):
        stock = []
        compartmentA = rucksack[0:int(len(rucksack)/2)]
        compartmentB = []
        for item in rucksack[int((len(rucksack)/2)):len(rucksack)]:
            compartmentB.append(item)
        for item in items:
            if item in compartmentA:
                stock.append(item)
        for item in stock:
            if item in compartmentB:
                priorities += (items.index(item))+1
    print("The total is: " + str(priorities))