Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> retail_price= 99
>>> quantity = int(input(" Quantity purchased: "))
 Quantity purchased: 8
>>> if quantity < 10:
	discount = 0
elif 10 <= quantity and quantity < 20:
	discount = 0.1 #10%
elif 20 <= quantity and quantity < 50:
	discount = 0.2 #20%
elif 50 <= quantity and quantity < 100:
	discount = 0.3 #30%
else:
	discount = 0.4 #40%

	
>>> subtotal = retail_price * quantity
>>> total_discount = subtotal * discount
>>> total = subtotal - total_discount
>>> print(format('\nSubtotal: ', '<10s'), '$', format(subtotal, ',.2f'))

Subtotal:  $ 792.00
>>> print(format('Discount:', '<10s'), '$', format(total_discount, ',.2f'))
Discount:  $ 0.00
>>> print(format('Total:', '<10s'), '$', format(total, ',.2f'))
Total:     $ 792.00
>>> 