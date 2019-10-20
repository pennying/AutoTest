import requests
import json
from common.utils.gettoken import tokenUtil
from common.utils.uploadFile import uploadFileUtil


class SendMsgByHttpUtil(object):

    # from_user 发送者
    # to_user 接收者
    # content 发送的消息文本

    # 发送文本
    def sendMsg(self, from_user, to_users, content):

        # 获取token
        token = tokenUtil.getToken()
        # 请求url
        url = 'http://eim.mygzb.com:9090/eim/api/message/send?access_token=' + token
        # data
        data = {
            "from_type": "user",
            "from": from_user,
            "to_users": [to_users],
            "msg_type": "text",
            "text": {
                "content": content
            }
        }

        response = requests.post(url, data=json.dumps(data))

        # 验证返回值
        if response.status_code == 200:
            print(response.status_code)
            print('发送消息成功')
        else:
            print(response.reason)
            print(response.headers)
        return response

    # 发送大表情
    def sendEmoji(self, from_user, to_users, content):

        # 获取token
        token = tokenUtil.getToken()
        # 请求url
        url = 'http://eim.mygzb.com:9090/eim/api/message/send?access_token=' + token
        # data
        data = {
            "from_type": "user",
            "from": from_user,
            "to_users": [to_users],
            "msg_type": "emoticon",
            "emoticon": {
                "id": '5_1',
                "pId": '5',
                "content": content
            }
        }

        response = requests.post(url, data=json.dumps(data))

        # 验证返回值
        if response.status_code == 200:
            print(response.status_code)
            print('发送消息成功')
        else:
            print(response.reason)
            print(response.headers)
        return response

    # 发送图片
    def sendPic(self, from_user, to_users):

        # 获取token
        token = tokenUtil.getToken()
        # 获取文件ID
        file_id = uploadFileUtil.uploadFile('aaaa.jpg', 'image')
        # 请求url
        url = 'http://eim.mygzb.com:9090/eim/api/message/send?access_token=' + token
        # data
        data = {
            "from": from_user,
            "to_all": "false",
            "to_users": [to_users],
            "msg_type": "image",
            "image": {
                "file_id": file_id
            }
        }

        response = requests.post(url, data=json.dumps(data))

        # 验证返回值
        if response.status_code == 200:
            print(response.status_code)
            print('发送图片成功')
        else:
            print(response.reason)
            print(response.headers)
        return response

    # 发送文件
    def sendFile(self, from_user, to_users):

        # 获取token
        token = tokenUtil.getToken()
        # 获取文件ID
        file_id = uploadFileUtil.uploadFile('file.txt', 'file')
        # 请求url
        url = 'http://eim.mygzb.com:9090/eim/api/message/send?access_token=' + token
        # data
        data = {
            "from": from_user,
            "to_all": "false",
            "to_users": [to_users],
            "msg_type": "file",
            "file": {
                "file_id": file_id
            }
        }

        response = requests.post(url, data=json.dumps(data))

        # 验证返回值
        if response.status_code == 200:
            print(response.status_code)
            print('发送文件成功')
        else:
            print(response.reason)
            print(response.headers)
        return response

    # 发送语音
    def sendVoice(self, from_user, to_users):

        # 获取token
        token = tokenUtil.getToken()
        # 获取文件ID
        file_id = uploadFileUtil.uploadFile('get.dms', 'voice', 'video/mpeg4')
        # 请求url
        url = 'http://eim.mygzb.com:9090/eim/api/message/send?access_token=' + token
        # data
        data = {
            "from": from_user,
            "to_all": "false",
            "to_users": [to_users],
            "msg_type": "voice",
            "voice": {
                "file_id": file_id,
                "length": '2',
                "size": '4776'
            }
        }

        response = requests.post(url, data=json.dumps(data))

        # 验证返回值
        if response.status_code == 200:
            print(response.status_code)
            print('发送语音成功')
        else:
            print(response.reason)
            print(response.headers)
        return response

    # 发送小视频
    def sendshortvideo(self, from_user, to_users):

        # 获取token
        token = tokenUtil.getToken()
        # 获取文件ID
        file_id = uploadFileUtil.uploadFile('video.mp4', 'file')
        # 获取文件ID
        img_file_id = uploadFileUtil.uploadFile('aaaa.jpg', 'image')
        # 请求url
        url = 'http://eim.mygzb.com:9090/eim/api/message/send?access_token=' + token
        # data
        data = {
            "from": from_user,
            "to_all": "false",
            "to_users": [to_users],
            "msg_type": "shortvideo",
            "shortvideo": {
                "file_id": file_id,
                "thumbnail_id": img_file_id
            }
        }

        response = requests.post(url, data=json.dumps(data))
        print(response.text)
        # 验证返回值
        if response.status_code == 200:
            print(response.status_code)
            print('发送语音成功')
        else:
            print(response.reason)
            print(response.headers)
        return response


sendMsgByHttpUtil = SendMsgByHttpUtil()
