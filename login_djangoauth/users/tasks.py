from celery import shared_task
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from conf.aliyun_api import parser_config


@shared_task
def send_sms(phone,code):
    sms_obj = AliYunSms(phone,code)
    print(sms_obj)
    sms_obj.send()




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
        print(response)
