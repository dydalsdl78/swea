T = 10

for t in range(10):
    N = int(input())
    dump = list(map(int, input().split()))

    for n in range(N):
        # 최대 최소 찾기
        max_value = dump[0]
        min_value = dump[0]
        for i in range(100):
            if dump[i] >= max_value:
                max_value = dump[i]
                max_idx = i
        for j in range(100):
            if dump[j] <= min_value:
                min_value = dump[j]
                min_idx = j

        dump[max_idx] -= 1
        dump[min_idx] += 1
        if n == N-1:
            max_value = max(dump)
            min_value = min(dump)
            print("#{} {}".format(t+1, max_value - min_value))
