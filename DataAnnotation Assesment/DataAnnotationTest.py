def sort_numbers(numbers_dictionary):
    sorted_numbers_list = sorted(numbers_dictionary.keys())
    return sorted_numbers_list

def create_subsets(numbers_list):
    step = 1
    subsets = []
    while len(numbers_list) != 0:
        if len(numbers_list) >= step:
            subsets.append(numbers_list[0:step])
            numbers_list = numbers_list[step:]
            step += 1
        else:
            return False

    return subsets

def create_needed_numbers_list(subsets):
    needed_numbers_list = []
    for x in subsets:
        needed_numbers_list.append(x[-1])

    return needed_numbers_list

def decode(file_path):
    file = open(file_path, "r")

    num_word_dict = {}

    for line in file:
        number, word = line.split(maxsplit=1)

        number = int(number)

        word = word.strip()

        num_word_dict[number] = word

    file.close()

    sorted_numbers = sort_numbers(num_word_dict)
    subsets = create_subsets(sorted_numbers)
    needed_numbers_list = create_needed_numbers_list(subsets)

    #print(needed_numbers_list)

    sentence = ""
    for i in range(0, len(needed_numbers_list) - 1):
        sentence += num_word_dict[needed_numbers_list[i]] + " "

    sentence += num_word_dict[needed_numbers_list[-1]]
    return(sentence)


file_path = "/Users/ikennanwafor/Downloads/coding_qual_input.txt"
print(decode(file_path))



