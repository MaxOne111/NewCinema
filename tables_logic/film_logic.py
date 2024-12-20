from tables_logic.database_base_logic import BaseLogic

class FilmLogic(BaseLogic):

	def _select_table(self):
		request = f"""SELECT film.id, film.name, release_year, director, film.id_genre, genre.name as 'genre'
FROM {self._get_table_name()} film LEFT JOIN Genre genre ON film.id_genre = genre.id """
		self._cursor.execute(request)
		self._records = self._cursor.fetchall()

	def _get_table_name(self):
		return "Film"

	def __add_film(self, film_name: str, release_year: int, director: str, genre_id: int):
		request = "INSERT INTO Film (name, release_year, director, id_genre) VALUES(?, ?, ?, ?)"
		values = (film_name, release_year, director, genre_id)	
		self._cursor.execute(request, values)
		self._con.commit()


	def enable_add_film_input(self):
		name = input("Enter film name: ")

		year = int(input("Enter a film release year: "))

		director = input("Enter a film director name: ")

		genre_id = int(input("Enter a film genre id: "))

		self.__add_film(name, year, director, genre_id)



	