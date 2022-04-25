class Database:

	def __init__(self, column, row):
		self.columns = []
		self.rows = [] 
		self.add_column(column, None)
		self.add_row(row, None)
		self.entries = []

	def add_column(c, index):
		if index:
			self.columns.insert(index, c)
		else:
			for i in c:
				self.columns.append(c)

	def add_row(r, index):
		if index:
			self.rows.insert(index, r)
		else:
			for i in r:
				self.rows.append(i)

	def del_column(index):
		for i in self.entries:
			if i.column == index:
				self.del_entry(i)
		if index == len(self.columns) - 1:
			self.columns = self.columns[:index]
		else:
			self.columns = self.columns[:index] + self.columns[index + 1:]

	def del_row(index):
		for i in self.entries:
			if i.row == index:
				self.del_entry(i)
		if index == len(self.row) - 1:
			self.row = self.row[:index]
		else:
			self.row = self.row[:index] + self.row[index + 1:]

	def edit_column(c, nc, index):
		if index:
			self.columns.remove(c)
			self.columns = self.columns[:index] + c + self.columns[index:]
		if nc:
			for i in self.entries:
				if i.column = c:
					i.edit_entry(nc, None, None, None)
			self.columns.insert(self.columns.index(c), nc)
			self.columns.remove(c)

	def edit_row(r, nr, index):
		if index:
			self.rows.remove(r)
			self.rows = self.rows[:index] + r + self.rows[index:]
		if nr:
			for i in self.entries:
				if i.row = r:
					i.edit_entry(None, nr, None, None)
			self.rows.insert(self.rows.index(r), nr)
			self.rows.remove(r)

	def add_entry(c, r, d):
		self.entries.append(entry(c, r, d, len(self.entries) - 1))

	def del_entry(e):
		if e.index == len(self.entries) - 1:
			self.entries = self.entries[:index]
		else:
			self.entries = self.entries[:e.index] + self.entries[e.index + 1:]
			for i in self.entries[e.index + 1:]:
				i.edit_entry(None, None, None, i.index - 1)


class entry:

	def __init__(self, column, row, description, index):
		self.column = column
		self.row = row
		self.description = description
		self.index = index

	def edit_entry(c, r, d, i):
		if c:
			self.column = c
		if r:
			self.row = r
		if d:
			self.description = d
		if i:
			self.index = i
