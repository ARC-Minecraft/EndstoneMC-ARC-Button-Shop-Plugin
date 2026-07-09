"""验证 PriceManager.py 和 dist/official_prices.yml 定价一致性"""
import re

f1 = open('src/endstone_arc_button_shop/PriceManager.py', encoding='utf-8').read()
f2 = open('dist/ARCButtonShop/official_prices.yml', encoding='utf-8').read()

# 提取 sell/buy 对
pairs1 = re.findall(r'(minecraft:\w+):\s+sell:\s+(\d+)\s+buy:\s+(\d+)', f1)
pairs2 = re.findall(r'(minecraft:\w+):\s+sell:\s+(\d+)\s+buy:\s+(\d+)', f2)

items1 = {k: (int(s), int(b)) for k, s, b in pairs1}
items2 = {k: (int(s), int(b)) for k, s, b in pairs2}

print(f'PriceManager items: {len(items1)}')
print(f'dist yml items: {len(items2)}')

# 检查 sell=2*buy 规则
violations1 = [(k, s, b) for k, (s, b) in items1.items() if s != b * 2]
violations2 = [(k, s, b) for k, (s, b) in items2.items() if s != b * 2]
print(f'PM sell!=2*buy violations: {len(violations1)}')
print(f'YML sell!=2*buy violations: {len(violations2)}')

# 检查两文件差异
all_keys = set(items1.keys()) | set(items2.keys())
diffs = []
for k in sorted(all_keys):
    if k not in items1:
        diffs.append(f'  {k}: only in YML, sell={items2[k][0]} buy={items2[k][1]}')
    elif k not in items2:
        diffs.append(f'  {k}: only in PM, sell={items1[k][0]} buy={items1[k][1]}')
    elif items1[k] != items2[k]:
        diffs.append(f'  {k}: PM=({items1[k][0]},{items1[k][1]}) YML=({items2[k][0]},{items2[k][1]})')

print(f'\nDifferences between files: {len(diffs)}')
for d in diffs[:30]:
    print(d)