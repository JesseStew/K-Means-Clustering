""" 
Program: hw3.py
Programmed By: Brett Spatz and Jesse Stewart
Description: K-Means Clustering Algorithm
Trace Folder: stewart013
"""

#---------------------------------Imports--------------------------------------
import math
#------------------------------------------------------------------------------



#---------------------------------Variables------------------------------------
k = int # Integer holding number of clusters
dataFile = "" # String holding name of file containing data
data = [] # List holding lists for each line in dataFile
clear = 100*'\n'
#------------------------------------------------------------------------------



#---------------------------------Classes/Functions----------------------------
"""
    Takes name of data file as a parameter. Creates a list for each line
    in data file. Appends the lists to the data variable.
"""
def getData(dataFile):
    with open (dataFile) as f: #Closes file after data is gathered
        lines = f.read().splitlines() #Splits at each new line
        #Creates a list for each line and converts data to floats
        for line in lines: 
            line = [float(i) for i in line.split(' ')] #Float for calculations
            data.append(line) #Append to data

"""
    Takes the data as a parameter. Returns the number of unique cluster
    values found within the data. Variable k will be set to this value.
"""
def numClusters(data):
    count = int
    tempList = [] #Holds list of all cluster values found in data
    for line in data:
        tempList.append(line[2])
    #Use set to get unique values. Returns the length of the set.
    count = len(set(tempList)) 
    return count

"""
 Find euclidean distance measure of two nodes.
 Input: two nodes from data.
 Returns: euclidean distance of two nodes.
"""
def euclideanDist(curr_node, comp_node):
    squared_euclidean = []
    euclidean_dist = 0
    for num in range(0,len(curr_node)-1):   #excludes final list item which contains cluster it belongs to.
        curr = float(curr_node[num])
        comp = float(comp_node[num])
        squared_euclidean.append((curr-comp)*(curr-comp))
    for itr in squared_euclidean:
        euclidean_dist = euclidean_dist + itr
    return math.sqrt(euclidean_dist)

#------------------------------------------------------------------------------



#---------------------------------Program Main---------------------------------
def main():
    dataFile = "synthetic_2D.txt"
    getData(dataFile)
#    k = numClusters(data)
    print(data)
    print("euclidean_dist: ", euclideanDist(data[0],data[1]))
    print("k: ", k)
    print("numClusters: ", numClusters(data))
	
main()		
#---------------------------------End of Program-------------------------------
