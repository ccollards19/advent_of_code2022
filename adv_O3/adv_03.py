def get_common_letter(elf_1, elf_2, elf_3):
    for letter_1 in elf_1:
        for letter_2 in elf_2:
            if letter_2 == letter_1:
                for letter_3 in elf_3:
                    if letter_3 == letter_2:
                        return letter_3
    return 0

def get_score(letter):
    score = 0
    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        score = score + 1
        if letter == char:
            return score
    return 0

with open('input') as file:
    score = 0
    count = 0
    file_contents = file.read()
    file_content = file_contents.split('\n')
    group = ["", "", ""]
    for line in file_content:
        if line == "":
            break
        group[count] = line
        count+=1
        if count == 3:
            letter = get_common_letter(group[0], group[1], group[2])
            score = score + get_score(letter)
            print("current = ", score, letter)
            count = 0
