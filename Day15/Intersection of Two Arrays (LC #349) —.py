# Intersection of Two Arrays (LC #349) — Solve using language Set operations (HashSet / set()).
num1 = [1,2,2,1]
num2 = [2,2]

A = set(num1)
B = set(num2)

print(A&B)