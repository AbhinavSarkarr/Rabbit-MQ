import pika 

connection_parameter = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()


channel.queue_declare(queue='letterbox')

def callback(ch, method, properties, body):
    print("Received in letterbox")
    print(body)

message = "Hello from publisher"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"Sent message: {message}")

connection.close()