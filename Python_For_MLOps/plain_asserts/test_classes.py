def str_to_int(string):
    error_msg = "Unable to convert to integer: '%s'" %str(string)
    try:
        integer = float(string.replace(',', '.'))
    except AttributeError:
        if isinstance(string, (int, float)):
            integer = string
        else: 
            raise RuntimeError(error_msg)
    except (TypeError, ValueError):
        raise RuntimeError(error_msg)
    
    return int(integer)

class TestStrToInt:
    def setup(self):
        print('\nthis is setup')
    
    def teardown(self):
        print('\nthis is teardown')
    def setup_class(cls):
        print('\nthis is setup class')
    def teardown_class(cls):
        print('\nthis is teardown class')
    def test_rounds_down(self):
        result = str_to_int(1.99)
        assert result ==2
    def test_rounds_down_half(self):
        result = str_to_int('1.2')
        assert result==2 