# data-visualization


## 项目介绍
<table>
    <tr>
        <td><b>日期</b></td>
        <td>2019/12/15</td>   
    </tr>
    <tr>
        <td><b>小组协作式数据交互可视化项目</b></td>
        <td> TED演讲数据可视化分析</td>   
    </tr>
	<tr>
        <td><b>完成情况</b></td>
        <td><b><code>完成</code></b></td>
    </tr>    
    <tr>
        <td rowspan="3"><b>小组成员</b></td>
        <td><a href="https://gitee.com/lujiayan">@卢佳燕</a> @李虹霓  @黄嘉雯</td>
	    
</table>

## 背景介绍
TED由Richard Saulman创立于1984年，是一家旨在将技术(technology)，娱乐(entertainment)和设计(design)领域的专家聚集在一起的非盈利组织。Ted的口号是"Ideas worth spreading"，也就是“值得传播的思想”。本研究首先针对ted_main.csv数据集，该数据集包含了2017年9月21日之前上传到官方网站TED.com的所有TED Talks演讲录制信息。

另一个数据集transcripts.csv包含了具体的演讲文本信息，我们稍晚一些时候再进行分析。

首先，让我们简单看一下ted_main.csv数据集的概况，并对数据集进行初步调整，看看有什么值得探索的方向。

## 数据集可探索、研究的方向
* 浏览量最高的10个TED视频可视化分析
* 讨论量最高的10个TED视频可视化分析
* 浏览和讨论是否成正比
* 演讲的人多数来是什么职业
* 什么时候演讲比较多
* TED演讲的评价分析
* 不同时间的观看数和评论数对比

## 预计产出的最小可行性产品
### 产出包含数据可视化和总结可交互数据可视化html（基于flask渲染的html页面）
* 交互部分
<table>
    <tr>
        <td>下拉选单联动可视化</td>
        <td>分类筛选</td>
		<td>不同主题标签的浏览量对比</td>   
    </tr>
	<tr>
        <td>可视化图关联表格处理</td>
        <td>表单折叠</td>
		<td>表格数据太长不美观问题</td>   
    </tr>
    <tr>
        <td>TED演讲top5视频</td>
        <td>点击图片跳转至对应TED视频连接</td>
	<td>top视频连接及对应图片封面</td>   
    </tr>
</table>
	
* 可视化部分
<table>
    <tr>
	     <td>各分类主题和浏览数量</td>
		 <td>条形图</td>
	</tr>
	<tr>
	     <td>浏览量vs评论量</td>
		 <td>相关关系图</td>
	</tr>
	<tr>
		 <td>不同时间的评论和观看数</td>
		 <td>交互折线图</td>
	</tr>
	<tr>
		 <td>演讲者职业和演讲数量</td>
		 <td>条形图</td>
	</tr>
	<tr>
		 <td>时间和演讲数量</td>
		 <td>折线图</td>
	</tr>
</table>



## 产品特色功能--可交互的数据可视化产品
* [pandas做数据清理和处理](https://github.com/LuJIAYan/data-visualization/blob/master/data/tedtalk/ted_clean2tu%20-%20%E5%B9%B4%E4%BB%BD.ipynb)
* [plotly可视化](https://github.com/LuJIAYan/data-visualization/tree/master/plotly%20html)
* [flask模块渲染页面](https://github.com/LuJIAYan/data-visualization/tree/master/flask_final) pythonanywhere部署努力中
* [dashipynb文件](https://github.com/LuJIAYan/data-visualization/tree/master/dash)

* [参考一些代码做美化](https://www.runoob.com/bootstrap/bootstrap-tutorial.html)  (Bootstrap 表单、面板、折叠、图片排版等、网上css样式）

# [原型文档](https://lujiayan.github.io/data-visualization/Axure/#g=1&p=%E9%A6%96%E9%A1%B5)

## 数据说明
简述：本数据集包含了2017年9月21日之前上传到官方网站TED.com的所有TED Talks演讲录制信息。

文件列表：

* ted_main.csv: 包含演讲主要信息，包括演讲标题，发言人，演讲内容，观看次数，评论数量，演讲评分等。
* transcripts.csv: 包含演讲链接和官方英文字幕。

### 数据来源
[数据内容](https://www.kaggle.com/rounakbanik/ted-talks)源自于kaggle平台用户分享，基于Creative Commons License发布，具体信息内容源自TED官网。

[flask参考](https://segmentfault.com/a/1190000017330435)

## TO do LIST
TED数据主题分析学习

## <a>版本更替</a>
版本|日期 | 修改内容 | 涉及人员
-|-|-|-
V1.1|2019.12.15 | 展示PRD,招募人员| 卢佳燕
V2|2019.12.18 | 数据清洗及部分可视化| 卢佳燕
V3|2019.12.30 | dash、flask| 卢佳燕
V4|2019.1.1 | 页面顶部标题图样式和交互处理| 李虹霓
V5|2019.1.1 | 页面底部图片样式和交互处理| 黄嘉雯
