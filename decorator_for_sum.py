
# A decorator that returns the sum of positive integers



def negative_num(fn):
    def result(l):
        positive_list = []
        for x in l:
            if x > 0 :
                positive_list.append(x)

        return fn(positive_list)
    return result

@negative_num
def add(positive_list):
    res = 0
    for x in positive_list:
        res = res + x
    return res 


print(add([-87 , 1 , 2, -8 , 5,4 ]))



# def positive_num(fn):
#     def negative(l):
#         for x in l:
#             if x < 0:
#                 l.remove(x)
#         return  fn(l)
#     return negative

# @positive_num
# def add(l1):
#     res = sum(l1)
#     return res

# list1 = [-23, 11 , 4, 5 ,-37]
# print(add(list1))