# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_mathclass.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlewis-l <lerman.maggiel@gmail.com>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/25 14:40:05 by mlewis-l          #+#    #+#              #
#    Updated: 2018/06/25 14:40:07 by mlewis-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math
import sys
from collections import _count_elements


def find_min(list_of_nums):
    return min(list_of_nums)

def find_max(list_of_nums):
    return max(list_of_nums)

def find_mean(list_of_nums):
    total = sum(list_of_nums)
    mean = total / len(list_of_nums)
    return mean


def find_median(list_of_nums):
    list_of_nums.sort()
    if len(list_of_nums) % 2 != 0:
        return list_of_nums[(len(list_of_nums) // 2)]
    else:
        return (list_of_nums[(len(list_of_nums) // 2) - 1] + list_of_nums[(len(list_of_nums) // 2)]) / 2.0


def find_mode(list_of_nums):
    nums = {}
    for i in range(len(list_of_nums)):
        if list_of_nums[i] in nums:
            nums[list_of_nums[i]] += 1
        else:
            nums[list_of_nums[i]] = 1
    highest = nums[list_of_nums[0]]
    current = list_of_nums[0]
    for key in nums:
        if nums[key] > highest:
            highest = nums[key]
            current = key
    return current


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
