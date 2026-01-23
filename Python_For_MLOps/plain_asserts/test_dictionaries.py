def test_dictionaries():
    result = {'key':'value', 'name': 'Gunay', 'lastname':'Hummatova'}
    expected = {'key': 'valu', 'name': 'Gunay', 'lastName': 'hummatova'}
    assert result == expected

    