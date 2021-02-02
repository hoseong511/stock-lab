import unittest
from stocklab.agent.ebest import Ebest
import inspect
import time
class TestEBest(unittest.TestCase):
    def setUp(self):
        self.ebest = Ebest("DEMO")
        self.ebest.login()

    def tearDown(self):
        self.ebest.logout()