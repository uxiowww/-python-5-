#1
def format_price (price, currency = "руб", discount = 0):
    if price < 0 or discount < 0 or discount > 100:
        return "error: неверные данные"
    
    finalPrice = price * (1 - discount/100)
    return f"{finalPrice:.2f} {currency}"

print(format_price(1500))
print(format_price(1500, "", 20))

#2
nums = [-5, 0, 3, 7,-2, 9, 1, -8]
res = list(map(lambda x: x**2, filter(lambda x: x>0, nums)))
print(res)

#3
def transfor_list(data, func):
    return [func(i) for i in data]

print(transfor_list(["a", "b", "c"], lambda x: x.upper()))
print(transfor_list([1,2,3], lambda x: x*2))


#Комплексное 
products = [
    {"name": "Laptop", "price": 950, "rating": 4.5, "in_stock": True},
    {"name": "Mouse", "price": -10, "rating": 4.8, "in_stock": True},
    {"name": "Keyboard", "price": 120, "rating": 3.9, "in_stock": False},
    {"name": "Monitor", "price": 300, "rating": 4.2, "in_stock": True},
    {"name": "Headphones", "price": 80, "rating": 4.6, "in_stock": True}
]

def is_valid(product):
    return product["price"] > 0 and product["rating"] >= 4.0 and product["in_stock"] is True
FilterProducts = list(filter(is_valid, products))
New_products = list(map(lambda p: {**p, "final_price": p["price"] * 0.85}, FilterProducts))
Items = sorted(New_products, key=lambda p: p["final_price"])
def print_catalog(items):
    for item in items:
        print(f"{item['name']}, Цена: {item['price']:.2f}, Итог: {item['final_price']:.2f}")

print_catalog(Items)