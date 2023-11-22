import COMP7039_CI_Code_Base_V1_1 as codebase
import pytest
from unittest.mock import patch, mock_open
from io import StringIO

# Test for valid input within range
@patch('builtins.input', side_effect=['5'])
def test_read_integer_between_numbers_valid(mock_input):
    assert codebase.read_integer_between_numbers("Enter number: ", 1, 10) == 5

# Test for input outside range
@patch('builtins.input', side_effect=['11', '5'])
def test_read_integer_between_numbers_out_of_range(mock_input):
    assert codebase.read_integer_between_numbers("Enter number: ", 1, 10) == 5

# Test for non-integer input
@patch('builtins.input', side_effect=['abc', '5'])
def test_read_integer_between_numbers_non_integer(mock_input):
    assert codebase.read_integer_between_numbers("Enter number: ", 1, 10) == 5


@patch('builtins.input', side_effect=['', 'hello'])
def test_read_nonempty_string(mock_input):
    assert codebase.read_nonempty_string("Enter string: ") == 'hello'

# Mock file content
mock_file_content = "Runner1,CK1\nRunner2,KY2\n"

@patch('builtins.open', return_value=StringIO(mock_file_content))
def test_runners_data(mock_open):
    names, ids = codebase.runners_data()
    assert names == ["Runner1", "Runner2"]
    assert ids == ["CK1", "KY2"]

@patch('your_module.read_integer_between_numbers', return_value=2)
@patch('your_module.reading_race_results', return_value=(["ID1", "ID2"], [30, 45]))
def test_race_results(mock_read_integer, mock_reading_race_results):
    assert codebase.race_results(["Location1", "Location2"]) == (["ID1", "ID2"], [30, 45], "Location2")

@patch('builtins.open', return_value=StringIO("Location1\nLocation2\n"))
def test_race_venues(mock_open):
    assert codebase.race_venues() == ["Location1", "Location2"]

def test_winner_of_race():
    ids = ["ID1", "ID2", "ID3"]
    times = [45, 30, 60]
    assert codebase.winner_of_race(ids, times) == "ID2"


@patch('builtins.print')
def test_display_races(mock_print):
    codebase.display_races(["ID1", "ID2"], [130, 90], "Venue1", "ID2")
    mock_print.assert_called()

@patch('builtins.open', new_callable=mock_open)
def test_updating_races_file(mock_open):
    codebase.updating_races_file(["Venue1", "Venue2"])
    mock_open.assert_called_with('./Races-1.txt', 'w')

@patch('builtins.print')
def test_competitors_by_county(mock_print):
    codebase.competitors_by_county(["Runner1", "Runner2"], ["CK1", "KY2"])
    mock_print.assert_called()
