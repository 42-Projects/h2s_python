# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    03_binary.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlewis-l <lerman.maggiel@gmaiil.com>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 16:43:44 by mlewis-l          #+#    #+#              #
#    Updated: 2018/06/13 16:43:48 by mlewis-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import sys
import math



def main(argv):
    num_of_args = len(sys.argv)
    if num_of_args != 2:
        print("Error: Invalid Input")
    if num_of_args == 2:
        x = int(argv[1])
        print(bin(x).strip('0b'))
        print(oct(x).strip('0o'))
        print(hex(x).strip('0x'))