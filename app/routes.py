from flask import Blueprint, request, render_template, jsonify, current_app
from .auth import token_required
from .s3 import upload_file_to_s3
from .encryption import encrypt_file
import jwt
import datetime

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
@token_required
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    encrypted_file = encrypt_file(file.read())
    s3_key = upload_file_to_s3(encrypted_file, file.filename)
    
    return jsonify({"message": "File uploaded successfully", "s3_key": s3_key})

@bp.route('/generate_token', methods=['GET'])
def generate_token():
    token = jwt.encode({
        'user': 'test_user',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, current_app.config['SECRET_KEY'], algorithm="HS256")
    return jsonify({'token': token})
