def hello():
    print("Hello World!")


def pack(a,b,c):
    return[a,b,c]


def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print("My lunchbox is empty!")
    for food_index in range(len(my_lunch)):
        if food_index == 0:
            print(f"First I eat {my_lunch[food_index]}")
        elif food_index < (len(my_lunch)-1):
            print(f"Next I eat {my_lunch[food_index]}")
        else:
            print("My lunchbox is empty")


hello()

print(pack(2,27,11))
print(pack("a", "b", "c"))

eat_lunch([])
eat_lunch(["Yogurt"])
eat_lunch(["Yogurt", "Strawberries", "Croissant", "Quiche"])

