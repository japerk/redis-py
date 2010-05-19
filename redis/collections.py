import collections

class RedisSet(collections.MutableSet):
	'''Redis based Mutable Set collection'''
	def __init__(self, r, key):
		self._r = r
		self._key = key
	
	def __contains__(self, item):
		return self._r.sismember(self._key, item)
	
	def __len__(self):
		return self._r.scard(self._key)
	
	def __iter__(self):
		return iter(self._r.smembers(self._key))
	
	def add(self, item):
		self._r.sadd(self._key, item)
	
	def discard(self, item):
		self._r.srem(self._key, item)
	
	# TODO: more optimal override intersection, union, and diff
