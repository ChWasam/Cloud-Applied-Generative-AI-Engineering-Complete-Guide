#! /bin/bash


/opt/kafka/bin/kafka-topics.sh --create --topic order --bootstrap-server broker:9092

# Event jo create karna ha wo order ka nam ka ho ga 
# localhost ke jagha broker ai ga 
#  aur broker container ka nam ha (DNS wala concept )

#  broker DNS sa nikal la ga aur 9092  calling kar lai ga 
