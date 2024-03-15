import config
from kafka import KafkaProducer
from kafka import KafkaConsumer
import json
from data_global import *


def sent_Notify_From_Shop_To_Client():
    
    # Topic mới
    topic_name = "notify"

    # Khai báo KafkaProducer với topic "notify"
    producer = KafkaProducer(
        bootstrap_servers=config.kafka_ip
    )

    # Tại đây sẽ có 2 trường hợp khách hàng đặt hàng thành công và không thành công
    if notify_for_client[0] == 1:
        data = {"The order has been successfully confirmed and is on its way for delivery."} 
    else: 
        data = {"The order has not been confirmed, please try again."}

    json_data = json.dumps(data)
    # Gửi dữ liệu đến topic "notify"
    producer.send(topic_name, json_data.encode('utf-8'))
    # Flush dữ liệu
    producer.flush()
    

def receive_Notify_From_Shop_To_Client():
    # Topic to subscribe to
    topic_name = "notify"

    # KafkaConsumer declaration with the "notify" topic
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=config.kafka_ip,
        auto_offset_reset="earliest",
        group_id="notify-group"
    )

    # Process messages received from the "notify" topic
    for message in consumer:
        message_data = json.loads(message.value.decode('utf-8'))
        print("Notification received:", message_data)

    # Close the consumer
    consumer.close()


sent_Notify_From_Shop_To_Client()

receive_Notify_From_Shop_To_Client()