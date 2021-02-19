# MIT License

# Copyright (c) 2021 nanato12

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


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
