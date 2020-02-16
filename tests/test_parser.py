import pytest
from bs4 import BeautifulSoup

from ParsedOperation import OperationType
from parser import parse_operation


@pytest.fixture()
def provide_operations():
    first = BeautifulSoup(""" <operation>
    <exec-date>2020-02-12</exec-date>
    <order-date>2020-02-11</order-date>
    <type>Obciążenie</type>
    <description>AUTOOSZCZĘDZANIE-PRZELEW</description>
    <amount curr='PLN'>-1.05</amount>
    <ending-balance curr='PLN'>-1.05</ending-balance>
  </operation>""", "xml")

    return [first]


def test_parse_operation(provide_operations):
    result = parse_operation(provide_operations[0], "1")
    assert result.Type == OperationType.OUTGOING
