f = open("C:\\Users\krish\Documents\GitHub\pract\\file.txt", "a")
f.write("new data appended to file.txt")
f.close()

f = open("C:\\Users\krish\Documents\GitHub\pract\\file.txt", "r")
print(f.read())

# g = open("C:\\Users\krish\Documents\GitHub\pract\\file1.txt", "x")
# g.write("new file")
# g.close()

g = open("C:\\Users\krish\Documents\GitHub\pract\\file1.txt", "r")
print(g.read())