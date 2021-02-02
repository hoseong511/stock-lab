import unittest
from stocklab.agent.ebest import EBest
import inspect
import time
class TestEBest(unittest.TestCase):
    def setUp(self):
        self.ebest = EBest("DEMO")
        self.ebest.login()
        print("hi")

    def tearDown(self):
        self.ebest.logout()
        print("bye")