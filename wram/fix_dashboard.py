import os

content = open('C:/QA/CUTOVER/fix_content.html', 'r', encoding='utf-8').read()
open('C:/QA/CUTOVER/cutover_dashboard.html', 'w', encoding='utf-8').write(content)
print(f"Done! Written {len(content)} chars")

