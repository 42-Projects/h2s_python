# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_phonebook.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlewis-l <lerman.maggiel@gmail.com>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/28 11:45:06 by mlewis-l          #+#    #+#              #
#    Updated: 2018/06/28 11:45:07 by mlewis-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def createHash(filename):
    file = open(filename, 'r', encoding="utf-8")
    text = file.readlines()
    file.close()
    dictionary = {}
    for line in text:
        name = line.replace("\n", "").split(",")
        print(name)
        dictionary[name[1]] = name[0]
    return dictionary

if __name__ == '__main__':
    names = createHash("names.txt")
    print(names)
    first = {}
    for key, value in names.items():
        if value in first:
            first[value] = [first[value][0] + 1, key]
        else:
            first[value] = [1, key]
    multiples = {}
    print(first)
    for key, value in names.items():
        if value[0] > 1:
            pass


