剑桥大学健康打卡自动脚本by xwclk
====
* 本代码仅供交流学习使用，基于selenium，模拟真人操作打卡
* location guard定位
* 需要安装火狐firefox浏览器
* python实现，要求版本最好为3.6
## config.yaml
* 本页面主要配置用户名(user)，密码(pass)，打卡时间(time)，打卡成功后提示语(cont)，firefox profile路径（后续讲这是什么？）
* 各参数修改时，切勿漏掉引号，必须保留引号
* 时间格式："hh:mm"。如01:23
## geckodriver
* windows用户：将其放至C:\Windows
* linux用户：将其放至/usr/bin
## firefox设置
1. 打开firefox，在地址栏输入about:profiles
2. 点击左上角的create a new profile
3. 点击next
4. 随便填一个不含空格不含中文的字符串
5. 这时候，观察刚刚创建的profile是否为default profile（若是，其属性为yes，若为no，点击下面的set as default profile）
6. 复制profile地址(root directory)，粘贴到config.yaml的firefox profile路径中（prof）
6. 关闭firefox，重新打开
7. 安装插件，location guard
8. Option中Default Level选择：Use fixed location
9. fix Location中拖动定位标志，拖到想要的地方去
10. 地址栏输入about:preference#privacy，拉到下面permission，location点击settings...，勾选最下面那一栏，并save changed
11. 关闭浏览器
## python配置(安装3.6的版本哦)
1. 进入工程主文件夹，打开命令行，输入pip install -r requirement.txt
2. python autodaka2.py
3. 尽情享受自动打卡的乐趣吧

