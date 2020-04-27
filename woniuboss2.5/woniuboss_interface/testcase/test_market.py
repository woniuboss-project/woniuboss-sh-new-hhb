import unittest
from parameterized import parameterized

from common.report import Report
from utils.Utils import Utility

info = Utility.get_json('..//config//testdata.conf')
marketdata = Utility.get_excel_to_tuple(info[2])
# print(marketdata)


class MarketTest(unittest.TestCase):


    @parameterized.expand(marketdata)
    def test_market(self,url,data,expect):
        resp = Report().do_report(url,data)
        content = resp.text
        self.assertEqual(content, expect)
# resp = Report().do_report(marketdata[2][0],marketdata[2][1])
# content = resp.text
# print(content)
# print(marketdata[2][2])
# if content == marketdata[2][2] :
#     print('success')
# else:
#     print('fail')
