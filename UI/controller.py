import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_collegamenti(self, e):
        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """
        self._view.lista_visualizzazione.controls.clear()
        try:
            self._model.costruisci_grafo(int(self._view.importo_medio_minimo.value))
            numero_edges = self._model.get_num_edges()
            numero_nodes = self._model.get_num_nodes()
            risultato = self._model.get_all_edges()
            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di filiali: {numero_nodes}"))
            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di collegamenti: {numero_edges}"))
            i = 1
            for edge in risultato:
                self._view.lista_visualizzazione.controls.append(ft.Text(f"{i}) {edge[0]} <=> {edge[1]} || Importo medio per bonifico: {edge[2]["weight"]}"))
        except ValueError:
            self._view.show_alert("Inserire un numero")

        # TODO
