# COMMENT class-iter
# class Calc:
#     def __init__(self, limit: int) -> None:
#         self.__limit = limit
#         self.__counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self) -> int:
#         if self.__counter < self.__limit:
#             self.__counter += 1
#             return self.__counter ** 2
#         else:
#             raise StopIteration

# N = 8 #it can be int(input()), but this version is easily can be tested
# my_iter = Calc(N)
# for num in my_iter:
#     print(num)

# COMMENT function-generator
# def calc(N: int):
#     for num in range(1, N + 1):
#         yield num ** 2
#
# mas = calc(8)
#
# for i_num in mas:
#     print(i_num)

# COMMENT class-iter
# N = 8
# gen = (num ** 2 for num in range(1, N + 1))
# for i_gen in gen:
#     print(i_gen)