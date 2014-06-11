import pika


def get_dev_channel(vhost):
    params = pika.ConnectionParameters(host='platform-rabbitmq-001.1515.mtvi.com',
                                       port=5672,
                                       virtual_host=vhost,
                                       credentials=get_dev_creds())
    connection = pika.BlockingConnection(params)
    return connection.channel()


def get_dev_creds():
    credentials = pika.PlainCredentials('rabbitadmin', 'R@bb1t@dm1n')
    return credentials
