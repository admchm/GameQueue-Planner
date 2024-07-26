import pytest
from gamequeue_planner.models.Platform.Platform import Platform


def test_const_sony_platforms():
    assert Platform.PlayStation.value == "PlayStation"
    assert Platform.PlayStation_2.value == "PlayStation 2"
    assert Platform.PlayStation_3.value == "PlayStation 3"
    assert Platform.PlayStation_4.value == "PlayStation 4"
    assert Platform.PSP.value == "PSP"
    assert Platform.PS_Vita.value == "PS Vita"
    
def test_const_sega_platforms():
    assert Platform.SEGA_Master_System.value == "SEGA Master System"
    assert Platform.Mega_Drive.value == "Genesis"
    assert Platform.SEGA_32X.value == "SEGA 32X"
    assert Platform.SEGA_CD.value == "SEGA CD"
    assert Platform.SEGA_SATURN.value == "SEGA Saturn"
    assert Platform.Dreamcast.value == "Dreamcast"
    
def test_const_nintendo_platforms():
    assert Platform.NES.value == "NES"
    assert Platform.SNES.value == "SNES"
    assert Platform.Nintendo_64.value == "Nintendo 64"
    assert Platform.GameCube.value == "GameCube"
    assert Platform.Wii.value == "Wii"
    assert Platform.Wii_U.value == "Wii U"
    assert Platform.Nintendo_Switch.value == "Nintendo Switch"
    assert Platform.Game_Boy.value == "Game Boy"
    assert Platform.Game_Boy_Color.value == "Game Boy Color"
    assert Platform.Game_Boy_Advance.value == "Game Boy Advance"
    assert Platform.Nintendo_DS.value == "Nintendo DS"
    assert Platform.Nindendo_DSi.value == "Nintendo DSi"
    assert Platform.Nintendo_3DS.value == "Nintendo 3DS"
    assert Platform.New_Nintendo_3DS.value == "New Nintendo 3DS"
    
def test_const_microsoft_platforms():
    assert Platform.Xbox.value == "Xbox"
    assert Platform.Xbox_360.value == "Xbox 360"
    assert Platform.Xbox_One.value == "Xbox One"
    assert Platform.Xbox_Series.value == "Xbox Series"
    
def test_const_res_immutable():
    with pytest.raises(AttributeError):
        Platform.Xbox_Series.value = "Xbox 720"