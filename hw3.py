""" 
Program:       hw3.py
Programmed By: Brett Spatz and Jesse Stewart
Description:   K-Means Clustering Algorithm
Trace Folder:  stewart013
"""

#---------------------------------Imports--------------------------------------
import math
#------------------------------------------------------------------------------



#---------------------------------Variables------------------------------------
k = int        # Integer holding number of clusters
dataFile = ""  # String holding name of file containing data
data = []      # List holding lists for each line in dataFile
ranSeed = 90   # Arbitrary integer constant to seed random number generator
#------------------------------------------------------------------------------



#---------------------------------Classes/Functions----------------------------
"""
    Description: Creates a list for each line in data file. Appends the lists 
                 to the data list.
    Input:       Name of data file.
"""
def getData(dataFile):
    with open (dataFile) as f:
        lines = f.read().splitlines()
        
        # Creates a list for each line and converts data to floats
        for line in lines: 
            line = [float(i) for i in line.split(' ')]
            data.append(line)


"""
    Description: Finds unique clusters to determine value of k.
    Input:       The pre-processed data (in the form of a list of lists).
    Returns:     Number of unique clusters found within the data.
"""
def numClusters(data):
    count = int
    tempList = [] # Holds list of all cluster values found in data
    for line in data:
        tempList.append(line[2])
        
    # Use set to get only unique values. Returns the length of the set.
    count = len(set(tempList)) 
    return count

 
"""
    Description: Find Euclidean distance measure of two nodes.
    Input:       Two nodes from data.
    Returns:     Euclidean distance of two nodes.
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


"""
    Description: Randomly determine the initial means.
    Input:       Pre-processed data, number of means to find (k).
"""   
def setInitialMeans(k, data):
    
#------------------------------------------------------------------------------



#---------------------------------Program Main---------------------------------
def main():
    dataFile = "synthetic_2D.txt"
    getData(dataFile)
    print(data)
    k = numClusters(data)
    print(k)
	
main()		
#---------------------------------End of Program-------------------------------
