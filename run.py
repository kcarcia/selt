from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import DesiredCapabilities
import argparse
import os
import json
from termcolor import colored
from configs.config import *


parser = argparse.ArgumentParser()
parser.add_argument("--browser", help="(String) Browser tests are run on. "
                                      "Options include: firefox, "
                                      "firefox-headless, chrome, "
                                      "chrome-headless. Default is "
                                      "chrome-headless.",
                    default=DEFAULT_BROWSER)


def init_browser():
    """
    Initializes the latest version of chrome, chrome-headless, firefox,
    or firefox-headless. The browser is passed through the command line via
    the --browser flag OR the default browser specified in config.py is used.
    :return webdriver: The webdriver used to run Selenium tests on

    NOTE: Currently, init_browser supports only the latest version of Firefox
    and the latest version of Chrome. It  should be expanded to introduce
    more configurability and browser options. Additionally, parallelization
    is not yet supported.
    """
    if "firefox" in browser.lower():
        binary = FirefoxBinary(FIREFOX_PATH)
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities["marionette"] = True

        if "headless" in browser.lower():
            os.environ['MOZ_HEADLESS'] = '1'

        return webdriver.Firefox(firefox_binary=binary,
                                 executable_path=GECKODRIVER_PATH)
    elif "chrome" in browser.lower():
        if "headless" in browser.lower():
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            return webdriver.Chrome(chrome_options=chrome_options)

        return webdriver.Chrome()


def import_modules():
    """
    Imports all view classes. Methods in classes are the tests, therefore,
    we must dynamically import classes containing methods.
    :return:

    NOTE:A future enhancement is that we only import classes used by the tests
    being run.
    """
    modules = dict()
    # Names of all view classes
    views = [doc.split(".")[0] for doc in os.listdir("views") if
                  doc.endswith(".py") and doc != "__init__.py"]

    for view in views:
        class_name = view.split("_")[0].capitalize() + view.split("_")[
            1].capitalize()

        # Import class
        package = __import__("views." + view)
        module = getattr(package, view)

        # Create instance of class
        sub_module = getattr(module, class_name)(driver)
        modules[view] = sub_module

    return modules


def open_file(filename):
    """
    Opens a file in read only mode and returns its content in JSON.
    :param filename: The name of the file to be opened
    :return: Contents of file in JSON
    """
    with open(filename, 'r') as f:
        return json.load(f)


def execute_tests(tests, modules_loaded):
    """
    Executes specified tests.
    :param tests: List of tests to run
    :param modules_loaded: List of imported modules
    :return:
    """
    for test in tests:
        # If a test has an enabled field set to true OR does not have an
        # enabled field, then we assume the test is enabled and run it
        if test.get("enabled", True):
            # Run group of tests
            if test["type"] == "test-group":
                module_name = test["test_name"]
                tests = open_file("tests/" + module_name + "_manifest.json")
                execute_tests(tests, modules_loaded)
            # Run individual test
            else:
                try:
                    module_name = test["test_name"].split(".")[0]
                    test_name = test["test_name"].split(".")[1]
                    getattr(modules_loaded[module_name], test_name)(*test.get(
                        "params", []))
                    print colored("PASSED: " + test_name, "green")
                except Exception as e:
                    print colored("FAILED: " + test_name + " with message: ",
                                  "red")
                    print colored(e, "red")


def run():
    """
    Imports modules then executes tests.
    :return:
    """
    modules_loaded = import_modules()
    use_cases = open_file("tests/manifest.json")
    for use_case in use_cases:
        print "\n"
        print(" START USE CASE TESTING ".center(80, '*'))
        print "Name: " + use_case["use_case_name"]
        print "Description: " + use_case["use_case_description"]
        execute_tests(use_case["tests"], modules_loaded)

    print(" END USE CASE TESTING ".center(80, '*'))


args = parser.parse_args()
browser = args.browser
driver = init_browser()
run()
