import os
from os import linesep as rn

forced = { 'css': 'CSS' }

template = open("template.md", "r").read()

list_files = lambda category: [category + '/' + x for x in os.listdir(category) if x.split('.')[-1] == 'md']

def list_categories():
  to_ret = {}
  for category in [d for d in os.listdir() if os.path.isdir(d) and not d.startswith('.')]:
    files = list_files(category)
    if len(files) > 0: to_ret[category] = files
  return to_ret

dic = list_categories()

def category_name(category: str):
  return forced.get(category, category.title())

def category_to_entry(category: str):
  return f"* [{ category_name(category) }](#{category})"

def file_to_entry(file: str):
  with open(file, 'r') as f:
    return f'- [{f.readline()[2:-1]}]({file})'

with open("README.md", "w") as readme:
  readme.write(template
    .replace("%%%CATEGORIES%%%", "\r\n".join(map(category_to_entry, dic.keys())))
    .replace('%%%TIL_LISTS%%%', "\r\n\r\n".join([f'''\
### {category_name(category)}

{rn.join([file_to_entry(f) for f in files])}''' for (category, files) in dic.items()])))