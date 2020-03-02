def lineSeg(w):
    return w*"-"

def span(w, n):
    return '+'+'+'.join([lineSeg(w) for i in range(n)])+'+'

print(span(12, 5))