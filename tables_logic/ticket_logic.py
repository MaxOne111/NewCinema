from tables_logic.database_base_logic import BaseLogic
from tabulate import tabulate

class TicketLogic(BaseLogic):

#--------------------SelectTable--------------------

	def _select_table(self):
		request = f"""
WITH Hall_data AS(
SELECT hall.name, hp.id as 'id_hall'
FROM Hall hall JOIN HallPlace hp ON hp.id_hall = hall.id)

SELECT ticket.id, film.name, session.session_date, hall_data.name AS 'hall', hp.place_number, hp.is_place_free, ticket.id_session, ticket.id_hall_place
FROM {self._get_table_name()} ticket 
LEFT JOIN Film film ON ticket.id_film = film.id 
LEFT JOIN Session session ON ticket.id_session = session.id
LEFT JOIN HallPlace hp ON ticket.id_hall_place = hp.id
LEFT JOIN Hall_data  hall_data ON hp.id = hall_data.id_hall
"""
		self._cursor.execute(request)
		self._records = self._cursor.fetchall()


#--------------------GetTableName--------------------

	def _get_table_name(self):
		return "Ticket"


#--------------------AddTicket--------------------

	def __add_ticket(self, session_id: int, film_id: int, hall_place_id: int):
		request = "INSERT INTO Ticket (id_session, id_film, id_hall_place) VALUES(?,?,?)"
		values = (session_id, film_id, hall_place_id)	
		self._cursor.execute(request, values)
		self._con.commit()

#--------------------EnableAddTicketInput--------------------

	def enable_add_ticket_input(self):

		request = f"""
SELECT DISTINCT id, name
FROM Film
"""

		self.__show_table_data(request)

		film_id = int(input("Enter a film id: "))

		request = f"""
SELECT DISTINCT id, session_date
FROM Session
"""
		self.__show_table_data(request)

		session_id = int(input("Enter a session id: "))

		request = f"""
WITH Hall_data AS(
SELECT hall.name, hp.id as 'id_hall'
FROM Hall hall JOIN HallPlace hp ON hp.id_hall = hall.id)

SELECT price, place_number, hall.name, hp.id
FROM HallPlace hp
LEFT JOIN Hall hall ON hp.id_hall = hall.id
WHERE is_place_free = 'y'
"""

		self.__show_table_data(request)

		hall_place_id = input("Enter a hall place id: ")

		self.__add_ticket(session_id, film_id, hall_place_id)

		self.__update_record("HallPlace", hall_place_id, 'is_place_free', 'n')


#--------------------ShowTable--------------------

	def __show_table_data(self, request: str): #test

		self._cursor.execute(request)

		self._records = self._cursor.fetchall()

		columns = [description[0] for description in self._cursor.description]

		print(tabulate(self._records, headers=columns, tablefmt='psql'))

#--------------------UpdateRecord--------------------

	def __update_record(self, table_name: str, id, param_name: str, value): #test
		request = f"UPDATE {table_name} SET {param_name} = ? where id = ?"	
		values = (value, id)
		self._cursor.execute(request, values)
		self._con.commit()
		