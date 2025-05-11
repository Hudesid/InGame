from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.attributes.serializers import Attribute
from apps.desktop_types.models import DesktopType
from apps.payment_types.models import PaymentType
from apps.products.models import Product, ProductImage
from apps.categories.models import Category
from apps.brands.models import Brand
from apps.banners.models import Banner
from apps.statuses.models import Status
from apps.catalogs.models import Catalog
from apps.news.models import New
from apps.leave_requests.models import LeaveRequest
from apps.services.models import Service, ServiceName
from apps.commits.models import Comment, DesktopComment, ProductComment
from apps.delivery_methods.models import DeliveryMethod
from apps.orders.models import Order, OrderDesktopItem, OrderProductItem
from apps.desktops.models import Desktop, DesktopImage
from apps.desktops_fps.models import Fps, Game
from apps.product_types.models import ProductType
from apps.trade_in.models import TradeIn
from apps.users.models import User
from rest_framework import serializers
from apps.users.models import Role
from apps.credits.models import Credit


class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get(self.username_field)
        password = attrs.get('password')
        User = get_user_model()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"error": 'No user found with the provided credentials'})

        if not user.check_password(password):
            raise serializers.ValidationError({"error": 'No active account found with the given credentials'})

        if not user.is_active:
            raise serializers.ValidationError({"error": 'User account is not active'})

        authenticate_kwargs = {
            self.username_field: email,
            'password': password
        }

        request = self.context.get('request')
        if request:
            authenticate_kwargs['request'] = request
        else:
            raise serializers.ValidationError({"error": 'Request context missing'})

        user = authenticate(**authenticate_kwargs)

        if user is None:
            raise serializers.ValidationError({"error": 'No active account found with the given credentials'})

        data = super().validate(attrs)
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name_uz', 'name_ru', 'image', 'description_uz', 'description_ru')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'type_uz', 'type_ru', 'value', 'category')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        representation['category'] = CategorySerializer(instance.category).data
        return representation



class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(max_length=128, write_only=True, required=True)
    password = serializers.CharField(max_length=128, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'password', 'password_confirmation', 'email', 'phone', 'role', 'is_active', 'is_staff', 'is_superuser')


    def validate(self, data):
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password or password_confirmation:
            if not password and not password_confirmation:
                raise serializers.ValidationError({"Both password and password confirmation are required."})
            if password != password_confirmation:
                raise serializers.ValidationError({"Passwords do not match."})

        return data


    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        return User.objects.create_user(**validated_data)


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date_joined'] = instance.date_joined
        representation['updated_at'] = instance.updated_at
        representation['role'] = RoleSerializer(instance.role).data
        return representation


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = ('id', 'name', 'bank_credit', 'logo', 'months')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ('id', 'name')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'product')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = instance.product.__str__()
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name_uz', 'name_ru', 'description_uz', 'description_ru', 'price', 'category', 'brand', 'discount', 'attributes', 'statuses', 'type', 'images')


    def create(self, validated_data):
        images = validated_data.pop('images', [])
        attributes = validated_data.pop('attributes', [])
        statuses = validated_data.pop('statuses', [])
        product = Product.objects.create(**validated_data)

        for image in images:
            ProductImage.objects.create(product=product, image=image)

        product.attributes.set(attributes)
        product.statuses.set(statuses)
        product.save()
        return product


    def update(self, instance, validated_data):
        attributes = validated_data.pop('attributes', [])
        statuses = validated_data.pop('statuses', [])

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.attributes.set(attributes)
        instance.statuses.set(statuses)
        instance.save()
        return instance


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        representation['category'] = CategorySerializer(instance.category).data
        representation['brand'] = BrandSerializer(instance.brand).data
        representation['attributes'] = AttributeSerializer(instance.attributes, many=True).data
        representation['statuses'] = StatusSerializer(instance.statuses, many=True).data
        representation['type'] = ProductTypeSerializer(instance.type).data
        representation['images'] = ProductImageSerializer(instance.images, many=True).data
        return representation


class DesktopTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesktopType
        fields = ('id', 'name')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class DesktopShortSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='desktop',
        lookup_field='slug'
    )

    class Meta:
        model = Desktop
        fields = ('id', 'name_uz', 'name_ru', 'url')


class GameSerializer(serializers.ModelSerializer):
    desktop_count = serializers.SerializerMethodField()
    desktops = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ('id', 'game_name', 'game_image', 'desktop_count', 'desktops')


    def create(self, validated_data):
        game_exists = Game.objects.filter(game_name=validated_data.get('game_name'))

        if game_exists:
            raise serializers.ValidationError("A game with this name already exists.")

        game = Game.objects.create(**validated_data)

        return game


    def update(self, instance, validated_data):
        game_exists = Game.objects.filter(game_name=validated_data.get('game_name'))

        if game_exists:
            raise ValueError({"errors": "A game with this name already exists."})

        for key, value in validated_data.items():
            setattr(instance, key, value)

        return instance


    def get_desktop_count(self, obj):
        return obj.fps.values('desktop').distinct().count()


    def get_desktops(self, obj):
        desktop_ids = obj.fps.values_list('desktop', flat=True).distinct()
        desktops = Desktop.objects.filter(id__in=desktop_ids)
        return DesktopShortSerializer(desktops, many=True, context={'request': self.context.get('request')}).data


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class GameShorterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'game_name', 'game_image')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class FpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fps
        fields = ('id', 'game_fps', 'desktop', 'game')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['game'] = GameShorterSerializer(instance.game).data
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class DesktopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesktopImage
        fields = ('id', 'image', 'desktop')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['desktop'] = instance.desktop.__str__()
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class DesktopSerializer(serializers.ModelSerializer):
    desktop_fps = serializers.ListField(child=serializers.DictField(), write_only=True)
    images = serializers.ListField(child=serializers.ImageField(), write_only=True)

    class Meta:
        model = Desktop
        fields = ('id', 'name_uz', 'name_ru', 'type', 'images', 'desktop_types', 'description_uz', 'description_ru', 'price', 'statuses', 'products', 'category', 'desktop_fps', 'attributes')


    def create(self, validated_data):
        attributes = validated_data.pop('attributes', [])
        desktop_types = validated_data.pop('desktop_types', [])
        statuses = validated_data.pop('statuses', [])
        products = validated_data.pop('products', [])
        images = validated_data.pop('images', [])
        desktop_fps = validated_data.pop('desktop_fps', [])

        desktop = Desktop.objects.create(**validated_data)

        for image in images:
            if not DesktopImage.objects.filter(desktop=desktop, image=image).exists():
                DesktopImage.objects.create(desktop=desktop, image=image)

        for fps in desktop_fps:
            game_id = fps.get('game_id')
            game_fps = fps.get('game_fps')
            game = Game.objects.get(id=game_id)

            if not Fps.objects.filter(game=game, desktop=desktop):
                Fps.objects.create(game=game, desktop=desktop, game_fps=game_fps)

        desktop.products.set(products)
        desktop.statuses.set(statuses)
        desktop.desktop_types.set(desktop_types)
        desktop.attributes.set(attributes)
        desktop.save()
        return desktop


    def update(self, instance, validated_data):
        attributes = validated_data.pop('attributes', [])
        desktop_types = validated_data.pop('desktop_types', [])
        statuses = validated_data.pop('statuses', [])
        products = validated_data.pop('products', [])
        images = validated_data.pop('images', [])
        desktop_fps = validated_data.pop('desktop_fps', [])

        for key, value in validated_data.items():
            setattr(instance, key, value)

        for image in images:
            if not DesktopImage.objects.filter(desktop=instance, image=image).exists():
                DesktopImage.objects.create(desktop=instance, image=image)

        for fps_data in desktop_fps:
            game = fps_data.get('game')
            game_fps = fps_data.get('game_fps')
            game = Game.objects.get(id=game)

            Fps.objects.update_or_create(
                game=game,
                desktop=instance,
                defaults={'game_fps': game_fps}
            )


        instance.products.set(products)
        instance.statuses.set(statuses)
        instance.desktop_types.set(desktop_types)
        instance.attributes.set(attributes)
        instance.save()
        return instance


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['attributes'] = AttributeSerializer(instance.attributes, many=True).data
        representation['fps'] = FpsSerializer(instance.fps, many=True).data
        representation['desktop_types'] = DesktopTypeSerializer(instance.desktop_types, many=True).data
        representation['statuses'] = StatusSerializer(instance.statuses, many=True).data
        representation['products'] = ProductSerializer(instance.products, many=True).data
        representation['images'] = DesktopImageSerializer(instance.images, many=True).data
        representation['category'] = CategorySerializer(instance.category).data
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class DeliveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMethod
        fields = ('id', 'name_uz', 'name_ru', 'price', 'estimated_delivery_time', 'logo')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class OrderShortSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="order-detail", lookup_field='pk')

    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'customer_phone', 'address', 'url')


class OrderProductItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProductItem
        fields = ('id', 'product', 'order', 'credit', 'credit_term', 'quantity')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['order'] = OrderShortSerializer(instance.order, context={"request": self.context['request']}).data
        representation['product'] = instance.product.__str__()
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class OrderDesktopItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDesktopItem
        fields = ('id', 'desktop', 'order', 'credit', 'credit_term', 'quantity', 'edit_product')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['order'] = OrderShortSerializer(instance.order, context={"request": self.context['request']}).data
        representation['edit_product'] = [product.__str__() for product in instance.edit_product.all()]
        representation['desktop'] = instance.desktop.__str__()
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.ListField(child=serializers.DictField(), write_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'customer_phone', 'address', 'comment', 'delivery_method', 'total_price', 'status', 'products')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = {"request": self.context['request']}
        products = []
        products += OrderProductItemSerializer(instance.product_items, many=True, context=request).data
        products += OrderDesktopItemSerializer(instance.desktop_items, many=True, context=request).data
        representation['products'] = products
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        representation['delivery_method'] = DeliveryMethodSerializer(instance.delivery_method).data
        return representation


    def create(self, validated_data):
        products = validated_data.pop('products', [])
        order = Order.objects.create(**validated_data)

        for product_data in products:
            if 'desktop' in product_data:
                desktop_id = product_data.pop('desktop')
                credit_id = product_data.pop('credit')
                edit_products_list = product_data.pop('edit_product', [])

                desktop = Desktop.objects.get(id=desktop_id)
                credit = Credit.objects.get(id=credit_id)
                edit_products = Product.objects.filter(id__in=edit_products_list)

                item = OrderDesktopItem.objects.create(
                    desktop=desktop,
                    order=order,
                    credit=credit,
                    **product_data
                )
                item.edit_product.set(edit_products)
            else:
                product_id = product_data.pop('product')
                credit_id = product_data.pop('credit')

                product = Product.objects.get(id=product_id)
                credit = Credit.objects.get(id=credit_id)

                OrderProductItem.objects.create(
                    product=product,
                    order=order,
                    credit=credit,
                    **product_data
                )

        return order


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ('id', 'name')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id', 'name_uz', 'name_ru', 'description_uz', 'description_ru', 'url', 'image')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('username', 'comment_uz', 'comment_ru', 'description_uz', 'description_ru', 'image', 'video')


    def validate_video(self, value):
        max_size = 500 * 1024 * 1024
        if value and value.size > max_size:
            raise serializers.ValidationError("Video 500 MB dan katta bo'lishi mumkin emas.")
        return value


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = ('id', 'product', 'username', 'comment', 'image', 'rating')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class DesktopCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesktopComment
        fields = ('id', 'desktop', 'username', 'comment', 'image', 'rating')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class ServiceShortNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceName
        fields = ('id', 'name')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class ServiceSerializer(serializers.ModelSerializer):
    services = serializers.ListField(child=serializers.CharField(max_length=255), write_only=True)

    class Meta:
        model = Service
        fields = ('id', 'name', 'phone', 'type', 'price', 'status', 'other_services', 'services')


    def create(self, validated_data):
        services = validated_data.pop('services', [])
        service = Service.objects.create(**validated_data)

        for name in services:
            ServiceName.objects.create(name=name, service=service)

        return service


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['services'] = ServiceShortNameSerializer(instance.services, many=True).data
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class ServiceShortSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='service-detail', lookup_field='pk')

    class Meta:
        model = Service
        fields = ('id', 'name', 'phone', 'url')


class ServiceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceName
        fields = ('id', 'name', 'service')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['service'] = ServiceShortSerializer(instance.service, context={"request": self.context['request']}).data
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'youtube_url')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class TradeInSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeIn
        fields = ('id', 'name', 'phone', 'telegram_nik', 'config')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ('id', 'name_uz', 'name_ru', 'image', 'type')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = ('id', 'name', 'phone', 'operator_commit', 'status')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at
        representation['updated_at'] = instance.updated_at
        return representation