import sqlite3


class DBAccessor():
    def __init__(self, db_name):
        self.__conn = sqlite3.connect(db_name)

    def all_customer_report(self):
        """The list of all customers and their representatives as specified in README"""
        query = 'SELECT * FROM customer'
        return self.execute_query(query)

    def all_genre_names(self):
        """ List of all genre names to populate the combo box as specified in README"""
        query = "SELECT Name FROM Genre ORDER BY Name"
        return self.execute_query(query)

    def all_genre_all(self):
        """ List of all genre names to populate the combo box as specified in README"""
        query = "SELECT * FROM Genre"
        return self.execute_query(query)

    def track_info_by_genre(self, genre):
        """ List of tracks including name, album title, artist, and unit price as specified in README"""
        result = "1"
        for tuple in self.all_genre_all():
            if tuple[1] == genre:
                result = str(tuple[0])

        query = "SELECT Name, AlbumId, Composer, UnitPrice FROM Track WHERE GenreId=" + result
        return self.execute_query(query)

    def execute_query(self, query):
        cursor = self.__conn.cursor()
        cursor.execute(query)
        result_set = cursor.fetchall()
        # the column headers are here:
        col_names = next(zip(*cursor.description))
        cursor.close()
        return [col_names] + result_set
