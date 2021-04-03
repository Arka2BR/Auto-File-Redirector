#***********************************************************************************************************************
#***********************************************************************************************************************

# Automatic File Re-director
# Original Creator : Arkaprabho Adhikary
# Original Creation Date: 03/04/2021
# Made while studying at NIT Goa

#***********************************************************************************************************************
#***********************************************************************************************************************

import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import shutil


class FileRedirector(FileSystemEventHandler):
    def on_modified(self, event):  # Very handy little pre defined method.

        for filename in os.listdir(trackingFolder):
            sourcepath = trackingFolder + "/" + filename
            destpath = destinationFolder + "/"
            if filename not in os.listdir(destpath):
                 shutil.move(sourcepath, destpath) #This is where the file movement takes place
            else:
                os.unlink(destpath + filename)
                shutil.move(sourcepath, destpath)




trackingFolder = "D:/Python Projects/Automatic File Redirection/Source"
destinationFolder = "D:/Python Projects/Automatic File Redirection/Target"

# For an event where file is in source it will be redirected to target
fileRedirector = FileRedirector()
# But events need to be observed
observer = Observer()
observer.schedule(fileRedirector, trackingFolder, recursive= True) # Schedule observation in tracking folder
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()