
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
env = Environment(loader=FileSystemLoader("."),
                  autoescape=select_autoescape(['html', 'xml']))
template = env.get_template("temple.html")
# data = {
#     "reportName":'哇哈哈',
#     'users': [
#         {
#             'url': 123,
#             'username': 56589
#         },
#         {
#             'url': 'sdfaadfda',
#             'username': "sdasdasda"
#         }
#     ]
# }

data = {
    'biaotou':[],
    'biaoneirong':[]
}
with open("./test.jtl", 'r', encoding='utf-8') as f:
    list1 = []
    for line in f:
        # 去除每一行的换行符
        line = line.strip('\n')
        split = line.split(',')
        list1.append(split)
        # print(len(split))
        # print(split)
    print(len(list1))
    print(list1[0])
data['biaotou'] = list1[0]
data['biaoneirong'] = [i for i in list1[1:]]

htmlname = datetime.datetime.now().strftime('%Y-%m-%d')

template.stream(data=data).dump(f"{htmlname}.html")

#learning_day01_15