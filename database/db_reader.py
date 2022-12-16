import sqlite3
import random

connection = sqlite3.connect("new_db.sqli")
c = connection.cursor()

c.execute("SELECT * FROM TRUTH")

a = [i for i in c.fetchall()]

connection.commit()
connection.close()

for i in a:
    print(i)

# class Engine:
#     def __init__(self):
#         # These lists are supposed to nest chosen level`s questions from low, middle or high lists.
#         self.t_all = []
#         self.d_all = []
#         self.n_all = []
#
#     def shuffled_list(self, object: list):
#         import random
#         random.shuffle(object)
#         random.shuffle(object)
#         random.shuffle(object)
#         return object
#
#     def out_of_objects(self, object: list):
#         if len(object) == 0:
#             return True
#         else:
#             return False
#
#     def set_levels(self, lifestyle, absurd, relations, personal, adult):
#         connection = sqlite3.connect("db.db")
#         c = connection.cursor()
#
#         def get_data_truth(level):
#             c.execute("SELECT * FROM TRUTH WHERE level=?", (level,))
#             return [i[1] for i in c.fetchall()]
#
#         def get_data_dare(level):
#             c.execute("SELECT * FROM DARE WHERE level=?", (level,))
#             return [i[1] for i in c.fetchall()]
#
#         def get_data_never(level):
#             c.execute("SELECT * FROM NEVER WHERE level=?", (level,))
#             return [i[1] for i in c.fetchall()]
#
#         levels = [[lifestyle,"lifestyle"],
#                   [absurd, "absurd"],
#                   [relations, "relations"],
#                   [personal, "personal"],
#                   [adult, "adult"]]
#
#         for level in levels:
#             if level[0] == True:
#                 self.t_all += get_data_truth(level[1])
#                 self.d_all += get_data_dare(level[1])
#                 self.n_all += get_data_never(level[1])
#             else:
#                 pass
#
#         connection.close()
#
#         for _ in [self.t_all, self.d_all, self.n_all]:
#             random.shuffle(_)
#             random.shuffle(_)
#             random.shuffle(_)

