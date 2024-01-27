def count_bit_changes(a, b):
    xor_result = bin(a ^ b)  
    count = xor_result.count('1')  

    return count

a = int(input())
b = int(input())

result = count_bit_changes(a, b)
print(result)