import pytest
import requests
from scripts.services import data_service
from mock import patch


def test_fetch_data_service():
    response = data_service.fetch_data()
    assert "data-engineering-zoomcamp" in str(response)


def test_fetch_data_service_with_error():
    with patch("scripts.services.data_service.requests.get") as mock_get:
        mock_get.status_code.return_value = 300
        with pytest.raises(requests.exceptions.HTTPError) as ex:
            data_service.fetch_data()
        assert "Failed to fetch data" in str(ex.value)
