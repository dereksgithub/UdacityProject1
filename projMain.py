# import all libraries
import cleaningDataframes
import statFunction
import visualizationModule
import pandas as pd

# read the data frames
df11 = pd.read_csv("2011 Stack Overflow Survey Responses.csv", encoding='latin-1')
df12 = pd.read_csv("2012 Stack Overflow Survey Responses.csv", encoding='latin-1')
# for the Year 2013, we need to specify dtype to avoid low mem warning
df13 = pd.read_csv("2013 Stack Overflow Survey Responses.csv", encoding='latin-1', dtype='unicode')
df14 = 2014
df15 = 2015
df16 = 2016
df17 = 2017
df18 = 2018
df19 = 2019
df20 = 2020
# calling all the cleaning functions and clean the datasets into 10 dataframes that we can perform
# meaningful analysis
# options 1 get the data from each year for business question 1
df11q1 = cleaningDataframes.clean2011data(df11, 1)
df12q1 = cleaningDataframes.clean2012data(df12, 1)
df13q1 = cleaningDataframes.clean2013data(df13, 1)
df14q1 = cleaningDataframes.clean2014data(df14, 1)
df15q1 = cleaningDataframes.clean2015data(df15, 1)
df16q1 = cleaningDataframes.clean2016data(df16, 1)
df17q1 = cleaningDataframes.clean2017data(df17, 1)
df18q1 = cleaningDataframes.clean2018data(df18, 1)
df19q1 = cleaningDataframes.clean2019data(df19, 1)
df20q1 = cleaningDataframes.clean2020data(df20, 1)

# options 2 get the data from each year for business question 2
df11q2 = cleaningDataframes.clean2011data(df11, 2)
df12q2 = cleaningDataframes.clean2012data(df12, 2)
df13q2 = cleaningDataframes.clean2013data(df13, 2)
df14q2 = cleaningDataframes.clean2014data(df14, 2)
df15q2 = cleaningDataframes.clean2015data(df15, 2)
df16q2 = cleaningDataframes.clean2016data(df16, 2)
df17q2 = cleaningDataframes.clean2017data(df17, 2)
df18q2 = cleaningDataframes.clean2018data(df18, 2)
df19q2 = cleaningDataframes.clean2019data(df19, 2)
df20q2 = cleaningDataframes.clean2020data(df20, 2)


# options 3 get the data from each year for business question 3
# 2011 Cleaning function ready
# df11q3 = cleaningDataframes.clean2011data(df11, 3)
# 2012 Cleaning function ready
# df12q3 = cleaningDataframes.clean2012data(df12, 3)
df13q3 = cleaningDataframes.clean2013data(df13, 3)
df14q3 = cleaningDataframes.clean2014data(df14, 3)
df15q3 = cleaningDataframes.clean2015data(df15, 3)
df16q3 = cleaningDataframes.clean2016data(df16, 3)
df17q3 = cleaningDataframes.clean2017data(df17, 3)
df18q3 = cleaningDataframes.clean2018data(df18, 3)
df19q3 = cleaningDataframes.clean2019data(df19, 3)
df20q3 = cleaningDataframes.clean2020data(df20, 3)


# merge 11 to 20 dataframes for analysis over 10 years

# for question 1:

# for question 2:

# for question 3:



# perform basid statistical analysis on each combined dataframe:
statFunction.listAvg()


visualizationModule.listBasicViz()

# basic statistics and visualizations:

# using our analysis answer the business questions
