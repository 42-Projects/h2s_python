# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_allyourbase.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlewis-l <lerman.maggiel@gmail.com>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/28 14:01:40 by mlewis-l          #+#    #+#              #
#    Updated: 2018/06/28 14:01:42 by mlewis-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math
import sys
def dec_to_bin(n):
    bits = []

    bits.append(str(0 if n%2 == 0 else 1))
    while n > 1:
        n = n // 2
        bits.append(str(0 if n%2 == 0 else 1))

    bits.reverse()
    return ''.join(bits)

def main(argv):
    print(dec_to_bin(argv[1]))

main(sys.argv)