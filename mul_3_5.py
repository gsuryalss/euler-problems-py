"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_natural(arr):

    sum_seq = 0
    for x in arr:
        sum_seq += x
    return sum_seq


def mul_3and5(num):

    arr = []

    while num > 0:
        if num % 3 == 0 or num % 5 == 0:
            arr.append(num)

        num -= 1

    return sorted(arr)


print("List all the natural numbers that are multiples of 3 or 5")
n = int(input("Enter the number:>>"))

nat_num = mul_3and5(n - 1)

if nat_num:
    print("Items are..\n", nat_num)
    print("Sum of all the multiples are\n", sum_natural(nat_num))
else:
    print("No numbers found")
