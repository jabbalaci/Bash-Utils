import redirect_to

def  test_redirect_to():
    url = 'http://docs.python-requests.org'
    result = 'http://docs.python-requests.org/en/master/'
    assert redirect_to.redirect(url) == result
