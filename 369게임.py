import sys
sys.stdin = open("369게임.txt")

N = int(input())
for n in range(1, N+1):
    cnt = 0
    m = n
    while m >= 1:
        num2 = m % 10
        m = m // 10
        if num2 == 3 or num2 == 6 or num2 == 9:
            cnt += 1
    if cnt:
        print("-"*cnt, end=" ")
    else:
        print(n, end=" ")

# N = int(input())
# for n in range(1, N+1):
#     str_n = str(n)
#     if str_n.count("3") + str_n.count("6") + str_n.count("9"):
#         cnt = str_n.count("3") + str_n.count("6") + str_n.count("9")
#         print("-" * cnt, end=' ')
#     else:
#         print(n, end=' ')
