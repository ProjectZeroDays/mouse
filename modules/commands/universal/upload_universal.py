import modules.helper as h
import re, os

class command:
    def __init__(self):
        self.name = "upload"
        self.description = "Upload local file."
        self.usage = "Usage: upload <filename> <path>"
    
    def run(self,session,cmd_data):
        w = os.environ['OLDPWD']
        os.chdir(w)
        if not cmd_data['args']:
            print self.usage
            w = os.environ['OLDPWD']
            os.chdir(w)
            return
        else:
            paths = re.split(r'(?<!\\) ', cmd_data['args'].rstrip())
            if len(paths) > 2:
                print "Usage: upload <filename> <path>"
                return
            
            local_dir = os.path.split(paths[0])[0]
            local_file = os.path.split(paths[0])[1]
            
            if len(paths) == 1:
                remote_dir = "."
                remote_file = local_file
            else:
                remote_dir = os.path.split(paths[1])[0]
                if not remote_dir:
                    remote_dir = "."
                remote_file = os.path.split(paths[1])[1]
                if not remote_file:
                    remote_file = local_file

            session.upload_file(paths[0],remote_dir,remote_file)
            h.info_general("File successfully uploaded!")
            w = os.environ['OLDPWD']
            os.chdir(w)
