import re
from jinja2 import Template


def get_page(f_out, f_template, f_parts):
    open(f_out, 'w').write(Template(open(f_template).read()).render(load_part(f_parts)))

def load_part(f_parts):
    data = re.split('\n+', open(f_parts).read())
