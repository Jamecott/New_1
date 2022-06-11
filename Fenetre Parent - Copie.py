import sys

from PySide2.QtWidgets import *



class MenuBarDemo(QMainWindow):
        def __init__(self):
                super().__init__()
                self.setWindowTitle('MALTOM')
                self.resize(600, 500)

                self.menuBar = self.menuBar()

                fichierMenu = self.menuBar.addMenu('Fichier')
                editionMenu = self.menuBar.addMenu('Edition')
                affichageMenu = self.menuBar.addMenu('Affichage')
                fenetreMenu = self.menuBar.addMenu('fenetre')
                aideMenu = self.menuBar.addMenu('Aide')

                nouveau_action = QAction('Nouveau', self)
                fichierMenu.addAction(nouveau_action)
                nouveau_action.setShortcut('Ctrl+N')


                ouvrirMenu = fichierMenu.addMenu('Ouvrir...')

                enregistrer_action = QAction('Enregistrer', self)
                fichierMenu.addAction(enregistrer_action)
                enregistrer_action.setShortcut('Ctrl+S')

                enregistrersousMenu = fichierMenu.addMenu('Enregistrer sous...')

                imprimer_action = QAction('Imprimer', self)
                fichierMenu.addAction(imprimer_action)
                imprimer_action.setShortcut('Ctrl+P')

                quitter_action = QAction('Quitter', self)
                fichierMenu.addAction(quitter_action)
                quitter_action.setShortcut('Ctrl+Q')
                quitter_action.triggered.connect(lambda:QApplication.quit())

                undoDeleteMenu = editionMenu.addMenu('Undo delete')

                yes_action = QAction('Yes', self)
                no_action = QAction('No', self)
                undoDeleteMenu.addAction(yes_action)
                undoDeleteMenu.addAction(no_action)

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = MenuBarDemo()
	demo.show()

	sys.exit(app.exec_())
