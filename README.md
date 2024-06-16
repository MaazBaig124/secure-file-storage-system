# Secure File Storage System

A secure file storage system that encrypts files before uploading them to the cloud. Implementing user authentication and access control mechanisms.

## Technologies

- Python
- Flask
- AWS S3
- AES Encryption
- JWT

## Concepts

- Encryption/Decryption
- Authentication
- Access Control
- Secure File Transfer
- Cloud Storage

## Setup

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Set environment variables: `SECRET_KEY`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_S3_BUCKET`
5. Run the application: `python run.py`

## Usage

1. Go to `http://127.0.0.1:5000/`
2. Upload a file to be encrypted and stored in AWS S3

## License

MIT
