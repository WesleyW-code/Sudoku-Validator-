import sys
import math
import pandas as pd
import numpy as np
import itertools

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# Where all the info will be stored for dataframe
rows = []
# Loop for rows:
for i in range(9):
    line_by_line = []
    rows.append(line_by_line)
    for j in input().split():
        n = int(j)
        line_by_line.append(n)

# Creating dataframe to add info above to.
data = np.array(rows)
dataframe = pd.DataFrame(data=data)

# Creating list of number to check each instance to, if all exist it will assign true.
list_of_nums = list(range(1,10))

true = 0

for row in range(9):
    # Setting to go through each row of the dataframe.
    current_row = dataframe.iloc[row,:]

    # sorting each row.
    sorting = current_row.sort_values()

    # If each row has all the values it will all show true
    test = list_of_nums == sorting
    if test.all() == True:
        # Then 1 will be added to the counter variable named "true"
        true += 1

for col in range(9):
    # Setting to go through each column of the dataframe.
    current_col = dataframe.iloc[:,col]
    
    # sorting each row.
    sorting = current_col.sort_values()

    # If each row has all the values it will all show true
    test = list_of_nums == sorting
    if test.all() == True:
        # Then 1 will be added to the counter variable named "true"
        true += 1

# Testing the subs-grids and if they have the numbers.
# Going through each start row of sub grid
for i in [0,3,6]:
    # Going through each start column of the sub grid
    for j in [0,3,6]:
            # Extracting the current sub grid
            current_sub = dataframe.iloc[i:i+3,j:j+3]
            # This list will have all the number of the subgrid to compare to the numbers needed.
            comparing_list = []
            # Iterating through each row of the sub grid dataframe
            # Only 3 throws at a time will be use , so only a subgrid at a time will be compared.
            for sub_row in range(3):
                # Starting from the begining of the row to the end
                current_row = current_sub.iloc[sub_row,:]
                # just taking the values of each sub grid dataframe and converting it to a list so it can be compared.
                lists_to_compare = current_row.values.tolist()
                # Adding the lists of numbers to the "comparing list" variable
                comparing_list.append(lists_to_compare)
                # Merging the lists inside the comparing list so that its one list.
                merged = list(itertools.chain(*comparing_list))
                # sorting that list
                merged.sort()
            # If that list is equal to the list of numbers requered then true will be increased by one.
            if merged == list_of_nums:
                true += 1

# If the rows are all correct then 9 will be added to true
# If the columns are all correct then 9 will be added to true
# If the subgrids are all correct then 9 will be added to true

# If the total of true is equal to 27 then the entire Sudoku grid is correct!!!
if true == 27:
    print("true")

# Else it is not :(
else:
    print("false")
        



