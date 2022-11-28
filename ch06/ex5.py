# ex5.py

for i in range(2, 10, 1):
    print("#  %d단  #   " % i, end="")
print("")

for i in range(1, 10, 1):
    for j in range(2, 10, 1):
        print("%d X %d = %2d\t" % (j, i, j * i), end="")
    print("")