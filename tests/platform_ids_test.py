import pytest

from gamequeue_planner.models.Platform.platform_ids import platform_ids

def test_expected_platform_ids_values():
    expected_platform_ids = {
        "PlayStation": 6,
        "PlayStation 2": 7,
        "Dreamcast": 8,
        "Nintendo 64": 9,
        "Game Boy": 10,
        "Game Boy Color": 11,
        "Game Boy Advance": 12,
        "Xbox": 13,
        "GameCube": 14,
        "SNES": 15,
        "Genesis": 16,
        "SEGA CD": 20,
        "SEGA 32X": 21,
        "NES": 22,
        "SEGA Saturn": 23,
        "SEGA Master System": 26,
        "Nintendo DS": 44,
        "PSP": 46,
        "Xbox 360": 69,
        "PlayStation 3": 81,
        "Wii": 82,
        "Nintendo DSi": 87,
        "Nintendo 3DS": 101,
        "PS Vita": 105,
        "Wii U": 132,
        "PlayStation 4": 141,
        "Xbox One": 142,
        "New Nintendo 3DS": 174,
        "Nintendo Switch": 203,
        "Xbox Series": 289
    }
    
    assert expected_platform_ids == platform_ids
    
def test_platform_id():
    assert platform_ids["PlayStation"] == 6
    assert platform_ids["PlayStation 2"] == 7 
    assert platform_ids["Dreamcast"] == 8
    assert platform_ids["Nintendo 64"] == 9 
    assert platform_ids["Game Boy"] == 10
    assert platform_ids["Game Boy Color"] == 11
    assert platform_ids["Game Boy Advance"] == 12
    assert platform_ids["Xbox"] == 13
    assert platform_ids["GameCube"] == 14
    assert platform_ids["SNES"] == 15
    assert platform_ids["Genesis"] == 16
    assert platform_ids["SEGA CD"] == 20
    assert platform_ids["SEGA 32X"] == 21
    assert platform_ids["NES"] == 22
    assert platform_ids["SEGA Saturn"] == 23
    assert platform_ids["SEGA Master System"] == 26
    assert platform_ids["Nintendo DS"] == 44
    assert platform_ids["PSP"] == 46
    assert platform_ids["Xbox 360"] == 69
    assert platform_ids["PlayStation 3"] == 81
    assert platform_ids["Wii"] == 82
    assert platform_ids["Nintendo DSi"] == 87
    assert platform_ids["Nintendo 3DS"] == 101
    assert platform_ids["PS Vita"] == 105
    assert platform_ids["Wii U"] == 132
    assert platform_ids["PlayStation 4"] == 141
    assert platform_ids["Xbox One"] == 142
    assert platform_ids["New Nintendo 3DS"] == 174
    assert platform_ids["Nintendo Switch"] == 203
    assert platform_ids["Xbox Series"] == 289
    
def test_if_platform_key_exist():
    expected_keys = {"PlayStation", "PlayStation 2", "Dreamcast", "Nintendo 64", "Game Boy", "Game Boy Color",
                     "Game Boy Advance", "Xbox", "GameCube", "SNES", "Genesis", "SEGA CD", "SEGA 32X", "NES",
                     "SEGA Saturn", "SEGA Master System", "Nintendo DS", "PSP", "Xbox 360", "PlayStation 3",
                     "Wii", "Nintendo DSi", "Nintendo 3DS", "PS Vita", "Wii U", "PlayStation 4", "Xbox One",
                     "New Nintendo 3DS", "Nintendo Switch", "Xbox Series"}
    
    assert set(platform_ids.keys()) == expected_keys
    
def test_if_no_extra_platform_key_exist():
    expected_keys = {"PlayStation", "PlayStation 2", "Dreamcast", "Nintendo 64", "Game Boy", "Game Boy Color",
                     "Game Boy Advance", "Xbox", "GameCube", "SNES", "Genesis", "SEGA CD", "SEGA 32X", "NES",
                     "SEGA Saturn", "SEGA Master System", "Nintendo DS", "PSP", "Xbox 360", "PlayStation 3",
                     "Wii", "Nintendo DSi", "Nintendo 3DS", "PS Vita", "Wii U", "PlayStation 4", "Xbox One",
                     "New Nintendo 3DS", "Nintendo Switch", "Xbox Series"}
    
    assert not set(platform_ids.keys()) - expected_keys
