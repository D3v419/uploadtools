import requests

# Define the target URL and the file to be uploaded
target_url = 'http://example.com/upload'
file_path = 'path/to/your/file.txt'

# Open the file in binary mode
with open(file_path, 'rb') as file:
    files = {'file': file}

    # Send the POST request to upload the file
    response = requests.post(target_url, files=files)

    # Check the response
    if response.status_code == 200:
        print('File uploaded successfully!')
        print('Response:', response.text)
    else:
        print('Failed to upload file. Status code:', response.status_code)
        print('Response:', response.text)