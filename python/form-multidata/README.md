#Multipart form example
This code shows up a nice way to send a multipart/form to FastApi direct via html.
The multipart is merging a file upload and simple body params (str, int, dict...) post.
It's possible to change is behavior by removing or adding arguments to 'receive_data()'.


To run:
python run.py