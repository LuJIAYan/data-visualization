#交互筛选出交互图ok，关于每个标签主题的每一年浏览量
from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Line

app = Flask(__name__)

# 准备工作 
# pandas 大法读内容, 用dropna()丢缺失值, 用unique()取唯一值, 不重覆
df = pd.read_csv('themes2.csv', encoding='gbk')
years_sum = pd.read_excel('years_sum.xlsx',encoding='utf-8')

regions_available_loaded = list(df.themes.dropna().unique())

# 基本cufflinks 及ploty設置, 查文檔看書貼上而已
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()


@app.route('/',methods=['GET'])
def TED_2019():

    data_str = df.to_html()  # 使用pandas 数据框之方法.to_html() !! 取代原 "Hello"
                             # pandas真是数据科学家的好朋友!
    
    regions_available = regions_available_loaded #下拉选单有内容
    return render_template('results2.html',
                           the_res = data_str,   # 表
                           the_select_region=regions_available)   

@app.route('/TED',methods=['POST'])
def hu_run_select() -> 'html':
    
    the_region = request.form["the_region_selected"] ## 取得用户交互输入
    
    print(the_region)                                 ## 检查用户输入, 在后台

    dfs = df.query("themes=='{}'".format(the_region)) ## 使用df.query()方法. 按用户交互输入the_region过滤

    data_str = dfs.to_html()  # <------------------数据产出dfs, 完成互动过滤呢
    
    ## plot_all = "交互式图还没做好" # <------------------交互式图  其實應該放這, 按過濾出的數據來做圖
    ## 交互式可视化画图
    test = the_region
    fig = dfs.iplot(kind="bar", x="years", y="views", asFigure=True)# 使用iplot 做bar圖
    py.offline.plot(fig, filename="成果.html",auto_open=False)                  # 備出"成果.html"檔案之交互圖
    with open("成果.html", encoding="utf8", mode="r") as f:                     # 把"成果.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())
    

    
    regions_available =  regions_available_loaded #下拉选单有内容
    return render_template('results2.html',
                            the_test = test,
                            the_plot_all = plot_all,
                            the_res = data_str,
                            the_select_region=regions_available,
                           )

#第二个图
@app.route('/TED',methods=['POST'])
def TED_zhi() -> 'html':
    
# 看看那些主题比较受关注（评论比较多）


    x=df['comments']
    y = df['themes']
# Use `y` argument instead of `x` for horizontal histogram

    fig = go.Figure(data=[go.Histogram(y=y)])
    fig.show()
    py.offline.plot(fig, filename="成果2.html",auto_open=False)  


#              ^^^这里可以只放数据data，也可以将数据data和排版layout结合，这是典型的面向对象
    with open("成果2.html.html", encoding="utf8", mode="r") as f:                     # 把"成果.html"當文字檔讀入成字符串
        plot_all2 = "".join(f.readlines())
    

    
    regions_available =  regions_available_loaded #下拉选单有内容
    return render_template('results2.html',
                            the_plot_all2 = plot_all2,
                           )





if __name__ == '__main__':
    app.run(port = 8013)   # debug=True, 在py使用, 在ipynb不使用