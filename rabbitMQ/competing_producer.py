import pika 
import time
import random

connection_parameter = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameter)
channel = connection.channel()

queue = channel.queue_declare(queue='mutiple_consumers')

message_id = 1
while(True):
    message = f"Message ID: {message_id}"
    channel.basic_publish(exchange='', routing_key='mutiple_consumers', body=message)
    print(f"Sent message: {message}")
    message_id += 1
    time.sleep(random.randint(1, 2))

