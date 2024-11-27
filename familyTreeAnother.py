import pandas as pd
# 读取CSV文件
df = pd.read_csv('family_tree.csv')
# 数据清洗示例：去除空值、格式化日期等
df.dropna(inplace=True)
df['birth_date'] = pd.to_datetime(df['birth_date'])
# 显示预处理后的数据
print(df.head())
class FamilyMember:
    def __init__(self, name, gender, birth_date, parent=None):
        self.name = name
        self.gender = gender
        self.birth_date = birth_date
        self.parent = parent
        self.children = []
    def add_child(self, child):
        self.children.append(child)
members = {}
for index, row in df.iterrows():
    member = FamilyMember(row['name'], row['gender'], row['birth_date'])
    members[row['name']] = member
for index, row in df.iterrows():
    if row['parent_name'] in members:
        parent = members[row['parent_name']]
        parent.add_child(members[row['name']])
        members[row['name']].parent = parent
from graphviz import Digraph
def visualize_family_tree(root):
    dot = Digraph(comment='Family Tree')
    def add_nodes_edges(member):
        dot.node(member.name, f"{member.name}\n{member.birth_date.strftime('%Y-%m-%d')}")
        if member.parent:
            dot.edge(member.parent.name, member.name)
        for child in member.children:
            add_nodes_edges(child)
    add_nodes_edges(root)
    dot.render('family_tree', format='png', view=True)
# 假设有一个根节点root
root = members['某家族始祖']
visualize_family_tree(root)
