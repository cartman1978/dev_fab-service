from django.contrib import admin
from .models import NewsletterSubscribtion, Message


class NewsletterSubscribtionAdmin(admin.ModelAdmin):
    model = NewsletterSubscribtion
    list_display = (
        "email",
    )


class MessageAdmin(admin.ModelAdmin):
    model = Message
    readonly_fields = (
        "subject",
        "user_email",
        "message",
    )
    

admin.site.register(NewsletterSubscribtion,
                    NewsletterSubscribtionAdmin)
admin.site.register(Message, MessageAdmin)

