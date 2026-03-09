class Node:

    def __init__(self, row):
        self.children = []
        self.parent = None

        self.id = row["id"]
        self.parent_id = row["id_parent"]
        self.name = row["name"]
        self.state = row["state"]
        self.image_bytes = row["image"]
