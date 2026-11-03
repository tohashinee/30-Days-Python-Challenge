#Frequency of Array Elements (GFG) — Count occurrences of each number using a HashMap / Dict.
Score = [100,90,10,100,20,10,10,95,80]
number = {}
for i in Score:
    exist = False
    for n in number:
        if n == i:
            total = number[i]
            number[i] = total+1
            exist = True
            break
    if exist == False:
        number[i] = 1
print(number)


#Iterate through a HashMap / Dict and print all Key-Value pairs sorted alphabetically by key.
marks = {"Hansika":100, "Bhoomika": 80, "Ashi": 50, "Lola":20}
reversedmarks = sorted(marks)
for i in reversedmarks:
    print(i + ":" + str(marks[i]))

#First Unique Character in a String (LC #387) — Use a character frequency map.
s = "leetcode"
cnum = {}
for i in s:
    if i in cnum:
        total = cnum[i]
        cnum[i] = total + 1
    else:
        cnum[i] = 1

for a in cnum:
    if cnum[a] == 1:
        print("First unique character: "+a)
        break

    
    


