# Secure File Storage System

## Overview

This project is a secure file storage system designed to encrypt files before uploading them to the cloud, ensuring data confidentiality and security. It also includes user authentication and access control mechanisms to restrict access to authorized users only.

## Project Demonstrations

- **File Encryption and Upload:** Files are encrypted using AES encryption before being uploaded to an AWS S3 bucket. This ensures that even if the files are accessed by unauthorized users, the contents remain secure.
- **User Authentication:** Implemented using JWT (JSON Web Token), ensuring that only authenticated users can access the file upload and download functionalities.
- **File Listing and Download:** Users can view a list of their uploaded files and download them in either encrypted or decrypted form.
- **Local Development Setup:** Uses LocalStack to simulate AWS S3 services locally, allowing for efficient development and testing without needing an actual AWS account.
- **Demonstration of Token Usage:** The `index.html` file in the project showcases the generated JWT token, demonstrating how it is used for secure operations.

## Technologies Used

- **Backend:** Python, Flask
- **Cloud Storage:** AWS S3 (simulated locally using LocalStack for development and testing)
- **Encryption:** AES (Advanced Encryption Standard)
- **Authentication:** JWT (JSON Web Token)
- **Frontend:** HTML, JavaScript

## Features

1. **File Encryption and Upload:**
   - Files are encrypted using AES encryption before being uploaded to the cloud.
   - The encrypted files are stored in an AWS S3 bucket (simulated locally using LocalStack).

2. **User Authentication and Access Control:**
   - Users authenticate via JWT tokens. These tokens are required for accessing the file upload and download endpoints.
   - Tokens include an expiration time to enhance security.

3. **File Listing and Download:**
   - Users can list all their uploaded files.
   - Users can download files in their encrypted form or download them decrypted.

4. **Local Development Setup:**
   - LocalStack is used to simulate AWS S3 services for local development and testing.
   - Docker is used to run LocalStack, providing a consistent development environment.

## Workflow

1. **User Authentication:**
   - Users generate a JWT token by accessing the `/generate_token` endpoint. This token is required for subsequent operations.

2. **File Upload:**
   - The frontend (`index.html`) allows users to upload files. Files are encrypted using AES before being sent to the backend.
   - The encrypted files are then uploaded to the simulated AWS S3 bucket using the provided JWT token for authentication.

3. **File Listing:**
   - Users can list all their uploaded files by accessing the `/list_files` endpoint.

4. **File Download:**
   - Users can download files in their encrypted form or request the server to decrypt and return the decrypted file. This is handled by the `/download/<filename>` and `/download_decrypted/<filename>` endpoints respectively.

## Demonstration Using `index.html`

- The `index.html` file includes a button to generate a JWT token, which is then displayed on the page.
- Users can upload files using this token, and the files are encrypted before upload.
- The page also lists all uploaded files and provides options to download them in encrypted or decrypted form.

## How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/secure-file-storage-system.git
   cd secure-file-storage-system
Set up the virtual environment and install dependencies:

python3 -m venv venv
source venv/bin/activate
	pip install -r requirements.txt

Run LocalStack using Docker:

	docker run -d -p 4566:4566 -p 4571:4571 localstack/localstack

Start the Flask application:


	python3 run.py


Open index.html in your web browser:
	Navigate to http://127.0.0.1:5000 to interact with the application.

Conclusion:
This project demonstrates a secure mechanism for storing files in the cloud with encryption and access control. The index.html file provides a practical demonstration of how JWT tokens are generated and used to secure file uploads and downloads.
