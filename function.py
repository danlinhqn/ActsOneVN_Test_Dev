from flask import Flask, request, jsonify
from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads

app = Flask(__name__)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

@app.route('/order', methods=['POST'])

# Hàm nhận đơn hàng
def get_Order():
    order_data = request.json
    producer.send('orders', value=order_data)
    return jsonify({'message': 'Order received'}), 200

def process_orders():
    consumer = KafkaConsumer('orders',
                             bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             group_id='my-group',
                             value_deserializer=lambda x: loads(x.decode('utf-8')))

    for message in consumer:
        order_data = message.value
        # Process and store the order in the database
        # Implement error handling for failures and retries