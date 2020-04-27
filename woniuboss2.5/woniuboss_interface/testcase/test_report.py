import unittest
from parameterized import parameterized

from common.report import Report
from utils.Utils import Utility

info = Utility.get_json('..//config//testdata.conf')
reportdata = Utility.get_excel_to_tuple(info[1])
# print(reportdata)


class ReportTest(unittest.TestCase):


    @parameterized.expand(reportdata)
    def test_report(self,url,data,expect):
        resp = Report().do_report(url,data)
        content = resp.text
        self.assertEqual(content, expect)
# if resp.text == reportdata[2][2] :
#     print('scuess')

# print(content)
# print("*********************************************")
# print(reportdata[0][2])


