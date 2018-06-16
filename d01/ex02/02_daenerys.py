# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_daenerys.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlewis-l <lerman.maggiel@gmaiil.com>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/12 09:59:41 by mlewis-l          #+#    #+#              #
#    Updated: 2018/06/12 10:23:07 by mlewis-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

person = input("Who goes there?\n")
 
if person == "Dany":
    q1 = input("Dany who?\n")
    if q1 == "DHTFHNUQARFMQMKGSPRLRSKBCMD":
        print("Welcome, Daenerys.")
    elif q1 == "Daenerys of the House Targaryen, the First of Her Name, The Unburnt, Queen of the Andals, the Rhoynar and the First Men, Queen of Meereen, Khaleesi of the Great Grass Sea, Protector of the Realm, Lady Regnant of the Seven Kingdoms, Breaker of Chains and Mother of Dragons":
        print("Welcome, Daenerys.")
elif person == "DHTFHNUQARFMQMKGSPRLRSKBCMD":
    print("Welcome, Deanerys.")
elif person == "Daenerys of the House Targaryen, the First of Her Name, The Unburnt, Queen of the Andals, the Rhoynar and the First Men, Queen of Meereen, Khaleesi of the Great Grass Sea, Protector of the Realm, Lady Regnant of the Seven Kingdoms, Breaker of Chains and Mother of Dragons":
    print("Welcome, Deanerys.")
else:
    print("Move alone, now.")
