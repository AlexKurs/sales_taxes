from decimal import Decimal as D, ROUND_HALF_EVEN

def round_to_5_cents(d):
    """
    Round a Decimal value to the nearest multiple of 0.05,
    """
    return (d*2).quantize(D('0.1'), ROUND_HALF_EVEN)/D(2)

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

print(n, product + ':', price)
print(n2, product2 + ':', price2)
print(n3, product3 + ':', price3)

print('---------')
print("Sales Taxes: ", round(round_to_5_cents(taxes), 2))
print("Total: ", round(total, 2))

