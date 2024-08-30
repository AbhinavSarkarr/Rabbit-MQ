import pika 
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)


message = "message broadcast through pubsub"

while(True):
    channel.basic_publish(exchange='pubsub', routing_key='', body=message)

    print(f"sent message: {message}")

    #channel.close()

