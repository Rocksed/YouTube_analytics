from utils.main import Channel


def test_Channel():
    # Test creating a Channel object
    c = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert c.id == 'UCMCgOm8GZkHp8zJ6l7_hIuA'
    assert c.name != ''
    assert c.description != ''
    assert c.views >= 0
    assert c.subscribers >= 0

    # Test getting data for a channel
    c.get_data()
    assert c.name != ''
    assert c.description != ''
    assert c.views >= 0
    assert c.subscribers >= 0

    # Test printing info for a channel
    c.print_info()
    # The print statements cannot be tested automatically, so we just need to make sure they don't raise an exception


test_Channel()
