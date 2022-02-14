import os
from os import linesep as rn

template = open("template.md", "r").read()

categories = list(filter(lambda f: os.path.isdir(f) and not f.startswith('.') and os.listdir(f), os.listdir(os.getcwd())))
files = [list(map(lambda x: category + '/' + x, os.listdir(category))) for category in categories]

def filename_to_title(str: str):
  return ' '.join(map(lambda x: x.capitalize(), str.split('/')[-1].split('.')[0].split('-')))

def category_to_entry(category: str):
  return f"* [{category.capitalize()}](#{category})"

def file_to_entry(file: str):
  return f'- [{filename_to_title(file)}]({file})'

with open("README.md", "w") as readme:
  readme.write(template
    .replace("%%%CATEGORIES%%%", "\r\n".join(map(category_to_entry, categories)))
    .replace('%%%TIL_LISTS%%%', "\r\n\r\n".join(
      [f'''\
### {category.capitalize()}

{rn.join(map(file_to_entry, files))}''' for (category, files) in zip(categories, files)])))