from fib import get_proginy_amount
def solve():
    n = 94
    m = 16
    proginey_amount = []
    for _ in range(1, m + 1):
        proginey_amount.append(1 + get_proginy_amount(_, 1))
    for _ in range(m, n):
        proginey_amount.append(sum(proginey_amount[_ - m: _ - 1]))
    print(proginey_amount[-1])
    # print(get_proginy_amount_recursive(n, m))

def get_proginy_amount_recursive(n: int, m: int) -> int:
    if n <= 2:
        return 1
    print(n, m)
    children_counter = 0
    children = 0
    if n == m:
        children = m - 2
    elif n < m:
        children = n - 2
    else: # m < n
        children = m - 1
    will_die_before_end = m < n
    if not will_die_before_end:
        children_counter += 1
    for _ in range(children):
        children_counter += get_proginy_amount_recursive(n - _ - 2, m)
    return children_counter
