import os
import re
import json

# =========================================================
# STORAGE FOLDERS
# =========================================================

ROADMAP_FOLDER = "storage/roadmaps"

CHAPTER_FOLDER = "storage/chapters"

# =========================================================
# CREATE STORAGE FOLDERS
# =========================================================

os.makedirs(
    ROADMAP_FOLDER,
    exist_ok=True
)

os.makedirs(
    CHAPTER_FOLDER,
    exist_ok=True
)

# =========================================================
# SAFE FILE NAME
# =========================================================

def clean_name(name):

    name = name.strip().lower()

    name = name.replace(" ", "_")

    name = re.sub(
        r'[^a-zA-Z0-9_]',
        '',
        name
    )

    return name

# =========================================================
# SAVE ROADMAP JSON
# =========================================================

def save_roadmap(
    topic,
    roadmap_content
):

    safe_topic = clean_name(topic)

    filename = f"{safe_topic}.json"

    file_path = os.path.join(
        ROADMAP_FOLDER,
        filename
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            roadmap_content,
            file,
            indent=4,
            ensure_ascii=False
        )

    return file_path

# =========================================================
# LOAD ROADMAP JSON
# =========================================================

def load_roadmap(topic):

    safe_topic = clean_name(topic)

    filename = f"{safe_topic}.json"

    file_path = os.path.join(
        ROADMAP_FOLDER,
        filename
    )

    if not os.path.exists(file_path):

        return None

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        roadmap = json.load(file)

    return roadmap

# =========================================================
# GET ALL SAVED ROADMAPS
# =========================================================

def get_saved_roadmaps():

    roadmap_files = []

    for file in os.listdir(ROADMAP_FOLDER):

        if file.endswith(".json"):

            roadmap_files.append(file)

    return roadmap_files

# =========================================================
# SAVE CHAPTER CONTENT
# =========================================================

def save_chapter_content(
    topic,
    chapter_name,
    content
):

    safe_topic = clean_name(topic)

    safe_chapter = clean_name(chapter_name)

    topic_folder = os.path.join(
        CHAPTER_FOLDER,
        safe_topic
    )

    os.makedirs(
        topic_folder,
        exist_ok=True
    )

    filename = f"{safe_chapter}.txt"

    file_path = os.path.join(
        topic_folder,
        filename
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)

    return file_path

# =========================================================
# LOAD CHAPTER CONTENT
# =========================================================

def load_chapter_content(
    topic,
    chapter_name
):

    safe_topic = clean_name(topic)

    safe_chapter = clean_name(chapter_name)

    filename = f"{safe_chapter}.txt"

    file_path = os.path.join(
        CHAPTER_FOLDER,
        safe_topic,
        filename
    )

    if not os.path.exists(file_path):

        return ""

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

    return content

# =========================================================
# GET SAVED CHAPTERS
# =========================================================

def get_saved_chapters(topic):

    safe_topic = clean_name(topic)

    topic_folder = os.path.join(
        CHAPTER_FOLDER,
        safe_topic
    )

    if not os.path.exists(topic_folder):

        return []

    chapter_files = []

    for file in os.listdir(topic_folder):

        if file.endswith(".txt"):

            chapter_files.append(file)

    return chapter_files

# =========================================================
# DELETE CHAPTER
# =========================================================

def delete_chapter(
    topic,
    chapter_name
):

    safe_topic = clean_name(topic)

    safe_chapter = clean_name(chapter_name)

    filename = f"{safe_chapter}.txt"

    file_path = os.path.join(
        CHAPTER_FOLDER,
        safe_topic,
        filename
    )

    if os.path.exists(file_path):

        os.remove(file_path)

        return True

    return False

# =========================================================
# DELETE ROADMAP
# =========================================================

def delete_roadmap(topic):

    safe_topic = clean_name(topic)

    filename = f"{safe_topic}.json"

    file_path = os.path.join(
        ROADMAP_FOLDER,
        filename
    )

    if os.path.exists(file_path):

        os.remove(file_path)

        return True

    return False
