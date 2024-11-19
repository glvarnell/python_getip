import pytest
from getip import getip


# Test cases for getip function
def test_getip_no_ips():
    result = getip("No IP addresses here!")
    assert result is None

def test_getip_single_ip():
    result = getip("Visit us at 192.168.1.1.")
    assert result == ["192.168.1.1"]

def test_getip_multiple_ips():
    result = getip("Multiple IPs: 10.0.0.1, 172.16.0.1, and 192.168.1.1.")
    assert result == ["10.0.0.1", "172.16.0.1", "192.168.1.1"]

def test_getip_leading_trailing_whitespace():
    result = getip("IP with spaces at ends: 255.255.255.255 ")
    assert result == ["255.255.255.255"]
    
    result = getip("  255.255.255.255 trailing spaces")
    assert result == ["255.255.255.255"]

def test_getip_ips_in_brackets():
    result = getip("[192.168.1.1] is the internal server.")
    assert result == ["192.168.1.1"]
    
    result = getip("Multiple IPs in brackets: [10.0.0.1], [172.16.0.1]")
    assert result == ["10.0.0.1", "172.16.0.1"]


if __name__ == "__main__":
    pytest.main(['test_getip.py', '-W', 'ignore'])