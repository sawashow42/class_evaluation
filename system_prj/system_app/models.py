from turtle import title
from django.db import models

# Create your models here.

class SystemAppModel(models.Model):
	class_id = models.IntegerField()
	title = models.CharField(verbose_name='科目名', max_length=20)
	difficulty = models.FloatField(verbose_name='単位取得難易度')
	amount_of_tasks = models.FloatField(verbose_name='課題の量')
	credit = models.IntegerField(verbose_name='単位数')
	term = models.CharField(verbose_name='学期',max_length=10)
	teacher = models.CharField(verbose_name='担当教員',max_length=50)
	way = models.CharField(verbose_name='授業方法',max_length=50)
	evaluation = models.TextField(verbose_name='成績評価方法')
	about = models.TextField(verbose_name='授業概要')

	def __str__(self):
		return self.title + ',' + str(self.difficulty) + ',' + str(self.amount_of_tasks) + ','\
			+ str(self.credit) + ',' + self.term + ',' + self.teacher + ',' + self.way + ','\
				+ self.evaluation + ',' + self.about