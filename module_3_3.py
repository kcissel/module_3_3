def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25, c=[1, 2, 3])


values_list = ['Hello', 3, True]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [56, 'строка']
print_params(*values_list_2, 42)

