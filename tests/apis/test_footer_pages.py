from fastapi.testclient import TestClient


def test_importing_api():
    # this will raise an exception if pydantic model validation fails for the api
    from oasis_optimal_footer_pages.apis import oasis_optimal_footer_pages

    assert oasis_optimal_footer_pages.name == 'oasis_optimal_footer_pages'


def test_static_files_serving():
    from oasis_optimal_footer_pages.apis import oasis_optimal_footer_pages

    app = oasis_optimal_footer_pages.load()
    client = TestClient(app)
    response = client.get('/static/terms.html')
    assert response.status_code == 200
