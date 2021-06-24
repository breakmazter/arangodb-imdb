import json

from actor_interface import add_data_node, add_data_edge
from settings import PATH_TO_DATA_NODE, PATH_TO_DATA_EDGE


def get_data():
    with open(PATH_TO_DATA_NODE, 'r') as read_obj_nodes, open(PATH_TO_DATA_EDGE, 'r') as read_obj_edges:

        for node in read_obj_nodes:
            res = json.loads(node)
            add_data_node.send(res['data'])

        print(f"All nodes loaded to database!!!")

        for edge in read_obj_edges:
            res = json.loads(edge)
            add_data_edge.send(res['data'])

        print(f"All edges loaded to database!!!")


if __name__ == "__main__":
    get_data()
