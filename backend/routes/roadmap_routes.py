from flask import Blueprint
from flask import request
from flask import jsonify

from services.roadmap_service import generate_roadmap
from utils.file_utils import save_roadmap

roadmap_bp = Blueprint("roadmap_bp", __name__)

@roadmap_bp.route("/generate-roadmap", methods=["POST"])
def create_roadmap():
    try:

        data = request.json

        topic = data.get("topic")
        model_name = data.get("model")

        roadmap = generate_roadmap(
            topic,
            model_name
        )

        return jsonify({
            "success": True,
            "roadmap": roadmap
        })
    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })


@roadmap_bp.route("/save-roadmap", methods=["POST"])
def save_created_roadmap():
    try:
        data = request.json

        topic = data.get("topic")
        roadmap = data.get("roadmap")

        path = save_roadmap(topic, roadmap)

        return jsonify({
            "success": True,
            "path": path
        })
    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })  
