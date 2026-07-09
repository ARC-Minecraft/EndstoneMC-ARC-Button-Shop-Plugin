import re

# Read code
with open('src/endstone_arc_button_shop/arc_button_shop.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Extract all GetText keys
keys = sorted(set(re.findall(r"\.GetText\(['\"]([^'\"]+)['\"]", code)))
print(f"Total unique GetText keys in code: {len(keys)}")
for k in keys:
    print(f"  CODE: {k}")

# Read CN.txt
with open('dist/ARCButtonShop/CN.txt', 'r', encoding='utf-8') as f:
    cn_lines = f.readlines()

cn_keys = set()
for line in cn_lines:
    line = line.strip()
    if line and not line.startswith('#') and '=' in line:
        key = line.split('=', 1)[0].strip()
        cn_keys.add(key)

print(f"\nTotal keys in CN.txt: {len(cn_keys)}")

# Find missing keys
missing_in_cn = [k for k in keys if k not in cn_keys]
print(f"\nKeys in code but MISSING from CN.txt ({len(missing_in_cn)}):")
for k in missing_in_cn:
    print(f"  MISSING: {k}")

# Find unused keys
unused_in_code = [k for k in sorted(cn_keys) if k not in set(keys)]
print(f"\nKeys in CN.txt but UNUSED in code ({len(unused_in_code)}):")
for k in unused_in_code:
    print(f"  UNUSED: {k}")