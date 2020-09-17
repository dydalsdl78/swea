import sys
sys.stdin = open("의석이의세로로말해요.txt")


T = int(input())

for tc in range(1, T+1):
    data = []
    ans = ""
    max_len = -1
    for n in range(5):
        string = input()
        data.append(string)
        if len(string) > max_len:
            max_len = len(string)

    print(max_len)
    for i in range(max_len):
        for j in range(5):
            if i >= len(data[j]):
                continue
            else:
                ans += data[j][i]

    print("#{} {}".format(tc, ans))

# T = int(input())

# for tc in range(1, T+1):
#     data = ['']*5
#     ans = ""
#     max_len = -1

#     for n in range(5):
#         data[n] = input()
#         if len(data[n]) > max_len:
#             max_len = len(data[n])

#     for i in range(max_len):
#         for j in range(5):
#             if i >= len(data[j]):
#                 continue
#             else:
#                 ans += data[j][i]

#     print("#{} {}".format(tc, ans))
