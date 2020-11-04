import sys
sys.stdin = open('단순2진암호코드.txt')

T = int(input())

numbers = {'0': '0001101',
           '1': '0011001',
           '2': '0010011',
           '3': '0111101',
           '4': '0100011',
           '5': '0110001',
           '6': '0101111',
           '7': '0111011',
           '8': '0110111',
           '9': '0001011'
           }

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input().split()) for _ in range(N)]
    code = []
    cnt = 0

    for x in range(N):
        for y in range(M-1, -1, -1):
            if arr[x][0][y] == '1':
                tmp = arr[x][0][y-55:y+1]
                cnt += 1
                break

    for i in range(0, 56, 7):
        if tmp[i:i+7] == numbers['0']:
            code.append(0)
        if tmp[i:i+7] == numbers['1']:
            code.append(1)
        if tmp[i:i+7] == numbers['2']:
            code.append(2)
        if tmp[i:i+7] == numbers['3']:
            code.append(3)
        if tmp[i:i+7] == numbers['4']:
            code.append(4)
        if tmp[i:i+7] == numbers['5']:
            code.append(5)
        if tmp[i:i+7] == numbers['6']:
            code.append(6)
        if tmp[i:i+7] == numbers['7']:
            code.append(7)
        if tmp[i:i+7] == numbers['8']:
            code.append(8)
        if tmp[i:i+7] == numbers['9']:
            code.append(9)

    odd, even = 0, 0
    for c in range(len(code)-1):
        if c % 2:
            even += code[c]
        else:
            odd += code[c]

    if (odd * 3 + even + code[-1]) % 10 == 0:
        print("#{} {}".format(t, sum(code)))
    else:
        print("#{} 0".format(t))
