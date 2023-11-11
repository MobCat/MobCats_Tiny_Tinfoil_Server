#!/env/Python 3.8.10
#!MobCat-2021
# THIS IS NOT HOW YOU MAKE A JSON FILE! I KNOW.
# But I don't know how to do proper json things with python and I don't think tinfoil even uses standed json formatting in the first place.
# If it bugs you that much, then you fix it. Otherwise "it just works."

import os # Import lib for file handleing. In our case reading and wrighting files.
import socket # Import web sockets lib for getting the system IP.
from datetime import datetime

# Variables for getting and setting local IP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
urlHead  = 'http://' + local_ip + '/' 

# Filter for only switch file extensions
ext = (".nsp", ".nsz", ".xci", ".xcz")

# Dumb fun, variables for how many files we have on the server counter
fileCount = 0
sizeCount = 0

# Splash screen / headder logo.
print("""
            +:            :+           
          +****:        :****+         
        +********:    :********+       
        *********:    :*********       
    :#+   *****:  :**:  :*****   +#:   
  :#####+   *:  :******:  :*   +#####: 
:#########+   :**********:   +#########
 *#######=-     +******+     -=#######*
   *###=- -=##*   +**+   *##=- -=###*  
     +- -=######*      *######=- -+    
       +##########-  -##########+      
         *######:  **  :######*        
           *##:  *####*  :##*          
               *########*              
               +########+              
                 +####+                
                   ++                  
      Tinfoil local server updater
""")

print("\nUpdating index.html for server...")
txt = open("index.htm", "w", encoding='utf-8') # wright a hole new file, overwrite anything that exists.

# Dumb json things / hacks.
txt.write('{\n')
txt.write('    "files": [\n')

# List all files in the files folder
# Filter them for switch files
# Make the directory listing HTML friendly TODO: Add more filtering or import a HTML encoding library
# Saves our URL directory list and how big the file is in our index.htm file
for root, dirs, files in os.walk("files"):
    for file in files:
        if file.endswith(ext):
             fileDir = os.path.join(root, file)
             fileSizeBytes = os.stat(fileDir).st_size
             filter1 = fileDir.replace(" ", "%20") # Making the directory string we gathered HTML friendly
             filter2 = filter1.replace("\\", "/")
             txt.write('        {\n')
             txt.write(f'            "url": "{urlHead}{filter2}",\n')
             txt.write(f'            "size": {fileSizeBytes}\n')
             txt.write('        },\n')
             fileCount += 1
             sizeCount += fileSizeBytes

sizeCountGB = sizeCount / 1073741824
sizeCountGB = round(sizeCountGB,2) # Otherwise it shows the value to the 9th decimal place and that's too much precision for this dumpster fire
txt.write('    ],\n')
# This is the pop up message of the day you get when you first open tinfoil and when you open the server in the file browser
# It can be edited to anything you want, but that's up to you
txt.write(f'    "success": "Welcome to MobCat\'s mini private tinfoil server.\\nThis is Still a WiP and only ment for LAN use.\\n\\nThis server has {fileCount} files totaling {sizeCountGB} GB\\n')
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
txt.write(f'Last Updated: {timestamp}"\n')
txt.write('}\n')
txt.close()

print("Finalizeing file...")
# this is even more dumb but idk how to json
txt = open("index.htm", "r", encoding='utf-8') # read the file we just made to get line count.
lastEdit = txt.readlines()
lastEdit[-4] = '        }\n' # Correct our last }, to a }
txt = open("index.htm", "w", encoding='utf-8') # Now we know where we want to edit, overwright the hole line.
txt.writelines(lastEdit)
txt.close()

# This dumpster fire of a script is compleat, tell the user about the files that where added and what there server IP is.
print(f"Done!\n{fileCount} files totaling {sizeCountGB} GB where updated or added\n")
print(f"Server IP was set to: {local_ip}\n")
# TODO: Maybe ad an OS pause here instead of using the bat file for pause for people who are not using the bat file but we'll see.
