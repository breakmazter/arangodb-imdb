import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from dramatiq.middleware import TimeLimitExceeded
from dramatiq.results import Results
from dramatiq.results.backends import RedisBackend
from dramatiq.results.errors import ResultTimeout

from pyArango import connection

from settings import RABBITMQ_URL, REDIS_HOST, REDIS_PASSWORD, REDIS_PORT, ARANGO_URL, ARANGO_USERNAME, ARANGO_PASSWORD

result_backend = RedisBackend(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
broker = RabbitmqBroker(url=RABBITMQ_URL)
broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(broker)

connect = connection.Connection(arangoURL=ARANGO_URL,
                                username=ARANGO_USERNAME, password=ARANGO_PASSWORD)

db = connect['testdb']

imdb_nodes = db['imdb_vertices']
imdb_edges = db['imdb_edges']


def should_retry(retries_so_far, exception):
    return retries_so_far < 3 and not (isinstance(exception, TimeLimitExceeded) or isinstance(exception, ResultTimeout))


@dramatiq.actor(queue_name='josef_add_data_node_queue',
                max_retries=3, time_limit=180000, retry_when=should_retry)
def add_data_node(data: dict):
    pass


@dramatiq.actor(queue_name='josef_add_data_edge_queue',
                max_retries=3, time_limit=180000, retry_when=should_retry)
def add_data_edge(data: dict):
    pass
