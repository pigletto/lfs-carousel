from django.conf.urls.defaults import *


# Carousel items
urlpatterns = patterns('lfs_carousel.views',
    url(r'^add-item/(?P<content_type_id>\d*)/(?P<object_id>\d*)/$', "add_item", name="lfs_carousel_add_item"),
    url(r'^update-items/(?P<content_type_id>\d*)/(?P<object_id>\d*)/$', "update_items", name="lfs_carousel_update_items"),
    url(r'^manage-items/(?P<content_type_id>\d*)/(?P<object_id>\d*)/$', "manage_items", name="lfs_carousel_manage_items"),
    #url(r'^update-active-items/(?P<product_id>\d*)$', "update_active_items", name="lfs_manage_update_active_images"),
    url(r'^move-item/(?P<id>\d+)$', "move_item", name="lfc_carousel_move_item"),
)
