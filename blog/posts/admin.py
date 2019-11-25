from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):

	list_display = (
				'title',
				'content',
				'created',
				'updated',
				)

	list_display_links = (
					'title',
					'created',
					'updated',
					)

	search_fields = (
				'title',
				'content',
				)

	list_filter = (
				'updated',
				'created',
				)

admin.site.register(Post, PostAdmin)