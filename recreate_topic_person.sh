#!/bin/sh

/opt/kafka_2.12-1.1.0/bin/kafka-topics.sh --delete --zookeeper localhost:2181 --topic person
/opt/kafka_2.12-1.1.0/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic person