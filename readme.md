https://realpython.com/flask-by-example-part-1-project-setup/#project-setup

to initialise env

. activate.sh


 1580  vi runtime.txt
 1581  heroku create wordcount-pro
 1582  heroku create wordcount-pro-sharper
 1583  heroku create wordcount-stage-sharper
 1584  git remote add pro git@heroku.com:wordcount-pro-sharper.git
 1585  git remote add stage git@heroku.com:wordcount-stage-sharper.git
