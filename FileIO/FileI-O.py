#Write a program that creates a text file notes.txt, writes 5 lines of text, and then reads it back line-by-line.
with open("notes.txt","w") as file:
    file.write("\n Hello")
    file.write("\n Welcome to this File")
    file.write("\n How is the waether?")
    file.write("\n Sunny Indeed!")
    file.write("\n Bye")


with open("notes.txt","r") as file:
    while True:
        line = file.readline()
        if not line:  # Empty string means End of File (EOF)
            break
        print(line.strip())

file.close()