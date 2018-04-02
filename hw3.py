""" 
Program: hw3.py
Programmed By: Brett Spatz and Jesse Stewart
Description: K-Means Clustering Algorithm
Trace Folder: stewart013
"""

#---------------------------------Imports--------------------------------------
import math
#import csv
#------------------------------------------------------------------------------



#---------------------------------Variables------------------------------------
K = 3
clear = 100*'\n'
#------------------------------------------------------------------------------



#---------------------------------Classes/Functions----------------------------
def input_data():
    #Creates a list of lists of the input data
    data = []
    with open('synthetic_2D.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.strip('\n')
            line = str(line).split(' ')
            data.append(line)
    return data

def euclidean_dist(curr_node, comp_node):
    #print("train_item_data[0]: ", train_item_data[0])
    squared_euclidean = []
    euclidean_dist = 0
    for num in range(0,len(curr_node)-1):
        curr = float(curr_node[num])
        comp = float(comp_node[num])
        squared_euclidean.append((curr-comp)*(curr-comp))
    for num in squared_euclidean:
        euclidean_dist = euclidean_dist + num
    return math.sqrt(euclidean_dist)

#------------------------------------------------------------------------------



#---------------------------------Program Main---------------------------------
def main():
    data = input_data()
    print(data)
    print("euclidean_dist: ", euclidean_dist(data[0],data[1]))
	
main()		
#---------------------------------End of Program-------------------------------
