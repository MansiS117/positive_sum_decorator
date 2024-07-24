# Sorting a dict based on its values

original_dict = {"seven" : 7 , "nine" : 9 , "one" : 1 , "six" : 6}

new_dict = dict(sorted(original_dict.items() , key = lambda item : item[1]))
print(new_dict)