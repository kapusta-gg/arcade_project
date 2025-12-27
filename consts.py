import json


def get_settings(key: str):
    with open("settings.json", "r") as f:
        data = json.load(f)["settings"]
    return data[key]


with open("settings.json", "r") as f:
    data = json.load(f)["settings"]
    window_size = data["window_sizes"]
    volume = data["volume"]

PIXELS_BOARD = 10
X, Y = 0, 1
WINDOWS_OPTIONS = ["1280x1024", "1920x1080", "2000x1080"]
