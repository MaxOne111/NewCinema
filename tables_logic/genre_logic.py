from tables_logic.database_base_logic import BaseLogic

class GenreLogic(BaseLogic):

	def _get_table_name(self):
		return "Genre"

	def __add_genre(self, name: str):
		request = "INSERT INTO Genre (name) VALUES(?)"
		values = (name,)	
		self._cursor.execute(request, values)
		self._con.commit()


	def enable_add_genre_input(self):
		name = input("Enter a genre name: ")

		self.__add_genre(name)