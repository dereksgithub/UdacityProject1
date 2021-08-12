# from pyecharts.charts import Bar
# from pyecharts import options as opts

def list_basic_viz():
    print("visualization")


# format the data for question and visualization
def q3_data_format(dfin):
    # print the reminder message
    print("Formatting the cleaned dataframes for visualization")
    # get the column section and use as a list
    all_list = dfin["Prog_languages"].tolist()
    # create a list to store all the languages mentioned in the survey response
    cleaned_list = []
    for i in all_list:
        m_list = i.split(";").strip()
        for m in m_list:
            cleaned_list.append(m)
    # use the Counter() function from collections
    # to count the number of appearances for each language


def q3_visualization():
    # take the
    #
    print("remember to remove spaces")




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