import re
from decimal import Decimal as D, ROUND_HALF_UP

def round_to_5_cents(d):
    """
    Round a Decimal value to the nearest multiple of 0.05,
    """
    return (d*2).quantize(D('0.1'), ROUND_HALF_UP)/D(2)

# Input 1

a = input('Please add the first product to cart: ')
b = input('Please add the second product to cart: ')
c = input('Please add the third product to cart: ')

n = int(a[0])
price = float(a[-5:])
product = a[2:-9]
if product == 'music CD':
    tax = D(price * 0.1)
    price = round(price + float(tax), 2)
else:
    tax = 0

n2 = int(b[0])
price2 = float(b[-5:])
product2 = b[2:-9]
if product2 == 'music CD':
    tax2 = D(price2 * 0.1)
    price2 = round(price2 + float(tax2), 2)
else:
    tax2 = 0

n3 = int(c[0])
price3 = float(c[-5:])
product3 = c[2:-9]
if product3 == 'music CD':
    tax3 = D(price3 * 0.1)
    price3 = round(price3 + float(tax3), 2)
else:
    tax3 = 0

total = n * price + n2 * price2 + n3 * price3
taxes = tax + tax2 + tax3

print('Output 1:')

print(n, product + ':', price)
print(n2, product2 + ':', price2)
print(n3, product3 + ':', price3)

print('---------')
print("Sales Taxes: ", round(round_to_5_cents(taxes), 2))
print("Total: ", round(total, 2))
print('---------')

# Input 2

x = input('Please add the first product to cart: ')
y = input('Please add the second product to cart: ')

n4 = int(x[0])
price4 = float(x[-5:])
product4 = x[2:-9]

if product4 == 'imported bottle of perfume':
    tax4 = D(price4 * 0.1)
    price4 = round(price4 + float(tax4), 2)
else:
    tax4 = 0

if re.search(r'\bimported\b', product4):
    itax = D(price4 * 0.05)
    price4 = round(price4 + float(itax), 2)

n5 = int(y[0])
price5 = float(y[-5:])
product5 = y[2:-9]

if product5 == 'imported bottle of perfume':
    tax5 = D(price5 * 0.1)
    if re.search(r'\bimported\b', product5):
        itax2 = D(price5 * 0.05)
        price5 = price5 + float(round_to_5_cents(itax2))
    price5 = round(price5 + float(round_to_5_cents(tax5)), 2)
else:
    tax5 = 0

total2 = n4 * price4 + n5 * price5
taxes2 = tax4 + tax5 + itax + itax2

print('Output 2:')

print(n4, product4 + ':', price4)
print(n5, product5 + ':', price5)

print('---------')
print("Sales Taxes: ", round(round_to_5_cents(taxes2), 2))
print("Total: ", round(total2, 2))

# Input 3

e = input('Please add the first product to cart: ')
f = input('Please add the second product to cart: ')
g = input('Please add the third product to cart: ')
h = input('Please add the fourth product to cart: ')


n6 = int(e[0])
price6 = float(e[-5:])
product6 = e[2:-9]

if product6 == 'imported bottle of perfume' or 'bottle of perfume':
    tax6 = D(price6 * 0.1)
    if re.search(r'\bimported\b', product6):
        itax3 = D(price6 * 0.05)
        price6 = round(price6 + float(itax3), 2)
    else:
        itax3 = 0
    price6 = round(price6 + float(tax6), 2)
else:
    tax6 = 0

n7 = int(f[0])
price7 = float(f[-5:])
product7 = f[2:-9]

if product7 == 'imported bottle of perfume' or 'bottle of perfume':
    tax7 = D(price7 * 0.1)
    if re.search(r'\bimported\b', product7):
        itax4 = D(price7 * 0.05)
        price7 = price7 + float(round_to_5_cents(itax4))
    else:
        itax4 = 0
    price7 = round(price7 + float(round_to_5_cents(tax7)), 2)
else:
    tax7 = 0

n8 = int(g[0])
price8 = float(g[-5:])
product8 = g[2:-9]


if product8 == 'imported bottle of perfume' or 'bottle of perfume':
    tax8 = D(price8 * 0.1)
    if re.search(r'\bimported\b', product8):
        itax5 = D(price8 * 0.05)
        price8 = price8 + float(round_to_5_cents(itax5))
    else:
        itax5 = 0
else:
    tax8 = 0


n9 = int(h[0])
price9 = float(h[-5:])
product9 = h[2:-9]

if product9 == 'imported bottle of perfume' or 'bottle of perfume':
    tax9 = D(price9 * 0.1)
    if re.search(r'\bimported\b', product9):
        itax6 = D(price9 * 0.05)
        price9 = price9 + float(round_to_5_cents(itax6))
    else:
        itax6 = 0
else:
    tax9 = 0

total3 = n6 * price6 + n7 * price7 + n8 * price8 + n9 * price9
taxes3 = tax6 + tax7 + tax8 + tax9

print('Output 3:')

print(n6, product6 + ':', price6)
print(n7, product7 + ':', price7)
print(n8, product8 + ':', price8)
print(n9, product9 + ':', price9)

print('---------')
print("Sales Taxes: ", round(round_to_5_cents(taxes3), 2))
print("Total: ", round(total3, 2))