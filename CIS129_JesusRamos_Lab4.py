# Module 4 Lab-4
# Jesus Ramos
# 02/19/2024
# This program determines the store bonus and employee bonus based on amount of monthly sales and percent of sales increase

# declare local variables
monthlySales = 0 # monthly sales amount
storeAmount = 0 # store bonus amount
empAmount = 0 # employee bonus amount
salesIncrease = 0 # percent of sales increase
prompt = '' # prompt will be a string literal

# this code gets the monthly sales
monthlySales = float(input('Enter the amount of monthly sales'))

# this code determines the store bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# this code gets the percent of increase in sales
salesIncrease = float(input('Enter the percent of sales increase'))
salesIncrease = salesIncrease/100

# this code determines the employee bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

# this code prints the bonus information
print('The store bonus amount is $', storeAmount)
print('The employee bonus amount is $', empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amount possible!')
