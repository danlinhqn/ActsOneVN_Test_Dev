import config
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "Son Moi",
    bootstrap_servers=config.kafka_ip,
    auto_offset_reset="earliest",
    group_id="consumer-group-a"
)

for message in consumer:
    print("Message:", message.value.decode('utf-8'))
    data = json.loads(message.value.decode('utf-8'))
    print("Data:", data)
    print("Name:", data["Name"])
    print("Age:", data["Age"])
    print("----")