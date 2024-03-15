import config
from kafka import KafkaProducer
from kafka import KafkaConsumer
import json
from data_global import *

# Hàm gửi thông báo từ Shop đến Client
def sent_Notify_From_Shop_To_Client():
    
    #time.sleep(3) # Đợi 3 giây để gửi thông báo xong
    # Topic mới
    topic_name = "notify"

    # Khai báo KafkaProducer với topic "notify"
    producer = KafkaProducer(
        bootstrap_servers=config.kafka_ip
    )

    # Tại đây sẽ có 2 trường hợp khách hàng đặt hàng thành công và không thành công
    if notify_For_Client[0] == 1:

        notify_Message = "The order has been successfully confirmed and is on its way for delivery."
        data = {"Notify Message:": notify_Message} 
    else: 
        notify_Message = "The order has not been confirmed, please try again."
        data = {"Notify Message:": notify_Message} 

    json_data = json.dumps(data)
    # Gửi dữ liệu đến topic "notify"
    producer.send(topic_name, json_data.encode('utf-8'))
    # Flush dữ liệu
    producer.flush()
    print("Sent Notify to the Client successfully!")
    
# Hàm nhận thông báo từ Shop
def receive_Notify_From_Shop_To_Client():
    
    print("Waiting for notification from the Shop ...")
    
    # KafkaConsumer declaration with the "notify" topic
    consumer = KafkaConsumer(
        "notify",
        bootstrap_servers=config.kafka_ip,
        auto_offset_reset="earliest",
        group_id="notify-group"
    )

    # Process messages received from the "notify" topic
    for message_Notify in consumer:
        try:
            message_data = json.loads(message_Notify.value.decode('utf-8'))
            notify_message = message_data['Notify Message:']
            print("Notification received:", notify_message)

        except Exception as e:
            # Xử lý bất kỳ lỗi nào nếu có
            print(f"Error while processing order: {str(e)}")
        
        finally:
            # Xóa thông tin đã nhận được, sau khi đã xử lý xong
            consumer.commit()
            consumer.close()
                