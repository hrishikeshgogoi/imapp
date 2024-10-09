Objective: To build a cloud based image management application using AWS and python

Methodology:(mac)
	I began by launching an EC2 instance and downloaded the pem file named “hrishi.pem” with public IP: “13.60.56.206”. Then I created a bucket named hrishib1--use1-az4--x-s3 with region code use1-az4. I went to my terminal and connected to the EC2 instance using the following commands:
chmod 400 ~/Downloads/hrishi.pem
ssh -i ~/Downloads/hrishi.pem ec2-user@13.60.56.206
	After successfully connecting to the server and installing the necessary dependencies I created a directory “comm” using mkdir comm and navigated to it using cd comm. Then I created a python file named test01.py using the command “touch test1.py”. I also created another directory with “mkdir templates” to store the html files. I created 2 HTML files using “touch templates/uploadpage.html” and “touch templates/images.html” for the upload page for the images and the other for listing respectively.
  I used “nano test1.py” to edit the python file. Then I used “nano templates/uploadpage.html” to edit the HTML file. Again, I used “nano templates/images.html” to edit the 2nd HTML file. After making these changes I used “python3 test1.py” to start the server getting the following output:
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:8080
* Running on http://172.31.39.171:8080
Unfortunately when trying to access the site “http://172.31.39.171:8080” the page does not load and I was unable to fix the issue during the allotted time so I was unable to move further with encryption and decryption stages
