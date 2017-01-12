import slogan

def test_get_slogan():
    word = 'pen'
    times = 2
    li = slogan.get_slogan(word, times)
    assert len(li) == 2
    for text in li:
        assert word in text
