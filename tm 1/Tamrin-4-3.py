def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

a, b = map(int, input().split())

count = sum(1 for i in range(min(a, b), max(a, b) + 1) if is_prime(i))

if a <= b:
    print(f"main order - amount: {count}")
else:
    print(f"reverse order - amount: {count}")
