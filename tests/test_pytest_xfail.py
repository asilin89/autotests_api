import pytest


@pytest.mark.xfail(reason="Test fails due to system issue")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Bug is fixed but xfail is still a marker for this test")
def test_without_bug():
    ...

@pytest.mark.xfail(reason="Remote server is temporary unavailable")
def test_external_service_is_unavailable():
    assert 1 == 2