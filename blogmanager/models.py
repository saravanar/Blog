from django.db import models

class Blog(models.Model):

    name = models.CharField(max_length=50, verbose_name="Blog Name")
    title = models.CharField(max_length=50, verbose_name="Blog Title",
                                null=True, blank=True)
    description = models.TextField(max_length=5000,
                                     verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
