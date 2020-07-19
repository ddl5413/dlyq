import requests

host = '221.180.173.13:93'
ctx = 'dlyq'

login_data = {'phoneNumber': 'bToRkEcoRPb6TLzsNF3RA5cBkOfUHJ7QDa12xzASHR79TtavTrougeLVhOnorAciZqpAB/c9AW6qVf7uhFlKkMYHrCxCOmBXvCNsgScsGFYnGTSdag9Q4XXGb6qisxCchlTrXdmGX07JuOgvDcn7kO2OfW+TLf5cA4BU5adpgag=',
        'last4CardId': 'JCmslX2JMhAF89Pp4aQ7ulDKEV1qQSaQuDXgYqF0RJWJzxvIY7buUk7NiHF2xP10utY8VxJ4Y6lQLQS7JJu8/zrmgLF1liQbX3ULrKWJTA+8AVGO2Fua2leTf2f3Gf5+MRns0K7+8OJhrm98cjTQPMoU4MGnQPmeK+ieTMNLgRY=',
        'loginPassWord': 'HTDMFyKQQFMmI6YyqFmrxd8Akl52bKzrgqZQdz/9wcubVmUjHsTmY8D/lGcrecG52mLgjsVwUWBwuPayAehKqH+W7Z5Maqrc3gA7UPWrfovAtk7Jf7fNuuNSrN9QZ36gr64zK+aqfICYnuJg25Hvu1uDUKO9JkNiV+DrejUo+tA='}
login_url = 'mobile/activity/activityAction/dl_login.action'
submit_url = 'mobile/activity/activityAction/dl_submitHealthCondition.action'
print('开始请求合教育')
r = requests.post(f'http://{host}/{ctx}/{login_url}', login_data)
cookies = requests.utils.dict_from_cookiejar(r.cookies)
print('服务器返回cookies:')
print(cookies)

submit_data = {'pid': 'a5a25bc6d93098a7f218c7499d5d8f41',
                'idcard': '8219',
                'birthday': '2012-12',
                'nowAddress': '悦丽海湾',
                'permanentAddress': '悦丽海湾',
                'studentPhone': '',
                'patriarchPhone': '15940900137',
                'goSchoolTransport': '步行',
                'medicalHistory': '无',
                'temperature': '36.5',
                'isHealth': '是',
                'symptom': '',
                'healthQrCodeUrl': '',
                'healthQrCodeColor': '绿色',
                'isInDalian': '是',
                'isGoOut': '否',
                'a_outPlace': '',
                'a_domesticPlace': '',
                'a_domesticPlaceRemark': '',
                'a_externalPlace': '',
                'a_backTime': '',
                'a_transport': '',
                'a_trainFrequency': '',
                'isolate': '未进行过隔离',
                'isolatePattern': '',
                'isolateStartTime': '',
                'isolateEndTime': '',
                'isHCheck': '未检测',
                'isXCheck': '未检测',
                'closeContactsMatters': '无特殊情况',
                'spareField2': '',
                'spareField3': '无接触',
                'b_outPlace': '',
                'b_domesticPlace': '',
                'b_domesticPlaceRemark': '',
                'b_externalPlace': '',
                'b_backTime': '',
                'b_transport': '',
                'b_trainFrequency': '',
                'maskQuantity': '20以上',
                'isOwnWrite': '是',
                'informantName': '',
                'informantIdNumber': '',
                'relation': ''}

r = requests.post(f'http://{host}/{ctx}/{submit_url}', cookies=cookies, data=submit_data)
print('提交结果:' + str(r.status_code))



