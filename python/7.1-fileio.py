# r - reading (default) , w - writing, a - adding extra data
# r+ - read + overwrite (unerased), w+ - read + overwrite, a - read + append (unerased)
# x - creating new file & open for writing
# t - open text file (default) , b - open binary file

#1 - read : open(r), read, close
file = open("fileio.txt","r")
data = file.read() #file.read(5) - print 5 chars
print(data)
data = file.readline()
print(data)
file.close()

#2 - write : open(w - over write/a - add), write, close
file1 = open("fileio.txt","w")
file1.write("hey, welcome here")
file1.close()

file1 = open("fileio.txt","a")
file1.write("it's a pleasant day")
file1.close()

#open
with open ("fileio.txt", "r") as a: #"w"
    data = a.read() #a.write("abc")
    print(data)

#delete file
import os
os.remove("fileio.txt")