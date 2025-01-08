temp = []

with open("day01input.txt", "r") as f:
    fullFile = f.readlines()
    for i in fullFile:
        temp.append(i.split(" "))
        for x in temp:
            # x.pop(1)
            print(type(x))

print(temp)
