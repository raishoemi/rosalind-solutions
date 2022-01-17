def solve():
    n = 30
    k = 2
    print(1 + get_proginy_amount(n, k))

def get_proginy_amount(n: int, k: int) -> int:
    if n <= 2:
        return 0
    children =  (n - 2) * k
    for _ in range(2, n - 1):
        children += k * get_proginy_amount(n - _, k)
    return children
