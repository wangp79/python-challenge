from ast import increment_lineno
from ipaddress import summarize_address_range
import os
import csv
from re import X
from statistics import mean
counter = 0
net_total_amount = 0
Average_Change = 0
percentage_profit = 0 
new_row_list = []
final_number_list = []
number = 0
x = 0
y = 0
budget_csv =os.path.join("Resources", "budget_data.csv")
path =  "/Users/tony/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

with open (budget_csv,'r') as csv_file:
    print(csv_file)
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
   
    print("Financial Analysis")
    print("------------------------")
    for row in csv_reader:
        counter = counter +1
        net_total_amount += float(row[1])
        Average_Change = net_total_amount/counter
        new_row_list.append(int(row[1])) # import to a list named: new_row_list
        

#print(new_row_list)  
#print(len(new_row_list))
#print(new_row_list[4])
differences = []
max_1 = 0 
index_of_max = 0 
for i  in range(0,len(new_row_list)):
    if(i+1!=len(new_row_list)):
        current_value = new_row_list[i]
        next_value = new_row_list[i+1]
        
        differences_value = current_value - next_value
        if(max_1 < differences_value):
            max_1 = differences_value
            index_of_max  = i
        
print(index_of_max)   
print(max_1)
        #print(current_value)
#print(differences)
#print(f"max number: {max(differences)}")

        

    
            

#         #x = new_row_list[x+1] - new_row_list[x]
#         #final_number_list.append(x)
        


        
# print(f"Total Months:{counter}")
# print(f"Total: {net_total_amount}")
# print(f"Average Change: {Average_Change}")
