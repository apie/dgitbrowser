#!/usr/bin/env python3
from flask import Flask, render_template

# Local
from dgitbrowser.browsers.repo import get_repo_file_listing
from dgitbrowser.renderers.file import highlight_file_html

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template(
        "base.html",
        title="Home",
        content="""
        <p>Hello, World!</p>
        <a href='/readme'>Bekijk de readme</a><br>
        <a href='/repo/test'>Bekijk de repo /test/</a><br>
        """,
    )


@app.route("/readme")
def readme():
    return render_template(
        "base.html", title="View Readme", content=highlight_file_html("README.md")
    )


@app.route("/repo/<repo_name>")
def browse_repo(repo_name):
    # TODO
    return get_repo_file_listing(repo_name)
