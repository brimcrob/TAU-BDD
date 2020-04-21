from selenium.webdriver.common.keys import Keys


def test_google_search(py):
    py.visit("https://google.com")
    py.get("[name='q']").type("Weather in Edinburgh", Keys.ENTER)
    assert "Weather in Edinburgh" in py.title
