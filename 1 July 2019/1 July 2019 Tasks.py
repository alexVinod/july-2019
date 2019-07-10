"""
Practice on Income Dataset
Define functions for the following data points

- Average Income of all states from 2005 to 2013
- State with highest average income in the last three years
- State with lowest average income from 2007 to 2010(inclusive)
- Print the list of all states in the same line with average income less than California
- Print the names of states based on descending order of income in the year 2009
- State with the lowest recorded income from 2005 to 2013
"""
import pandas as pd
filepath = 'DataFiles/Income.csv'
def readCSVdata(filepath):
    return pd.read_csv(filepath)
readCSVdata(filepath)
incomedf=pd.read_csv(filepath)
incomedf


# Average Income of all states from 2005 to 2013
def averageIncomeOfAllStates(startYear,endYear):
    l=[]
    for i in range(len(incomedf.columns)):
        if incomedf.columns[i] == startYear : 
            startindex = i
            #print(startindex)
        elif incomedf.columns[i] == endYear : 
            endindex = i
            #print(endindex)
    # len(incomedf.values)
        
    for i in range(startindex,endindex+1):        
        for data in incomedf.values:
            #print(data[i])
            #print(data[i],end=" ")
            l.append(data[i])            
    #print(sum(l))
    a=sum(l)//len(l)    
    print("Average Income of all states from {} to {} : {} ".format(startYear,endYear,a))
        
        #print(i[startindex],i[endindex])
averageIncomeOfAllStates('2005','2013')

# State with highest average income in the last three years
def stateHighestAverageIncomeLast3Year(lastYears):
    averageLast3Years=[]
    for i in range(len(incomedf.values)):
        last3Years=[]
        for j in range(lastYears+1):
            if j!=0:
                last3Years.append(incomedf.values[i][-j])
                #print(incomedf.values[i][-j], end=" ")
            #elif j == 0 :
            #   print(incomedf.values[i][1])
        averageLast3Years.append(sum(last3Years)//len(last3Years))
    nameIndex=averageLast3Years.index(max(averageLast3Years))
    print("\n{} State with highest average income in the last {} years : {}".format(incomedf.values[nameIndex][1],lastYears,max(averageLast3Years)))
stateHighestAverageIncomeLast3Year(3)