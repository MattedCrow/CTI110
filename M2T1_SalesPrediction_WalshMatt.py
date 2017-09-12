# CTI-110 
# M2T1 - Sales Prediction 
# Matthew 'Melissa' Walsh
# 09.07.17
# This program calculates the profit from a given amount of total sales.

#Get projected total sales
total_sale = float(input('Enter the projected sales: '))

#Calculate profit
profit = total_sale * 0.23

#Display profit
print('The profit is $', format(profit, ',.2f'))
