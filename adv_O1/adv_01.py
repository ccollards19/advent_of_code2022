current_biggest = 0
second_biggest = 0
third_biggest = 0
current = 0
tmp = 0
with open('input') as file:
    file_contents = file.read()
    file_content = file_contents.split('\n')
    for line in file_content:
        if line == "":
            if current_biggest < current :
                tmp = current_biggest
                current_biggest = current
                current = tmp
            if second_biggest < current:
                tmp = second_biggest
                second_biggest = current
                current = tmp
            if third_biggest < current:
                tmp = third_biggest
                third_biggest = current
                current = tmp
            print("current = ", current_biggest +  second_biggest + third_biggest)
            current = 0
        else :
            tmp = int(line)
            current = current + tmp
