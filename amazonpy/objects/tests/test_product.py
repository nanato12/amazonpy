from typing import Any, List

import pytest

from amazonpy.consts import Config
from amazonpy.objects import Product


class TestProduct:
    @pytest.fixture
    def valid_param(self) -> List[Any]:
        return ["id", "タイトル", "説明", "値段", ["タイプ1", "タイプ2"]]

    def test_constract(self, valid_param: List[Any]) -> None:
        """ インスタンス化できること """
        product = Product(*valid_param)

        assert product.id == valid_param[0]
        assert product.title == valid_param[1]
        assert product.description == valid_param[2]
        assert product.price == valid_param[3]
        assert product.another_type == valid_param[4]
        assert product.url == Config.HOST + Config.PRODUCT_PATH.format(valid_param[0])
