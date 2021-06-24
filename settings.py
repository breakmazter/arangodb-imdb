########################
# CONFIGS FOR RABBITMQ #
########################

RABBITMQ_HOST = '34.145.90.213'
RABBITMQ_PORT = 5672
RABBITMQ_VHOST = ''
RABBITMQ_LOGIN = 'user'
RABBITMQ_PASSWORD = '12JqEf2T5Fn6QZCF'

RABBITMQ_URL = f'''amqp://{RABBITMQ_LOGIN}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}'''

#####################
# CONFIGS FOR REDIS #
#####################

REDIS_HOST = '35.247.62.69'
REDIS_PORT = 6379
REDIS_USERNAME = 'user'
REDIS_PASSWORD = 'LYWxyNDJSg7h'

######################
# CONFIGS FOR ARANGO #
######################

ARANGO_HOST = '34.134.76.229'
ARANGO_PORT = 8529
ARANGO_USERNAME = 'root'
ARANGO_PASSWORD = 'fa22qge3'

ARANGO_URL = f'http://{ARANGO_HOST}:{ARANGO_PORT}'


################
# PATH TO DATA #
################

PATH_TO_DATA_NODE = 'data/json_data/imdb_vertices.data.json'
PATH_TO_DATA_EDGE = 'data/json_data/imdb_edges.data.json'
