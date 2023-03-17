import requests  
import json 
import os  
from urllib.request import urlopen 
import glob 
import re 
import base64

# Get the desired output filename from the user
name = input('enter final file name: ')

# Define headers to be sent with the HTTP request
headers = {
    'authority': 'api.mubi.com',
    'accept': '*/*',
    'accept-language': 'en',
    'authorization': 'Bearer ADDHERE', # add the authorization token here
    'client': 'web',
    'client-accept-audio-codecs': 'aac',
    'client-accept-video-codecs': 'h265,vp9,h264',
    'client-country': 'US',
    'dnt': '1',
    'origin': 'https://mubi.com',
    'referer': 'https://mubi.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

# Make a GET request to the specified URL with the given headers, and load the response JSON into a dictionary
response = requests.get('https://api.mubi.com/v3/films/ADDHERE/viewing/secure_url', headers=headers) # mubi movie ID goes here
mubi = json.loads(response.text)

# Extract the video title and secure URL from the response
title = mubi['mux']['video_title']
mubi = mubi['url']

# Retrieve the encryption key from the secure URL using a regular expression
kid = requests.get(mubi)
result = re.search(r'cenc:default_KID="(\w{8}-(?:\w{4}-){3}\w{12})">', str(kid.text))

# Define a function for generating the PSSH box, which contains information about the encryption key
def get_pssh(keyId):
    array_of_bytes = bytearray(b'\x00\x00\x002pssh\x00\x00\x00\x00')
    array_of_bytes.extend(bytes.fromhex("edef8ba979d64acea3c827dcd51d21ed"))
    array_of_bytes.extend(b'\x00\x00\x00\x12\x12\x10')
    array_of_bytes.extend(bytes.fromhex(keyId.replace("-", "")))
    return base64.b64encode(bytes.fromhex(array_of_bytes.hex()))

# Extract the encryption key ID from the regular expression match and generate the PSSH box
kid = result.group(1).replace('-', '')
assert len(kid) == 32 and not isinstance(kid, bytes), "wrong KID length"
pssh = format(get_pssh(kid).decode('utf-8'))
# Set the headers for the request
headers = {
    'Accept': 'application/json, text/plain, */*',                 
    'Accept-Language': 'en-US,en;q=0.9',                             
    'Connection': 'keep-alive',                               
    'Content-Type': 'application/json',                             
    'Origin': 'https://cdrm-project.com',                              
    'Referer': 'https://cdrm-project.com/',                            
    'Sec-Fetch-Dest': 'empty',                                        
    'Sec-Fetch-Mode': 'cors',                                         
    'Sec-Fetch-Site': 'same-origin',                                   
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', # Set the user agent for the request
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"', 
    'sec-ch-ua-mobile': '?0',                                          
    'sec-ch-ua-platform': '"Windows"',                                 
}

# Set the JSON data for the request
json_data = {
    'license': 'https://lic.drmtoday.com/license-proxy-widevine/cenc/?specConform=true',
    'headers': 'dt-custom-data: ADDHERE', # add your encoded headers, starts with "ey"
    'pssh': f'{pssh}',                                                
    'buildInfo': '',                                                 
    'proxy': '',                                                      
    'cache': False,                                                    
}

# Send a POST request with the headers and JSON data to the specified URL
response = requests.post('https://cdrm-project.com/wv', headers=headers, json=json_data)

# Search for a decryption key pattern in the response text
result = re.search(r"[a-z0-9]{16,}:[a-z0-9]{16,}", str(response.text))

# Get the decryption key and format it properly
decryption_key = result.group()
print(decryption_key)
decryption_key = f'key_id={decryption_key}'
decryption_key = decryption_key.replace(":",":key=")
# Download the video using N_m3u8DL-RE
folder_path = f"E:/uncomplete"
os.system(fr'N_m3u8DL-RE "{mubi}" --auto-select --save-name "{name}" --auto-select --save-dir {folder_path} --tmp-dir {folder_path}/temp')
# Run shaka-packager to decrypt the video file
dest_dir = f"{folder_path}/{name}"
os.system(fr'shaka-packager in="{folder_path}/{name}.mp4",stream=video,output="{dest_dir}/decrypted-video.mp4" --enable_raw_key_decryption --keys {decryption_key}')  # The decrypted video file will be saved in E:\uncomplete\{name}\decrypted-video.mp4

# Define a regex pattern to match the audio file names
regex_pattern = re.escape(name) + r"\.[a-z]{2}\.m4a"
# Loop through all files in the folder_path directory
for filename in os.listdir(folder_path):
    if filename.endswith(".srt") and name in filename:
        source_path = os.path.join(folder_path, filename)
        dest_path = os.path.join(dest_dir, filename)
        shutil.move(source_path, dest_path)
    # If the file name matches the regex pattern
    if re.match(regex_pattern, filename):
        # Extract the language code from the file name
        letters = re.search(re.escape(name) + r"\.([a-zA-Z]{2})\.m4a", filename).group(1)
        # Run shaka-packager to decrypt the audio file
        os.system(fr'shaka-packager in="{folder_path}/{name}.{letters}.m4a",stream=audio,output="{dest_dir}/decrypted-audio.{letters}.m4a" --enable_raw_key_decryption --keys {decryption_key}')
        os.remove(f"{folder_path}/{name}.{letters}.m4a")
        os.remove(f"{folder_path}/{name}.mp4")
