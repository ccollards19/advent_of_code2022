with open('input') as file:
    count = 0
    file_contents = file.read()
    file_content = file_contents.split('\n')
    group = ["", "", ""]
    for line in file_content:
        if line == "":
            break
        splitted = line.split(",")
        pair_1 = splitted[0].split("-")
        pair_2 = splitted[1].split("-")
        if ((int)(pair_1[0]) >= (int)(pair_2[0])  and (int)(pair_1[0]) <= (int)(pair_2[1])) or ((int)(pair_2[0]) >= (int)(pair_1[0]) and (int)(pair_2[0]) <= (int)(pair_1[1])):
            count+=1
        print(pair_1, pair_2, count)
