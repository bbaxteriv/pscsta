f = open("pokey.txt")
lines = f.readlines()

for i in range(1,int(lines[0])+1):
    dict = {}
    a = lines[i].split()
    for ii in a:
        dict[ii] =