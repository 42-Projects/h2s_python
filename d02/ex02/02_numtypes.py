# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_numtypes.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlewis-l <lerman.maggiel@gmaiil.com>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 14:10:51 by mlewis-l          #+#    #+#              #
#    Updated: 2018/06/13 14:10:53 by mlewis-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math
def main (argv):
    num_of_args = len(sys.argv)
    if num_of_args != 3:
        print("Error: Invalid Input")
    if num_of_args == 3:
        dec_sol = (int(argv[1]) / int(argv[2]))
        whole_sol = math.floor(dec_sol)
        rem = (int(argv[1]) % int(argv[2]))
        print("{} divided by {} equals {} remainder {}".format(argv[1], argv[2], whole_sol, rem))
        a = 10
        b = 10.5
        c = complex('1+2j')
        c_strip = str(c).strip('(' ')')
        type_a = str(type(a)).strip("class<>")
        type_b = str(type(b)).strip("class<>")
        type_c = str(type(c)).strip("class<>")
        print("Variable a contains: {} which is of type: {}".format(a, type_a))
        print("Variable b contains: {} which is of type: {}".format(b, type_b))
        print("Variable c contains: {} which is of type: {}".format(c_strip, type_c))
main(sys.argv)
