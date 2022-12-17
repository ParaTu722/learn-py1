def ji_suan_he(i, j):
    sums = 0
    while i <= j:
        sums += i   # sums = sums + 1
        i = i + 1
    print(f"\t{sums}")
while True:
    i = int(input("请输入累加计算的起始值："))
    j = int(input("请输入累加计算的末尾值："))
    print('')
    if i == '886' or j == '886':
        break
    else:
        ji_suan_he(i, j)
