score = 0
with open('input') as file:
    file_contents = file.read()
    file_content = file_contents.split('\n')
    for line in file_content:
        game = line.split(' ')
        if game[0] == '':
            break
        if game[1] == 'X':
            if game[0] == 'A':
                score = score + 3
            if game[0] == 'B':
                score = score + 1
            if game[0] == 'C':
                score = score + 2
        if game[1] == 'Y':
            score = score + 3
            if game[0] == 'A':
                score = score + 1 
            if game[0] == 'B':
                score = score + 2
            if game[0] == 'C':
                score = score + 3
        if game[1] == 'Z':
            score = score + 6
            if game[0] == 'A':
                score = score + 2
            if game[0] == 'B':
                score = score + 3
            if game[0] == 'C':
                score = score + 1
        print("current score = ", score)
