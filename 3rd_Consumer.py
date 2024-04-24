from confluent_kafka import Consumer, KafkaError
import numpy as np

# Function to calculate distance between two points
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Function to update cluster centroids based on new data point
def update_centroids(centroids, data_point, learning_rate):
    nearest_centroid_idx = np.argmin([euclidean_distance(data_point, centroid) for centroid in centroids])
    centroids[nearest_centroid_idx] += learning_rate * (data_point - centroids[nearest_centroid_idx])
    return centroids

# Kafka consumer setup
def streaming_consumer():
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'streaming_group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe(['preprocessed_data_topic'])
    print('Streaming Consumer Subscribed successfully')

    # Initialize cluster centroids randomly
    num_clusters = 3
    data_dim = 2
    centroids = np.random.rand(num_clusters, data_dim)

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            
            # Process incoming data point
            data_point = np.frombuffer(msg.value(), dtype=float)
            nearest_centroid_idx = np.argmin([euclidean_distance(data_point, centroid) for centroid in centroids])
            centroids = update_centroids(centroids, data_point, learning_rate=0.1)
            
            # Periodically output or store the updated cluster centroids
            if msg.offset() % 100 == 0:
                print("Updated cluster centroids:", centroids)
    
    except KeyboardInterrupt:
        pass
    
    finally:
        # Close Kafka consumer
        consumer.close()

# Run the consumer
streaming_consumer()

