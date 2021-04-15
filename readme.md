https://realpython.com/flask-by-example-part-1-project-setup/#project-setup

to initialise env

. activate.sh



export APP_SETTINGS="config.DevelopmentConfig"


 1580  vi runtime.txt
 1581  heroku create wordcount-pro
 1582  heroku create wordcount-pro-sharper
 1583  heroku create wordcount-stage-sharper
 1584  git remote add pro git@heroku.com:wordcount-pro-sharper.git
 1585  git remote add stage git@heroku.com:wordcount-stage-sharper.git


push to staging or prod


     git push stage master

     git push pro master


     https://wordcount-stage-sharper.herokuapp.com/

     https://wordcount-pro-sharper.herokuapp.com/




     heroku config:set APP_SETTINGS=config.StagingConfig --remote stage

     heroku config:set APP_SETTINGS=config.ProductionConfig --remote pro