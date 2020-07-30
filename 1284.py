T = int(input())

for i in range(1, T+1):
    P, Q, R, S, W = map(int, input().split()) 
    if R >= W:
        a = P * W
        b = Q
        if a > b:
            print(f"#{i} {b}")
        if a < b:
            print(f"#{i} {a}")

    elif R < W:
        a = P * W
        b = Q + (W - R) * S
        if a > b:
            print(f"#{i} {b}")
        if a < b:
            print(f"#{i} {a}")    

