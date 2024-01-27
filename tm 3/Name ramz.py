
def asli():
    jomle = inp.split(' ')
    jomle.sort(key=lambda x: int(x[1:]))
    for i in jomle:
        print(i[0],end='')
inp=str(input())
asli()