# perform basic statistical anakysis on dataframes for a first-look view of data
import pandas as pd

def listAvg(input_col):
    """
    :param input_col

    :return: output the average of the column
    """
    avg_col = pd.avg()
    # this list average salary
    print("average " + input_col + "is: "+ avg_col)
    # return the calculated average
    return avg_col




def corr_df(df_in, column_name):
    """
    This function uses the correlation function of numpy to calculate basic corr.

    :param df_in: the input dataframe
    :param column_name: the column that the user would like to use as the ref col for corr
    :return: a list of corr / col
    """
    



