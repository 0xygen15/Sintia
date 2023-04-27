# import loader
# from mainUnit.users import Users
# from mainUnit.games import Tord, Nie, ThreeOfFive, Themes
# from mainUnit.keyboards import TordKeyboard, NieKeyboard, ThemesKeyboard, ThreeOfFiveKeyboard
# from mainUnit.database import Database
# from loader import loc_objects
# from loader import user_objects
#
# import time
#
# test_user = Users(
#     user_id="107985053",
#     lang_code="ru",
#     tord_game=Tord("107985053", loc_objects["ru"]),
#     nie_game=Nie("107985053", loc_objects["ru"]),
#     the_35_game=ThreeOfFive("107985053", loc_objects["ru"]),
#     themes_game=Themes("107985053", loc_objects["ru"]),
#     tord_kb=TordKeyboard(loc_objects["ru"]),
#     nie_kb=NieKeyboard(loc_objects["ru"]),
#     the_35_kb=ThreeOfFiveKeyboard(loc_objects["ru"]),
#     themes_kb=ThemesKeyboard(loc_objects["ru"]),
#     chat_id="107985053",
#     chat_type="user",
#     username="test_username",
#     fName="test fName",
#     lName="test lName",
#     is_bot=False
# )
#
# test_user_edited = Users(
#     user_id="107985053",
#     lang_code="en",
#     tord_game=Tord("107985053", loc_objects["en"]),
#     nie_game=Nie("107985053", loc_objects["en"]),
#     the_35_game=ThreeOfFive("107985053", loc_objects["en"]),
#     themes_game=Themes("107985053", loc_objects["en"]),
#     tord_kb=TordKeyboard(loc_objects["en"]),
#     nie_kb=NieKeyboard(loc_objects["en"]),
#     the_35_kb=ThreeOfFiveKeyboard(loc_objects["en"]),
#     themes_kb=ThemesKeyboard(loc_objects["en"]),
#     chat_id="107985053",
#     chat_type="user",
#     username="test_username",
#     fName="test fName",
#     lName="test lName",
#     is_bot=False
# )
#
#
#
# start_time = time.time()
# Database.create_users_db()
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"The function <<<Database.create_users_db()>>> took {elapsed_time} seconds to execute.\n\n")
#
# start_time = time.time()
# Database.add_user_to_db(test_user)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"The function <<<Database.add_user_to_db(test_user)>>> took {elapsed_time} seconds to execute.\n\n")
#
# start_time = time.time()
# Database.get_user_obj_from_db("107985053")
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"The function <<<Database.add_user_to_db(test_user)>>> took {elapsed_time} seconds to execute.\n\n")
#
# assert "user" in loader.user_objects["107985053"].chat_type
#
#
# start_time = time.time()
# Database.update_user_obj("107985053", test_user_edited)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"\n\nThe function <<<Database.add_user_to_db(test_user)>>> took {elapsed_time} seconds to execute.\n\n")
#
#

# import sqlite3
#
# # filename to form database
# file = "database/users.db"
#
# try:
#     conn = sqlite3.connect(file)
#     print("Database Sqlite3.db formed.")
# except:
#     print("Database Sqlite3.db not formed.")