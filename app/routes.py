from flask import Blueprint, request, render_template, jsonify, current_app, send_file
from .auth import token_required
from .s3 import upload_file_to_s3
from .encryption import encrypt_file, decrypt_file
import jwt
import datetime
from functools import wraps
from io import BytesIO
import boto3



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


@bp.route('/list_files', methods=['GET'])
@token_required
def list_files():
    s3 = boto3.client('s3', endpoint_url=current_app.config['AWS_S3_ENDPOINT_URL'])
    response = s3.list_objects_v2(Bucket=current_app.config['AWS_S3_BUCKET'])
    files = [obj['Key'] for obj in response.get('Contents', [])]
    return jsonify({'files': files})

@bp.route('/download/<filename>', methods=['GET'])
@token_required
def download_file(filename):
    s3 = boto3.client('s3', endpoint_url=current_app.config['AWS_S3_ENDPOINT_URL'])
    s3_response = s3.get_object(Bucket=current_app.config['AWS_S3_BUCKET'], Key=filename)
    return send_file(BytesIO(s3_response['Body'].read()), attachment_filename=filename, as_attachment=True)

@bp.route('/download_decrypted/<filename>', methods=['GET'])
@token_required
def download_decrypted_file(filename):
    s3 = boto3.client('s3', endpoint_url=current_app.config['AWS_S3_ENDPOINT_URL'])
    s3_response = s3.get_object(Bucket=current_app.config['AWS_S3_BUCKET'], Key=filename)
    decrypted_content = decrypt_file(s3_response['Body'].read())
    return send_file(BytesIO(decrypted_content), attachment_filename=filename, as_attachment=True)
