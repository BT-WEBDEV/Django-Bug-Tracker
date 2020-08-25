from django.contrib import admin
from tickets.models import Priority, Category, Ticket

# Register your models here.

class PriorityAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class TicketAdmin(admin.ModelAdmin):
    pass

admin.site.register(Priority, PriorityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ticket, TicketAdmin)