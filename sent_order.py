import config
from kafka import KafkaProducer
import json
from notify_client import *

# Hàm này sẽ gửi thông tin đặt hàng từ Client lên Kafka
def sent_Order_From_Client():
    # Danh sách các topic tùy chọn
    valid_topics = ["Clothing", "Cosmetics"]

    # Hiển thị danh sách tùy chọn cho người dùng
    print("Please choose product type:")
    for i, topic in enumerate(valid_topics, 1):
        print(f"{i}. {topic}")

    # Yêu cầu người dùng chọn một topic
    choice = input("Select a topic by entering the corresponding number: ").strip()

    # Kiểm tra xem lựa chọn có hợp lệ không
    try:
        choice_index = int(choice)
        if choice_index < 1 or choice_index > len(valid_topics):
            raise ValueError
    except ValueError:
        print("Wrong choice!")
        exit()

    # Chọn topic dựa trên lựa chọn của người dùng
    topic_name = valid_topics[choice_index - 1]

    # Khai báo KafkaProducer với topic tương ứng
    producer = KafkaProducer(
        bootstrap_servers=config.kafka_ip
    )

    # Nhập dữ liệu từ người dùng
    t_shirt = input("Product's Name: ")
    client_name = input("Your Name: ")
    age = input("Qty Want Buy: ")

    # Tạo đối tượng JSON từ dữ liệu người dùng
    data = {"Product's Name:": t_shirt, "Client's Name": client_name, "Qty": int(age)}
    json_data = json.dumps(data)

    # Gửi dữ liệu đến topic
    producer.send(topic_name, json_data.encode('utf-8'))
    # Flush dữ liệu
    producer.flush()

    # Thông báo ngay khi đặt hàng xong bước 1
    print("Order sent!, please wait for the confirmation from the Shop ...")

    # Tại đây sẽ chạy file nhận thông báo từ Shop
    receive_Notify_From_Shop_To_Client()
    
    print("$ ---------------------------------- $")
    print("Buy more, happy more :)")
    
# Hàm chạy chương trình
def run_program():
    while True:
        try:
            sent_Order_From_Client()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Retry in 15 seconds...")
            time.sleep(5)
            continue
        time.sleep(1)  # Chờ 10 giấy trước khi chạy lại
        
# Chạy chương trình
print("Begin order product in Shop ...")
run_program()