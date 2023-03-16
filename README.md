# Mubi Downloader

This is a Python script that allows users to download movies from the Mubi streaming service. It uses the Mubi API to extract the video URL and encryption key, and then uses Widevine DRM to download and decrypt the video.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Legal Notice](#legal-notice)

## Installation
1. Clone the repository or download the zip file.
2. Install the required libraries using pip. Run the following command in your terminal:
pip install requests
3. Install Widevine DRM. Follow the instructions on the [Widevine website](https://www.widevine.com/).

## Usage
1. Open the `mubi_downloader.py` file in a text editor.
2. Fill in your Mubi account information in the `headers` dictionary.
3. Open your terminal and navigate to the directory containing the `mubi_downloader.py` file.
4. Run the following command in your terminal:
python mubi_downloader.py

5. Enter the desired filename for your downloaded movie when prompted.

## Legal Notice
This script is intended for personal use only. The Mubi terms of service explicitly prohibit the downloading and/or redistribution of their content. Please respect the intellectual property rights of the creators and owners of the content.

This script is provided "as is" without warranty of any kind. The developers of this script do not accept any responsibility or liability for the use of this script, including but not limited to any damages or losses arising from its use. By using this script, you agree to assume all risks associated with its use.

This script may use third-party libraries and APIs, which are subject to their own licenses and terms of use. Please review the licenses and terms of use of any third-party libraries and APIs used by this script before using this script.
