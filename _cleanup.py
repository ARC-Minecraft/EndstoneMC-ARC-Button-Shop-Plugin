#!/usr/bin/env python3
"""Cleanup script to remove leftover YAML content from PriceManager.py"""

with open('src/endstone_arc_button_shop/PriceManager.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the end of new _create_default_config method
# and the start of _parse_config method
new_method_end = None
parse_config_start = None

for i, line in enumerate(lines):
    # Find the last line of the new _create_default_config (the except block with 'Failed to create default config')
    if 'Failed to create default config' in line and i < 200:
        new_method_end = i
    # Find the start of _parse_config
    if 'def _parse_config' in line:
        parse_config_start = i

print(f'New method end line (0-indexed): {new_method_end}')
print(f'Parse config start line (0-indexed): {parse_config_start}')

if new_method_end is not None and parse_config_start is not None:
    print(f'Lines to remove: {new_method_end + 2} to {parse_config_start} (1-indexed)')
    print(f'Total lines before: {len(lines)}')
    
    # Keep lines 0 to new_method_end (inclusive), then a blank line, then lines from parse_config_start onwards
    new_lines = lines[:new_method_end + 1] + ['\n'] + lines[parse_config_start:]
    
    print(f'Total lines after: {len(new_lines)}')
    
    with open('src/endstone_arc_button_shop/PriceManager.py', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print('File cleaned successfully!')
else:
    print('ERROR: Could not find method boundaries!')
    if new_method_end is None:
        print('  - Could not find end of _create_default_config')
    if parse_config_start is None:
        print('  - Could not find start of _parse_config')