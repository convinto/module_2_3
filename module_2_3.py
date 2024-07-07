my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):

    namber = (my_list[index])
    index += 1
    if namber > 0:
        print(namber)
    if namber < 0:
        break
