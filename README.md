<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Kanopy_logo.png/800px-Kanopy_logo.png?" alt="Kanopy Logo" width="200"/>

## Kanopy Downloader

"Kanopy downloader" allows you to download videos from Kanopy, a streaming platform for movies, documentaries, and more. Also decrypts and both video and audio files, and downloads the subtitles for the movie.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Legal Notice](#legal-notice)

## Installation
1. Clone the repository or download the zip file.
2. Install the required libraries using one of the following methods:
    * Run the 'install_requirements.bat'
    * Manually install each library specified in 'requirements.txt'.
    * Run 'pip install -r requirements.txt'
3. Install [shaka-packager](https://github.com/shaka-project/shaka-packager/releases/tag/v2.6.1) and [N_m3u8DL-RE](https://github.com/nilaoda/N_m3u8DL-RE/releases)
4. Once installed, add the folders where the tools are installed to your system's `PATH` environment variable. 

   - On Windows:

     1. Open the Start menu and search for "Environment Variables".
     2. Click "Edit the system environment variables".
     3. Click the "Environment Variables" button.
     4. Under "System variables", scroll down and find "Path", then click "Edit".
     5. Click "New" and enter the path to the folder where each tool is installed.
     6. Click "OK" to close all the windows.

## Usage

1. Open 'headers.py` file in a text editor.
2. Play the movie on Kanopy which you want to download, search for "plays" in your network traffic, copy that url as CURL (bash), paste into curlconverter.com, copy both the headers and json_data, and paste into the python file.
3. Edit the folder path, and thats it.
4. Open your terminal and navigate to the directory containing the `kanopy_downloader.py` file. (or add it to PATH)
5. Run the following command in your terminal:

    ```
    python kanopy_downloader.py
    ```

6. If you entered all the details correctly, your movie will start downloading.

## Legal Notice
- This program is intended solely for educational and informational purposes. The authors and contributors of this program do not condone or encourage any illegal or unethical activities. Any misuse of this program for unlawful or unethical purposes is strictly prohibited.
- Users must agree to use this program only for lawful purposes and in compliance with all applicable laws and regulations. The authors and contributors of this program will not be held responsible for any misuse or illegal activity undertaken by users.
- The use of this program is at the sole discretion of the user. The authors and contributors of this program are not responsible for any damages, direct or indirect, that may occur from using this program. Users agree to indemnify and hold harmless the authors and contributors of this program from any and all claims, damages, and expenses, including attorney's fees, arising from the use of this program.
- This program is provided "as is" without warranty of any kind, either express or implied, including but not limited to the implied warranties of merchantability, fitness for a particular purpose, or non-infringement. The authors and contributors of this program shall not be liable for any damages, including but not limited to direct, indirect, incidental, consequential, or punitive damages arising from the use of this program or any information contained therein.
