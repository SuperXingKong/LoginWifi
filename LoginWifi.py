import json
import requests
import socket
import re
import os

IP = socket.gethostbyname(socket.gethostname())


def is_set_account():
    if os.path.exists("account.json"):
        return True
    else:
        return False


def set_account():

    service = input("请输入运营商(校园网输入1，中国移动输入2): ")
    username = input("请输入学号: ")
    pwd = input("请输入密码: ")
    account = {"service": service, "username": username, "password": pwd}
    account_file = open("account.json", "w")
    account_file.write(json.dumps(account))
    account_file.close()
    print("设置成功！\n账号:{:}\n密码:{:}".format(
        username, pwd))


def read_account():
    account_file = open("account.json", "r")
    account_data = json.load(account_file)
    account_file.close()
    return account_data


if not is_set_account():
    set_account()

config = read_account()

msg_dict = {
    "aW51c2UsIGxvZ2luIGFnYWlu": "多端登录",
    "NTEy": "AC认证失败",
    "dXNlcmlkIGVycm9yMQ==": "账户不存在",
    "QXV0aGVudGljYXRpb24gRmFpbCBFcnJDb2RlPTE2": "非正常时段",
    "\\u8ba4\\u8bc1\\u6210\\u529f": "认证成功",
    "bGRhcCBhdXRoIGVycm9y": "账号或密码错误",
    "\\u5bc6\\u7801\\u4e0d\\u80fd\\u4e3a\\u7a7a": "密码不能为空"
}


def sendLoginPacket():
    print("#开始登录")
    if config["service"] == "2":
        url = "http://10.9.1.3:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1"\
            "&user_account=%2Cb%2C"+str(config["username"])+"%40zgyd"\
            "&user_password="+str(config["password"]) +\
            "&wlan_user_ip="+str(IP) +\
            "&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.3&v=8593"
    elif config["service"] == "1":
        url = "http://10.9.1.3:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1"\
            "&user_account=%2C0%2C"+str(config["username"]) +\
            "&user_password="+str(config["password"]) +\
            "&wlan_user_ip="+str(IP) +\
            "&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.3&v=4479"
    else:
        print("请选择运营商为校园网或中国移动")
        return False
    session = requests.Session()
    response = session.get(url)
    text = response.text
    result = re.compile("\"result\":\"(\w)\"")
    result = result.search(text).group(1)
    msg = re.compile("\"msg\":\"([^\"]*)\"")
    msg = msg.search(text).group(1)
    if result == "1" and msg_dict[msg] == "认证成功":
        print("认证成功")
        return True
    elif result == "0":
        if msg:
            print(msg_dict[msg])
            return False
        else:
            ret_code = re.compile("\"ret_code\":(\w)")
            ret_code = ret_code.search(text).group(1)
            if ret_code == "2":
                print("已登录")
                return True
            elif ret_code == "1":
                print("您的账号余额不足，请充值后使用(有可能是中国移动用户选择了运营商为校园网的原因)")
                return False


text = sendLoginPacket()

input("按回车键退出程序")
