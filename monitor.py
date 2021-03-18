import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from services.validator import Validator
from services.parser import Parser
from data.database import DataBase
from config import ARQUIVE_FILED_FILES, ARQUIVE_FILES
from services.file_handler import move_file


class Watcher:
    DIRECTORY_TO_WATCH = "files"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()
    

class Handler(FileSystemEventHandler):
    @staticmethod
    def process_new_file(event):
        print("Initiating processing of file " + event.src_path)
        try:
            validator = Validator(event.src_path)
            if validator.is_valid():
                parser = Parser(event.src_path)
                data = parser.parse()
            else:
                move_file(event.src_path, ARQUIVE_FILED_FILES)
                print("File %s is not valid" % event.src_path)
                return

            database = DataBase()
            database.store_product(data)

            # post to presta
            # delete file
            # log
            # fail manda email
            print("Received created event - %s." % event.src_path)
            move_file(event.src_path, ARQUIVE_FILES)
        except Exception as e:
            print("Failed to process file - %s." % event.src_path)
            print(str(e))
            move_file(event.src_path, ARQUIVE_FILED_FILES)
            # TODO: SEND MAIL EXCEPTION HAPPENED

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            Handler.process_new_file(event)

        elif event.event_type == 'modified':
            print("Received modified event - %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()
