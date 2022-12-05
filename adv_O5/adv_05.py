def make_crate(tab):
    crate = []
    i = 0
    while i < 9:
        i+=1
        arr = []
        crate.append(arr)
    for line in tab :
        i = 0
        for elem in line :
            if elem != '   ':
                crate[i].append(elem)
            i+=1
    i = 0
    while i < 9:
        crate[i].reverse()
        i+=1
    return crate

tab = []
tmp = []
with open('input') as file:
    nl = 0
    for line in file:
        arr = []
        count = 0
        if line == "":
            break
        if line == "\n":
            nl = 1
            crates = make_crate(tab)
            for stri in crates:
                print(stri)
            continue
        while count < len(line) and nl != 1:
            arr.append(line[count : (count + 3)])
            count+=4
        if nl == 1:
            nline = line.split(' ')
            count = (int)(nline[1])
            start = (int)(nline[3])
            dest = (int)(nline[5])
            print(count, start, dest)
            while count > 0:
                tmp.append(crates[start - 1].pop())
                count+=-1
            tmp.reverse()
            crates[dest - 1] = crates[dest - 1] + tmp
            tmp.clear()
            #make_move(crates, line)
            for stri in crates:
                print(stri)
            nl = 1
        else : 
            tab.append(arr)
#print(tab)
