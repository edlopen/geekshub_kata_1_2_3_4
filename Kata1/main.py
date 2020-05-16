price = 3.49
discount = 0.4
price_discounted = price * discount
bread_count = int(input("Introduce el nº de barras vendidas: "))

print(f"Precio habitual {price}")

print(f"Descuento {price_discounted}")
print(f"Conste final: {bread_count * price_discounted}")