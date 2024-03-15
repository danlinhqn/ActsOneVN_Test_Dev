import config
from kafka import KafkaConsumer
import json
from common_logic import *
from notify_client import *

# Khởi tạo Kafka consumer
consumer = KafkaConsumer(
    "Clothing", "Cosmetics",
    # Sử dụng địa chỉ IP của Kafka broker
    bootstrap_servers=config.kafka_ip,
    # Sử dụng earliest offset reset để đảm bảo consumer đọc từ offset sớm nhất trên partition ( vùng chứa dữ liệu độc lập trong Kafka. )
    auto_offset_reset="earliest",
    # Tại vì đang dùng consumer group ở đầy là [ "Clothing", "Cosmetics" ] nên cần phải có group_id
    group_id="client_Group"
)

# Lặp qua các tin nhắn từ các topic
for message in consumer:
    try:
        # Kiểm tra nếu topic là "Clothing", sẽ có discount 30%
        if message.topic == "Clothing":
            print("Clothing have Discount 30%:", message.topic)
            
        # Kiểm tra nếu topic là "Cosmetics", sẽ có discount 5%
        if message.topic == "Cosmetics":
            print("Cosmetics have Discount 5%:", message.topic)
            
        # Xử lý dữ liệu ở đây, thêm các điều kiện xử lý để có thể trả về thông tin cụ thể
        order_Need_Processing = (json.loads(message.value.decode('utf-8')))
        
        order_Data_Got = order_Need_Processing
      
        database_Save = os.path.join(os.path.dirname(__file__), 'database.json')
        check_And_Append_Database(order_Data_Got, database_Save)
        
        # Thông báo ra cho client đặt hàng thành công hay không thành công
        sent_Notify_From_Shop_To_Client()

    except Exception as e:
        # Xử lý bất kỳ lỗi nào nếu có
        print(f"Error while processing order: {str(e)}")
    finally:
        # Xóa thông tin đã nhận được, sau khi đã xử lý xong
        consumer.commit()
        break 
    
# Đóng consumer
consumer.close()
