from enum import Enum


class Query(Enum):
    # 1. Get all data or batch data.
    GET_ALL_DATA = """
    WITH imdb_vertices
        FOR n IN imdb_vertices
            LIMIT @batch_size
            RETURN n
        """

    # 2. Get all movie with genre "Drama" and runtime >= n
    GET_MOVIE = """
    WITH imdb_vertices
        FOR n IN imdb_vertices
            FILTER n.type == 'Movie'
            FILTER n.genre == @genre AND n.runtime >= @runtime
            LIMIT @batch_size
            RETURN n
        """

    # 3. Get top movie with title and genre "Drama" and runtime >= n
    GET_TOP_MOVIE = """   
        WITH imdb_vertices
        FOR n IN imdb_vertices
            FILTER n.type == 'Movie'
            FILTER n.genre == @genre AND n.runtime >= @runtime
            SORT n.title
            LIMIT @batch_size
            RETURN n.title
        """

    # 4. Find all the movies that Will Smith has acted in
    GET_MOVIE4ACTOR = """
    WITH imdb_vertices
        FOR actor IN imdb_vertices 
            FILTER actor.name == 'Will Smith'
            FOR vertex, edge, path IN 1..1 OUTBOUND actor GRAPH 'IMDB'
                FILTER path.vertices[1].type == 'Movie' 
                RETURN DISTINCT vertex.title
        """

    # 5. Find all the movies directed by James Cameron and then list the associated actors for those movies.
    GET_ALL_ACTOR4DIRECT = """
    WITH imdb_vertices
        FOR director IN imdb_vertices
            FILTER director.name == "James Cameron"
            LIMIT 1
            FOR vertex, edge, path IN 1..1 OUTBOUND director GRAPH "IMDB"
                FILTER path.edges[*].`$label` ALL == 'DIRECTED'
                    FOR vertex2, edge2, path2 IN 1..1 INBOUND vertex GRAPH "IMDB"
                        FILTER path2.edges[*].`$label` ALL == 'ACTS_IN'
                        RETURN DISTINCT vertex2.name
        """

    # 6. Get all actor with relation actor
    GET_RELATION_ACTOR = """
    WITH imdb_vertices
        FOR actor IN imdb_vertices
            FILTER actor.name == 'Keanu Reeves'
            FOR vertex, edge, path IN 1..3 ANY actor GRAPH "IMDB"
                PRUNE path.vertices[*].genre ALL == "Action"
                FILTER vertex.genre == "Action"
                FILTER path.vertices[*]._key ALL != "action"
                FILTER path.vertices[2].name != null
                LIMIT 100
                RETURN DISTINCT path.vertices[2].name
        """

    # 7. Get count documents in collection
    GET_COUNT_SLOW = """
    WITH imdb_vertices
        RETURN LENGTH(imdb_vertices)
        """

    GET_COUNT_FAST = """
    WITH imdb_vertices
        FOR doc IN imdb_vertices
            COLLECT WITH COUNT INTO length
            RETURN length
        """