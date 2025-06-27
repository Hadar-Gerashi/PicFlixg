# routes/user_routes.py
import os
from flask import Blueprint, request, session, redirect, url_for, render_template, flash, jsonify
from werkzeug.utils import secure_filename
from models.user import read_user_by_id, update_text, update_user_profile_image, read_users_by_name
from models.videos import read_user_videos
from models.categories import read_categories, read_user_categories, update_categories_user

import cloudinary
import cloudinary.uploader
import cloudinary.api

user_bp = Blueprint('user_bp', __name__)


@user_bp.route("/profile/<int:user_id>", methods=["GET", "POST"])
def profile(user_id):
    logged_user_id = session.get("user_id")
    user = read_user_by_id(user_id)

    if request.method == 'POST' and logged_user_id == user_id:
        action = request.form.get('action')

        if action == "update":
            file = request.files.get('profile_image')
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)

                if user.profile_image:
                    try:
                        old_public_id = f"profile_{logged_user_id}"
                        cloudinary.uploader.destroy(old_public_id, resource_type="image")
                        print(f"✅ Old profile image deleted from Cloudinary")
                    except Exception as e:
                        print(f"❌ Error deleting old profile image: {str(e)}")

                try:
                    upload_result = cloudinary.uploader.upload(
                        file.stream,
                        resource_type="image",
                        public_id=f"profile_{logged_user_id}",
                        transformation=[
                            {'width': 300, 'height': 300, 'crop': 'fill', 'gravity': 'face'},
                            {'quality': 'auto', 'fetch_format': 'auto'}
                        ]
                    )

                    image_url = upload_result.get("secure_url")
                    new_filename = f"profile_{logged_user_id}{ext}"

                    update_user_profile_image(user_id, new_filename)

                    print(f"✅ Profile image uploaded successfully: {image_url}")

                except Exception as e:
                    print(f"❌ Failed to upload profile image to Cloudinary: {str(e)}")
                    return f"❌ Failed to upload image: {str(e)}", 500

        elif action == "remove":

            if user.profile_image:
                try:
                    public_id = f"profile_{logged_user_id}"
                    result = cloudinary.uploader.destroy(public_id, resource_type="image")
                    print(f"✅ Profile image deleted from Cloudinary: {result}")
                except Exception as e:
                    print(f"❌ Error deleting profile image from Cloudinary: {str(e)}")

            update_user_profile_image(user_id, None)

        return redirect(url_for('user_bp.profile', user_id=user_id))

    videos = read_user_videos(user_id)
    categories = read_categories()
    categories_user = read_user_categories(user_id)

    return render_template("profile.html", videos=videos, categories=categories,
                           profile_user_id=user_id, logged_user_id=logged_user_id, user=user,
                           categories_user=categories_user)


@user_bp.route('/profile/<int:user_id>/update_text', methods=['POST'])
def update_profile_text(user_id):
    data = request.get_json()
    new_text = data.get('profile_text', '').strip()

    success = update_text(user_id, new_text)
    if not success:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'success': True}), 200


@user_bp.route('/search_users')
def search_users():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"users": []})

    return read_users_by_name(query)


@user_bp.route('/update_categories', methods=['POST'])
def update_user_categories():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    user_id = session['user_id']
    data = request.get_json()
    selected_categories = data.get('categories', [])

    try:
        selected_categories = list(map(int, selected_categories))
        update_categories_user(user_id, selected_categories)
        return jsonify({'success': True}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Update failed'}), 500
