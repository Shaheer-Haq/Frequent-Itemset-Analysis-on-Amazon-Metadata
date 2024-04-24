#!/bin/bash

# Start Zookeeper
gnome-terminal -- zookeeper-server-start.sh /home/shaheer/Downloads/kafka/config/zookeeper.properties &

sleep 5

# Start Kafka Server
gnome-terminal -- kafka-server-start.sh /home/shaheer/Downloads/kafka/config/server.properties &

sleep 10

# Preprocess data
#python preprocess.py

# Start Kafka Producer
python kafka_producer.py &

# Start Kafka Consumer (Apriori Algorithm)
python apriori_consumer.py &

# Start Kafka Consumer (PCY Algorithm)
python pcy_consumer.py &

# Start Kafka Consumer (k-Means Algorithm)
python 3rd_Consumer.py &

# Start MongoDB Integration
python mongodb_integration.py &

