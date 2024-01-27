def process_command(command, numbers):
    if command == "sum":
        result = sum(numbers)
    elif command == "average":
        result = round(sum(numbers) / len(numbers), 2)
    elif command == "lcd":
        result = find_lcd(numbers)
    elif command == "gcd":
        result = find_gcd(numbers)
    elif command == "min":
        result = min(numbers)
    elif command == "max":
        result = max(numbers)
    else:
        print("Invalid command")
        return
    
    print(result)

def find_lcd(numbers):
    def find_lcm(x, y):
        return x * y // find_gcd(x, y)

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = find_lcm(result, numbers[i])
    return result

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

command = input().strip()
numbers = []

while True:
    line = input().strip()
    if line == "end":
        break
    numbers.append(int(line))

process_command(command, numbers)
