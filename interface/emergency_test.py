# coding = utf-8
import unittest
import json
import requests
import urllib.parse
import time


class DemoApi(object):
    def __init__(self, base_url):
        self.base_url = base_url

    # 添加事件接口
    def addEmergency(self, basicId, citizenAddress, citizenName, citizenPhone, emergencyAddress, emergencyContent,
                     emergencyId,
                     emergencySource, emergencyTitle, orgId, emergencyTypeId, emergency_fileList, userId):
        url = urllib.parse.urljoin(self.base_url, 'emergency')
        headers = {
            # 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Content-Type': 'application/json'
        }
        data = {
            'basicId': basicId,
            'citizenAddress': citizenAddress,
            'citizenName': citizenName,
            'citizenPhone': citizenPhone,
            'emergencyAddress': emergencyAddress,
            'emergencyContent': emergencyContent,
            'emergencyId': emergencyId,
            'emergencySource': emergencySource,
            'emergencyTitle': emergencyTitle,
            'orgId': orgId,
            'emergencyTypeId': emergencyTypeId,
            'emergency_fileList': emergency_fileList,
            'userId': userId,
        }
        print(u'\n事件列表')
        print(u'\n请求url：\n%s' % url)
        print(u'\n参数：\n%s' % data)
        print(u'\n响应：')
        response = requests.post(url, headers=headers, data=json.dumps(data))
        # response = requests.post(url, headers=headers, data=data)
        print(response.text)
        return response

    # 查询事件列表
    def emergencyList(self, userAcceptance, userId, pageNum, count, startDate, endDate, emergencyStatus,
                      emergencyTypeOneId, emergencyTypeTwoId, orgId, orgSubsetCode, ifThisOrg):
        url = urllib.parse.urljoin(self.base_url, 'search/emergency/1/10')
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        }
        data = {
            'userAcceptance': userAcceptance,
            'userId': userId,
            'pageNum': pageNum,
            'count': count,
            'startDate': startDate,
            'endDate': endDate,
            'emergencyStatus': emergencyStatus,
            'emergencyTypeOneId': emergencyTypeOneId,
            'emergencyTypeTwoId': emergencyTypeTwoId,
            'orgId': orgId,
            'orgSubsetCode': orgSubsetCode,
            'ifThisOrg': ifThisOrg
        }
        print(u'\n事件列表')
        print(u'\n请求url：\n%s' % url)
        print(u'\n参数：\n%s' % data)
        print(u'\n响应：')
        # response = requests.post(url, headers=headers, data=json.dumps(data))
        response = requests.post(url, headers=headers, data=data)
        print(response.text)
        return response

    def deleteEmergency(self):
        time.sleep(200)
        url = urllib.parse.urljoin(self.base_url, 'emergency/7157340330418')
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            # 'Content-Type': 'application/json'
        }
        print(u'\n事件列表')
        print(u'\n请求url：\n%s' % url)
        print(u'\n响应：')
        # response = requests.post(url, headers=headers, data=json.dumps(data))
        # response = requests.post(url, headers=headers, data=data)
        response = requests.delete(url)
        print(response.text)
        return response


class TestEmergency(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.base_url = 'http://sqwy.wt.com:5130/smart_community_information_correct/'
        cls.base_url = 'http://sqwytst.wt.com:14352/smart_community_information/'
        cls.basicId = ''
        cls.citizenAddress = '山西省大同市云州区倍加造镇三零二线'
        cls.citizenName = '大同金融办'
        cls.citizenPhone = '18710001031'
        cls.emergencyAddress = '山西省大同市云州区倍加造镇三零二线'
        cls.emergencyContent = '1'
        cls.emergencyId = '7157340330418'
        cls.emergencySource = '3'
        cls.emergencyTitle = '1'
        cls.orgId = '100'
        cls.emergencyTypeId = '5'
        cls.userId = '201'
        cls.userAcceptance = '0'
        cls.pageNum = '1'
        cls.count = '10'
        cls.startDate = ''
        cls.endDate = ''
        cls.emergencyStatus = '0'
        cls.emergencyTypeOneId = ''
        cls.emergencyTypeTwoId = ''
        cls.orgSubsetCode = ''
        cls.ifThisOrg = ''
        # 之前这里加了双引号导致报错   "[]"
        cls.emergency_fileList = [{'emergencyId': '7157340330418', 'ext': "png", 'fileName': "房屋分布",
                                   'fileUrl': "group3/M00/00/34/wKgDFmDvlXaAOv3nAAfvdsxUnR4072.png",
                                   'id': '1626314103188', 'size': "520054",
                                   'url': "group3/M00/00/34/wKgDFmDvlXaAOv3nAAfvdsxUnR4072.png"}]
        cls.app = DemoApi(cls.base_url)

    # @unittest.skip("Don't run")
    def testAddEmergency(self):
        response = self.app.addEmergency(self.basicId, self.citizenAddress, self.citizenName, self.citizenPhone,
                                         self.emergencyAddress,
                                         self.emergencyContent, self.emergencyId, self.emergencySource,
                                         self.emergencyTitle, self.orgId, self.emergencyTypeId, self.emergency_fileList,
                                         self.userId)
        jsonstr = response.json()
        # assert response.code == 200
        assert jsonstr['message'] == 'request successful'

    # @unittest.skip("Don't run")
    def testEmergencyList(self):
        response = self.app.emergencyList(self.userAcceptance, self.userId, self.pageNum, self.count, self.startDate,
                                          self.endDate, self.emergencyStatus, self.emergencyTypeOneId,
                                          self.emergencyTypeTwoId, self.orgId, self.orgSubsetCode, self.ifThisOrg)
        jsonstr = response.json()
        # assert response.code == 200
        assert jsonstr['message'] == 'request successful'
        assert jsonstr['data']['resultList'][0]['emergencyTitle'] == '1'

    @unittest.skip("Don't run")
    def testDeleteEmergency(self):
        response = self.app.deleteEmergency()
        jsonstr = response.json()
        # assert response.code == 200
        assert jsonstr['message'] == 'request successful'


if __name__ == '__main__':
    unittest.main()
