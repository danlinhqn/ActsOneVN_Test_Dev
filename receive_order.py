import config
from kafka import KafkaConsumer
import json
from common_logic import *
from notify_client import *
import time

# Get order information from Client
def receive_Order_From_Client():
    
    # Create Kafka consumer
    consumer = KafkaConsumer(
        "Clothing", "Cosmetics",
        # Use the IP address of the Kafka broker
        bootstrap_servers=config.kafka_ip,
        # Sử dụng earliest offset reset để đảm bảo consumer đọc từ offset sớm nhất trên partition ( vùng chứa dữ liệu độc lập trong Kafka. )
        # Use earliest offset reset to ensure the consumer reads from the earliest offset on the partition (an independent data container within Kafka).
        auto_offset_reset="earliest",
        # Tại vì đang dùng consumer group ở đầy là [ "Clothing", "Cosmetics" ] nên cần phải có group_id
        # Because a consumer group ["Clothing", "Cosmetics"] is being used here, a group_id is required.
        group_id="client_Group"
    )

    # Loop through messages from topics
    for order_Message in consumer:
        try:
            # Get JSON data from message
            order_Need_Processing = (json.loads(order_Message.value.decode('utf-8')))
            
            # Check if the topic is "Clothing", there will be a 30% discount
            if order_Message.topic == "Clothing":
                print("Clothing have Discount 30%:", order_Message.topic)
                order_Need_Processing["Discount"] = "30%"
                order_Need_Processing["Type"] = "Clothing"

            # Check if the topic is "Cosmetics", there will be a 5% discount
            if order_Message.topic == "Cosmetics":
                print("Cosmetics have Discount 5%:", order_Message.topic)
                order_Need_Processing["Discount"] = "5%"
                order_Need_Processing["Type"] = "Cosmetics"
            
            # Save order information to the database
            order_Data_Got = order_Need_Processing
            database_Save = os.path.join(os.path.dirname(__file__), 'database.json')
            check_And_Append_Database(order_Data_Got, database_Save)
            
            # Notify the client whether the order was successful or not
            sent_Notify_From_Shop_To_Client()

        except Exception as e: print(f"Error while processing order: {str(e)}")
        finally:
            consumer.commit()
            break 

    # Close consumer
    consumer.close()
    
    print("$ ---------------------------------- $")
    print("Wait for new order...")

# Use for run program
def run_program():
    while True:
        try:
            receive_Order_From_Client()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Retry in 15 seconds...")
            time.sleep(15)
            continue
        time.sleep(10)  # Wait for 10 seconds before processing the next order

# Run program
print("Wait for new order...")
run_program()