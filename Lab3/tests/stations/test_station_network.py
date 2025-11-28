"""Тесты для StationNetwork"""
from stations.station_network import StationNetwork


def test_station_network_init():
    network = StationNetwork("N001", "Moscow Network", "Central")
    assert network.network_id == "N001"
    assert network.network_name == "Moscow Network"


