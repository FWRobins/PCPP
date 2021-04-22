import sqlite3

class Todo():
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute("""
                        CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        priority INTEGER NOT NULL
                        );
                        """)

    def add_task(self):
        name = input('Enter task name: ')
        priority = int(input("task priority: "))
        print()
        if not self.find_task(name):
            self.c.execute("""
            INSERT INTO tasks (name, priority)
            values (?,?);
            """, (name, priority))
            self.conn.commit()
        else:
            print('record already exists \n')

    def show_all(self):
        for row in self.c.execute("""SELECT * FROM tasks"""):
            print(row)
        print()

        # fetchall doesnt use iterator but memory issues on bog data
        # self.c.execute("""SELECT * FROM tasks""")
        # rows = c.fetchall()
        # for row in rows:
        #     print(row)

        # fetchone get one row per call like a generator
        # self.c.execute("""SELECT * FROM tasks""")
        # print(self.c.fetchone())
        # print(self.c.fetchone())


    def close_conn(self):
        self.conn.close()

    def find_task(self, name):
        self.c.execute("""select * from tasks
        WHERE name like ?""", (name,))
        rows = self.c.fetchall()
        return rows

    def find_task_by_id(self, id):
        self.c.execute("""SELECT * FROM tasks
        WHERE id = ?""", (id,))
        return True if len(self.c.fetchall()) ==1 else False

    def show_task_by_name(self):
        name = input("task name to find: ")
        print()
        for row in self.c.execute("""select * from tasks
        WHERE name like ?""", (name,)):
            print(row)
        print()

    def update_priority_by_id(self):
        id_to_update = int(input("task id to be updated: "))
        updated_priority = int(input("new priority level? "))
        if self.find_task_by_id(id_to_update):
            self.c.execute("""
            UPDATE tasks
            SET priority = ?
            WHERE id = ?""", (updated_priority, id_to_update))
            self.conn.commit()

    def delete_task(self):
        id_to_delete = int(input("recode id to delete: "))
        if self.find_task_by_id(id_to_delete):
            self.c.execute("""
            DELETE FROM tasks
            WHERE id = ?""", (id_to_delete, ))
            self.conn.commit()





# tasks = [
#     ('My second task', 5),
#     ('My third task', 10),
#     ('My forth task', 11),
# ]
#
# c.executemany("""
# INSERT INTO tasks (name, priority)
# values (?,?);
# """, tasks)
#
# conn.commit()

app = Todo()

while True:
    try:
        choice = int(input("""1 - Show Tasks \
        \n2 - Add Task \
        \n3 - Change Priority \
        \n4 - Delete Task \
        \n5 - Exit\n
        """))
    except:
        print('please select from options above by number')
        continue
    if choice not in range(1,6):
        print('please select from options above by number')
        continue
    if choice == 1:
        app.show_all()
    if choice == 2:
        app.add_task()
    if choice == 3:
        app.update_priority_by_id()
    if choice == 4:
        app.delete_task()
    if choice == 5:
        app.close_conn()
        exit('Good Bye')
