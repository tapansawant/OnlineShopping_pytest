import pytest


@pytest.fixture(scope="Session", autouse=True)
def setUp():
    print("Open Amazon app")
    print("User logged in")
    yield
    print("logged out")
    print("Closed Amazon app")
