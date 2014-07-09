# Sofware Engineering
## Summer 2014 CS373 World Cup

our group: Aseal Yousuf, Eros Smith, Jeremiah Hendrix Martinez, Jungmo Ku, Kim Yu Ng, Prithvi Shahi

Project Site (PythonAnywhere)

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
5. "python3 manage.py syncdb" to create the designed model from model.py
6. "python3 manage.py shell < country_insert.py"
  6.5.the "country_insert.py", "player_insert_script.py", "match_insert_script.py"
7. "python3 manage.py runserver"


## Dependencies
1. Python 3.4.1
2. Django 1.6.5
3. MySQL 5.5
4. Twitter Bootstrap
