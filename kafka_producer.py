from confluent_kafka import Producer
import json
import subprocess

def produce_data(producer, topic, data):
    producer.produce(topic, value=data)
    producer.flush()

# Kafka producer setup
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# Load preprocessed data from JSON file
with open('preprocessed_data.json', 'r') as f:
    preprocessed_data = json.load(f)

# Produce preprocessed data to Kafka topic
produce_data(producer, 'preprocessed_data_topic', json.dumps(preprocessed_data))

# Create Kafka topic
topic_creation_command = "/home/shaheer/Downloads/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic preprocessed_data_topic"
subprocess.run(topic_creation_command, shell=True)

