from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


class TestAbs:
    def test_abs1(self):
        assert abs(-42) == 42, "Should be absolute value of a number"

    def test_abs2(self):
        assert abs(-42) == -42, "Should be absolute value of a number"
