from llm import llm
from extract import extract
from execution import execution
import os
import platform
import files
import sys

operating_system = platform.system()
version = platform.version()

current_path = os.getcwd()
files = files.files()

systemprompt =  f""" you are an ai thet creates Bash commands. Just prind the command you been asked for. No explentions needed
                    Explain the command only if you asked for it.
                    Operating System: 
                    Current directory: {os}
                    version: {version}
 



                """
text = ' '.join(sys.argv[1:])
if len(text) == 0:
    sys.stderr.write("Missing argument by executing. You have to provide the prompt.\n")
    sys.exit()


answer = llm(systemprompt, text)
command = extract(answer)
if command:
    execution(command)
else:
    print(answer)


