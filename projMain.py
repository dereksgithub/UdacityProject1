# import all libraries
import cleaningDataframes
import statFunction
import visualizationModule

# calling all the cleaning functions and clean the datasets into 10 dataframes that we can perform
# meaningful analysis
# options 1 get the data from each year for business question 1
df11q1 = cleaningDataframes.clean2011data(1)
df12q1 = cleaningDataframes.clean2012data(1)
df13q1 = cleaningDataframes.clean2013data(1)
df14q1 = cleaningDataframes.clean2014data(1)
df15q1 = cleaningDataframes.clean2015data(1)
df16q1 = cleaningDataframes.clean2016data(1)
df17q1 = cleaningDataframes.clean2017data(1)
df18q1 = cleaningDataframes.clean2018data(1)
df19q1 = cleaningDataframes.clean2019data(1)
df20q1 = cleaningDataframes.clean2020data(1)

# options 2 get the data from each year for business question 2
df11q2 = cleaningDataframes.clean2011data(2)
df12q2 = cleaningDataframes.clean2012data(2)
df13q2 = cleaningDataframes.clean2013data(2)
df14q2 = cleaningDataframes.clean2014data(2)
df15q2 = cleaningDataframes.clean2015data(2)
df16q2 = cleaningDataframes.clean2016data(2)
df17q2 = cleaningDataframes.clean2017data(2)
df18q2 = cleaningDataframes.clean2018data(2)
df19q2 = cleaningDataframes.clean2019data(2)
df20q2 = cleaningDataframes.clean2020data(2)


# options 3 get the data from each year for business question 3
df11q3 = cleaningDataframes.clean2011data(3)
df12q3 = cleaningDataframes.clean2012data(3)
df13q3 = cleaningDataframes.clean2013data(3)
df14q3 = cleaningDataframes.clean2014data(3)
df15q3 = cleaningDataframes.clean2015data(3)
df16q3 = cleaningDataframes.clean2016data(3)
df17q3 = cleaningDataframes.clean2017data(3)
df18q3 = cleaningDataframes.clean2018data(3)
df19q3 = cleaningDataframes.clean2019data(3)
df20q3 = cleaningDataframes.clean2020data(3)


# merge 11 to 20 dataframes for analysis over 10 years

# for question 1:

# for question 2:

# for question 3:



# perform basid statistical analysis on each combined dataframe:
statFunction.listAvg()


visualizationModule.listBasicViz()

# basic statistics and visualizations:

# using our analysis answer the business questions
