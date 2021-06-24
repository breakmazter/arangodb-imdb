import dramatiq

from actor_interface import should_retry, imdb_edges


@dramatiq.actor(queue_name='josef_add_data_edge_queue',
                max_retries=3, time_limit=180000, retry_when=should_retry)
def add_data_edge(data: dict):
    del data['_rev']
    del data['_id']

    imdb_doc = imdb_edges.createDocument(data)
    imdb_doc.save()

    print(f"{data['_key']} added to database!")
