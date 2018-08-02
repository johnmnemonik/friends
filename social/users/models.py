from django.db import models

class Friend(models.Model):
	name = models.CharField(max_length=255)
	friends = models.ManyToManyField('self', blank=True)

	def __str__(self):
		return self.name

	def return_friend(self):
		friend_and_friend = []
		msg = "друзья друзей"
		obj = self.friends.all()
		for _ in obj:
			friend_and_friend.append(_.name)
		return ", ".join(friend_and_friend)

