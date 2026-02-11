import psutil

def test_cpu():
    assert 0 <= psutil.cpu_percent() <= 100