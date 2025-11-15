# DGitbrowser
A simple web UI to browse git repositories.

Run web UI using `uv`:

    uv run flask --app dgitbrowser/app run

Run scripts:

    uv run -m dgitbrowser.scripts.print_file <path>
    uv run -m dgitbrowser.scripts.print_git_log <path>
    uv run -m dgitbrowser.scripts.print_readme <path>
