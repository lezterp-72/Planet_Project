from planet_classes import *
def test_planet():
    earth = planet(name = "Earth", radius = 6371, color = "blue")
    assert earth.radius == 6371

def test_moon():
    luna = moon(name = "Luna", radius = 1737.4, color = "white",  tidally_locked = True)
    assert luna.tidally_locked == True

def test_moon_list():
    earth = planet(name = "Earth", radius = 6371, color = "blue")
    luna = moon(name = "Luna", radius = 1737.4, color = "white",  tidally_locked = True)
    luna.update_planet(earth)
    fake = moon(name = "He he ha ha", radius = 3, color = "Yellow", tidally_locked = True)
    fake.update_planet(earth)
    assert luna in earth.moon_list and fake in earth.moon_list



