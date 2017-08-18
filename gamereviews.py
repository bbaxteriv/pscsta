f = open("gamereviews.txt")
lines = f.readlines()

dict = {}
games = ['']
stars = []

rates = 0



for i in range(1,int(lines[0])+1,1):
    lines[i] = lines[i].strip().split(',')

    if lines[i][1] not in dict:
        dict[lines[i][1]] = (int(lines[i][2]),1)
    else:
        v = dict[lines[i][1]]

        dict[lines[i][1]] = (v[0] + int(lines[i][2]), v[1] + 1)

for i in sorted(dict.keys()):

    v = dict[i]

    stars = dict[i][0] / dict[i][1]

    print(i,'gets',stars, 'stars')