# import all libraries
import cleaningDataframes
import statFunction
import visualizationModule

# calling all the cleaning functions and clean the datasets into 10 dataframes that we can perform
# meaningful analysis
df11 = cleaningDataframes.clean2011data()
df12 = cleaningDataframes.clean2012data()
df13 = cleaningDataframes.clean2013data()
df14 = cleaningDataframes.clean2014data()
df15 = cleaningDataframes.clean2015data()
df16 = cleaningDataframes.clean2016data()
df17 = cleaningDataframes.clean2017data()
df18 = cleaningDataframes.clean2018data()
df19 = cleaningDataframes.clean2019data()
df20 = cleaningDataframes.clean2020data()
statFunction.listAvg()
visualizationModule.listBasicViz()

# basic statistics and visualizations:

# using our analysis answer the business questions
