# coding=utf-8

import os
import zipfile
from project import base_project_path

req_path = "requirements.txt"
# ChromeDriver淘宝下载镜像链接
chrome_driver_link = "http://npm.taobao.org/mirrors/chromedriver/2.43/chromedriver_win32.zip"

if __name__ == '__main__':
    # 自动安装环境依赖
    file_path = os.path.dirname(__file__)
    print(file_path)
    result_cmd = os.popen('pip install -r '+file_path+'/'+req_path)
    result_str = result_cmd.read()
    print(result_str)
    # 自动获取Chrome Driver文件
    if not os.path.exists(base_project_path + r'assets/drivers'):
        os.mkdir(base_project_path + r'assets/drivers')
    try:
        import requests as req
        response = req.get(chrome_driver_link)
        with open(base_project_path + r"assets/drivers/chromedriver_win32.zip", "wb") as driver_file:
            driver_file.write(response.content)
        print("chromedriver_win32.zip has been downloaded")
        zip_file = zipfile.ZipFile(base_project_path + r"assets/drivers/chromedriver_win32.zip", "r")
        for file in zip_file.namelist():
            zip_file.extract(file, base_project_path + r'assets/drivers/')
        zip_file.close()
        print("chromedriver_win32.zip has been extract into assets/drivers/")
    except Exception as error:
        print(error)
        print("error with getting chromedriver_win32.zip")
