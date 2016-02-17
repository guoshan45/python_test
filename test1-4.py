# Write a program that given a text file will create a new text file in
# which all the lines from the original file are numbered from 1 to n
# (where n is the number of lines in the file).


fo = open("temp.txt", "rw+")
i = 0
fo.writelines("#:0")
while(fo.readline()):
    i += 1
    number_line = "#:%s" % i
    fo.writelines(number_line)
fo.close()
