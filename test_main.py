from main import convert_date


def test_convert_date():
    assert convert_date('2022-10-08') == '08/10/2022'
    assert convert_date('88873283') == None




