from typing import Dict, List

import pytest
from bs4 import BeautifulSoup

from amazonpy import get_proxies
from amazonpy.objects import Proxy


class TestGetProxies:
    @pytest.fixture
    def full_html(self) -> str:
        return """
        <table class="table table-striped table-bordered dataTable" cellspacing="0" width="100%" id="proxylisttable" role="grid"
            aria-describedby="proxylisttable_info" style="width: 100%;">
            <tbody>
                <tr role="row" class="odd">
                    <td>142.93.50.179</td>
                    <td>3128</td>
                    <td>US</td>
                    <td class="hm">United States</td>
                    <td>elite proxy</td>
                    <td class="hm sorting_1">no</td>
                    <td class="hx">no</td>
                    <td class="hm">8 seconds ago</td>
                </tr>
                <tr role="row" class="even">
                    <td>1.20.100.45</td>
                    <td>51685</td>
                    <td>TH</td>
                    <td class="hm">Thailand</td>
                    <td>elite proxy</td>
                    <td class="hm sorting_1">no</td>
                    <td class="hx">no</td>
                    <td class="hm">8 seconds ago</td>
                </tr>
                <tr role="row" class="odd">
                    <td>37.49.127.229</td>
                    <td>8080</td>
                    <td>DE</td>
                    <td class="hm">Germany</td>
                    <td>anonymous</td>
                    <td class="hm sorting_1">no</td>
                    <td class="hx">no</td>
                    <td class="hm">8 seconds ago</td>
                </tr>
            </tbody>
        </table>
        """

    @pytest.fixture
    def full_data(self) -> List[Dict[str, str]]:
        return [
            {
                "ip": "142.93.50.179",
                "port": "3128",
                "code": "US",
                "country": "United States",
                "anonymity": "elite proxy",
                "is_google": False,
                "is_https": False,
                "refresh": "8 seconds ago",
            },
            {
                "ip": "1.20.100.45",
                "port": "51685",
                "code": "TH",
                "country": "Thailand",
                "anonymity": "elite proxy",
                "is_google": False,
                "is_https": False,
                "refresh": "8 seconds ago",
            },
            {
                "ip": "37.49.127.229",
                "port": "8080",
                "code": "DE",
                "country": "Germany",
                "anonymity": "anonymous",
                "is_google": False,
                "is_https": False,
                "refresh": "8 seconds ago",
            },
        ]

    def test_get_proxies(
        self, mocker, full_html: str, full_data: List[Dict[str, str]]
    ) -> None:
        mocker.patch(
            "amazonpy.proxies.BeautifulSoup",
            return_value=BeautifulSoup(full_html, "html.parser"),
        )
        proxies: List[Proxy] = get_proxies()

        assert len(proxies) == 3

        proxy: Proxy
        data: Dict[str, str]
        for proxy, data in zip(proxies, full_data):
            assert proxy.ip == data["ip"]
            assert proxy.port == data["port"]
            assert proxy.code == data["code"]
            assert proxy.country == data["country"]
            assert proxy.anonymity == data["anonymity"]
            assert proxy.is_google == data["is_google"]
            assert proxy.is_https == data["is_https"]
            assert proxy.refresh == data["refresh"]
