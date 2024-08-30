import pika 


connection_parameters = pika.ConnectionParameters('localhost')  
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

queue = channel.queue_declare('letterbox')

channel.basic_consume(
    queue='letterbox',
    auto_ack=True,
    on_message_callback=lambda ch, method, properties, body: print(f"Received message: {body}"))

print("Starting Consuming")
channel.start_consuming()