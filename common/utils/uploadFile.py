#!/usr/bin/env python
# coding=utf-8

from poster3.streaminghttp import register_openers
from requests_toolbelt import MultipartEncoder
from common.utils.gettoken import tokenUtil
import requests
import json


class UploadFileUtil(object):

    # fileName 文件名称
    # uploadType 上传文件类型：image、file、voice
    # fileType Content-Type参数：根据文件格式填写对应类型，例如：语音填video/mpeg4

    # 上传文件
    def uploadFile(self, fileName, uploadType, fileType=None):

        # 请求URL
        token = tokenUtil.getToken()
        url = 'http://eim.mygzb.com:9090/fs/upload?accessToken=' + token + '&type=' + uploadType

        # 打开二进制文件
        register_openers()
        upload_file_path = "/Users/app/Documents/autoTest/GZBAPP/source/" + fileName
        filebuff = open(upload_file_path, "rb")

        # 数据流
        m = MultipartEncoder(
            fields={'data': (fileName, filebuff, fileType)}
        )

        # 发送post请求
        response = requests.post(url, data=m, headers={'Content-Type': m.content_type, 'Content-Length': '3166027'})
        print(response.text)
        # 判断file_id是否获取成功
        if response.status_code == 200:
            result = json.loads(response.text)
            fileid = result.get("id")
            print("上传文件成功，fileid=" + fileid)
        else:
            print(response.status_code)
            print(response.reason)
            print(response.headers)

        return fileid


uploadFileUtil = UploadFileUtil()
