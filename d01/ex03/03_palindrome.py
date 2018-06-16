# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    03_palindrome.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlewis-l <lerman.maggiel@gmaiil.com>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/12 10:30:06 by mlewis-l          #+#    #+#              #
#    Updated: 2018/06/12 11:24:30 by mlewis-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

string = input("Please enter string to check for palindrome\n")
from string import ascii_letters

def is_palindrome(candidate):
    stripped = [char.lower() for char in candidate if char in ascii_letters]
    return stripped == stripped[::-1]

if is_palindrome(string):
    print("Yes, this string is a palindrome.")
else:
    print("No, this string is not a palindrome.")
