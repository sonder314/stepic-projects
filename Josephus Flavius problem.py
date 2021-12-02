# solution 1
# Yes, it's not as elegant as formulas of great mathematicians but I made it entirelly by myself

def task(n, k):
    index = -1
    count = 0
    wariors = [i for i in range(1, n + 1)]
    if len(wariors) == 2:
        return 1
    while len(wariors) != 1:
        index += 1
        count += 1
        if index >= len(wariors):
            index = 0
        if count == k:
            del wariors[index]
            count = 1
            if index == len(wariors):
                index = 0
    return wariors[0]

n, k = int(input()), int(input())

print(task(n, k))

# solution 2
# This is ideal solution with recursion

def task(n, k):
    if n == 1:
        return 1
    else:
        return (task(n-1, k) + k - 1 ) % n + 1

n, k = int(input()), int(input())

print(task(n, k))

