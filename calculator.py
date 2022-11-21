inp_str = input("Введите выражение: ")
available_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '*']
res_str = ''
corr = False
for i in inp_str:
    if i in available_symbols:
        corr = True
        res_str += i
    else:
        corr = False
        break
    if corr:
    print(f'{inp_str} = {eval(res_str)}')
