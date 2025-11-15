# Gitbrowser
A simple web UI to browse git repositories.

Run web UI using `uv`:

  uv run flask --app gitbrowser/app run

Run scripts:

  uv run -m gitbrowser.scripts.print_file <path>
  uv run -m gitbrowser.scripts.print_git_log <path>
  uv run -m gitbrowser.scripts.print_readme <path>
