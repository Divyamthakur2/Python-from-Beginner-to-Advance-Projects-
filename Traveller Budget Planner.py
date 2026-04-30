# Traveller Budget Planner
destination_name = "London"
number_of_days = 2
train_ticket_cost = 14.2
hotel_cost_per_night = 50
food_budget_per_day = 60
spending_money = 100
total_hotel_cost = (number_of_days* hotel_cost_per_night)
total_food_cost = (number_of_days * food_budget_per_day)
grad_total = total_food_cost + total_hotel_cost + train_ticket_cost + spending_money

print("=" *35)
print("TRIP BUDGET PLANNER" .center(35))
print("=" *35)
print("Destination :", destination_name)
print("Duration :", number_of_days)
print("-" *35)
print("Train Return : £", train_ticket_cost)
print("Hotel Total  : £", total_hotel_cost)
print("Food Total   : £", total_food_cost)
print("Spending     : £", spending_money)
print("-" *35)
print("Grand Total  : £", grad_total)
print("=" *35)


