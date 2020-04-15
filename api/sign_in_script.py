import time
import re


class Sign(object):

    def __init__(self, session, classid, courseid, activeid, sign_type):
        self.classid = classid
        self.courseid = courseid
        self.activeid = activeid
        self.sign_type = sign_type
        self.session = session
        self.headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}

    def general_sign(self):
        """普通签到"""
        r = self.session.get(
            'https://mobilelearn.chaoxing.com/widget/sign/pcStuSignController/preSign?activeId={}&classId={}&fid=&courseId={}'.format(
                self.activeid,
                self.classid,
                self.courseid),
            headers=self.headers,
            verify=False)
        title = re.findall('<title>(.*)</title>', r.text)[0]
        if "签到成功" not in title:
            # 网页标题不含签到成功，则为拍照签到
            return self.tphoto_sign()
        else:
            sign_date = re.findall('<em id="st">(.*)</em>', r.text)[0]
            return {
                'date': sign_date,
                'status': 3000
            }

    def hand_sign(self):
        """手势签到"""
        hand_sign_url = "https://mobilelearn.chaoxing.com/widget/sign/pcStuSignController/signIn?&courseId={}&classId={}&activeId={}".format(
            self.courseid, self.classid, self.activeid)
        r = self.session.get(hand_sign_url, headers=self.headers, verify=False)
        title = re.findall('<title>(.*)</title>', r.text)
        sign_date = re.findall('<em id="st">(.*)</em>', r.text)[0]
        return {
            'date': sign_date,
            'status': 3001
        }

    def qcode_sign(self):
        """二维码签到"""
        params = {
            'name': '',
            'activeId': self.activeid,
            'uid': '',
            'clientip': '',
            'useragent': '',
            'latitude': '-1',
            'longitude': '-1',
            'fid': '',
            'appType': '15'
        }
        self.session.get(
            'https://mobilelearn.chaoxing.com/pptSign/stuSignajax',
            params=params)
        return {
            'date': time.strftime("%m-%d %H:%M", time.localtime()),
            'status': 3004
        }

    def addr_sign(self):
        """位置签到"""
        params = {
            'name': '',
            'activeId': self.activeid,
            'address': '中国',
            'uid': '',
            'clientip': '0.0.0.0',
            'latitude': '-2',
            'longitude': '-1',
            'fid': '',
            'appType': '15',
            'ifTiJiao': '1'
        }
        self.session.get(
            'https://mobilelearn.chaoxing.com/pptSign/stuSignajax',
            params=params)
        return {
            'date': time.strftime("%m-%d %H:%M", time.localtime()),
            'status': 3003
        }

    def tphoto_sign(self):
        """拍照签到"""
        params = {
            'name': '',
            'activeId': self.activeid,
            'address': '中国',
            'uid': '',
            'clientip': '0.0.0.0',
            'latitude': '-2',
            'longitude': '-1',
            'fid': '',
            'appType': '15',
            'ifTiJiao': '1',
            'objectId': '5712278eff455f9bcd76a85cd95c5de3'
        }
        self.session.get(
            'https://mobilelearn.chaoxing.com/pptSign/stuSignajax',
            params=params)
        return {
            'date': time.strftime("%m-%d %H:%M", time.localtime()),
            'status': 3002
        }