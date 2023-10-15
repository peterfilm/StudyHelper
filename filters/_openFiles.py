import subprocess
from modules.api import conf

def open_in_kmplayer(file_path):
    try:
        # Loop through the list of file paths and open each photo in Photoshop
        command = [conf['KMPLAYER_PATH'], file_path]
        subprocess.Popen(command)

    except Exception as e:
        print(f"Error: {e}")