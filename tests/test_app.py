from falemais.ext.site.controller import (calculate_plan_30, calculate_plan_60,
                                          calculate_plan_120,
                                          calculate_without_plan)


def test_app_is_created(app):
    assert app.name == "falemais.app"


def test_config_is_loaded(config):
    assert config["DEBUG"] is False


def test_request_returns_404(client):
    assert client.get("/url_that_does_not_exists").status_code == 404

def test_calculate_without_plan():
    for i, j, k in zip(range(50), range(50), range(50)):
        assert type(calculate_without_plan(i, j, k)) == str and calculate_without_plan(i, j, k) is not None

def test_calculate_plan_30():
    for i, j, k in zip(range(50), range(50), range(50)):
        assert type(calculate_plan_30(i, j, k)) == str and calculate_plan_30(i, j, k) is not None

def test_calculate_plan_60():
    for i, j, k in zip(range(50), range(50), range(50)):
        assert type(calculate_plan_60(i, j, k)) == str and calculate_plan_60(i, j, k) is not None

def test_calculate_plan_120():
    for i, j, k in zip(range(50), range(50), range(50)):
        assert type(calculate_plan_120(i, j, k)) == str and calculate_plan_120(i, j, k) is not None