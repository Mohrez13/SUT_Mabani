def count_bit_changes(a, b):
    xor_result = bin(a ^ b)
    count = xor_result.count('1')
    return count

def main():
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))

    result = count_bit_changes(a, b)
    print(f"Number of bit changes: {result}")

if __name__ == "__main__":
    main()
