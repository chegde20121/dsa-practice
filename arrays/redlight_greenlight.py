# Standalone version with hardcoded input

test_cases = [
    (4, 10, [2, 13, 4, 16]),
    (5, 8, [9, 3, 8, 8, 4]),
    (4, 6, [1, 2, 3, 4])
]

for n, k, a in test_cases:
    ans = 0

    for h in a:
        if h > k:
            ans += 1

    print(ans)