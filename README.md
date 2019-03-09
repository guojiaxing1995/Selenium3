# Selenium3
python3 + selenium3 web自动化

项目整合了数据驱动、关键字驱动和行为驱动测试框架。其中数据驱动采用PO分层的设计思想，结合unnitest实现分层自动化。支持多个浏览器同时运行case、生成结果报告、保存错误截图和自定义日志等功能



### 数据驱动
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/guojiaxing1995/Selenium3/blob/master/github_img/数据驱动.png" width="180" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/guojiaxing1995/Selenium3/blob/master/github_img/配置文件.png"  width="300"/>

配置文件中配置需要测试的浏览器和元素定位信息。用例层调用业务层，业务层调用元素层，一个页面的元素放在一个page。分层设计方便了项目维护，减少维护成本。


### 关键字驱动

目录中keyword包下为关键字驱动内容。由于用的不多，目前只封装了get_url、input、click、sleep、close_browser关键字。系统运行的用例数据目前支持从excel表格中读取，后期有计划增加用例存储的形式，如mysql、mongodb数据库，项目中也已有python连接数据库的功能实现。

### 行为驱动

选择的是behave库进行行为驱动。
