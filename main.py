from tables_logic.film_logic import FilmLogic
from tables_logic.session_logic import SessionLogic
from tables_logic.hall_logic import HallLogic
from tables_logic.hall_place_logic import HallPlaceLogic
from tables_logic.ticket_logic import TicketLogic
from tables_logic.genre_logic import GenreLogic
from close_db import DataBaseClosing

#----------Methods---------

def open_menu(user_type: str):
	user_menu = {}
	if user_type == "admin":
		user_menu = {
			1 : "Добавить фильм",
			2 : "Обновить фильм",
			3 : "Удалить фильм",
		}
	elif user_type == "user":
		user_menu = {
			1 : "Посмотреть афишу",
			2 : "Купить билет",
		}
	else:
		print("Пользователь не найден")
	
#----------MAIN----------

film_logic: FilmLogic = FilmLogic()
session_logic: SessionLogic = SessionLogic()
hall_logic: HallLogic = HallLogic()
hall_place_logic: HallPlaceLogic = HallPlaceLogic()
ticket_logic: TicketLogic = TicketLogic()
genre_logic: GenreLogic = GenreLogic()

close_db: DataBaseClosing = DataBaseClosing()

while True:

	user_menu = {
		1 : "Добавить фильм",
		2 : "Добавить сенанс",
		3 : "Добавить зал",
		4 : "Добавить место в зале",
		5 : "Добавить билет",
		6 : "Добавить жанр",
		7 : "Обновить фильм",
		8 : "Обновить сеанс",
		9 : "Обновить зал",
		10 : "Обновить место в зале",
		11 : "Обновить билет",
		12 : "Обновить жанр",
		13 : "Удалить фильм",
		14 : "Удалить сеанс",
		15 : "Удалить зал",
		16 : "Удалить место в зале",
		17 : "Удалить билет",
		18 : "Удалить жанр",
	}

	for point in user_menu:
		print(f"{point}. {user_menu[point]}")	

	menu_point = int(input("Select menu point: "))
	
	if menu_point not in user_menu:
		print("Такого пункта меню нет")
		continue
	else:		
		if menu_point == 1:
			film_logic.show_table()
			film_logic.enable_add_film_input()
			film_logic.show_table()

		elif menu_point == 2:
			session_logic.show_table()
			session_logic.enable_add_session_input()
			session_logic.show_table()

		elif menu_point == 3:
			hall_logic.show_table()
			hall_logic.enable_add_hall_input()
			hall_logic.show_table()

		elif menu_point == 4:
			hall_place_logic.show_table()
			hall_place_logic.enable_add_hall_place_input()
			hall_place_logic.show_table()

		elif menu_point == 5:
			ticket_logic.show_table()
			ticket_logic.enable_add_ticket_input()
			ticket_logic.show_table()

		elif menu_point == 6:
			genre_logic.show_table()
			genre_logic.enable_add_genre_input()
			genre_logic.show_table()

		elif menu_point == 7:
			film_logic.show_table()
			film_logic.enable_update_record_input()
			film_logic.show_table()

		elif menu_point == 8:
			session_logic.show_table()
			session_logic.enable_update_record_input()
			session_logic.show_table()

		elif menu_point == 9:
			hall_logic.show_table()
			hall_logic.enable_update_record_input()
			hall_logic.show_table()

		elif menu_point == 10:
			hall_place_logic.show_table()
			hall_place_logic.enable_update_record_input()
			hall_place_logic.show_table()

		elif menu_point == 11:
			ticket_logic.show_table()
			ticket_logic.enable_update_record_input()
			ticket_logic.show_table()

		elif menu_point == 12:
			genre_logic.show_table()
			genre_logic.enable_update_record_input()
			genre_logic.show_table()

		elif menu_point == 13:
			film_logic.show_table()
			film_logic.enable_delete_record_input()
			film_logic.show_table()

		elif menu_point == 14:
			session_logic.show_table()
			session_logic.enable_delete_record_input()
			session_logic.show_table()

		elif menu_point == 15:
			hall_logic.show_table()
			hall_logic.enable_delete_record_input()
			hall_logic.show_table()

		elif menu_point == 16:
			hall_place_logic.show_table()
			hall_place_logic.enable_delete_record_input()
			hall_place_logic.show_table()

		elif menu_point == 17:
			ticket_logic.show_table()
			ticket_logic.enable_delete_record_input()
			ticket_logic.show_table()

		elif menu_point == 18:
			genre_logic.show_table()
			genre_logic.enable_delete_record_input()
			genre_logic.show_table()
			
			
close_db.close_db()

			


