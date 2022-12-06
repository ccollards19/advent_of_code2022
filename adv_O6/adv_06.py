def no_double(word):
    i = 0
    lenw = len(word)
    while i < lenw:
        j = i + 1
        while j < lenw:
            if word[i] == word[j]:
                return 0
            j+=1
        i+=1
    return 1

def get_mark(line):
    index = 0;
    for letter in line:
        if no_double(line[index : (index + 14)]) == 1:
            break;
        index+=1
    return index

with open('input') as file:
    line = file.read()
    mark_index = get_mark(line);
    print (mark_index + 14)
