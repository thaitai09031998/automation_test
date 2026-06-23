import pytest
from ultils.api_helper import APIHelper
from ultils.config_reader import ConfigReader

class TestDummyJSONProductsAPI:
  
    @pytest.fixture(autouse=True)
    def setup(self):
        config = ConfigReader()
        base_url = config.get_base_url()
        self.api_helper = APIHelper(base_url=base_url)

    @pytest.mark.get
    def test_get_products(self):

        response = self.api_helper.get("/product/1")

        assert response.status_code == 200
        product = response.json()
        assert product["id"] == 1
        assert product["title"] == "Essence Mascara Lash Princess"