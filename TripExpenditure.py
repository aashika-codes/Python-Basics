def hotel_cost(nights):
    return 140*nights
def plane_cost(city):
    if "Tampa"==city:
        return 220
    elif "Los Angeles"==city:
        return 475
def car_rental(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
def trip_cost(city,days,spendingmoney):
    return car_rental(days)+hotel_cost(days)+plane_cost(city)+spendingmoney
print("cost of car rental:", car_rental(5))
print("cost of plain ride", plane_cost("Tampa"))
print("cost of hotel room", hotel_cost(7))
print("the total cost of the trip is", trip_cost("Tampa",7,3000))