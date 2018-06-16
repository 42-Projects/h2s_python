# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    04_bool.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlewis-l <lerman.maggiel@gmaiil.com>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 10:48:42 by mlewis-l          #+#    #+#              #
#    Updated: 2018/06/14 10:48:43 by mlewis-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def eval_bool(bool1, bool2, op):
    if op == "or":
        return bool1 or bool2
    elif op == "==":
        return bool1 == bool2
    elif op == "=":
        return bool1 == bool2
    elif op == '!=':
        return bool1 != bool2
    elif op == "and":
        return bool1 and bool2

Pool = 11
boolRack1 = ["False",True,True,None,True,None,None,False,False,None,True,False]
compRack = ["or","or","or","==","!=","==","and","==","!=","and","!=","and"]
boolRack2 = [False,False,None,None,True,True,False,True,None,False,True,None]

choices = []

choices.append(random.sample(boolRack1, 1)[0])
choices.append(random.sample(compRack, 1)[0])
choices.append(random.sample(boolRack2, 1)[0])

answer = eval_bool(choices[0], choices[2], choices[1])
print("{} {} {} => {}".format(choices[0], choices[1], choices[2], answer))
