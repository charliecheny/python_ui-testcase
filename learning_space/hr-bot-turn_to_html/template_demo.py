
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import os
env = Environment(loader=FileSystemLoader("."),
                  autoescape=select_autoescape(['html', 'xml']))
template = env.get_template("temple.html")
reportname = datetime.datetime.now().strftime('%Y-%m-%d')
htmlname = 'test'
data = {
    'reportName': reportname,
    'biaotou':[],
    'biaoneirong':[]
}
# 寻找当前文件夹路径下以.jtl结尾的文件，找不到就默认找test.jtl
t = 'test.jtl'
for file in os.listdir("."):
    if file.endswith('.jtl'):
        t = file
        break
with open(t, 'r', encoding='utf-8') as f:
    list1 = []
    for line in f:
        # 去除每一行的换行符
        line = line.strip('\n')
        # 以逗号切分字符串
        split = line.split(',')
        # 将每个切出来的字符串加入到列表中
        list1.append(split)
data['biaotou'] = list1[0]
data['biaoneirong'] = [i for i in list1[1:]]
template.stream(data=data).dump(f"{htmlname}.html")


#learning_day01_15