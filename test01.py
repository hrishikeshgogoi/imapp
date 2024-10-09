from flask import Flask, render_template, request, redirect, url_for, flash
import boto3
from botocore.exceptions import NoCredentialsError
import os

app = Flask(__name__)
app.secret_key = 'commvault_test0001' 

S3_BUCKET =
S3_REGION = 'use1-az4'
s3 = boto3.client('s3', region_name=S3_REGION)

@app.route('/')
def home():
    return render_template('uploadpage.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('home'))
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('home'))
    try:
        s3.upload_fileobj(
            file,
            S3_BUCKET,
            file.filename,
            ExtraArgs={"ACL": "public-read", "ContentType": file.content_type}
        )
        flash('File successfully uploaded')
        return redirect(url_for('list_images'))
    except NoCredentialsError:
        flash('Credentials not available')
        return redirect(url_for('home'))

@app.route('/images')
def list_images():
    try:
        objects = s3.list_objects_v2(Bucket=S3_BUCKET)
        if 'Contents' in objects:
            images = [obj['Key'] for obj in objects['Contents']]
        else:
            images = []
        return render_template('images.html', images=images)
    except NoCredentialsError:
        flash('Credentials not available')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
