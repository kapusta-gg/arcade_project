import json

with open("settings.json", "r") as f:
    data = json.load(f)["settings"]
    window_size = data["window_sizes"]
    volume = data["volume"]
WINDOW_SIZES = window_size
SOUND_VOLUME = volume
X, Y = 0, 1
WINDOWS_OPTIONS = ["1280x1024", "1920x1080", "2000x1080"]
