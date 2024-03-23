import re

def extract(text):
    pattern = r"```(bash)?\n([\s\S]*?)\n```"
    matches = re.findall(pattern, text)

    if matches:
        command = matches[0][1].strip()
        return command
    else:
        return None