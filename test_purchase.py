import pytest


@pytest.fixture
def setUp():
    print("setup started")
    yield
    print("exited")


def test_AddItemtoCart(setUp):
    print("Added items successfully")


def test_RemoveItemtoCart(setUp):
    print("removed successfully")
