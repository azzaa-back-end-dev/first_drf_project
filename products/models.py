from django.db import models
from django.utils.translation import gettext_lazy as _



class Category(models.Model):
    title = models.CharField(_("title"), max_length=100)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural=_("categories")

    def __str__(self):
        return self.title


class Manufacturer(models.Model):
    name = models.CharField(_("name"), max_length=100)

    class Meta:
        verbose_name = _("manufacturer")
        verbose_name_plural = _("manufacturers")

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"))
    discount = models.FloatField(_("discount"), default=0)
    price = models.FloatField(_("price"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.CASCADE)
    short_desc = models.TextField(_("short description"))
    manufacturer = models.ForeignKey(Manufacturer, verbose_name=_("manufacturer"), on_delete=models.CASCADE)
    view_count = models.IntegerField(_("view count"), default=0)


    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE,
                                related_name='product_images')
    image = models.ForeignKey("common.Media", verbose_name=_("image"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('product image')
        verbose_name_plural = _('product images')

    def __str__(self):
        return f"Image Id: {self.id}|Product: {self.product.title}"


class Characteristic(models.Model):
    title = models.CharField(_("title"), max_length=100)
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("characteristic")
        verbose_name_plural = _("characteristics")

    def __str__(self):
        return self.title


class CharacteristicValue(models.Model):
    title = models.CharField(_("title"), max_length=100)
    characteristic = models.ForeignKey(Characteristic, verbose_name=_("characteristic"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("characteristic value")
        verbose_name_plural = _("characteristic values")


class Instruction(models.Model):
    title = models.CharField(_("title"), max_length=100)
    desc = models.TextField(_("description"))
    left_image = models.ForeignKey("common.Media", verbose_name=_("left image"), on_delete=models.CASCADE,
                                   related_name='instructions_left_image')
    right_image = models.ForeignKey("common.Media", verbose_name=_("right image"), on_delete=models.CASCADE,
                                    related_name='instructions_right_image')

    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("instruction")
        verbose_name_plural = _("instructions")


    def __str__(self):
        return self.title


