import os
import telebot


def get_scripts() -> dict:
    scripts = dict()
    scripts["python"] = [i for i in os.listdir("./Scripts/") if i.endswith(".py")]
    scripts["shell"] = [i for i in os.listdir("./Scripts/") if i.endswith(".sh")]

    return scripts



if __name__ == "__main__":
    pass
