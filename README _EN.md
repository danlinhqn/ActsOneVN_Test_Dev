### Tìm hiểu về Kafka cơ bản
* Có thể xem tại file này " Cơ Chế Cở Bản Kafka.png "

### Setup Kafka on Ubuntu 
* Can use Ubuntu 20.04 LTS for base
* Install Java

```bash
root$ sudo apt update
root$ sudo apt install default-jre
root$ java -version
```

### Download and Install Kafka
```bash
root$ mdkir ~/Downloads
root$ curl "https://downloads.apache.org/kafka/2.8.0/kafka_2.13-2.8.0.tgz" -o ~/Downloads/kafka.tgz
root$ mkdir ~/kafka && cd ~/kafka
root$ tar -xvzf ~/Downloads/kafka.tgz --strip 1
```
