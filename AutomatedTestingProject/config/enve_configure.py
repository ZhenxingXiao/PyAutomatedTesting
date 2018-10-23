# coding=utf-8

import os
import zipfile
from project import base_project_path

req_path = "requirements.txt"
# ChromeDriver淘宝下载镜像链接
chrome_driver_link = "http://npm.taobao.org/mirrors/chromedriver/2.43/chromedriver_win32.zip"
firefox_driver_link = "http://npm.taobao.org/mirrors/geckodriver/v0.23.0/geckodriver-v0.23.0-win64.zip"


def download_and_unzip_drivers(driver_link):
    right_index = driver_link.rfind('/')
    zip_file_name = driver_link[right_index+1:len(driver_link)]
    import requests as req
    response = req.get(driver_link)
    with open(base_project_path + r"assets/driver_files/"+zip_file_name, "wb") as driver_file:
        driver_file.write(response.content)
    print(zip_file_name + " has been downloaded")
    zip_file = zipfile.ZipFile(base_project_path + r"assets/driver_files/"+zip_file_name, "r")
    for file in zip_file.namelist():
        zip_file.extract(file, base_project_path + r'assets/driver_files/')
    zip_file.close()
    print(zip_file_name + " has been extract into assets/driver_files/")


if __name__ == '__main__':
    # 自动安装环境依赖
    file_path = os.path.dirname(__file__)
    print(file_path)
    result_cmd = os.popen('pip install -r '+file_path+'/'+req_path)
    result_str = result_cmd.read()
    print(result_str)
    # 自动获取Chrome Driver文件
    if not os.path.exists(base_project_path + r'assets/driver_files'):
        os.mkdir(base_project_path + r'assets/driver_files')
    try:
        download_and_unzip_drivers(chrome_driver_link)
        download_and_unzip_drivers(firefox_driver_link)
    except Exception as error:
        print(error)
        print("error with getting driver files")
