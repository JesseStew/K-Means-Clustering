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
