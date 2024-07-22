import pytest

# I decided to use freezgun for testing dates. It seems not that crucial for now,
# but in the past I was using different format with hh-mm-ss. I'm not sure if I
# won't use it again in the future, and that's why I'm including it:
from freezegun import freeze_time
from src.gamequeue_planner.models.DatesEditor import DatesEditor

@freeze_time("2023-07-19")
def test_get_current_time():
    editor = DatesEditor()
    assert editor.get_current_time() == '_2023-07-19'

@freeze_time("2000-01-01")
def test_get_current_time_different_date():
    editor = DatesEditor()
    assert editor.get_current_time() == '_2000-01-01'
    
if __name__ == "__main__":
    pytest.main()