
import pandas as pd 
df = pd.read_csv('planet_data.csv', index_col='eName')


class planet():   #instantiate like this: earth = planet("Earth", "blue", 3)
    def __init__(self,name, color = "blue", radius = 1):
        self.color = color
        self.radius = radius
        self.name = name
        self.moon_list = []
class moon():
    def __init__(self,name, color = "white", radius = 1, tidally_locked=False, planet_companion =None):
        self.name = name
        self.color = color
        self.radius = radius
        self.planet_companion = planet_companion
        self.tidally_locked = tidally_locked
    def update_planet(self, planet):
        planet.moon_list.append(self)


def print_largest(pl): #I did this whole thing for you - it selects the largest moon given a planet object 
    largest = None  #will be a moon type object
    for moon in pl.moon_list:
        if largest is None:
            largest = moon
        else:
            if largest.radius < moon.radius: largest = moon      
    if largest is not None:
        print(f"The largest moon of {pl.name} is {largest.name}")


# print(df[['isPlanet','meanRadius','orbit_type', 'orbits']])

d_planet = dict() #key: name of planet. value: planet object
d_moon = dict() #key: name of moon. value: moon object
for index, row in df.iterrows(): #get all the planets first
    if row['isPlanet'] is True:
        d_planet[index] = planet(name = index, radius = row['meanRadius'])

for index, row in df.iterrows(): #get all the planets first
    if row['isPlanet'] is False:
        d_moon[index] = moon(name = index, radius = row['meanRadius'], planet_companion = row['orbits'])



for key, val in d_planet.items():  #now we can check to see what is in our planet dictionary
    print(key, val.radius)

for key, val in d_moon.items(): #check that the planets got updated
    val.update_planet(d_planet[val.planet_companion])
    print(key, val.radius, val.planet_companion)

for key, val in d_planet.items():  #get the largest moon for each planet!
    print_largest(val) #sample output: The largest moon of Uranus is Titania
    print(key, [moon.name for moon in val.moon_list]) #sample output: Pluto ['Charon', 'Nix', 'Hydra', 'Kerberos', 'Styx']





