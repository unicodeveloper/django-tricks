from django.contrib import admin

# Register your models here.
from .models import Trick
from .models import Category
from .models import Tag
from .models import Profile
from .models import Vote
from .models import Tag_Trick
from .models import Category_Trick


admin.site.register(Trick)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Vote)
admin.site.register(Tag_Trick)
admin.site.register(Category_Trick)

