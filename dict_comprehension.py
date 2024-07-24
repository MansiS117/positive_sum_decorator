# dict1 = {"one" : 1 , "two" : 2 , "three " : 3 }
#create a new dict where values are greater than 1 using dict comprehension


dict1 = {"one" : 1 , "two" : 2 , "three " : 3 }
new_dict = {x : y  for x , y in dict1.items() if  y > 1}
print(new_dict)