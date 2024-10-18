import os
from google.cloud import storage

# put your key in the same folder, rename "your_key.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'your_key.json'

storage_client = storage.Client()

# create bucket, only need to create once (line 10-12 can be ignore after creation)
#bucket_name = 'ck-data-bucket'
#bucket = storage_client.bucket(bucket_name)
#bucket = storage_client.create_bucket(bucket, location="US")

# upload file from your computer
def upload_file(file_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(file_name)
        blob.upload_from_filename(file_path)
        print(f"File uploaded to {file_name} in bucket {bucket_name}.")
        return True
    
    except Exception as e:
        print(e)
        return

# upload some text directly
def upload_text(text, file_name, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(file_name)
        blob.upload_from_string(text)
        print(f"Text uploaded to {file_name} in bucket {bucket_name}.")
        return True

    except Exception as e:
        print(e)
        return

# download a file from your bucket
def download(file_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(file_name)
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob, f)
        print(f"File downloaded to {file_path}.")
        return True
    except Exception as e:
        print(e)
        return

# run the following lines (55, 57, 59) one by one to test upload/download, change the parameters before run

#upload_file('notepad01.txt', r'C:\Users\user\Desktop\notepad01.txt', 'ck-data-bucket')

#upload_text('1234567890', 'upload_text02.txt', 'ck-data-bucket')

#download('notepad01.txt', r'C:\Users\user\Desktop\download2.txt', 'ck-data-bucket')