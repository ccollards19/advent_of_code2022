def follow(head, tail):
    new_tail = [0, 0]
    new_tail[1] = tail[1]
    new_tail[0] = tail[0]
    if abs(head[0] - tail[0]) > 1:
        if (head[0] > tail[0]):
            new_tail[0]+=1
        if (head[0] < tail[0]):
            new_tail[0]+=-1
        if abs(head[1] - tail[1]) > 0:
            if (head[1] > tail[1]):
                new_tail[1]+=1
            if (head[1] < tail[1]):
                new_tail[1]+=-1
    elif abs(head[1] - tail[1]) > 1:
        if (head[1] > tail[1]):
            new_tail[1]+=1
        if (head[1] < tail[1]):
            new_tail[1]+=-1
        if abs(head[0] - tail[0]) > 0:
            if (head[0] > tail[0]):
                new_tail[0]+=1
            if (head[0] < tail[0]):
                new_tail[0]+=-1
            
    return new_tail

def is_new(tail, history):
    for pos in history:
        if pos[0] == tail[0] and pos[1] == tail[1]:
            return 0
    return 1
        
with open('input') as file:
    rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    history = [[0, 0]]
    count = 0
    for line in file :
        line = line.strip('\n')
        line = line.split(' ')
        #print(line, rope)
        count = (int)(line[1])
        while (count > 0):
            if (line[0] == 'U'):
                rope[0][1]+=1
            elif (line[0] == 'D'):
                rope[0][1]+=-1
            elif (line[0] == 'R'):
                rope[0][0]+=1
            elif (line[0] == 'L'):
                rope[0][0]+=-1
            i = 1
            while i < 10:
                rope[i] = follow(rope[i-1], rope[i])
                i+=1
            i+=-1
            #print(rope)
            if is_new(rope[i], history) == 1:
                    history.append(rope[i])
            count+=-1
        #print(line, rope)
        #print()
        #print(head, tail)
    print(len(history))
