# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_brainstorm.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlewis-l <lerman.maggiel@gmaiil.com>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 11:32:44 by mlewis-l          #+#    #+#              #
#    Updated: 2018/06/13 11:32:49 by mlewis-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

answer_list = []
cat = ['A boy\'s name', 'A river', 'An animal', 'Things that are cold,Insects', 'TV Shows', 'Things that grow' \
             'Fruits', 'Things that are black', 'School subjects', 'Movie titles', 'Musical Instruments']
print("We are playing with the category ...")
print (random.choice(cat))
i = 0
while (i < 10):
    answer = input("answer {}: ".format(i + 1))
    i += 1
    answer_list.append(answer)
for answer in answer_list:
    print("\t\t",answer.rstrip("[]"))
    print("\n")