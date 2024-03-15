# Tìm hiểu về Kafka cơ bản
* Có thể xem tại file này " Cơ Chế Cở Bản Kafka.png "

# Setup Kafka on Ubuntu 
* Can use Ubuntu 20.04 LTS for base
* Install Java
''' sudo apt update
sudo apt install default-jre
java -version '''

# Download and Install Kafka
mdkir ~/Downloads
curl "https://downloads.apache.org/kafka/2.8.0/kafka_2.13-2.8.0.tgz" -o ~/Downloads/kafka.tgz
mkdir ~/kafka && cd ~/kafka
tar -xvzf ~/Downloads/kafka.tgz --strip 1