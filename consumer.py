#!/usr/bin/env python

from kafka import KafkaConsumer
import json

# Subscribing a consumer to listen to topic 'meetup-stream'
meetup_consumer = KafkaConsumer('meetup-stream', group_id = '1', bootstrap_servers = ['localhost:9092'])

# Printing it for verification
for message in meetup_consumer:
	print (message.value)