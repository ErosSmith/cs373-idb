# Sofware Engineering
## CS373-Summer 2014
## Project: World Cup'14

Our group: CSID <br>
Aseal Yousuf aseal134 <br>
Eros Smith eros <br>
Jeremiah Hendrix Martinez jeremiah <br>
Jungmo Ku suhojm <br>
Kim Yu Ng kimyu92 <br>
Prithvi Shahi pshahi92 <br>


Project Site (PythonAnywhere)
Site:
1. [main](http://erossmith.pythonanywhere.com/)
2. [mirror](http://kimyu92.pythonanywhere.com/)

## Sturcture
Files : Path
> 1. *.py        /src/mv_landing
> 2. apiary.apib /
> 3. models.html /
> 4. Report.pdf  /
> 5. tests.out /
> 6. tests.py /world_cup/wc_app/


## Usage for model:
1. setup mysql environment and installation [ref](https://www.pythonanywhere.com/wiki/UsingMySQL)
2. create db scheme from mysql thru terminal [ref](http://stackoverflow.com/questions/22340875/creating-a-localhost-mysql-database-to-use-with-django)
3. grant user access to the db
4. configure the db settings on settings.py (world_cup)
5. create the designed model from model.py <br>
<code> python3 manage.py syncdb </code>
6. load required data with python scripts <br>
<code> python3 manage.py shell < country_insert.py </code><br>
  data: the "country_insert.py", "player_insert_script.py", "match_insert_script.py"
7. enjoy <br> 
   localhost:8000/admin <br>
<code> python3 manage.py runserver" </code>

## Test model
> preq: setup the model mentioned above <br>
> location: test_Model.py <br>
<code>python3 manage.py test</code>


## Dependencies
1. Python 3.4.1
2. Django 1.6.5
3. MySQL 5.5
4. Twitter Bootstrap
