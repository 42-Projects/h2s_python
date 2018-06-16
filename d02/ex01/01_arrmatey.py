# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_arrmatey.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlewis-l <lerman.maggiel@gmaiil.com>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 12:44:32 by mlewis-l          #+#    #+#              #
#    Updated: 2018/06/13 12:44:33 by mlewis-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main(argv):
    for i in range(len(argv)):
        if i > 0:
            print("Arg Number {}: ".format(i), argv[i].rstrip('[]'))
    lst = argv[1:]
    lst.sort(key=len, reverse=True)
    for item in lst:
        print(item)
main(sys.argv)