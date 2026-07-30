import json
import os


def load_json(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def load_all_sources(folder_path):

    articles = []

    for file in os.listdir(folder_path):

        if file.endswith(".json"):

            path = os.path.join(folder_path, file)

            data = load_json(path)

            if isinstance(data, list):
                articles.extend(data)

            elif isinstance(data, dict):
                articles.append(data)

    return articles