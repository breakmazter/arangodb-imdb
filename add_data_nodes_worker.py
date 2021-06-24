import dramatiq

from actor_interface import should_retry, imdb_nodes


@dramatiq.actor(queue_name='josef_add_data_node_queue',
                max_retries=3, time_limit=180000, retry_when=should_retry)
def add_data_node(data: dict):
    del data['_rev']
    del data['_id']

    imdb_doc = imdb_nodes.createDocument(data)
    imdb_doc.save()

    print(f"{data['_key']} added to database!")
