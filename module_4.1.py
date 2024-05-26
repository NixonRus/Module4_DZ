from fake_math import divide1 as fm
from true_math import divide2 as tm

result1 = fm(88, 4)
result2 = fm(5, 0)
result3 = tm(64, 2)
result4 = tm(17, 0)
print(result1)
print(result2)
print(result3)
print(result4)



# fake_math
# def divide1(a,b):
#     if b == 0:
#         return 'Ошибка'
#     result = a / b
#     return result


#true_math
# from math import inf
# def divide2(a,b):
#     if b == 0:
#         return inf
#     result = a / b
#     return result