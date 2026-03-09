from node import Node

def build_tree(rows):
    nodes_by_id = {}
    root_nodes = []

    for row in rows:
        node = Node(row)
        nodes_by_id[node.id] = node

    for node in nodes_by_id.values():
        if node.parent_id is None:
            root_nodes.append(node)
        else:
            parent = nodes_by_id.get(node.parent_id)
            parent.children.append(node)
            node.parent = parent

    return nodes_by_id, root_nodes



