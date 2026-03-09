import sys
from db import get_hierarchy
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QMenu, QAbstractItemView

from tree_builder import build_tree
from tree_model import build_model, add_node
from PyQt5.QtCore import Qt

from node import Node

class MainWindow(QMainWindow):
    def __init__(self, model):
        super().__init__()

        self.setWindowTitle("Hieraarchy view")
        self.resize(640, 480)

        self.tree = QTreeView()
        self.tree.setModel(model)
        self.setCentralWidget(self.tree)
        self.tree.expandAll()

        self.tree.setEditTriggers(
            QTreeView.DoubleClicked |
            QTreeView.EditKeyPressed
        )

        model.itemChanged.connect(self.on_item_changed)

        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.open_menu)
    
    def on_item_changed(self, item):
        node = item.data(Qt.UserRole)
        new_name = item.text()
        node.name = new_name

    def open_menu(self, position):
    
        index = self.tree.indexAt(position)
        item = self.tree.model().itemFromIndex(index)

        if not index.isValid():
            return

        menu = QMenu()
        add_action = menu.addAction("Добавить дочерний элемент")
        action = menu.exec_(self.tree.viewport().mapToGlobal(position))

        if action == add_action:
            self.add_child(item)

    def add_child(self, parent_item):
        parent_node = parent_item.data(Qt.UserRole)
        row = {
            "id": None,
            "id_parent": parent_node.id,
            "name": "Новый элемент",
            "state": 1,
            "image": None
        }
        new_node = Node(row)
        parent_node.children.append(new_node)
        add_node(self.tree.model(), parent_item, new_node)
        index = parent_item.child(parent_item.rowCount()-1).index()
        self.tree.setCurrentIndex(index)
        self.tree.edit(index)
        self.tree.expand(parent_item.index())




def main():
    app = QApplication(sys.argv)

    rows = get_hierarchy()
    nodes_by_id, root_nodes = build_tree(rows)
    model = build_model(root_nodes)
    
    window = MainWindow(model)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()