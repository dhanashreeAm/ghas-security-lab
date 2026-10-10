command = "grep -R " + query + " ."
subprocess.run(command, shell=True, check=False)
