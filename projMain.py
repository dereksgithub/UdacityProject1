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
df14 = pd.read_csv("2014 Stack Overflow Survey Responses.csv", encoding='latin-1', dtype='unicode')
df15 = pd.read_csv("2015 Stack Overflow Survey Responses.csv", encoding='latin-1', dtype='unicode')
df16 = pd.read_csv("2016 Stack Overflow Survey Responses.csv", encoding='latin-1', dtype='unicode')
df17 = pd.read_csv("2017 Stack Overflow Survey Responses.csv", encoding='latin-1', dtype='unicode')
df18 = pd.read_csv("2018 Stack Overflow Survey Responses.csv", encoding='latin-1', dtype='unicode')
df19 = pd.read_csv("2019 Stack Overflow Survey Responses.csv", encoding='latin-1', dtype='unicode')
df20 = pd.read_csv("2020 Stack Overflow Survey Responses.csv", encoding='latin-1', dtype='unicode')

# calling all the cleaning functions and clean the datasets into 10 dataframes that we can perform
# meaningful analysis
# options 1 get the data from each year for business question 1
# df11q1 = cleaningDataframes.clean2011data(df11, 1)
# df12q1 = cleaningDataframes.clean2012data(df12, 1)
# df13q1 = cleaningDataframes.clean2013data(df13, 1)
# df14q1 = cleaningDataframes.clean2014data(df14, 1)
# df15q1 = cleaningDataframes.clean2015data(df15, 1)
# df16q1 = cleaningDataframes.clean2016data(df16, 1)
# df17q1 = cleaningDataframes.clean2017data(df17, 1)
# df18q1 = cleaningDataframes.clean2018data(df18, 1)
# df19q1 = cleaningDataframes.clean2019data(df19, 1)
# df20q1 = cleaningDataframes.clean2020data(df20, 1)

# options 2 get the data from each year for business question 2
# df11q2 = cleaningDataframes.clean2011data(df11, 2)
# df12q2 = cleaningDataframes.clean2012data(df12, 2)
# df13q2 = cleaningDataframes.clean2013data(df13, 2)
# df14q2 = cleaningDataframes.clean2014data(df14, 2)
# df15q2 = cleaningDataframes.clean2015data(df15, 2)
# df16q2 = cleaningDataframes.clean2016data(df16, 2)
# df17q2 = cleaningDataframes.clean2017data(df17, 2)
# df18q2 = cleaningDataframes.clean2018data(df18, 2)
# df19q2 = cleaningDataframes.clean2019data(df19, 2)
# df20q2 = cleaningDataframes.clean2020data(df20, 2)

# options 3 get the data from each year for business question 3
# 2011 Cleaning function ready
df11q3 = cleaningDataframes.clean2011data(df11, 3)
# 2012 Cleaning function ready
df12q3 = cleaningDataframes.clean2012data(df12, 3)
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

visualizationModule.list_basic_viz()

# format the dataframes for Q3:
dict_q3_2011 = visualizationModule.q3_data_format(df11q3, 2011)
dict_q3_2012 = visualizationModule.q3_data_format(df12q3, 2012)
dict_q3_2013 = visualizationModule.q3_data_format(df13q3, 2013)
dict_q3_2014 = visualizationModule.q3_data_format(df14q3, 2014)
dict_q3_2015 = visualizationModule.q3_data_format(df15q3, 2015)
dict_q3_2016 = visualizationModule.q3_data_format(df16q3, 2016)
dict_q3_2017 = visualizationModule.q3_data_format(df17q3, 2017)
dict_q3_2018 = visualizationModule.q3_data_format(df18q3, 2018)
dict_q3_2019 = visualizationModule.q3_data_format(df19q3, 2019)
dict_q3_2020 = visualizationModule.q3_data_format(df20q3, 2020)

# take all the dictionaries into our visualization function and plot the functions
# visualizationModule.q3_visualization_for_all_years(dict_q3_2011, dict_q3_2012, dict_q3_2013, dict_q3_2014, dict_q3_2015,
                                                   # dict_q3_2016, dict_q3_2017, dict_q3_2018, dict_q3_2019, dict_q3_2020)
# first let's get all the barcharts from 2011 to 2020:
visualizationModule.q3_visualization_bar_single_year(dict_q3_2011, "2011proglangbar.html")
visualizationModule.q3_visualization_bar_single_year(dict_q3_2012, "2012proglangbar.html")
visualizationModule.q3_visualization_bar_single_year(dict_q3_2013, "2013proglangbar.html")
visualizationModule.q3_visualization_bar_single_year(dict_q3_2014, "2014proglangbar.html")
visualizationModule.q3_visualization_bar_single_year(dict_q3_2015, "2015proglangbar.html")
visualizationModule.q3_visualization_bar_single_year(dict_q3_2016, "2016proglangbar.html")
visualizationModule.q3_visualization_bar_single_year(dict_q3_2017, "2017proglangbar.html")
visualizationModule.q3_visualization_bar_single_year(dict_q3_2018, "2018proglangbar.html")
visualizationModule.q3_visualization_bar_single_year(dict_q3_2019, "2019proglangbar.html")
visualizationModule.q3_visualization_bar_single_year(dict_q3_2020, "2020proglangbar.html")
# take the input x,y axis data, label data etc. for the visualization for q3:
# visualizationModule.q3_visualization()

# basic statistics and visualizations:

# using our analysis answer the business questions
