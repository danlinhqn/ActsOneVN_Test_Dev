import config
from kafka import KafkaProducer
from kafka import KafkaConsumer
import json
from data_global import *

# Function to send notification from Shop to Client
def sent_Notify_From_Shop_To_Client():

    # Topic notify
    topic_name = "notify"

    # KafkaProducer "notify" topic
    producer = KafkaProducer(
        bootstrap_servers=config.kafka_ip
    )

    # In here have 2 case: Susscess and Fail
    if notify_For_Client[0] == 1:

        notify_Message = "The order has been successfully confirmed and is on its way for delivery."
        data = {"Notify Message:": notify_Message} 
    else: 
        notify_Message = "The order has not been confirmed, please try again."
        data = {"Notify Message:": notify_Message} 

    json_data = json.dumps(data)

    # Send data to the "notify" topic
    producer.send(topic_name, json_data.encode('utf-8'))
    
    # Flush data
    producer.flush()
    print("Sent Notify to the Client successfully!")

# Function to receive notification from Shop
def receive_Notify_From_Shop_To_Client():
    
    print("Waiting for notification from the Shop ...")
    
    # KafkaProducer "notify" topic receive
    consumer = KafkaConsumer(
        "notify",
        bootstrap_servers=config.kafka_ip,
        auto_offset_reset="earliest",
        group_id="notify-group"
    )

    # Get and show Notify from the Shop
    for message_Notify in consumer:
        try:
            message_data = json.loads(message_Notify.value.decode('utf-8'))
            notify_message = message_data['Notify Message:']
            print("Notify:", notify_message)

        except Exception as e: print(f"Error while processing order: {str(e)}")
        finally:
            consumer.commit()
            consumer.close()
                