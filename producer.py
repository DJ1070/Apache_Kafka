#!/usr/bin/env python
from kafka import KafkaClient, SimpleProducer
import json,requests
from rockset import Client

#Rockset
rs = Client(api_server='api.rs2.usw2.rockset.com',
            api_key='4UXp24ceoewlfu59reP0icx49HH9IvDfDSYx6vsOCCa1hXS3NVJYFdRk9BhKaqgn')

# Creating Kafka client
kafka = KafkaClient('localhost:9092')

#Creating a Kafka producer instance
meetup_producer = SimpleProducer(kafka)

r = requests.get("https://stream.meetup.com/2/rsvps",stream=True)

# Sending messages to Consumer.
for line in r.iter_lines():
    meetup_producer.send_messages('meetup-stream',line)
    obj = json.loads(line.decode('utf-8'))
## printing the cities on console
    rsvps= (obj['group']['group_city'])
    print(rsvps)

kafka.close()