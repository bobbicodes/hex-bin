def repeat(x, n):
    return n*x

def row(middle, divider, width, squares):
    return divider+divider.join([repeat(middle, width) for i in range(squares)])+divider

print(row("-", "+", 12, 5))
print(row("X", "|", 12, 5))
print(row("X", "|", 12, 5))