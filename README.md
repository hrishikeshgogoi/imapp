Objective: To build a cloud based image management application using AWS and python

Methodology:(mac)
	I began by launching an EC2 instance and downloaded the pem file named “hrishi.pem” with public IP: “13.60.56.206”. Then I created a bucket named "hrishib1--use1-az4--x-s3" with region code "use1-az4". I went to my terminal and connected to the EC2 instance using the following commands:
chmod 400 ~/Downloads/hrishi.pem
ssh -i ~/Downloads/hrishi.pem ec2-user@13.60.56.206
	After successfully connecting to the server and installing the necessary dependencies I created a directory “comm” using mkdir comm and navigated to it using cd comm. Then I created a python file named test01.py using the command “touch test1.py”. I also created another directory with “mkdir templates” to store the html files. I created 2 HTML files using “touch templates/uploadpage.html” and “touch templates/images.html” for the upload page for the images and the other for listing respectively.
  I used “nano test1.py” to edit the python file. Then I used “nano templates/uploadpage.html” to edit the HTML file. Again, I used “nano templates/images.html” to edit the 2nd HTML file. After making these changes I used “python3 test1.py” to start the server getting the following output:
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:8080
* Running on http://172.31.39.171:8080

	WIP

In the python file named test01.py First I imported Flask for building the web application, I import boto3 for interacting with the S3 services and os for handling file paths. NoCredentialsError for cases where AWS credentials are missing
I set a secret key to enable session management.I initialised s3 client: with s3 bucket and region. I implemented the home function to render the home page. The upload_image function handles the image upload logic when a user submits a file. The list_images function lists all the images currently stored in the S3 bucket. And the last snippet starts the flask development server and makes it accessible on all network interfaces on port 8080.
The body of the uploadpage.html conatins the logic for the 1st page where images can be uploaded. It includes a file input, a submit button, and displays any flashed messages (like success or error notifications) after the file is processed.
The body of the images.html file conatins the logic for displaying the list of images. The user can click on the "Upload more images" link to return to the upload page and upload additional images. Also images is a placeholder representing a list of image filenames stored in the S3 bucket.**
