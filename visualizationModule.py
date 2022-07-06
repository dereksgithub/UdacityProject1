# from pyecharts.charts import Bar
# from pyecharts import options as opts
from operator import itemgetter
from collections import Counter
from pyecharts.charts import Bar
# from pyecharts import options as opts
import numpy as np
import pyecharts.options as opts
from pyecharts.charts.basic_charts.line import Line
import pandas as pd


# basic visualization for any cleaned dataframe:
def list_basic_viz():
    print("visualization")


# format the data for question and visualization
def q3_data_format(df_in, year_df, n_lang):
    """
    This function formats the cleaned question 3 dataframe and transform it into a dictionary.
    e.g. {'SQL': 57.356076759061835, 'JavaScript': 50.49751243781094}
    :param df_in: the survey result dataframe that is cleaned for question 3
    :param year_df: this sets the year of the data e.g. 2011, 2012
    :param n_lang: how many languages would like to explore
    :return: res_year: the result dict for this year
    """
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
    # remove "Other(s):", "None", "Cloud (AWS, GAE, Azure, etc.)", "iOS", "Android"
    cleaned_list = [x for x in cleaned_list if
                    x not in ("Other(s):", "None", "Windows Phone",
                              "Cloud (AWS, GAE, Azure, etc.)", "iOS", "Android")]
    # format the language names with the following rules:
    replacements = {"VB": "Visual Basic",
                    "vb.net": "VB.NET",
                    "VB.Net": "VB.NET",
                    "Arduino / Raspberry Pi": "Assembly",
                    "Bash/Shell": "Bash/Shell/PowerShell",
                    "Bash": "Bash/Shell/PowerShell",
                    "bash": "Bash/Shell/PowerShell",
                    "perl": "Perl",
                    "Visual Basic 6": "Visual Basic",
                    "C++11": "C++",
                    "HTML": "HTML/CSS",
                    "HTML5": "HTML/CSS",
                    "groovy": "Groovy",
                    "LAMP": "Bash/Shell/PowerShell",
                    "python": "Python"}
    cleaned_list = [replacements.get(x, x) for x in cleaned_list]
    # clean the CSS/HTML name confusion
    if year_df < 2013:
        cleaned_list = [x for x in cleaned_list if x not in ("HTML/CSS", "")]
        replacements2 = {"CSS": "HTML/CSS"}
        cleaned_list = [replacements2.get(x, x) for x in cleaned_list]
    else:
        cleaned_list = [x for x in cleaned_list if x not in ("CSS", "")]
    # use the Counter() function from collections
    # to count the number of appearances for each language
    lang_year = Counter(cleaned_list)
    # language of this year in dict format:
    lang_year = dict(lang_year)
    # transform each language's appearance in "%"
    for key in lang_year:
        lang_year[key] = (lang_year[key] / total_num_rows) * 100
    # keep only the top 25 results
    # res_year = dict(sorted(lang_year.items(), key=itemgetter(1), reverse=True)[:n_lang])
    res_year = dict(sorted(lang_year.items(), key=itemgetter(1), reverse=True)[:n_lang])
    # keep only the top 11 that we need this is from reading the visuals.
    res_dict_filter = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])
    lang_to_keep = ("SQL", "JavaScript", "HTML/CSS", "C", "C++", "PHP", "C#", "Python",
                    "Bash/Shell/PowerShell", "Java")
    # filter out only the 10 results that we need to know
    res_year = res_dict_filter(res_year, lang_to_keep)
    # add the year information
    res_year['Year'] = year_df
    # return the dict for plotting
    return res_year


def q3_visualization_bar_single_year(dict_year, viz_html_name):
    """
    This method visualize the dict data from the method q3_data_format(df_in, year_df), into bar charts
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


def q3_visualization_for_all_years(*argv):
    """
    This function can take multiple dictionaries as input and transform them into a dataframe that is ready for
    visualization using pyecharts library.
    :return: this function renders the visualization into a HTML page, with no specific output
    """
    # using a for loop to iterate through the dicts
    # for arg_dict in argv:
    #     which_year = arg_dict['Year']
    #     del arg_dict['Year']
    #     print(which_year)
    #     print(arg_dict)
    df_raw = pd.DataFrame(argv)
    # there will be many NaNs, replace them with 0 for plotting
    df_cleaned = df_raw.fillna(0)
    # keep only 2 decimals
    df_plotting = df_cleaned.round(2)

    # print(df_plotting["Year"])
    # for col in df_cleaned.columns:
    #    print(col)

    # start the plotting section:
    week_name_list = df_plotting["Year"]
    # initialize the line object
    line = Line(init_opts=opts.InitOpts(width="2000px", height="1600px"))
    line.add_xaxis(xaxis_data=week_name_list)
    for col in df_cleaned.columns:
        if col != "Year":
            line.add_yaxis(series_name=col, y_axis=df_cleaned[col])
        # markpoint_opts=opts.MarkPointOpts(
        # data=[ opts.MarkPointItem(type_="max", name="最大值"),
        #         opts.MarkPointItem(type_="min", name="最小值"), ] ),
        # markline_opts=opts.MarkLineOpts(
        #      data=[opts.MarkLineItem(type_="average", name="平均值")] ),)
    # line.add_yaxis(
    #         series_name="最低气温",
    #         y_axis=low_temperature,
    #         markpoint_opts=opts.MarkPointOpts(
    #             data=[opts.MarkPointItem(value=-2, name="low point", x=1, y=-1.5)]
    #         ),
    #         markline_opts=opts.MarkLineOpts(
    #             data=[
    #                 # opts.MarkLineItem(type_="average", name="Average"),
    #                 # opts.MarkLineItem(symbol="none", x="90%", y="max"),
    #                 opts.MarkLineItem(symbol="circle", type_="max", name="high point"),
    #             ]
    #         ),
    # )

    line.set_global_opts(
        title_opts=opts.TitleOpts(title="% of Programming Language from the Survey ",
                                  subtitle="% of people from the survey who uses this Language"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        toolbox_opts=opts.ToolboxOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    line.render("lang_10_years.html")
