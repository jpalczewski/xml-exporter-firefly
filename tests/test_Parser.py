import pytest
from bs4 import BeautifulSoup

from src.xml_parser.Parser import Parser
from src.xml_parser.models.Operation import OperationType


@pytest.fixture()
def provide_operations():
    first = BeautifulSoup(
        """ <operation>
    <exec-date>2020-02-12</exec-date>
    <order-date>2020-02-11</order-date>
    <type>Obciążenie</type>
    <description>AUTOOSZCZĘDZANIE-PRZELEW</description>
    <amount curr='PLN'>-1.05</amount>
    <ending-balance curr='PLN'>-1.05</ending-balance>
  </operation>""",
        "xml",
    )
    malformed = BeautifulSoup(
        """ <operation>
        <exac-date>2020-02-12</exec-date>
        <order-date>2020-02-11</order-dato>
        <type>Obciążenie</type>
        <description>AUTOOSZCZĘDZANIE-PRZELEW</description>
        <amount curr='PLN'>-1.05</amount
        <ending-balance curr='PLN'>-1.05</ending-balance>
      </operation>""",
        "xml",
    )
    return [first, malformed]


def test_parse_operation(provide_operations):
    parser = Parser("1")
    result = parser.parse_operation(provide_operations[0])
    assert result.Type == OperationType.OUTGOING
    assert result.execDate == "2020-02-12"


def test_handle_malformed(provide_operations):
    with pytest.raises(ValueError):
        parser = Parser("1")
        result = parser.parse_operation(provide_operations[1])
        assert result.execDate == "2020-02-12"
