import time 
from watchdog.observers import Observer
from watchdog.events import *


a = "/Applications/XAMPP/xamppfiles/htdocs/demo/uploadfile"
 
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("文件被修改了 %s"%event.src_path)
 
    def on_created(self, event):
        #exec(open("yolov5/detect.py").read())
        print("文件被创建了 %s" % event.src_path)
 
 
if __name__ == "__main__":
    path = a
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
 
    try:
        while True:
            time.sleep(1)
 
    except KeyboardInterrupt:
        observer.stop()
