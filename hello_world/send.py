import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('172.18.0.2'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello world!')

print("[x] Send 'Hello World!'")
connection.close()
