from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon, QPixmap, QColor
from PyQt5.QtCore import Qt

state_color = {
    0: QColor("red"),
    1: QColor("yellow"),
    2: QColor("green")
}

def build_model(root_nodes):
    model = QStandardItemModel()

    for node in root_nodes:
        add_node(model, None, node)

    return model

def add_node(model, parent_item, node):
    item = QStandardItem(node.name)
    item.setData(node, Qt.UserRole)
    color = state_color.get(node.state, QColor("white"))
    item.setBackground(color)
    flags = item.flags()
    flags |= Qt.ItemIsEditable
    item.setFlags(flags)
 
    if node.image_bytes:
        pixmap = QPixmap()
        pixmap.loadFromData(node.image_bytes)
        icon = QIcon(pixmap)
        item.setIcon(icon)

    if parent_item is None:
        model.appendRow(item)
    else:
        parent_item.appendRow(item)
    
    for child in node.children:
        add_node(model,item, child)
