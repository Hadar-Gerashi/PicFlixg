from flask import Flask
from config import Config
from routes.auth_routes import auth_bp
from routes.video_routes import video_bp
from routes.user_routes import user_bp

app = Flask(__name__, static_folder='static', template_folder="template")
app.config.from_object(Config)

app.register_blueprint(auth_bp)
app.register_blueprint(video_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(port=Config.PORT)
