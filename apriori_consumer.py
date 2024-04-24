from confluent_kafka import Consumer, KafkaError

def apriori_consumer():
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'apriori_group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe(['preprocessed_data_topic'])
    print('Apriori Consumer Subscribed successfully')

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
        print('Apriori Consumer - Received message: {}'.format(msg.value().decode('utf-8')))
    
    consumer.close()

# Run the consumer
apriori_consumer()

