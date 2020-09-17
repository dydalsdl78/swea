import sys
sys.stdin = open("String.txt", encoding='UTF-8')

T = 10

for t in range(1, T+1):
    N = int(input())
    chars = input()
    string = input()
    len_chars = len(chars)

    cnt = 0
    for i in range(len(string)-len_chars+1):
        if string[i:i+len_chars] == chars:
            cnt += 1

    print("#{} {}".format(t, cnt))
