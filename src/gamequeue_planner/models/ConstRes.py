from enum import Enum

class ConstRes(Enum):
    four_digits = 4
    seven_digits = 7
    
    default_missing_day = "-01"
    default_missing_month_and_day = "-12-01"