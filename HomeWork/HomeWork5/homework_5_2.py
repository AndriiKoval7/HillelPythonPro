def arithmetic_mean(dgt_list):
    count_dgt = len(dgt_list)
    sum_dgt = 0
    for dgt in dgt_list:
        try:
            sum_dgt += float(dgt)
        except ValueError as ex:
            print(f'{ex.__class__}: {ex}')
            return
    return round((sum_dgt / count_dgt), 2)

filename = 'digits.txt'
try:
    my_file = open(filename, 'r', encoding = 'utf-8')
except FileNotFoundError as ex:
    print(f'{ex.__class__}: {ex}')
else:
    txt = my_file.readlines()
    # print(txt)
    gd_list = []
    digits_list = []
    for dgts_line in txt:
        dgts_line = dgts_line.strip()
        dgts_line = dgts_line.replace("\n", "")
        digits_list.append(dgts_line.split(';'))
        for dgt in digits_list:
            for i in dgt:
                gd_list.append(i)
    print('The arithmetic average is: ', arithmetic_mean(dgt_list=gd_list))
    my_file.close()
