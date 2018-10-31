salary = float(input("What is your starting annual salary? "))
portion_saved = float(input("What is the portion that you have saved? "))
cost_of_dream_home = float(input("What is the cost of your dream home? "))
print("What is your starting annual salary? ", salary, "What is the portion that you have save? ", portion_saved, "What is the cost of your dream home? ", cost_of_dream_home)

r = 0.04
portion_down_payment = 0.25 
actual_down_payment = (portion_down_payment * cost_of_dream_home)
current_savings = 0
montly_income = (salary /12) * (portion_saved)
mon_rot = (r /12)
month = 0


while current_savings < actual_down_payment :
    month += 1
    current_savings += (mon_rot * current_savings) + montly_income
    
    print("Number of months is ", month)


