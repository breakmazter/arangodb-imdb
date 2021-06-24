from actor_interface import db
from query_data import Query


#############
# READ DATA #
#############

def get_all_data(batch_size: int):
    bindVars = {
        'batch_size': batch_size,
    }

    query_result = db.AQLQuery(Query.GET_ALL_DATA.value, bindVars=bindVars, rawResults=True)

    for document in query_result:
        print(document)


def get_all_data_with_filter(genre: str, runtime: int, batch_size: int):
    bindVars = {
        'batch_size': batch_size,
        'genre': genre,
        'runtime': runtime,
    }

    query_result = db.AQLQuery(Query.GET_MOVIE.value, bindVars=bindVars, rawResults=True)

    for document in query_result:
        print(document)


def get_top_movie(genre: str, runtime: int, batch_size: int):
    bindVars = {
        'batch_size': batch_size,
        'genre': genre,
        'runtime': runtime,
    }

    query_result = db.AQLQuery(Query.GET_TOP_ACC.value, bindVars=bindVars, rawResults=True)

    for document in query_result:
        print(document)


###################
# GRAPH OPERATION #
###################

def find_all_movie4actor():
    query_result = db.AQLQuery(Query.GET_MOVIE4ACTOR.value, rawResults=True)

    for document in query_result:
        print(document)


def find_all_actor4director():
    query_result = db.AQLQuery(Query.GET_ALL_ACTOR4DIRECT.value, rawResults=True)

    for document in query_result:
        print(document)


def query_graph():
    query_result = db.AQLQuery(Query.GET_COUNT_SLOW.value, rawResults=True)

    for document in query_result:
        print(document)


if __name__ == "__main__":
    query_graph()
