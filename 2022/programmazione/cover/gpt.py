def range_cover(N, K, ranges):
    covered = [0] * 1000001
    for start, end in ranges:
        for i in range(start, end+1):
            covered[i] += 1
    return covered.count(K)

if __name__ == "__main__":
    N, K = map(int, input().strip().split())
    ranges = [list(map(int, input().strip().split())) for _ in range(N)]
    result = range_cover(N, K, ranges)
    print(result)