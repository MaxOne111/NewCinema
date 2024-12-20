import sqlite3
from tabulate import tabulate

class BaseLogic:
	
	def __init__(self):
		self.__connection_to_db()

	def __connection_to_db(self):
		self._con = sqlite3.connect('Cinema.db')
		self._cursor = self._con.cursor()

	def __get_columns(self):
		self._cursor.execute(f"PRAGMA table_info({self._get_table_name()})")
		columns_info = self._cursor.fetchall()
		
		column_names = [column[1] for index, column in enumerate(columns_info) if index != 0]
		column_types = [column[2] for index, column in enumerate(columns_info) if index != 0]
		
		columns = dict(zip(column_names, column_types))
		
		return columns

	def __convert_type(self, type_name: str, value: str):
		if type_name == "INTEGER":
			value = int(value)
		elif type_name == "REAL":
			value = float(value)

		return value

	def __update_record(self, id, param_name: str, value):
		request = f"UPDATE {self._get_table_name()} SET {param_name} = ? where id = ?"	
		values = (value, id)
		self._cursor.execute(request, values)
		self._con.commit()

	def __delete_record(self, id):
		request = f"DELETE FROM {self._get_table_name()} where id = ?"
		values = (id,)	
		self._cursor.execute(request, values)
		self._con.commit()

	def _select_table(self): #-------------------virtual--------------------
		request = f"SELECT * FROM {self._get_table_name()}"
		self._cursor.execute(request)
		self._records = self._cursor.fetchall()

	def _get_table_name(self): #-------------------virtual--------------------
		return ""

	def show_table(self):
		self._select_table()
		
		columns = [description[0] for description in self._cursor.description]

		print(tabulate(self._records, headers=columns, tablefmt='psql'))

	def enable_update_record_input(self):
		columns = self.__get_columns()
			
		names = list()

		id = int(input(f"Enter a {self._get_table_name().lower()} id you want to change: "))

		print("----------Fields----------")

		for index, name in enumerate(columns, 1):
			names.append(name)
			print(f"{index}. {name}")

		print("--------------------------")

		point = int(input("Select a field number you want to change: "))

		if point == 0 or point > len(names):
			print("Error: element is not found")
			return

		type_name = columns[names[point-1]]		

		value = input("Enter a new value: ")

		value = self.__convert_type(type_name, value)

		self.__update_record(id, names[point-1], value)		

	def enable_delete_record_input(self):

		id = int(input(f"Enter a {self._get_table_name().lower()} id you want to delete: "))	

		self.__delete_record(id)
		