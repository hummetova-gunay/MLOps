def test_long_lists():
    result = ['blah', 'blah', 'blahhhhhhhhhhhhh']
    expected = ['blah', 'blah', 'blahhhhhhhhhhhh']
    assert result == expected