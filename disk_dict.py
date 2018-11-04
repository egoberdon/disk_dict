import json
from datetime import datetime


class DiskDict(dict):

	def __init__(self, name, stale_timer=300):
		super().__init__(self)
		self.filename = name
		self.stale_timer = stale_timer
		self.last_saved = None

	def __str__(self):

		return f"<Stored Dict @ {self.filename}>"

	def load(self):
		try:
			with open(self.filename) as f:
				self.update(json.load(f))
		except FileNotFoundError:
			print("File not Found Compadre, try saving one first, ya feel?")
		else:
			print(f"Loaded from file, dict now has {len(self)} items")

	def save(self):
		try:
			with open(self.filename, 'w') as f:
				json.dump(self, f)
		except Exception as exc:
			print("Sorry this happened while saving {}".format(exc))
		else:
			self.last_saved = datetime.now()
			print("Dictionary successfully written to disk.")

	def is_stale(self):
		if not self.last_saved:
			return True

		# number of seconds since last save
		stale_seconds = (datetime.now() - self.last_saved).total_seconds()

		return stale_seconds > self.stale_timer
