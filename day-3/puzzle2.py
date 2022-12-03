with open("day-3/data.txt", "r") as file:
    items = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    priorities = 0
    count = 0
    compartment = []
    for rucksack in file.read().split("\n"):
        if count == 3:
            for i in compartment:
                if i != "0":
                    priorities += (items.index(i))+1
            compartment = []
            count = 0
        if count == 0:
            for item in rucksack:
                if item not in compartment:
                    compartment.append(item)
            print("New Group")
        else:
            for item in compartment:
                if item != "0" and item not in rucksack:
                    compartment[compartment.index(item)] = "0"
        count += 1
    for i in compartment:
                if i != "0":
                    priorities += (items.index(i))+1
    print("The total is: " + str(priorities))