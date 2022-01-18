#data types
# var1= " Hello world"
# var2= "4.4"
# var3="32"
# var4="33"
# #print(int(var2)+int(var4))
# #print(type(var2))
# #print(int(var2)+int(var3))
# print(100*str(int(var4)+int(var3)))
# str()
# int()
# float()


# # string
# upd = "Upendra is programmer and hacker and AI ML DL NLP DEVELoper"
# print(upd[0:7])
# print(upd[0:2222])
# print(len(upd))
# print(upd[0:8:2])
# print(upd[0::2])
# print(upd[::])
# print(upd[::-1])
# print(upd[-4::2])
# print(type(upd))
# print(upd.isalnum())#
# print(upd.isalpha())#
# print(upd.endswith("DEVELoper"))#
# print(upd.count("e"))#
# print(upd.capitalize())#
# print(upd.find("is"))#
# print(upd.lower())#
# print(upd.upper())#
# print(upd.replace("is","are"))#

# list
# dailyneeds = ["vim", "colgate", "soap", "brush", "handwash", 22]
# print(dailyneeds)
# print(dailyneeds[5])
# print(dailyneeds[3])

# numbers = [2,3,5,6,1,7]
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# print(numbers[2])

# slicing
# print(numbers[:])
# print(numbers[1:4])

# # extended slicing
# print(numbers[::1])
# numbers.append(33)
# print(numbers)
# numbers.insert(2,44)
# print(numbers)
# numbers.remove(44)
# print(numbers)
# numbers.pop()
# print(numbers)

# MUTABLE AND IMMUTABLE
# ro = (1,3,5)
# print(ro)
# (parenthesis)[squarebracket]{dictionary}


# Dictionary is key value pairs
# d1 = {}
# d2 = {"upendra":"pizza",
#       "rohan":"meat",
#       "mohan":"egg",
#       "sunita":"veg",
#       "raj":{"aacc":"barr","tar":"har","car":"myanmar"}}
# d2["Ankit"]="leadd"
# d2['anshul']='55'
# del d2['anshul']
# print(d2.copy())
# d3=d2
# del d3["rohan"]
# print(d2)
# print(d2.get("upendra"))
# d2.update({"rena": "coaclate"})
# print(d2.keys())


# d2 = {"Upendra":"pizza",
#       "Rohan":"meat",
#       "Mohan":"egg",
#       "Sunita":"veg",
#       "Raj":{"aacc":"barr","tar":"har","car":"myanmar"}}

# member = input("name:")
# # print(d2[member])
# a = member.capitalize()
# print(a , " = ", d2[a])

# print("Enter your name")
# name = input()
# print(d2[name])


#
# d2 = [["Upendra",1], ["Rohan",2],
#       ["Mohan",3],
#       ["Sunita",4],
#       ["Raj",7]]
#
# d1 = dict(d2)
# print(d1)
# for item, u in d1.items():
#     print(item, u)

# d4 = {"Upendra": "pizza",
#           "Rohan": "meat",
#           "Mohan": "egg",
#           "Sunita": "veg",
#           "Raj": {"aacc": "barr", "tar": "har", "car": "myanmar"}}
#
# for i, u in d4.items():
#     print(i, "is eating this", u)

# upendra = 48000
# raj = 30000
# sangram = 35000
#
# rocky = 50000
# if rocky>raj:
#     print("Salary of rocky is more than raj")
# if rocky!=raj:
#     print("Salary of rocky is not equal raj;")
# if rocky>sangram:
#     print("Salary of rocky is more than sangram")
# if rocky>upendra:
#     print("Salary of rocky is more than upendra")
#
# else:
#     print("Work hard if you want salary more than these guys")




#
# print("What is your number")
# number = int(input())
# if number>19:
#     print('you can fuck')
# elif number==19:
#     print('We think weather you are able to fuck or not')
#
# else:
#     print('you are not able to fuck')



n = 32

winning_number = 33
print("this is the number guessing game")
number = int(input("Guess you number between 1 to 50:\n"))
guess = 1
game_over = False

while (guess<=9):
    if (winning_number == number):
        print(f"You win, and you guess the number is {guess} time")

    else:
        if(winning_number > number):
            print("you guess to low")
            # game_over = True
        else:
            if(winning_number < number):
                print("You guess too high")
                guess +=1
                number=int(input("Guess again:"))