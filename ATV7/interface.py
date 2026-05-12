from  PySide6 import QtWidgets, QtCore

import sys
import random

class myWidget(QtWidgets.QWidget):
    def __init__(self, w, h):
        super().__init__()
        self.sorting_squares = ["Bubblesort", "Selectionsort", "Insertionsort"]
        self.sorting_linearithmics = ["Shellsort", "Mergesort", "QuickSort", "Heapsort"]
        self.files = ["nomes100k.txt", "nomes250k.txt", "nomes500k.txt", "nomes1m.txt"]
        self.groups = ["Bubblesort x Selection x Insertion", "Shellsort x Mergesort x Quicksort x Heapsort"]

        self.resize(w, h)
        self.setWindowTitle("Estatísticas de Ordenação")

        self.layout_w = QtWidgets.QHBoxLayout(self)
        self.layout_w.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_w.setSpacing(50)

        self.file_button = QtWidgets.QPushButton("Selecionar Arquivo")
        self.file_button.setFixedSize(200, 30)
        self.file_button.clicked.connect(self.choice_file)

        self.sort_button = QtWidgets.QPushButton("Métodos de Ordenação")
        self.sort_button.setFixedSize(200, 30)
        self.sort_button.clicked.connect(self.choice_group)
        
        self.layout_w.addWidget(self.file_button)
        self.layout_w.addWidget(self.sort_button)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

        self.setup_styles()

    def choice_file(self):
        Select_file_window = QtWidgets.QInputDialog(self)
        Select_file_window.setWindowTitle("seleção")
        Select_file_window.setLabelText("Escolha um arquivo para ordenar")
        Select_file_window.setComboBoxItems(self.files)
        Select_file_window.resize(400, 200)

        if Select_file_window.exec():
            file_name = Select_file_window.textValue()

            if file_name:
                print(file_name)

    def choice_group(self):
        grp, ok = QtWidgets.QInputDialog.getItem(
            self,
            "seleção",
            "escolha um grupo",
            self.groups,
            0,
            False
        )
        if not ok:
            return

        if grp == self.groups[0]:
            return self.choice_sorting_squares()
        elif grp == self.groups[1]:
            return self.choice_sorting_linearithmics()
            
    def choice_sorting_linearithmics(self):
        dialog = CheckBoxWindow("Algoritmos O(nlog(n))", self.sorting_linearithmics, self)
        dialog.resize(400, 100)

        if dialog.exec(): 
            choices = dialog.get_results()
            print(f"O usuário escolheu: {choices}")
        return choices
    
    def choice_sorting_squares(self):
        dialog = CheckBoxWindow("Algoritmos O(n^2)", self.sorting_squares, self)
        dialog.resize(400, 100)
        if dialog.exec(): 
            choices = dialog.get_results()
            print(f"O usuário escolheu: {choices}")
        return choices

    def setup_styles(self):
        self.setStyleSheet("""
            QWidget{
                background-color: #313131;
            }
            QPushButton{
                background-color: #800080;
                color: white;
                font-weight: bold;
                margin 200px 0;
            }  
            QLabel{
                color: white;
                font-size: 16px;
            }
                           
            QCheckBox{
                
                color: white;
                background-color: transparent;
            }
            QCheckBox::indicator{
                border: 2px solid #fdfdfd;
                background-color: #f0f0f0;
                border-radius: 4px;
            }
            QCheckBox::indicator:checked{
               background-color: #800080
            }
                           
            QInputDialog{
                background-color: #313131;
            }
            QInputDialog QComboBox {
                color: white; 
                background-color: #454545;
                selection-background-color: #800080;
            }
            QInputDialog QAbstractItemView {
                color: white;
                background-color: #313131;
                selection-background-color: #800080;
        }
        """)



class CheckBoxWindow(QtWidgets.QDialog):
    def __init__(self, title, itens, parent):
        super().__init__(parent)
        self.setWindowTitle(title)

        layout = QtWidgets.QVBoxLayout(self)
        
        self.label = QtWidgets.QLabel("Selecione os métodos para comparação")
        layout.addWidget(self.label)

        self.checkboxes = []
        for item in itens:
            cb = QtWidgets.QCheckBox(item)
            layout.addWidget(cb)
            self.checkboxes.append(cb)

        self.buttons = QtWidgets.QDialogButtonBox()

        # Adiciona à caixa dizendo qual a "função" de cada um (Accept ou Reject)
        self.buttons.addButton(QtWidgets.QDialogButtonBox.Ok)
        self.buttons.addButton(QtWidgets.QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        layout.addWidget(self.buttons)
    
    def get_results(self):
        return [cb.text() for cb in self.checkboxes if cb.isChecked()]


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    widget = myWidget(800, 400)
    widget.show()
    sys.exit(app.exec())