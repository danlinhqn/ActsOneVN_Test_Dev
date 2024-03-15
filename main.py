from kafka import KafkaProducer, KafkaConsumer

# Thử kết nối với Kafka producer
try:
    producer = KafkaProducer(bootstrap_servers='192.168.1.7:9092')
    print("Kết nối thành công với Kafka producer!")
    producer.close()
except Exception as e:
    print("Lỗi khi kết nối với Kafka producer:", e)

# Thử kết nối với Kafka consumer
try:
    consumer = KafkaConsumer('test-topic', bootstrap_servers='localhost:9092', group_id='test-group')
    print("Kết nối thành công với Kafka consumer!")
    consumer.close()
except Exception as e:
    print("Lỗi khi kết nối với Kafka consumer:", e)
