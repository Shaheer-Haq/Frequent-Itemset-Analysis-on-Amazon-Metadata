# Frequent-Itemset-Analysis-on-Amazon-Metadata
## Introduction
This report outlines the development of a basic tool to analyze the frequent itemsets on Amazon's MetaData. This repository contains the code files including data preprocessing, Kafka Integration with one producer and three consumers (each with a seperate Algorithm), and MongoDB integration. Below is a brief overview of each file and its purpose.

#Files:
## 1. preprocess.py:
This script preprocesses the raw data stored in a JSON file, converting string values to uppercase. It then writes the preprocessed data to another JSON file.

## 2. kafka_producer.py: 
This script reads the preprocessed data from the JSON file and produces it to a Kafka topic named 'preprocessed_data_topic'.

## 3. apriori_consumer.py: 
This script implements a Kafka consumer for the Apriori algorithm. It subscribes to the 'preprocessed_data_topic' and processes incoming messages.

## 4. pcy_consumer.py: 
Similar to 'apriori_consumer.py', this script implements a Kafka consumer for the PCY (Park-Chen-Yu) algorithm.

## 5. 3rd_consumer.py: 
This script implements a Kafka consumer for the k-Means algorithm. It receives preprocessed data and performs clustering using the streaming approach.

## 6. mongodb_integration.py: 
This script continuously sends preprocessed data to a MongoDB database.

## 7. start_services.sh: 
This bash script automates the process of starting Zookeeper, Kafka Server, Kafka Producer, Kafka Consumers, and MongoDB integration.

# Instructions:
To run the assignment:

1. Make sure you have Kafka and MongoDB installed and running on your system.
2. Run the 'start_services.sh' script to start all necessary services.
3. Ensure that the input data file is present in the specified path (/media/shaheer/New Volume/Sampled_amazon_Meta.json).
4. Execute each Python script ('preprocess.py', 'kafka_producer.py', 'apriori_consumer.py', 'pcy_consumer.py', '3rd_Consumer.py', 'mongodb_integration.py') in separate terminals or as background processes.

# Notes:

1. Adjust file paths and configurations in the scripts as needed to match your environment.
2. Make sure to install required Python packages using 'pip install -r requirements.txt'.
3. You may need to modify Kafka and MongoDB connection configurations based on your setup.

# Conclusion:

This repository provides a comprehensive solution for data preprocessing, streaming to Kafka, and integration with MongoDB. The included scripts automate the data pre-processing, message production, and consumption by various algorithms (Apriori, PCY, k-Means), as well as continuous data storage in MongoDB.

By following the instructions and customizing configurations as needed, you can leverage this codebase to perform real-time analytics on your data streams.

# Contributors:

1. Moeez Ahmed Khan: 21i-1694
2. Meeran Ali: 21i-1743
3. Shaheer-E-Haq: 21i-1657
