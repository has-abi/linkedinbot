from flask import Blueprint, jsonify, request
from ..services.scraper_service import scrap_linkedin_profile

scraper_route = Blueprint('scraper_route', __name__, url_prefix="/api/scraper")


@scraper_route.route("/ping", methods=["GET"])
def ping():
    """Ping the scraper

    Returns:
        Response: An object indicating the success of the ping
    """
    return jsonify({
        "statue":"success",
        "message":"pong!"
    })

@scraper_route.route("/", methods=["POST"])
def scrap_profile():
    profile_username = request.form["username"]
    return  scrap_linkedin_profile(profile_username)
