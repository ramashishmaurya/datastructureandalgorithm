n = 5

# Upper half
for i in range(1, n + 1):

    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print stars
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half
for i in range(n - 1, 0, -1):

    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print stars
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()