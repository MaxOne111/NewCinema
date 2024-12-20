from tables_logic.database_base_logic import BaseLogic

class HallLogic(BaseLogic):

	def _get_table_name(self):
		return "Hall"

	def __add_hall(self, name: str):
		request = "INSERT INTO Hall (name) VALUES(?)"
		values = (name,)	
		self._cursor.execute(request, values)
		self._con.commit()



	def enable_add_hall_input(self):
		name = input("Enter a hall name: ")

		self.__add_hall(name)



	