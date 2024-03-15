import config
from kafka import KafkaProducer
import json

topic_Name = "Son Moi"
producer = KafkaProducer(
    bootstrap_servers=config.kafka_ip
    )

json_data = json.dumps({"Name": "John", "Age": 30})

producer.send(topic_Name, json_data.encode('utf-8'))
producer.flush()

print("Message sent to Kafka Topic", topic_Name)