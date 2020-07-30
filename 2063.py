N = int(input())

scores = map(int, input().split())
scores = sorted(scores)
idx = int(len(scores) / 2)
print(scores[idx])