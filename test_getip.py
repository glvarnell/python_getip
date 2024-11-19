import pytest
import getip

def test_getip():
    assert getip.getip('valid ip 0.0.0.0')[0] == '0.0.0.0'
    assert getip.getip('valid ip 1.1.1.1')[0] == '1.1.1.1'
    assert getip.getip('valid ip 123.34.567.89')[0] == '123.34.567.89'
    assert getip.getip('127.0.0.1 test at start of string') == ['127.0.0.1']
    assert getip.getip('test at end of string 127.0.0.1') == ['127.0.0.1']
    assert getip.getip('0.0.0.0 test multiple ips in string 127.0.0.1') == ['0.0.0.0','127.0.0.1']
    assert getip.getip('test bad ip 1234.0.0.0') == None
    assert getip.getip('test bad ip 0.0.0') == None
    assert getip.getip('This is bad, but will match the good part 0.0.0.0.0') == ['0.0.0.0']