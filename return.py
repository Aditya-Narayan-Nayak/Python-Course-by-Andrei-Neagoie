# def sum(num1, num2):
#     return num1 + num2
#
#
# # should do one thing really well
# # should return something
# total = sum(10, 5)
# print(sum(10, total))
def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func(num1, num2)

total = sum(10, 20)
print(total)