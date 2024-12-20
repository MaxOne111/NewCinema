from tables_logic.database_base_logic import BaseLogic

class SessionLogic(BaseLogic):

	def _get_table_name(self):
		return "Session"

	def __add_session(self, date: str):
		request = "INSERT INTO Session (session_date) VALUES(?)"
		values = (date,)	
		self._cursor.execute(request, values)
		self._con.commit()


	def enable_add_session_input(self):
		date = input("Enter session date: ")

		self.__add_session(date)


	