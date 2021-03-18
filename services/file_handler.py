import shutil
import ntpath
import os
from datetime import datetime


def move_file(path_from, path_to):
    final_file_name = "%s-%s%s"
    try:
        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y-%H-%M-%S")
        os.makedirs(path_to, exist_ok=True)

        file_base_name = ntpath.basename(path_from)
        file_name, file_extension = os.path.splitext(file_base_name)
        final_path = os.path.join(path_to, final_file_name % (file_name, date_time, file_extension))
        shutil.move(path_from, final_path)

        print("File move successfully from %s to %s" % (path_from, path_to))
    except Exception as e:
        print("Filed to move file from %s to %s" % (path_from, path_to))
        # TODO: SEND EMAIL FAILED TO MOVE FILE
