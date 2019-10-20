# -*- coding: utf-8 -*-
import sys;
#sys.path.append('')

import xmpp2

# 注意帐号信息，必须加@域名格式
from_user = 'u110064@vm1'
password = '123456'

# 可以添加多个接收人
to_user = ['chenjiangpeng@xtpt.e-u.cn']
msg = "您好！这是条测试信息！"


def to_msg():
    """
    基于xmpp协议的即时通讯消息发送，需求安装xmpp库
    使用openfire搭建的即时通讯都可以使用
    google talk也可以使用
    """
    clientexam = xmpp2.client('gzbeim.ejiahe.com')
    clientexam.connect(server=('gzbeim.ejiahe.com', 5222))
    clientexam.auth(from_user, password, 'botty')
    # for i in to_user:
    #     clientexam.sendInitPresence()
    #     message = xmpp2.Message(i, msg, typ = 'chat')
    #     clientexam.send(message)
    #     time.sleep(0.2)


if __name__ == '__main__':
    to_msg()
