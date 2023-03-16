word = 'X-DSPAM-Confidence:'

with open("mbox.txt", 'r') as fp:
    zbroj2 = 0
    counter2 = 0
    # read all lines in a list
    lines = fp.readlines()
    for line in lines:
        # check if string present on a current line
        if line.find(word) != -1:
            line_r2 = line.rsplit()
            zbroj2 += float(line_r2[1])
            counter2 += 1
        """
            print(word, 'string exists in file')
            print('Line Number:', lines.index(line))
            print('Line:', line)
            """
with open("mbox-short.txt", 'r') as fp:
    # read all lines in a list
    lines = fp.readlines()
    zbroj = 0
    counter = 0
    for line in lines:
        # check if string present on a current line
        if line.find(word) != -1:
            line_r = line.rsplit()
            zbroj += float(line_r[1])
            counter += 1
            """
            print(word, 'string exists in file')
            print('Line Number:', lines.index(line))
            print('Line:', line)
            """
print(word, zbroj2/counter2)
print(word, zbroj/counter)
