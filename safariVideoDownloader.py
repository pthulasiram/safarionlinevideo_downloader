
from bs4 import BeautifulSoup
import requests
import shutil
import os
import subprocess
import json

with open('./config.json') as f:
    data = json.load(f)
url = data['url']
domain = data['domain']
output_folder = data['output_folder']
username = data['username']
password = data['password']

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

lessons = soup.find_all('li', class_='toc-level-1')
print(len(lessons))

shutil.rmtree(output_folder, ignore_errors=True)
os.makedirs(output_folder)
module_name = 'Module 0'
for lesson in lessons:
    lesson_name = lesson.a.text
    if lesson_name.startswith('Module') and not 'Summary' in lesson_name:
        module_name = lesson_name
        os.makedirs(output_folder + '/' + module_name)
        # print(module_name)
        for index, video in enumerate(lesson.ol.find_all('a')):
            video_name = str(index) + ' - ' + video.text
            video_url = video.get('href')
            video_out = output_folder + '/' + module_name + '/' + video_name + '.mp4'
            #print('        ', domain + video_url)
            #print('        ', video_out)
            url_opath = "youtube-dl -f 133 -u {} -p {} --output '{}' -f worst {}".format(
                username, password, video_out, video_url)
            print(url_opath)
            #print("youtube-dl -u {} -p {} --output '{}' {}".format(username, password, video_out, video_url))
            subprocess.run(url_opath, shell=True, check=True)
    else:
        os.makedirs(output_folder + '/' + module_name + '/' + lesson_name)
        # print('   ', lesson_name)
        for index, video in enumerate(lesson.ol.find_all('a')):
            video_name = str(index) + ' - ' + video.text
            video_url = video.get('href')
            video_out = output_folder + '/' + module_name + \
                '/' + lesson_name + '/' + video_name + '.mp4'
            # print('        ', domain + video_url)
            # print('        ', video_out)
            url_opath = "youtube-dl -u {} -p {} --output '{}' -f worst {}".format(
                username, password, video_out, video_url)
            print(url_opath)
            #print("youtube-dl -u {} -p {} --output '{}' {}".format(username, password, video_out, video_url))
            subprocess.run(url_opath, shell=True, check=True)
