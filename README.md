### Basic Mechanism of Kafka
![Text Description](docs/Kafka.png)

### Setup Kafka on Ubuntu 
* Can use Ubuntu 20.04 LTS for base
* Install Java

```bash
root$ apt update
root$ apt install default-jre
# Check Version after setup
root$ java -version
```

# Cách 1 ------------------------------------------------- /

### Download and Install Kafka
```bash
root$ mkdir ~/Downloads
root$ curl "https://downloads.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz" -o ~/Downloads/kafka.tgz
root$ mkdir ~/kafka && cd ~/kafka
root$ tar -xvzf ~/Downloads/kafka.tgz --strip 1

# Edit Kafka config file
nano ~/kafka/config/server.properties
# Add this line in the end of the file, for can delete topic
detete.topic.enable = true
# remove comment in this line "listeners=PLAINTEXT://:9092" to "listeners=PLAINTEXT://localhost:9092"
# remove comment in this line "advertised.listeners=PLAINTEXT://your.host:9092"  to "advertised.listeners=PLAINTEXT://localhost:9092"  
# Also can check the line have : "log.dirs=/tmp/kafka-logs" and can change the location for save Logs
```
### Setup Zookeeper
```bash
nano /etc/systemd/system/zookeeper.service
```
### Use this Content for Setup Zookeeper
```bash
[Unit]
Requires=network.target remote-fs.target
After=network.target remote-fs.target

[Service]
Type=simple
User=kafka
ExecStart=/home/kafka/kafka/bin/zookeeper-server-start.sh /home/kafka/kafka/config/zookeeper.properties
ExecStop=/home/kafka/kafka/bin/zookeeper-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```
### Begin Start Kafka

systemctl start kafka

# Start the ZooKeeper service in 1 Terminal
root$ cd ~/kafka 
root$ bin/zookeeper-server-start.sh config/zookeeper.properties

# Start the Kafka broker service in another Terminal
root$ cd ~/kafka 
root$ bin/kafka-server-start.sh config/server.properties

# Cách 2 -------------------

Using docker image
Get the docker image

$ docker pull apache/kafka:3.7.0
Start the kafka docker container

$ docker run -p 9092:9092 apache/kafka:3.7.0
Once the Kafka server has successfully launched, you will have a basic Kafka environment running and ready to use.

### Lỗi gặp phải khi làm 15.04.2024
* Có gặp trường hợp Server Kafka bị lỗi phần log, khắc phúc bằng cách xóa thư mục log và chạy lại
* thư mục Log tại đây: /tmp/kafka-logs

ssh root@192.168.1.7
cd /mnt/c/Users/ad/Desktop/AtcsOneVN_Test_Dev
