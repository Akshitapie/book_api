from django.contrib import admin
from .models import Book, Rental
from django.utils.html import format_html


class AdminBook(admin.ModelAdmin):
    model = Book

    def Edit(self, obj):
        return format_html(
            '<button  style="height:40px;" class="btn btn-secondary"><a class="btn btn-secondary" href="/admin/book_api/book/{}/change/">Change</a></button>',
            obj.id,
        )

    def Add(self, obj):
        return format_html(
            '<button  style="height:40px;"><a class="btn btn-secondary" href="/admin/book_api/book/add/">Add Book</a></button>',
            obj.id,
        )

    list_display = (
        "title",
        "author_name",
        "publish_date",
        "page",
        "cover_url",
        "Edit",
        "Add",
    )


class AdminRental(admin.ModelAdmin):
    model = Rental

    def Edit(self, obj):
        return format_html(
            '<button  style="height:40px;"><a class="btn btn-secondary" href="/admin/book_api/rental/{}/change/">Change</a></button>',
            obj.id,
        )

    list_display = (
        "user",
        "book_id",
        "book_get_date",
        "return_date",
        "fees",
        "Edit",
    )


admin.site.register(Book, AdminBook)
admin.site.register(Rental, AdminRental)
