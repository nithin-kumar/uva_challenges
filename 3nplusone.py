import sys
cache = {1: 1}
def get_cycle_length(n):
    cycle_length = cache.get(n)
    if cycle_length is None:
        cycle_length = get_cycle_length(n // 2 if n % 2 == 0 else 3 * n + 1) + 1
        cache[n] = cycle_length
    return cycle_length

def main():
    for line in sys.stdin:
        min_num, max_num = map(int, line.split())
        assert 0 < min_num < 1000000 and 0 < max_num < 1000000
        max_cycle_length = max(map(get_cycle_length, range(min_num, max_num+1)))
    print min_num, max_num, max_cycle_length

if __name__ == '__main__':
    main()