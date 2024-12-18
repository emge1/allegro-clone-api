from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from v1.prometheus.views import metrics_view
from django.conf.urls.static import static


urlpatterns = [
    # API (v1)
    path('', include('v1.accounts.urls')),
    path('', include('v1.user_roles.urls')),
    path('', include('v1.carts.urls')),
    path('', include('v1.categories.urls')),
    path('', include('v1.subcategories.urls')),
    path('', include('v1.products.urls')),
    path('', include('v1.product_medias.urls')),
    path('', include('v1.product_details.urls')),
    path('', include('v1.product_abouts.urls')),
    path('', include('v1.product_tags.urls')),
    path('', include('v1.product_variants.urls')),
    path('', include('v1.product_variant_items.urls')),
    path('', include('v1.product_reviews.urls')),
    path('', include('v1.product_review_votings.urls')),
    path('', include('v1.product_questions.urls')),
    path('', include('v1.customer_orders.urls')),
    path('', include('v1.product_transactions.urls')),

    # Core
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        path('docs/', include_docs_urls(title='Allegro clone')),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        path('metrics/', metrics_view),
    ]