# there will be some installations
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language for testing")


def get_browser_options(req):
    lang_prop = req.config.getoption("--language")
    if not len(lang_prop):
        raise pytest.UsageError("language should be spesified")
    options = Options()
    args = ["--headless", "--lang=" + lang_prop]
    for opt in args:
        options.add_argument(opt)
    return options

@pytest.fixture()
def browser(request):
    browser = None
    browser = webdriver.Chrome(options=get_browser_options(request))
    browser.implicitly_wait(5)
    yield browser
    browser.quit()