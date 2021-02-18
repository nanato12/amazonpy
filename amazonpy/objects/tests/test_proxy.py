from typing import Any, List

import pytest

from amazonpy.consts import Config
from amazonpy.objects import Proxy


class TestProxy:
    @pytest.fixture
    def valid_param(self) -> List[Any]:
        return [
            "0.0.0.0",
            "8000",
            "JP",
            "Japan",
            "anonymous",
            True,
            True,
            "4 minutes ago",
        ]

    def test_constract(self, valid_param: List[Any]) -> None:
        """ インスタンス化できること """
        proxy = Proxy(*valid_param)

        assert proxy.ip == valid_param[0]
        assert proxy.port == valid_param[1]
        assert proxy.code == valid_param[2]
        assert proxy.country == valid_param[3]
        assert proxy.anonymity == valid_param[4]
        assert proxy.is_google == valid_param[5]
        assert proxy.is_https == valid_param[6]
        assert proxy.refresh == valid_param[7]

    @pytest.mark.parametrize(
        "is_https,url",
        [
            (True, "https://0.0.0.0:8000"),
            (False, "http://0.0.0.0:8000"),
        ],
    )
    def test_url(self, valid_param: List[Any], is_https: bool, url: str) -> None:
        valid_param[6] = is_https
        proxy = Proxy(*valid_param)

        assert proxy.url == url

    @pytest.mark.parametrize(
        "is_https,protcol",
        [
            (True, "https"),
            (False, "http"),
        ],
    )
    def test_protcol(
        self, valid_param: List[Any], is_https: bool, protcol: str
    ) -> None:
        valid_param[6] = is_https
        proxy = Proxy(*valid_param)

        assert proxy.protcol == protcol
