from pyramid import testing
from forbes.data.billionaires import BILLIES
import pytest


@pytest.fixture
def testapp():
    """Create an instance of our app for testing."""
    from forbes import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


@pytest.fixture
def billie_view_response():
    """Return a list view response."""
    from forbes.views.default import billie_view
    request = testing.DummyRequest()
    return billie_view(request)


def test_billie_view_returns_dict_given_request(billie_view_response):
    """Assert if list view returns a valid response."""
    assert isinstance(billie_view_response, dict)


def test_billie_view_returns_proper_len_of_content(billie_view_response):
    """Assert list view returns proper length of content."""
    assert len(billie_view_response.get('billie_entries')) == len(BILLIES)


def test_layout(testapp):
    """Assert that layout file contains correct data."""
    response = testapp.get('/', status=200)
    html = response.html
    assert 'JourNull' in html.find('p').text


def test_root_contents(testapp):
    """Assert that listing view contais the correct ammount of article tags."""
    response = testapp.get('/', status=200)
    html = response.html
    assert len(BILLIES) == len(html.findAll("article"))
