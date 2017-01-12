import github_user_email as g

def test_extract_email():
    github_username = 'jabbalaci'
    email = 'jabba.laci@gmail.com'
    assert g.extract_email(github_username) == email
