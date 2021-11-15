import re
from decimal import Decimal as D, ROUND_HALF_UP

def round_to_5_cents(d):
    """
    Round a Decimal value to the nearest multiple of 0.05,
    """
    return (d*2).quantize(D('0.1'), ROUND_HALF_UP)/D(2)

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

print(n4, product4 + ':', price4)
print(n5, product5 + ':', price5)

print('---------')
print("Sales Taxes: ", round(round_to_5_cents(taxes2), 2))
print("Total: ", round(total2, 2))