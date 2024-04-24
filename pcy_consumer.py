from confluent_kafka import Consumer, KafkaError

def pcy_consumer():
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'pcy_group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe(['preprocessed_data_topic'])
    print('PCY Consumer Subscribed successfully')

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
        print('PCY Consumer - Received message: {}'.format(msg.value().decode('utf-8')))
    
    consumer.close()

# Run the consumer
pcy_consumer()

