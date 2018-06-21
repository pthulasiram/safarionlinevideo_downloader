# safarionlinevideo_downloader
Safari Video downloader is a python script to download entire course video's for offline watching.



Pre requisites:
 * Linux Machine
 * Install Python3
 * Install youtube_dl
 
 Usage:
   * open config.json file and update required details like username and password
     {
        "url": "https://www.safaribooksonline.com/library/view/ultimate-go-programming/9780134757476/",
        "domain": "https://www.safaribooksonline.com",
        "output_folder": "./output",
        "username": "username",
        "password": "password"
    }

   * run the following command in shell
     python3 safariVideoDownloader.py

 Note:
 * User required valid account on https://www.safaribooksonline.com/

 References:
 https://www.python.org/downloads/
 https://rg3.github.io/youtube-dl/
