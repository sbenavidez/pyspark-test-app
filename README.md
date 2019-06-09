# pyspark-test-app

This is a pyspark application to test different transformation running on a dockerize spark or running on AWS EMR.


To run the dockerize Spark-Jupyter environment do:

git clone \
  --branch master --single-branch --depth 1 --no-tags \
  https://github.com/garystafford/pyspark-setup-demo.git

#deploy docker swarm service
docker stack deploy -c stack.yml pyspark

#check status
docker stack ps pyspark --no-trunc

#find url of jupyter notebook on boot log
docker logs $(docker ps | grep pyspark_pyspark | awk '{print $NF}')

#submit spark app 
$SPARK_HOME/bin/spark-submit xxxx.py
