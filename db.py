import sqlite3

def get_hierarchy():
    connection = sqlite3.connect("data/task")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(
        '''
SELECT id, id_parent, name, image, state
FROM hierarhy
'''
    )
    records = cursor.fetchall()
    
    connection.close()
    return records