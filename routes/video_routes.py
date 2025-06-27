# routes/video_routes.py
import os
import random

import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import Blueprint, request, redirect, url_for
from werkzeug.utils import secure_filename
from models.user import read_user_by_id
from models.videos import create_video, delete_video_by_id, read_video_id, read_videos, \
    read_videos_guest
from models.categories import create_category_video, read_categories
from models.likes import update_like, read_liked_video_ids_by_user
from flask import render_template, session, send_from_directory, jsonify
from config import Config

video_bp = Blueprint('video_bp', __name__)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in {"mp4", "avi", "mov", "mkv"}


@video_bp.route("/")
def root():
    return redirect('/home')


@video_bp.route("/home")
def home():
    username = session.get('username', 'Guest')
    user_id = session.get("user_id")

    user = read_user_by_id(user_id) if user_id else None

    if user_id:
        videos = read_videos(user_id)
    else:
        videos = read_videos_guest()
        random.shuffle(videos)

    if videos is None:
        videos = []

    categories = read_categories()

    liked_videos = set()
    if user_id:
        liked_videos = read_liked_video_ids_by_user(user_id)

    return render_template(
        "index.html",
        categories=categories,
        videos=videos,
        username=username,
        user_id=user_id,
        liked_videos=liked_videos
        , user=user
    )


@video_bp.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(Config.UPLOAD_FOLDER, filename)


@video_bp.route("/upload_video", methods=["GET", "POST"])
def upload_video():
    if request.method == "POST":
        file = request.files["file"]
        user_id = session.get("user_id")
        selected_categories = request.form.getlist('category_id[]')

        if not user_id:
            return "❌ Error: User not logged in", 401
        if not selected_categories:
            return "❌ Please select a category"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)

            if not filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
                filename += '.mp4'

            try:
                upload_result = cloudinary.uploader.upload(
                    file.stream,
                    resource_type="video",
                    public_id=f"{name}_{user_id}"
                )

            except Exception as e:
                return f"❌ Failed to upload to Cloudinary: {str(e)}", 500

            video_url = upload_result.get("secure_url")
            new_filename = f"{name}_{user_id}{ext}"

            create_video(user_id, new_filename)
            video_id = read_video_id(user_id, new_filename)

            for i in selected_categories:
                create_category_video(video_id, i)

            return redirect(url_for("user_bp.profile", user_id=user_id))

        return "❌ Unsupported format!"

    return '''
           <form method="post" enctype="multipart/form-data">
               קטגוריה: <input type="text" name="category_id" required><br>
               <input type="file" name="file" accept="video/*" required><br>
               <button type="submit">העלה</button>
           </form>
       '''


@video_bp.route("/delete_video", methods=["POST"])
def delete_video():
    video_url = request.form["video_url"]
    video_id = request.form["video_id"]
    print(f"🔍 Deleting video: {video_url}")

    delete_video_by_id(video_id, "category_video")
    delete_video_by_id(video_id, "videos")

    try:

        public_id = os.path.splitext(video_url)[0]
        print(f"📡 Deleting from Cloudinary: {public_id}")

        result = cloudinary.uploader.destroy(public_id, resource_type="video")
        print(f"✅ Cloudinary deleted: {result}")
    except Exception as e:
        print(f"❌ Error deleting from Cloudinary: {str(e)}")

    return redirect(url_for("user_bp.profile", user_id=session.get("user_id")))


@video_bp.route("/toggle_like", methods=["POST"])
def toggle_like():
    user_id = session.get("user_id")
    video_id = request.form["video_id"]

    if not user_id:
        return jsonify({"status": "error", "message": "You must be logged in to like"}), 401

    result = update_like(user_id, video_id)
    return jsonify(result)
