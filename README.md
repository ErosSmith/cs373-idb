# Sofware Engineering
## CS373-Summer 2014
## Project: World Cup'14

Our group: Aseal Yousuf, Eros Smith, Jeremiah Hendrix Martinez, Jungmo Ku, Kim Yu Ng, Prithvi Shahi

Project Site (PythonAnywhere)
Site:
1. [main](http://erossmith.pythonanywhere.com/)
2. [mirror](http://kimyu92.pythonanywhere.com/)

## Sturcture
Files : Path
> 1. *.py        /src/mv_landing
> 2. apiary.apib /
> 3. models.html /world_cup/wc_app
> 4. Report.pdf  /world_cup/
> 5. tests.out
> 6. tests.py


## Usage for model:
1. setup mysql environment and installation [ref](https://www.pythonanywhere.com/wiki/UsingMySQL)
2. create db scheme from mysql thru terminal [ref](http://stackoverflow.com/questions/22340875/creating-a-localhost-mysql-database-to-use-with-django)
3. grant user access to the db
4. configure the db settings on settings.py (world_cup)
5. to create the designed model from model.py <br>
> python3 manage.py syncdb
6. to load required data with python scripts <br>
> python3 manage.py shell < country_insert.py
  data: the "country_insert.py", "player_insert_script.py", "match_insert_script.py"
7. enjoy =) localhost:8000/admin <br>
> python3 manage.py runserver"


## Dependencies
1. Python 3.4.1
2. Django 1.6.5
3. MySQL 5.5
4. Twitter Bootstrap
