from flask import Blueprint
from flask import request
from flask import jsonify

from services.content_service import (
    generate_chapter_content
)

from utils.file_utils import (
    save_chapter_content,
    load_chapter_content,
    get_saved_chapters
)

content_bp = Blueprint(
    "content_bp",
    __name__
)

# =========================================================
# GENERATE SINGLE CHAPTER CONTENT
# =========================================================

@content_bp.route(
    "/generate-chapter",
    methods=["POST"]
)
def generate_single_chapter():

    try:

        data = request.json

        topic = data.get("topic")
        chapter_name = data.get("chapter")
        subtopics = data.get("subtopics")
        model_name = data.get("model")

        # ---------------------------------------------
        # VALIDATION
        # ---------------------------------------------

        if not topic:

            return jsonify({
                "success": False,
                "message": "Topic Is Required"
            })

        if not chapter_name:

            return jsonify({
                "success": False,
                "message": "Chapter Name Is Required"
            })

        if not model_name:

            return jsonify({
                "success": False,
                "message": "Model Name Is Required"
            })

        # ---------------------------------------------
        # GENERATE CONTENT
        # ---------------------------------------------

        content = generate_chapter_content(
            topic=topic,
            chapter_name=chapter_name,
            subtopics=subtopics,
            model_name=model_name
        )

        return jsonify({
            "success": True,
            "chapter": chapter_name,
            "content": content
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })


# =========================================================
# SAVE CHAPTER CONTENT
# =========================================================

@content_bp.route(
    "/save-chapter",
    methods=["POST"]
)
def save_chapter():

    try:

        data = request.json

        topic = data.get("topic")
        chapter_name = data.get("chapter")
        content = data.get("content")

        # ---------------------------------------------
        # VALIDATION
        # ---------------------------------------------

        if not topic:

            return jsonify({
                "success": False,
                "message": "Topic Is Required"
            })

        if not chapter_name:

            return jsonify({
                "success": False,
                "message": "Chapter Name Is Required"
            })

        if not content:

            return jsonify({
                "success": False,
                "message": "Content Is Required"
            })

        # ---------------------------------------------
        # SAVE CONTENT
        # ---------------------------------------------

        file_path = save_chapter_content(
            topic=topic,
            chapter_name=chapter_name,
            content=content
        )

        return jsonify({
            "success": True,
            "message": "Chapter Saved Successfully",
            "path": file_path
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })


# =========================================================
# LOAD SAVED CHAPTER CONTENT
# =========================================================

@content_bp.route(
    "/load-chapter",
    methods=["POST"]
)
def load_chapter():

    try:

        data = request.json

        topic = data.get("topic")
        chapter_name = data.get("chapter")

        # ---------------------------------------------
        # VALIDATION
        # ---------------------------------------------

        if not topic:

            return jsonify({
                "success": False,
                "message": "Topic Is Required"
            })

        if not chapter_name:

            return jsonify({
                "success": False,
                "message": "Chapter Name Is Required"
            })

        # ---------------------------------------------
        # LOAD CONTENT
        # ---------------------------------------------

        content = load_chapter_content(
            topic=topic,
            chapter_name=chapter_name
        )

        if content == "":
            return jsonify({
                "success": False,
                "message": "Chapter Content Not Found"
            })

        return jsonify({
            "success": True,
            "chapter": chapter_name,
            "content": content
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })


# =========================================================
# GET SAVED CHAPTER LIST
# =========================================================

@content_bp.route(
    "/saved-chapters",
    methods=["POST"]
)
def saved_chapters():

    try:

        data = request.json

        topic = data.get("topic")

        # ---------------------------------------------
        # VALIDATION
        # ---------------------------------------------

        if not topic:

            return jsonify({
                "success": False,
                "message": "Topic Is Required"
            })

        # ---------------------------------------------
        # GET CHAPTER FILES
        # ---------------------------------------------

        chapters = get_saved_chapters(
            topic=topic
        )

        return jsonify({
            "success": True,
            "chapters": chapters
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })
    
    