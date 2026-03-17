from django.db import models


class SellerApplication(models.Model):
	class Status(models.TextChoices):
		PENDING = 'Pending', 'Pending'
		APPROVED = 'Approved', 'Approved'
		DECLINED = 'Declined', 'Declined'

	user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='seller_applications')
	status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
	decline_reason = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.user.email} - {self.status}'
