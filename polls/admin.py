from django.contrib import admin
from .models import Question,Choice


# 垂直排列显示
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     # 选项里新的选项条数
#     extra = 0


# 扁平化显示
class ChoiceInline(admin.TabularInline):
    model = Choice
    # 选项里新的选项条数
    extra = 0


class QuestionAction(admin.ModelAdmin):
    fields = ['pub_date','question_text']


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text','pub_date']


admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)
