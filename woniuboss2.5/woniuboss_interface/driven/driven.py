
import unittest
from utils.Utils import Utility
class Driven:
    @classmethod
    def start(cls):
        ts = unittest.TestSuite()
        load = unittest.TestLoader()
        text_name = Utility.trans_str('..\\config\\test.conf')
        # test = load.loadTestsFromName('woniusales_exam02.testcase.testsales')
        texts = load.loadTestsFromNames(text_name)
        ts.addTests(texts)
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime())
        with open('..\\report\\%s_report.html'%(ctime),'w') as f:
            from HTMLTestRunner import HTMLTestRunner
            runner = HTMLTestRunner(stream=f,verbosity=2)
            runner.run(ts)

if __name__ == '__main__':
    Driven.start()

