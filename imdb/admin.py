from django.contrib import admin
from datetime import date,datetime
# Register your models here.
from imdb.models import Rating,Movie,Actor,Director,Cast
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe



class RatingAdmin(admin.ModelAdmin):
    def upper_case_name(self, obj):
        return ("Rating for %s " % (obj.movie.name,))
    list_display = ('upper_case_name','rating_one_count','rating_two_count',"rating_three_count","rating_four_count","rating_five_count")
    upper_case_name.short_description = 'Movie'


class MovieReleasedFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Movie released')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'release_date'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('90s', _('in the two thousands early')),
            ('21st', _('in the two thousands late')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '90s':
            return queryset.filter(release_date__gte=date(1980, 1, 1),
                                    release_date__lte=date(1999, 12, 31))
        if self.value() == '21st':
            return queryset.filter(release_date__gte=date(2000, 1, 1),
                                    release_date__lte=date(2022, 12, 31))



class MovieAdmin(admin.ModelAdmin):
    def director_name(self,obj):
        return f'{obj.director.name}'

    def actors_count(self,obj):
        return f'{obj.actors.count()}'

    list_display = ('name','actors_count','director_name')
    director_name.short_description = 'Director'

    date_hierarchy = 'release_date'

    list_filter = (MovieReleasedFilter, )
    empty_value_display = '-empty-'

# StackInLine
class CastInline(admin.TabularInline):
    model = Cast
    extra = 0

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender',"actor_name","actor_id")
    # inlines = [CastInline]
    def actor_name(self, obj):
        return obj.name

    actor_name.empty_value_display = '???'

    # readonly_fields = ('actor_id',)

    def actor_ids(self, instance):
        # assuming get_full_address() returns a list of strings
        # for each line of the address and you want to separate each
        # line by a linebreak
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            ((line,) for line in instance.get_full_address()),
        ) or mark_safe("<span class='errors'>I can't determine this id.</span>")

    # short_description functions like a model field's verbose_name
    actor_ids.short_description = "Actor ID"


class CastAdmin(admin.ModelAdmin):
    def actor_name(self,obj):
        return f'{obj.actor.name}'

    def movie_name(self, obj):
        return f'{obj.movie.name}'
    movie_name.short_description = 'Acted In'
    actor_name.short_description = 'Played by'
    list_filter = ('is_debut_movie', 'movie')
    search_fields = ['movie__name']
    raw_id_fields = ("actor",)
    list_display = ('actor_name','role','movie_name','is_debut_movie')
    list_display_links = ('actor_name',)
    fieldsets = (
        (None, {
            'fields': ('role', 'is_debut_movie', )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('actor', 'movie'),
        }),
    )

    def make_debut(self, request, queryset):

        rows_updated = queryset.update(is_debut_movie='True')
        if rows_updated == 1:
            message_bit = "1 actor was"
        else:
            message_bit = "%s more actors were" % rows_updated


        self.message_user(request, "%s successfully changed as debut." % message_bit)

    make_debut.allowed_permissions = ('view',)
    make_debut.short_description = "Mark selected actors as debut"

    actions = [make_debut]

admin.site.disable_action('delete_selected')

admin.site.register(Actor,ActorAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Cast,CastAdmin)
admin.site.register(Rating,RatingAdmin)
admin.site.register(Director)

