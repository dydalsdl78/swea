import sys
sys.stdin = open("2007.txt")

T = int(input())

for t in range(1, T+1):
    string = input()
    max_len = 30

    find = 0

    for i in range(len(string)):
        if find == 0:
            for d in range(1, max_len-i):
                if string[i:i+d] == string[i+d:i+d*2]:
                    print("#{} {}".format(t, d))
                    find = 1
                    break
        if find == 1:
            break

        # print("?")
