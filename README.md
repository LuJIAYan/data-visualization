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
        <td><b><code>初稿</code></b></td>
    </tr>    
    <tr>
        <td rowspan="6"><b>小组成员</b></td>
        <td><a href="https://gitee.com/lujiayan">@卢佳燕</a></td>
    </tr>
   
</table>

## 背景介绍
TED由Richard Saulman创立于1984年，是一家旨在将技术(technology)，娱乐(entertainment)和设计(design)领域的专家聚集在一起的非盈利组织。Ted的口号是"Ideas worth spreading"，也就是“值得传播的思想”。每年2-3月，TED大会在北美召集众多领域的杰出人物，为他们提供了一个平台，将多年的工作和研究提炼为简短有力的演讲（通常少于18分钟），并上传到TED官网供观众免费收看。同时，独立运行的TEDx鼓励各地的TED粉丝自发组织TED风格的活动，在世界各地的社区分享想法。

## 数据集可探索、研究的方向
* 浏览量最高的10个TED视频可视化分析
* 讨论量最高的10个TED视频可视化分析
* 浏览和讨论是否成正比，是否有水分
* 演讲的人多数来是什么职业
* 什么时候演讲比较多

## 预计产出的最小可行性产品
### 产出包含数据可视化和总结可交互数据可视化html（基于flask渲染的html页面）
* 交互部分
<table>
    <tr>
        <td>下拉选单联动可视化</td>
        <td>分类筛选</td>
		<td>不用年份演讲浏览数量</td>   
    </tr>
	<tr>
        <td>TED演讲时间分布</td>
        <td>拖动的时间轴</td>
		<td>不同时间演讲分类对应的评论数量</td>   
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
		 <td>演讲者职业和演讲数量</td>
		 <td>条形图</td>
	</tr>
	<tr>
		 <td>时间和演讲数量</td>
		 <td>折线图</td>
	</tr>
</table>



## 产品特色功能--可交互的数据可视化产品
* pandas做数据清理和处理
* plotly可视化
* flask模块渲染页面
* 参考一些代码做美化

# [原型文档](https://lujiayan.github.io/Interactive-data-visualization/Axure/#g=1)

## 数据说明
简述：本数据集包含了2017年9月21日之前上传到官方网站TED.com的所有TED Talks演讲录制信息。
文件列表：
* ted_main.csv: 包含演讲主要信息，包括演讲标题，发言人，演讲内容，观看次数，评论数量，演讲评分等。
* transcripts.csv: 包含演讲链接和官方英文字幕。

### 数据来源
数据内容源自于kaggle平台用户分享，基于Creative Commons License发布，具体信息内容源自TED官网。

## TO LIST
TED数据主题分析学习

## <a>版本更替</a>
版本|日期 | 修改内容 | 涉及人员
-|-|-|-
V1.1|2019.12.15 | 展示PRD,招募人员| 卢佳燕
