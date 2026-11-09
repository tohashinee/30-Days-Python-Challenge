# Bubble Sort
marks = [87,21,56,90,12,45,60]
swap = True
while swap:
    swap = False
    n = len(marks)-1
    for i in range(n):
        if marks[i] > marks[i+1]:
            temp = marks[i+1]
            marks[i+1] = marks[i]
            marks[i] = temp
            swap = True
    n = n-1
print(marks)


