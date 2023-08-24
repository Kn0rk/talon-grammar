import os
import re
import tempfile
from talon import Context, Module, actions, ui
mod = Module()
ctx = Context()
@mod.action_class
class Actions:
    def hoverkeyboard_exec():
        """Runs hoverkeyboard command"""
        folder=tempfile.gettempdir()
        # check if folder exists
        if not os.path.exists(folder+"/hoverkeyboard"):
            print("hoverkeyboard folder not found")
            return
        for file in os.listdir(folder+"/hoverkeyboard"):
            with open(folder+"/hoverkeyboard/"+file, "r") as f:
                contents = f.read()
            
            print("Running hoverkeyboard command: "+   contents)
            pattern = r"(actions\.)([a-zA-Z0-9_]+)\((.*)\)"
            match = re.search(pattern, contents)
            if match:
                obj=match.group(1)
                func=match.group(2)
                args=match.group(3)
                #remove quotes
                args=args.replace('"','')
                args=args.replace("'",'')
                actions.sleep("51ms")
                getattr(actions, func)(args)
            else:
                print("hoverkeyboard command not found")
                
            # contents = contents.replace("actions.","")
            # getattr(actions, c)("31ms")
            # actions.sleep("31ms")
            # eval(contents)
            os.remove(folder+"/hoverkeyboard/"+file)