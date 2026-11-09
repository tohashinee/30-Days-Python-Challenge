#Linear Search - The overall time complexity of a linear search is O(n) (Linear Time). This means the execution time increases proportionally with the size of the input array (n)
student = ["Ali","Priya","Fred","Lomesh","Bobby","Lola"]
found = False
name = input("Enter name to be searched: ")
index = 0
while found==False and index < len(student):
    if student[index] == name:
        found = True
        break
    index = index+1
if found == False:
    print("This student does not study here...")
else:
    print("Found")
    
