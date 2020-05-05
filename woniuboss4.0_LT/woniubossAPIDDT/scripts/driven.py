# -*- coding: utf-8 -*-
from HTMLTestRunner import HTMLTestRunner
import unittest

from woniubossAPIDDT.tools.uiti import uiti


class Driven:

    def start(self):
        ts=unittest.TestSuite()
        loader=unittest.TestLoader()
        text=uiti.get_str('..\\conf\\test.conf')
        tests = loader.loadTestsFromNames(text)
        ts.addTests(tests)
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        with open('..\\logs\\%s_report.html'%(ctime),'w',encoding='utf-8') as f:
            runner = HTMLTestRunner(stream=f,verbosity=2)
            runner.run(ts)

if __name__ == '__main__':
    Driven().start()

