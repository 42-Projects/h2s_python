# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bonus_mathclass.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlewis-l <lerman.maggiel@gmail.com>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/28 11:36:58 by mlewis-l          #+#    #+#              #
#    Updated: 2018/06/28 11:36:59 by mlewis-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from statistics import mean
from statistics import median
from statistics import mode
import math

def find_min(list_of_nums):
    return min(list_of_nums)

def find_max(list_of_nums):
    return max(list_of_nums)

def find_mean(list_of_nums):
    return mean(list_of_nums)

def find_median(list_of_nums):
    return median(list_of_nums)

def find_mode(list_of_nums):
    return mode(list_of_nums)

if __name__ == "__main__":
    numList = [int(x) for x in sys.argv[1:]]
    min_num = find_min(numList)
    max_num = find_max(numList)
    mean = find_mean(numList)
    median = find_median(numList)
    mode = find_mode(numList)

    print("Min: {}".format(min_num))
    print("Max: {}".format(max_num))
    print("Mean: {}".format(mean))
    print("Median: {}".format(median))
    print("Mode: {}".format(mode))