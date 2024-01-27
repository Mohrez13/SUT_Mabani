def check_invitation(guest_code, n):
    guests_64bit = guest_code[0] | (guest_code[1] << 32)  
    for i in range(n):
        invited_guest = int(input())  
        if (guests_64bit >> invited_guest) & 1 == 1:
            print("yes")  
        else:
            print("no")  
guest_code = [int(input()), int(input())]  
n = int(input())   
check_invitation(guest_code, n)
