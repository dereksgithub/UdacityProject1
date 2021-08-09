#
import numpy as np
import pandas as pd


def clean2011data(df11, questionoption2011):
    # display the reminder that the program has started
    print("extracting data from the 2011 survey data")

    # place holder
    # print(df11)

    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2011 == 1:
        # process the 2011 dataset and get the information needed only for question and return the dataframe
        print("question1")
    elif questionoption2011 == 2:
        #
        print("question2")
    else:
        # here we take the columns that contains languages merge columns
        df11['Prog_languages'] = df11[df11.columns[31:43]].apply(
            lambda x: ';'.join(x.dropna().astype(str)),
            axis=1)
        # rename the merged column
        dfout = pd.DataFrame(df11['Prog_languages'])
        # add the 2011 year column
        dfout['Year'] = '2011'
        # testing
        # print(dfout)
        return dfout


def clean2012data(df12, questionoption2012):
    # display the reminder that the program has started
    print("extracting data from the 2012 survey data")
    # place holder
    # print(df12)

    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2012 == 1:
        print("question1")
    elif questionoption2012 == 2:
        print("question2")
    else:
        # here we take the columns that contains languages merge columns
        df12['Prog_languages'] = df12[df12.columns[23:37]].apply(
            lambda x: ';'.join(x.dropna().astype(str)),
            axis=1)
        # rename the merged column
        dfout = pd.DataFrame(df12['Prog_languages'])
        # add the 2012 year column
        dfout['Year'] = '2012'
        # testing
        # print(dfout)
        return dfout


def clean2013data(df13, questionoption2013):
    # display the reminder that the program has started
    print("extracting data from the 2013 survey data")
    # place holder
    # print(df13)

    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2013 == 1:
        print("question1")
    elif questionoption2013 == 2:
        print("question2")
    else:
        # sort out all columns that contains languages amd merge them into one col
        df13['Prog_languages'] = df13[df13.columns[57:70]].apply(
            lambda x: ';'.join(x.dropna().astype(str)),
            axis=1)
        # rename the merged column
        dfout = pd.DataFrame(df13['Prog_languages'])
        # add the 2013 year column
        dfout['Year'] = '2013'
        # testing
        # print(dfout)
        return dfout


def clean2014data(df14, questionoption2014):
    # display the reminder that the program has started
    print("extracting data from the 2014 survey data")
    # place holder
    # print(df14)

    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2014 == 1:
        print("question1")
    elif questionoption2014 == 2:
        print("question2")
    else:
        # sort out all columns that contains languages amd merge them into one col
        df14['Prog_languages'] = df14[df14.columns[43:54]].apply(
            lambda x: ';'.join(x.dropna().astype(str)),
            axis=1)
        # rename the merged column
        dfout = pd.DataFrame(df14['Prog_languages'])
        # add the 2014 year column
        dfout['Year'] = '2014'
        # testing
        print(dfout)
        return dfout


def clean2015data(df15, questionoption2015):
    # display the reminder that the program has started
    print("extracting data from the 2015 survey data")
    # place holder
    print(df15)

    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2015 == 1:
        print("question1")
    elif questionoption2015 == 2:
        print("question2")
    else:


        print("question3")


def clean2016data(df16, questionoption2016):
    # display the reminder that the program has started
    print("extracting data from the 2016 survey data")
    # place holder
    print(df16)

    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2016 == 1:
        print("question1")
    elif questionoption2016 == 2:
        print("question2")
    else:
        print("question3")


def clean2017data(df17, questionoption2017):
    # display the reminder that the program has started
    print("extracting data from the 2017 survey data")
    # place holder
    print(df17)

    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2017 == 1:
        print("question1")
    elif questionoption2017 == 2:
        print("question2")
    else:
        print("question3")


def clean2018data(df18, questionoption2018):
    # display the reminder that the program has started
    print("extracting data from the 2018 survey data")
    # place holder
    print(df18)

    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2018 == 1:
        print("question1")
    elif questionoption2018 == 2:
        print("question2")
    else:
        print("question3")


def clean2019data(df19, questionoption2019):
    # display the reminder that the program has started
    print("extracting data from the 2019 survey data")
    # place holder
    print(df19)

    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2019 == 1:
        print("question1")
    elif questionoption2019 == 2:
        print("question2")
    else:
        print("question3")


def clean2020data(df20, questionoption2020):
    # display the reminder that the program has started
    print("extracting data from the 2020 survey data")
    # place holder
    print(df20)

    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2020 == 1:
        print("question1")
    elif questionoption2020 == 2:
        print("question2")
    else:
        print("question3")
