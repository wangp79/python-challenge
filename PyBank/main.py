from ast import increment_lineno
from ipaddress import summarize_address_range
import os
import csv
from re import X
from statistics import mean
counter = 0
net_total_amount = 0
Average_Change = 0
new_row_list = []
months = []

# reading csv file
budget_csv =os.path.join("Resources", "budget_data.csv")
path =  "/Users/tony/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

# open csv file as read only
with open (budget_csv,'r') as csv_file:
    print(csv_file)
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
   
    print("Financial Analysis")
    print("------------------------")
    for row in csv_reader:
        months.append(row[0]) # import all months name into a seperated new list
        counter = counter +1
        net_total_amount += float(row[1]) # calculate total amount
        new_row_list.append(int(row[1])) # import all months profit value into a new list and convert to Intiger
        
print(f"Total Months:{counter}")
print(f"Total: {net_total_amount}")

differences = []
for i  in range(0,len(new_row_list)): 
    if(i+1!=len(new_row_list)):
        current_value = new_row_list[i]
        next_value = new_row_list[i+1]
        
        differences_value = next_value - current_value # calculating profits between each month
        differences.append(differences_value) # put all compared profit into a new list
        
max_index = differences.index(max(differences)) # return the highest profit increase month's index
min_index = differences.index(min(differences)) # return the hightest profit decrease month's index
Average_Change = float(mean(differences)) # calculate the mean value among each month's profit differences

print(f"Average Change:{Average_Change}")
print(f"Greatest Increase in Profits:{months[max_index+1]} ({max(differences)})")
print(f"Greatest Decrease in Profits:{months[min_index+1]}({min(differences)}")