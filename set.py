rainbow_colors = {'red', 'orange', 'yellow', 'blue', 'indigo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 43, 45, 3, 3, 3]
text_tuple = ('fgfcv', 'fddfgdf', 'dfsdd', 'hi', 'hi', 'hi')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(7777)
set_from_tuple.add('hello')

# #видалення
# x = set_from_list.pop()
# set_from_list.remove(3)
# set_from_list.discard(43)
# #set_from_list.remove(3)
# set_from_list.clear()
#
# print(x)
print(set_from_list)
print(set_from_tuple)
