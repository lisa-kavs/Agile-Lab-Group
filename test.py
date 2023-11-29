import codebase
import pytest
from unittest.mock import patch, mock_open
from io import StringIO

#Test 1: read_integer_between_valid
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

# Test 2: read_nonempty_string
@patch('builtins.input', side_effect=['', 'hello'])
def test_read_nonempty_string(mock_input):
    assert codebase.read_nonempty_string("Enter string: ") == 'hello'

# Mock file content
mock_file_content = "Runner1,CK1\nRunner2,KY2\n"

# Test 4: runners_data
@patch('builtins.open', return_value=StringIO(mock_file_content))
def test_runners_data(mock_open):
    names, ids = codebase.runners_data()
    assert names == ["Runner1", "Runner2"]
    assert ids == ["CK1", "KY2"]

# Test 4: race_results
@patch('codebase.read_integer_between_numbers', return_value=2)
@patch('codebase.reading_race_results', return_value=(["ID1", "ID2"], [30, 45]))
def test_race_results(mock_read_integer, mock_reading_race_results):
    assert codebase.race_results(["Location1", "Location2"]) == (["ID1", "ID2"], [30, 45], "Location2")

# Test 5: race_venues
@patch('builtins.open', return_value=StringIO("Location1\nLocation2\n"))
def test_race_venues(mock_open):
    assert codebase.race_venues() == ["Location1", "Location2"]

# Test 6: winner_of_race
def test_winner_of_race():
    ids = ["ID1", "ID2", "ID3"]
    times = [45, 30, 60]
    assert codebase.winner_of_race(ids, times) == "ID2"

# Test 7: display_races
@patch('builtins.print')
def test_display_races(mock_print):
    codebase.display_races(["ID1", "ID2"], [130, 90], "Venue1", "ID2")
    mock_print.assert_called()

# Test 8: users_venue
@patch('codebase.read_nonempty_string', return_value='Newvenue')
@patch('codebase.read_integer', side_effect=[120, 0])
@patch('builtins.open', new_callable=mock_open)
def test_users_venue(mock_open, mock_read_integer, mock_read_string):
    codebase.users_venue(["Venue1"], ["ID1", "ID2"])
    mock_open.assert_called_with('Newvenue.txt', 'a')

# Test 9: updating_races_file
@patch('builtins.open', new_callable=mock_open)
def test_updating_races_file(mock_open):
    codebase.updating_races_file(["Venue1", "Venue2"])
    mock_open.assert_called_with('./Races-1.txt', 'w')

# Test 10: competitors_by_county
@patch('builtins.print')
def test_competitors_by_county(mock_print):
    codebase.competitors_by_county(["Runner1", "Runner2"], ["CK1", "KY2"])
    mock_print.assert_called()

# Test 11: reading_race_results
@patch('builtins.open', return_value=StringIO("ID1,30\nID2,45\n"))
def test_reading_race_results(mock_open):
    assert codebase.reading_race_results("Location") == (["ID1", "ID2"], [30, 45])

# Test 12: reading_race_results_of_relevant_runner
@patch('builtins.open', new_callable=mock_open, read_data="ID1,30\nID2,45\n")
def test_reading_race_results_of_relevant_runner(mock_open):
    assert codebase.reading_race_results_of_relevant_runner("Location", "ID1") == 30
    assert codebase.reading_race_results_of_relevant_runner("Location", "ID3") is None

# Test 13: displaying_winners_of_each_race
@patch('codebase.reading_race_results', return_value=(["ID1", "ID2"], [30, 45]))
@patch('codebase.winner_of_race', return_value="ID1")
@patch('builtins.print')
def test_displaying_winners_of_each_race(mock_print, mock_winner_of_race, mock_reading_race_results):
    codebase.displaying_winners_of_each_race(["Location1", "Location2"])
    mock_print.assert_called()

# Test 14: relevant_runner_info
@patch('codebase.read_integer_between_numbers', return_value=1)
def test_relevant_runner_info(mock_read_integer):
    assert codebase.relevant_runner_info(["Runner1", "Runner2"], ["ID1", "ID2"]) == ("Runner1", "ID1")

# Test 15: convert_time_to_minutes_and_seconds
def test_convert_time_to_minutes_and_seconds():
    minutes, seconds = codebase.convert_time_to_minutes_and_seconds(90)
    assert minutes == 1
    assert seconds == 5400

# Test 16: sorting_where_runner_came_in_race
@patch('builtins.open', return_value=StringIO("ID1,30\nID2,45\nID3,60\n"))
def test_sorting_where_runner_came_in_race(mock_open):
    position, total_runners = codebase.sorting_where_runner_came_in_race("Location", 45)
    assert position == 2
    assert total_runners == 3

# Test 17: displaying_race_times_one_competitor
@patch('codebase.reading_race_results_of_relevant_runner', side_effect=[30, None, 45])
@patch('codebase.convert_time_to_minutes_and_seconds', side_effect=[(0, 1800), (0, 2700)])
@patch('codebase.sorting_where_runner_came_in_race', side_effect=[(1, 3), (2, 3)])
@patch('builtins.print')
def test_displaying_race_times_one_competitor(mock_print, mock_sorting, mock_convert, mock_reading):
    codebase.displaying_race_times_one_competitor(["Location1", "Location2", "Location3"], "Runner1", "ID1")
    mock_print.assert_called()

# Test 18: finding_name_of_winner
def test_finding_name_of_winner():
    assert codebase.finding_name_of_winner("ID1", ["ID1", "ID2"], ["Runner1", "Runner2"]) == "Runner1"

# Test 19: displaying_runners_who_have_won_at_least_one_race
@patch('codebase.reading_race_results', side_effect=[[("ID1", "ID2"), (30, 45)], [("ID3", "ID4"), (60, 75)]])
@patch('codebase.winner_of_race', side_effect=["ID1", "ID3"])
@patch('codebase.finding_name_of_winner', side_effect=["Runner1", "Runner3"])
@patch('builtins.print')
def test_displaying_runners_who_have_won_at_least_one_race(mock_print, mock_finding, mock_winner, mock_reading):
    codebase.displaying_runners_who_have_won_at_least_one_race(["Location1", "Location2"], ["Runner1", "Runner2", "Runner3", "Runner4"], ["ID1", "ID2", "ID3", "ID4"])
    mock_print.assert_called()

# Test 20: main
@patch('builtins.input', side_effect=["1", "7"])
@patch('codebase.race_venues', return_value=["Location1", "Location2"])
@patch('codebase.runners_data', return_value=(["Runner1", "Runner2"], ["ID1", "ID2"]))
@patch('codebase.race_results', return_value=(["ID1", "ID2"], [30, 45], "Location1"))
@patch('codebase.winner_of_race', return_value="ID1")
@patch('codebase.display_races')
@patch('codebase.updating_races_file')
def test_main(mock_updating, mock_display, mock_winner, mock_race_results, mock_runners_data, mock_race_venues, mock_input):
    codebase.main()
    mock_race_venues.assert_called()
    mock_runners_data.assert_called()
    mock_race_results.assert_called()
    mock_winner.assert_called()
    mock_display.assert_called()
    mock_updating.assert_called()