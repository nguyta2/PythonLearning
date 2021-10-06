import re
import sys
from collections import defaultdict

input = '''
2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>
'''

lines = []

regex = re.compile(r'<([a-z]+)(\s[^>]*)?>')
input = input.strip()
input = input.splitlines()

for line in input:
    lines.append(line)

tag_attributes = defaultdict(list)

for i in range(1, len(lines)):
    for groups in regex.findall(lines[i]):
        tag, attr = groups
        tag_attributes[tag].extend(re.findall(r'(\w+)=[\'\"]', attr))

for tag, attr in sorted(tag_attributes.items()):
    print(':'.join([tag, ','.join(sorted(set(attr)))]))
