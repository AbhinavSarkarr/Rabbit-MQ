import pika 
import time
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def on_message_recieved(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f"Received message: {body}, will take {processing_time} to process")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Finished processing message")


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='mutiple_consumers', on_message_callback=on_message_recieved)
print("Starting Consuming")
channel.start_consuming()
