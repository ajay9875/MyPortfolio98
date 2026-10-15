from django.db import models

class VisitorCount(models.Model):
    count = models.IntegerField(default=0)

    class Meta:
        db_table = 'visitor_count'   # ← custom table name

    def __str__(self):
        return f"Total Visitors: {self.count}"