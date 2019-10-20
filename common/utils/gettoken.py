import requests
import json


class TokenUtil(object):

    # 获取token
    def getToken(self):

        # 请求URL
        agent_id = '301189'
        agent_secret = 'kDDfHj1CP7WfLOgv1cJoFD1lkifEJVn1'
        url = 'http://eim.mygzb.com:9090/eim/api/get_token?agent_id=' + agent_id + '&agent_secret=' + agent_secret

        # 发送post请求
        response = requests.post(url)

        # 判断token是否获取成功
        if response.status_code == 200:
            result = json.loads(response.text)
            access_token = result.get("access_token")
            print('获取token成功，token='+access_token)
        else:
            print(response.status_code)
            print(response.reason)
            print(response.headers)

        return access_token


tokenUtil = TokenUtil()
