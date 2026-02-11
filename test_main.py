from main import get_stats

def test_stats_range():
    cpu, ram, disk = get_stats()
    assert 0 <= cpu <= 100
    assert 0 <= ram <= 100
    assert 0 <= disk <= 100