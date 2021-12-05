weight = float(input("How many bananas are you buying in kg? "))
banana_cost = weight * 3
if banana_cost <= 50:
    order_cost = banana_cost + 4.99
else:
    order_cost = banana_cost + 3.49
print("Your order will cost £" + str(order_cost))
