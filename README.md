What is it?
===========

LFS Carousel is pluggable carousel/slider application for use with LFS (Lightning Fast Shop)

See project wiki for more details: https://github.com/pigletto/lfs-carousel/wiki/What-is-it%3F

Basic usage
===========

* add lfs_carousel to INSTALLED_APPS in your settings.py
* add lfs_carousel urls to your site urls.py like:

  <pre lang="python"><code>
      from lfs_carousel import carousel
      urlpatterns += patterns("",
        (...)
        (r'^carousel/', include(carousel.urls)),
        (...)
      )
  </code></pre>
  
* add carousel to the management panel. It will be visible at 'Shop' -> 'Settings' page as new 'Carousel' tab:
  copy lfs/templates/manage/shop/shop.html to your theme and modify it by adding:

  ```html
      {% load lfs_carousel_tags %}
      ( ... )
      <div id="manage-tabs">
        <ul>
            <li class="ui-tabs-nav-item"><a href="#data">{% trans 'Shop' %}</a></li>
            <li class="ui-tabs-nav-item"><a href="#default-values">{% trans 'Default Values' %}</a></li>
            <li class="ui-tabs-nav-item"><a href="#portlets">{% trans 'Portlets' %}</a></li>
            **<li class="ui-tabs-nav-item"><a href="#carousel-items">{% trans 'Carousel' %}</a></li>**
        </ul>
      (...)
      <div id="portlets">
        {{ portlets|safe }}
      </div>
      {% carousel_management shop %}
  ```
  
* add carousel to your shop's start page

  By default lfs_carousel uses coin-slider but you can use anything you want. 
  
  First add necessary JavaScript and CSS files either to base.html or to shop.html:

  ```html
      <link rel="stylesheet" href="{{ STATIC_URL }}coin-slider/coin-slider-styles.css" type="text/css" />
      <script type="text/javascript" src="{{ STATIC_URL }}coin-slider/coin-slider.min.js"></script>
      <script type="text/javascript">
            $(document).ready(function() {
                $('#coin-slider').coinslider({ width: 400, navigation: true, delay: 10000, hoverPause: true });
            });
      </script>
  ```
  
  Second: copy lfstheme/templates/lfs/shop/shop.html to your theme and add:
  ```html
    {% load lfs_carousel_tags %}
    (...)
    {% carousel_show shop %}
  ```
  
* run syncdb (!)
