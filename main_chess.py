import os
import sys
from app_files.controller_chess import Controller


main_dir = os.path.dirname(__file__)
files_dir = os.path.join(main_dir, 'app_files')
sys.path.append(files_dir)


controller_ch = Controller()

if __name__ == "__main__":
    controller_ch.menu()
