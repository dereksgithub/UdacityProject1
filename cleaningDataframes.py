# get pandas:
import pandas as pd


# cleaning function for 2011 data
def clean2011data(df11, questionoption2011):
    """
    This is the cleaning function dedicated for the 2011 data
    :param df11: data frame for 2011 survey result
    :param questionoption2011: 1,2, or 3 ( any input other than 1 or 2 will be recognized as 3)
    :return: the cleaned dataframe for question 1, 2 or 3
    """
    # display the reminder that the program has started
    print("extracting data from the 2011 survey data")
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
        dfout11 = pd.DataFrame(df11['Prog_languages'])
        # add the 2011 year column
        dfout11['Year'] = '2011'
        # drop NaN rows
        dfout11 = dfout11.dropna()
        # testing
        # print(dfout11)
        return dfout11


def clean2012data(df12, questionoption2012):
    """
    This is the cleaning function dedicated for the 2012 data
    :param df12: data frame for 2012 survey result
    :param questionoption2012: 1,2, or 3 ( any input other than 1 or 2 will be recognized as 3)
    :return: the cleaned dataframe for question 1, 2 or 3
    """
    # display the reminder that the program has started
    print("extracting data from the 2012 survey data")
    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2012 == 1:
        print("question1")
    elif questionoption2012 == 2:
        print("question2")
    else:
        # here we take the columns that contains languages merge columns
        df12['Prog_languages'] = df12[df12.columns[22:37]].apply(
            lambda x: ';'.join(x.dropna().astype(str)),
            axis=1)
        # rename the merged column
        dfout12 = pd.DataFrame(df12['Prog_languages'])
        # add the 2012 year column
        dfout12['Year'] = '2012'
        # drop NaN rows
        dfout12 = dfout12.dropna()
        # testing
        # print(dfout12)
        return dfout12


def clean2013data(df13, questionoption2013):
    """
    This is the cleaning function dedicated for the 2013 data
    :param df13: data frame for 2013 survey result
    :param questionoption2013: 1,2, or 3 ( any input other than 1 or 2 will be recognized as 3)
    :return: the cleaned dataframe for question 1, 2 or 3
    """
    # display the reminder that the program has started
    print("extracting data from the 2013 survey data")
    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2013 == 1:
        print("question1")
    elif questionoption2013 == 2:
        print("question2")
    else:
        # sort out all columns that contains languages amd merge them into one col
        df13['Prog_languages'] = df13[df13.columns[56:70]].apply(
            lambda x: ';'.join(x.dropna().astype(str)),
            axis=1)
        # rename the merged column
        dfout13 = pd.DataFrame(df13['Prog_languages'])
        # add the 2013 year column
        dfout13['Year'] = '2013'
        # drop NaN rows
        dfout13 = dfout13.dropna()
        # testing
        # print(dfout13)
        return dfout13


def clean2014data(df14, questionoption2014):
    """
    This is the cleaning function dedicated for the 2014 data
    :param df14: data frame for 2014 survey result
    :param questionoption2014: 1,2, or 3 ( any input other than 1 or 2 will be recognized as 3)
    :return: the cleaned dataframe for question 1, 2 or 3
    """
    # display the reminder that the program has started
    print("extracting data from the 2014 survey data")
    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2014 == 1:
        print("question1")
    elif questionoption2014 == 2:
        print("question2")
    else:
        # sort out all columns that contains languages amd merge them into one col
        df14['Prog_languages'] = df14[df14.columns[42:54]].apply(
            lambda x: ';'.join(x.dropna().astype(str)),
            axis=1)
        # rename the merged column
        dfout14 = pd.DataFrame(df14['Prog_languages'])
        # add the 2014 year column
        dfout14['Year'] = '2014'
        # drop NaN rows
        dfout14 = dfout14.dropna()
        # testing
        # print(dfout14)
        return dfout14


def clean2015data(df15, questionoption2015):
    """
    This is the cleaning function dedicated for the 2015 data
    :param df15: data frame for 2015 survey result
    :param questionoption2015: 1,2, or 3 ( any input other than 1 or 2 will be recognized as 3)
    :return: the cleaned dataframe for question 1, 2 or 3
    """
    # display the reminder that the program has started
    print("extracting data from the 2015 survey data")
    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2015 == 1:
        print("question1")
    elif questionoption2015 == 2:
        print("question2")
    else:
        # sort out all columns that contains languages amd merge them into one col
        df15['Prog_languages'] = df15[df15.columns[10:50]].apply(
            lambda x: ';'.join(x.dropna().astype(str)),
            axis=1)
        # Rename the column header
        dfout15 = pd.DataFrame(df15['Prog_languages'])
        # add the year 2015 column
        dfout15['Year'] = '2015'
        # testing
        # print(dfout15)
        # 2015 data row 0 is not meaningful, remove row 0
        dfout15 = dfout15.drop([0])
        # drop NaN rows
        dfout15 = dfout15.dropna()
        # testing code
        # print(dfout15)
        # return the cleaned dataset
        return dfout15


def clean2016data(df16, questionoption2016):
    """
    This is the cleaning function dedicated for the 2016 data
    :param df16: data frame for 2016 survey result
    :param questionoption2016: 1,2, or 3 ( any input other than 1 or 2 will be recognized as 3)
    :return: the cleaned dataframe for question 1, 2 or 3
    """
    # display the reminder that the program has started
    print("extracting data from the 2016 survey data")
    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2016 == 1:
        print("question1")
    elif questionoption2016 == 2:
        print("question2")
    else:
        # get the column where all languages are stored
        dfout16 = pd.DataFrame(df16['tech_do'])
        # rename the column name to 'Prog_languages'
        dfout16 = dfout16.rename(columns={'tech_do': 'Prog_languages'})
        # add the year column
        dfout16['Year'] = 2016
        # drop the NaNs
        dfout16 = dfout16.dropna()
        # testing
        # print(dfout16)
        # return the cleaned dataset
        return dfout16


def clean2017data(df17, questionoption2017):
    """
    This is the cleaning function dedicated for the 2017 data
    :param df17: data frame for 2017 survey result
    :param questionoption2017: 1,2, or 3 ( any input other than 1 or 2 will be recognized as 3)
    :return: the cleaned dataframe for question 1, 2 or 3
    """
    # display the reminder that the program has started
    print("extracting data from the 2017 survey data")
    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2017 == 1:
        print("question1")
    elif questionoption2017 == 2:
        print("question2")
    else:
        # get the column where all languages are stored
        dfout17 = pd.DataFrame(df17['HaveWorkedLanguage'])
        # rename the column name to 'Prog_languages'
        dfout17 = dfout17.rename(columns={'HaveWorkedLanguage': 'Prog_languages'})
        # add the year column
        dfout17['Year'] = 2017
        # drop the NaNs
        dfout17 = dfout17.dropna()
        # testing
        print(dfout17)
        # return the cleaned dataset
        return dfout17


def clean2018data(df18, questionoption2018):
    """
    This is the cleaning function dedicated for the 2018 data
    :param df18: data frame for 2018 survey result
    :param questionoption2018: 1,2, or 3 ( any input other than 1 or 2 will be recognized as 3)
    :return: the cleaned dataframe for question 1, 2 or 3
    """
    # display the reminder that the program has started
    print("extracting data from the 2018 survey data")
    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2018 == 1:
        print("question1")
    elif questionoption2018 == 2:
        print("question2")
    else:
        dfout18 = pd.DataFrame(df18['LanguageWorkedWith'])
        # rename the column name to 'Prog_languages'
        dfout18 = dfout18.rename(columns={'LanguageWorkedWith': 'Prog_languages'})
        # add the year column
        dfout18['Year'] = 2018
        # drop the NaNs
        dfout18 = dfout18.dropna()
        # testing
        print(dfout18)
        # return the cleaned dataset
        return dfout18


def clean2019data(df19, questionoption2019):
    """
    This is the cleaning function dedicated for the 2019 data
    :param df19: data frame for 2019 survey result
    :param questionoption2019: 1,2, or 3 ( any input other than 1 or 2 will be recognized as 3)
    :return: the cleaned dataframe for question 1, 2 or 3
    """
    # display the reminder that the program has started
    print("extracting data from the 2019 survey data")
    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2019 == 1:
        print("question1")
    elif questionoption2019 == 2:
        print("question2")
    else:
        dfout19 = pd.DataFrame(df19['LanguageWorkedWith'])
        # rename the column name to 'Prog_languages'
        dfout19 = dfout19.rename(columns={'LanguageWorkedWith': 'Prog_languages'})
        # add the year column
        dfout19['Year'] = 2019
        # drop the NaNs
        dfout19 = dfout19.dropna()
        # testing
        # print(dfout19)
        # return the cleaned dataset
        return dfout19


def clean2020data(df20, questionoption2020):
    """
    This is the cleaning function dedicated for the 2020 data
    :param df20: data frame for 2020 survey result
    :param questionoption2020: 1,2, or 3 ( any input other than 1 or 2 will be recognized as 3)
    :return: the cleaned dataframe for question 1, 2 or 3
    """
    # display the reminder that the program has started
    print("extracting data from the 2020 survey data")
    # option = 1 means we use the cleaning function to clean the dataframe and get information needed to answer business
    # question 1
    if questionoption2020 == 1:
        print("question1")
    elif questionoption2020 == 2:
        print("question2")
    else:
        dfout20 = pd.DataFrame(df20['LanguageWorkedWith'])
        # rename the column name to 'Prog_languages'
        dfout20 = dfout20.rename(columns={'LanguageWorkedWith': 'Prog_languages'})
        # add the year column
        dfout20['Year'] = 2020
        # drop the NaNs
        dfout20 = dfout20.dropna()
        # testing
        # print(dfout20)
        # return the cleaned dataset
        return dfout20
