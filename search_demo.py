import subprocess


def search_files(user_query):
    # Intentionally vulnerable: do not use in production.
    command = "grep -R " + user_query + " ."
    subprocess.run(command, shell=True, check=False)
