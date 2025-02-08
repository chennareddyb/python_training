# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print("We sell ",num_pizzas," different kinds of pizza!")


pizza_and_prices = zip(prices, toppings)
tmp_list = [list(x) for x in zip(prices, toppings)]
print(tmp_list)
tmp_list.sort()
print(tmp_list)
cheapest_pizza = tmp_list[0]
print(cheapest_pizza)
priciest_pizza = tmp_list[-1]
print(priciest_pizza)
tmp_list.pop()
print(tmp_list)
tmp_list.insert(4,[2.5, "peppers"]
)
print(tmp_list)
three_cheapest = tmp_list[:3]
print(three_cheapest)
