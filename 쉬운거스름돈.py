import sys
sys.stdin = open("쉬운거스름돈.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    ans = []                                            # 답
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]  # 돈 단위
    for w in won:                                       # 돈 단위 큰 수 부터 반복문                             # 몫이 0이 아니면
        ans.append(N // w)                              # 몫을 ans에 추가
        N = N % w                                       # 나머지는 다시 N에 저장

    print("#{}".format(t))
    print("{}".format(" ".join(map(str, ans))))         # 형변환하여 조인해서 출력
