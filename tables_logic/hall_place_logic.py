from tables_logic.database_base_logic import BaseLogic

class HallPlaceLogic(BaseLogic):

	def _select_table(self):
		request = f"""
SELECT hp.id, hp.price, hall.name AS 'hall', hp.place_number, is_place_free, hp.id_hall
FROM {self._get_table_name()} hp LEFT JOIN Hall hall ON hp.id_hall= hall.id 
"""
		self._cursor.execute(request)
		self._records = self._cursor.fetchall()

	def _get_table_name(self):
		return "HallPlace"

	def __add_hall_place(self, price: float, place_number: int, place_is_free: str, hall_id: int):
		request = "INSERT INTO HallPlace (price, place_number, is_place_free, id_hall) VALUES(?,?,?,?)"
		values = (price, place_number, place_is_free, hall_id)	
		self._cursor.execute(request, values)
		self._con.commit()

	def enable_add_hall_place_input(self):

		price = float(input("Enter a hall place price: "))

		place_number = int(input("Enter a place number: "))

		is_place_free = input("Enter a place is free(y/n): ")

		hall_id = int(input("Enter a hall id: "))

		self.__add_hall_place(price, place_number, is_place_free, hall_id)



	