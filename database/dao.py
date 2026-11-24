from database.DB_connect import DBConnect

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    def get_banche(self, e):
        db = DBConnect.get_connection()
        cursor = db.cursor()
        query = "SELECT * FROM banca"
        cursor.execute(query)

    def get_bonifichi(self, e):
        db = DBConnect.get_connection()
        cursor = db.cursor()
        query = "SELECT * FROM bonifico"
        cursor.execute(query)

    def get_filiale(self, e):
        db = DBConnect.get_connection()
        cursor = db.cursor()
        query = "SELECT * FROM filiale"
        cursor.execute(query)
    # TODO