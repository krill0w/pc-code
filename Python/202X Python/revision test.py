counter = 0
for counter in range(1,101):
    if counter%3:
        print("Fizz")
    elif counter%5:
        print("Buzz")
    else:
        print(counter)
    counter += 1