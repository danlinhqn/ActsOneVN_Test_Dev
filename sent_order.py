import config
from kafka import KafkaProducer
import json
from notify_client import *

# Use for sent order from client to Kafka
def sent_Order_From_Client():

    # List topics for user choose
    valid_topics = ["Clothing", "Cosmetics"]

    # Show list topic for user choose
    print("Please choose product type:")
    for i, topic in enumerate(valid_topics, 1):
        print(f"{i}. {topic}")

    # Choice topic
    choice = input("Select a topic by entering the corresponding number: ").strip()

    # Check after user choice
    try:
        choice_index = int(choice)
        if choice_index < 1 or choice_index > len(valid_topics):
            raise ValueError
    except ValueError:
        print("Wrong choice!")
        exit()

    # Choice topic base on user choice
    topic_name = valid_topics[choice_index - 1]

    # Declare KafkaProducer with the corresponding topic
    producer = KafkaProducer(
        bootstrap_servers=config.kafka_ip
    )

    # Input data from user
    t_shirt = input("Product's Name: ")
    client_name = input("Your Name: ")
    age = input("Qty Want Buy: ")

    # Create JSON object from user data
    data = {"Product's Name:": t_shirt, "Client's Name": client_name, "Qty": int(age)}
    json_data = json.dumps(data)

    # Send data to topic
    producer.send(topic_name, json_data.encode('utf-8'))

    # Flush data
    producer.flush()

    # Nofity to user after sent order step 1
    print("Order sent!, please wait for the confirmation from the Shop ...")

    # step 2, in here we will receive notify from shop to client
    receive_Notify_From_Shop_To_Client()
    
    print("$ ---------------------------------- $")
    print("Buy more, happy more :)")
    
# Use for run program
def run_program():
    while True:
        try:
            sent_Order_From_Client()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Retry in 15 seconds...")
            time.sleep(5)
            continue
        time.sleep(1)  # Wait for 1 second
        
# Run program
print("Begin order product in Shop ...")
run_program()