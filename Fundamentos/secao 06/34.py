def calculate_least_common_multiple():
    n = 20
    integers = list(range(2, n + 1))
    lcm = 1
    while (len(integers) > 0):
        first = integers.pop(0)
        if first == 1:
            continue
        lcm *= first
        integers = [x // first if x % first == 0 else x for x in integers]
    return lcm

least_common_multiple = calculate_least_common_multiple()
print(least_common_multiple)