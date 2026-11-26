from database.DB_connect import DBConnect
from model.filiale import Filiale
from model.bonifico import Bonifico
from model.banca import Banca

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    @staticmethod
    def get_banche():
        db = DBConnect.get_connection()
        cursor = db.cursor()
        query = "SELECT * FROM banca"
        cursor.execute(query)

    @staticmethod
    def get_bonifichi(soglia):
        db = DBConnect.get_connection()
        cursor = db.cursor()
        query = f"SELECT id_filiale_origine, id_filiale_destinazione, avg(importo) as m FROM bonifico GROUP BY id_filiale_origine, id_filiale_destinazione HAVING avg(importo) >= {soglia}"
        cursor.execute(query)
        risultato = []
        for riga in cursor.fetchall():
            bonifico = [riga[0], riga[1], riga[2]]
            risultato.append(bonifico)
        return risultato


    @staticmethod
    def get_filiali():
        db = DBConnect.get_connection()
        cursor = db.cursor()
        query = "SELECT * FROM filiale"
        cursor.execute(query)
        risultato = {}
        for elemento in cursor.fetchall():
            filiale = Filiale(
            id = elemento[0],
            codice = elemento[1],
            nome = elemento[2],
            citta = elemento[3],
            provincia = elemento[4],
            latitudine = elemento[5],
            longitudine = elemento[6]
            )
            risultato[filiale.id] = filiale
        return risultato
