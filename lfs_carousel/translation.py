try:
    from modeltranslation.translator import translator, TranslationOptions
    from .models import CarouselItem

    # CarouselItem
    class CarouselItemTranslationOptions(TranslationOptions):
        fields = ('title', 'link', 'text')

    translator.register(CarouselItem, CarouselItemTranslationOptions)
except ImportError:
    pass
