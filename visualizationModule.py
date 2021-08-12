# from pyecharts.charts import Bar
# from pyecharts import options as opts
from operator import itemgetter
from collections import Counter
from pyecharts.charts import Bar
from pyecharts import options as opts
import numpy as np


# basic visualization for any cleaned dataframe:
def list_basic_viz():
    print("visualization")


# format the data for question and visualization
def q3_data_format(df_in, year_df):
    # print the reminder message
    print("Formatting the cleaned dataframes for visualization")
    # get the total number of rows of cleaned data
    total_num_rows = len(df_in.index)
    # get the column section and use as a list
    all_list = df_in["Prog_languages"].tolist()
    # create a list to store all the languages mentioned in the survey response
    cleaned_list = []
    for i in all_list:
        m_list = i.split(";")
        for m in m_list:
            cleaned_list.append(m.strip())
    # use the Counter() function from collections
    # to count the number of appearances for each language
    lang_year = Counter(cleaned_list)
    # language of this year in dict format:
    lang_year = dict(lang_year)
    # transform each language's appearance in "%"
    for key in lang_year:
        lang_year[key] = (lang_year[key] / total_num_rows) * 100
    # keep only the top n results
    res_year = dict(sorted(lang_year.items(), key=itemgetter(1), reverse=True)[:25])
    # add the year information
    res_year['Year'] = year_df
    # return the dict for plotting
    return res_year


def q3_visualization_bar_single_year(dict_year, viz_html_name):
    """
    :param dict_year:
    result of this function is a rendered html visualization barchart
    """
    # keep the year data for title and x axis
    year_num = dict_year['Year']
    # then delete the year entry
    del dict_year['Year']
    # get the lists ready for plotting
    res_keys = list(dict_year.keys())
    lang_values = list(dict_year.values())
    # round up the percentage values
    lang_values = list(np.around(np.array(lang_values), 2))
    bar = Bar()
    bar.add_xaxis(res_keys)
    bar.add_yaxis("Percentage", lang_values)
    # set the title ready
    bar.set_global_opts(title_opts=opts.TitleOpts(title="25 Most Popular Languages from \n StackOverflow"
                                                        "Survey Result for year " + str(year_num)))
    bar.render(viz_html_name)


def q3_visualization_for_all_years():
    print("testing")

# Pyecharts HTML render example:
# from pyecharts.charts import Bar
# from pyecharts import options as opts
#
# # V1 版本开始支持链式调用
# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
#     .add_yaxis("商家aaa", [114, 55, 27, 101, 125, 27, 105])
#     .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
#     .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
# )
# bar.render("example.html")

# 不习惯链式调用的开发者依旧可以单独调用方法
# bar = Bar()
# bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
# bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
# bar.render(example.html)
