Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> movies={1994:"Pulp Fiction",1997:"Seven",2000:"Cast Away",2006:"Blood Diamond"}
>>> movies
{2000: 'Cast Away', 1994: 'Pulp Fiction', 1997: 'Seven', 2006: 'Blood Diamond'}
>>> len(movies)
4
>>> movies.keys()
dict_keys([2000, 1994, 1997, 2006])
>>> movies.values()
dict_values(['Cast Away', 'Pulp Fiction', 'Seven', 'Blood Diamond'])
>>> new={1972:"The Godfather",1980:"Raging Bull",2004:"The Aviat"}
>>> new
{1980: 'Raging Bull', 1972: 'The Godfather', 2004: 'The Aviat'}
>>> movies.update(new)
>>> movies
{2000: 'Cast Away', 1972: 'The Godfather', 2006: 'Blood Diamond', 2004: 'The Aviat', 1994: 'Pulp Fiction', 1980: 'Raging Bull', 1997: 'Seven'}
>>> movies.clear()
>>> movies
{}
>>> 
