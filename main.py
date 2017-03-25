# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
from index import Index
from re_money import ReMoney

from flask import Flask, render_template, request

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='&&',
        block_end_string='&&',
        variable_start_string='&',
        variable_end_string='&',
        comment_start_string='&#',
        comment_end_string='#&',
    ))

app = CustomFlask(__name__)


urls = (
    '/' , 'Index',
    '/wx', 'Handle',
    '/test', 'ReMoney',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
