import subprocess

def execution(command):
    output = subprocess.run(command, shell=True, capture_output=True, text=True)
    return output.stdout
