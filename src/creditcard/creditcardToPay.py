def need_to_pay(yearmonth, my, pf, zs):
    unpay = my + pf + zs
    print yearmonth + ' credit card cost: ', str(unpay)
    return unpay


# 2016.12
my = 3901.5
pf = 1204
zs = 4845.63
need_to_pay('2016.12', my, pf, zs)

# 2017.01
my = 1759.61
zs = 7918.85
pf = 378
pay01 = need_to_pay('2017.01', my, pf, zs)

# 2017.02
my = 1586.88
pf = 527
zs = 4643.27
pay02 = need_to_pay('2017.02', my, pf, zs)

# 2017.03
my = 1464.51
pf = 527.98
zs = 859.97
pay03 = need_to_pay('2017.03', my, pf, zs)

# 2017.04
my = 1555.71
pf = 15239.68
zs = 741.67
pay04 = need_to_pay('2017.04', my, pf, zs)

# 2017.05
my = 2422.25
pf = 549.79
zs = 3321.99
pay05 = need_to_pay('2017.05', my, pf, zs)

# 2017.06
my = 1233.34
pf = 494.22
zs = 635.47
pay06 = need_to_pay('2017.06', my, pf, zs)

# 2017.07
my = 1468.5
pf = 1439.42
zs = 613.41
pay07 = need_to_pay('2017.07', my, pf, zs)

# 2017.08
my = 762.7
pf = 2262.01
zs = 2784.27
pay08 = need_to_pay('2017.08', my, pf, zs)

# 2017.09
my = 1181.86
pf = 2820.0
zs = 1716.25
pay09 = need_to_pay('2017.09', my, pf, zs)

# 2017.10
my = 1381.04
pf = 2285
zs = 1391
pay10 = need_to_pay('2017.10', my, pf, zs)

# 2017.11
my = 1698.51
pf = 7973
zs = 386.8
pay11 = need_to_pay('2017.11', my, pf, zs)

print '2017.all ' + str(sum([pay01, pay02, pay03, pay04, pay05, pay06, pay07, pay08, pay09, pay10, pay11]))
