import configparser
import os
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


class AliYunSms:
    def __init__(self,phone,params):
        self.phone = phone
        self.params = params
        self.sms_param = parser_config('AliYun')
        self.SignName = self.sms_param['SignName']
        self.TemplateCode = self.sms_param['TemplateCode']
        self.client = AcsClient(self.sms_param['ACCESS_KEY_ID'], self.sms_param['ACCESS_KEY_SECRET'], 'cn-hangzhou')


    def send(self):
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https')  # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')

        request.add_query_param('RegionId', "cn-hangzhou")
        request.add_query_param('PhoneNumbers', self.phone)
        request.add_query_param('SignName', self.SignName)
        request.add_query_param('TemplateCode', self.TemplateCode)
        request.add_query_param('TemplateParam', self.params)

        response = self.client.do_action_with_exception(request)

        return response



def parser_config(sign):
    project_dir = os.path.dirname(os.path.abspath('conf'))  # 获取当前文件的目录
    config_path = os.path.join(project_dir, "conf", "config.ini")
    cf = configparser.ConfigParser()
    cf.read(config_path)

    # secs = cf.sections()   # 获取ini文件中的所有section，并以列表形式返回
    # mysql_options = cf.options("MySQL") #获取某个section名所对应的键
    # mysql_items = cf.items("MySQL")  # 获取section对应的全部键值对
    if sign == 'AliYun':
        ACCESS_KEY_ID = cf.get("AliYun", "KEY_ID")
        ACCESS_KEY_SECRET = cf.get("AliYun", "KEY_SECRET")
        SignName = cf.get("AliYun", "NAME")
        TemplateCode = cf.get("AliYun", "CODE")
        result = {
            'ACCESS_KEY_ID':ACCESS_KEY_ID,
            'ACCESS_KEY_SECRET':ACCESS_KEY_SECRET,
            'SignName':SignName,
            'TemplateCode':TemplateCode
        }
        return result
    elif sign == 'MySQL':
        host = cf.get("MySQL", "host")
        user = cf.get("MySQL", "user")
        password = cf.get("MySQL", "password")
        db = cf.get("MySQL", "db")
        charset = cf.get("MySQL", "charset")
        port = cf.get("MySQL", "port")
        result = {
            'host':host,
            'user':user,
            'password':password,
            'db':db,
            'charset':charset,
            'port':port
        }
        return result
    elif sign == 'Redis':
        location = cf.get("Redis", "LOCATION")
        result = {
            'LOCATION':location
        }
        return result
    else:
        print('不存在该配置内容！')
