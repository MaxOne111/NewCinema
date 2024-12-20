from tables_logic.database_base_logic import BaseLogic

class DataBaseClosing(BaseLogic):

	def close_db(self):
		self._con.close()

	