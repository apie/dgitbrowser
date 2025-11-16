#!/usr/bin/env python3
from flask import Flask, render_template

# Local
from dgitbrowser.browsers.repo import get_repo_file_listing
from dgitbrowser.git_commands.log import get_repo_log
from dgitbrowser.renderers.file import highlight_file_html

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template(
        "base.html",
        title="Home",
        content="""
        <p>The following repositories are available at this location:
            <ul>
                <li><a href='/repo/test'>test</a></li>
            </ul>
        </p>
        """,
    )


@app.route("/readme")
def readme():
    return render_template(
        "base.html", title="Readme", content=highlight_file_html("README.md")
    )


@app.route("/repo/<repo_name>")
def browse_repo(repo_name):
    return render_template(
        "repo.html",
        title=f"Browsing repo: {repo_name}",
        files=get_repo_file_listing(repo_name),
        commits=get_repo_log(repo_name),
        readme=highlight_file_html("README.md"),
    )
