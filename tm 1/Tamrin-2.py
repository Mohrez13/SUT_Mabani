def calculate_sum_without_addition(n, m):
    while m:
        carry = n & m
        n = n ^ m
        m = carry << 1

    return n

n = int(input())
m = int(input())
k = int(input())

result = calculate_sum_without_addition(n, m)

print(result)
if result == k:
    print("YES")
else:
    print("NO")