def pm(start, end):
    print(f"{start} -> {end}")

def h(n, start, end):
    if n == 1:
        pm(start, end)
    else:
        h(n-1, start, 6-start-end)
        pm(start, end)
        h(n-1, 6-start-end, end)

h(5, 1, 3)