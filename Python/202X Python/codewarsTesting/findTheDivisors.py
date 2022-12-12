def divisors(integer):
    n = []
    for x in range(1, integer+1):
        if integer%x == 0:
          print(f'{integer} is a prime!')
        else:
          n.append(x)
    print(n)
    pass
divisors(15)