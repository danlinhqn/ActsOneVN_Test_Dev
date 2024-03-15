import json
import os
from data_global import *

def check_And_Append_Database(order_Data, database_File):
    try:
        # Đọc dữ liệu từ file database.json
        with open(database_File, 'r', encoding='utf-8') as file:
            database = json.load(file)
    except FileNotFoundError:
        # Nếu file không tồn tại, tạo một dictionary trống
        database = {}

    # Kiểm tra xem dữ liệu đã tồn tại trong database hay chưa
    if order_Data not in database.values():
        # Nếu không tồn tại, thêm dữ liệu vào database
        database[len(database) + 1] = order_Data
        
        # Ghi dữ liệu mới vào file database.json
        with open(database_File, 'w', encoding='utf-8') as file:
            
            # Sử dụng indent=4 để ghi dữ liệu vào file theo định dạng đẹp
            json.dump(database, file, indent=4) 
            
        # Đặt hàng thành công
        notify_For_Client.insert(0,1)
        print("Data imported successfully.")
    else:
        
        # Đặt hàng không thành công
        notify_For_Client.insert(0,2)
        print("Data already exists in the database.")
