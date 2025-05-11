import logging

from rest_framework import status
from rest_framework.views import APIView

logger = logging.getLogger(__name__)

"""
response structure

{
    status: True or False,
    message: "something"
    errors: {},
    data: {}
}
"""

responses_info = {
    "400": "Noto'g'ri ma'lumot kiritilgan.",
    "404": "DataNotFound",
    "user_create": "%s muvaffaqiyatli yaratildi.",
    "user_update": "%s muvaffaqiyatli yangilandi.",
    "user_delete": "User muvaffaqiyatli o'chirildi.",
    "user_info": "User ma'lumotlari muvaffaqiyatli olindi.",
    "attribute_create": "%s muvaffaqiyatli yaratildi.",
    "attribute_update": "%s muvaffaqiyatli yangilandi.",
    "attribute_delete": "Attribute muvaffaqiyatli o'chirildi.",
    "attribute_info": "Attribute ma'lumotlari muvaffaqiyatli olindi.",
    "banner_create": "%s muvaffaqiyatli yaratildi.",
    "banner_update": "%s muvaffaqiyatli yangilandi.",
    "banner_delete": "Banner muvaffaqiyatli o'chirildi.",
    "banner_info": "Banner ma'lumotlari muvaffaqiyatli olindi.",
    "brand_create": "%s muvaffaqiyatli yaratildi.",
    "brand_update": "%s muvaffaqiyatli yangilandi.",
    "brand_delete": "Brand muvaffaqiyatli o'chirildi.",
    "brand_info": "Brand ma'lumotlari muvaffaqiyatli olindi.",
    "catalog_create": "%s muvaffaqiyatli yaratildi.",
    "catalog_update": "%s muvaffaqiyatli yangilandi.",
    "catalog_delete": "Catalog muvaffaqiyatli o'chirildi.",
    "catalog_info": "Catalog ma'lumotlari muvaffaqiyatli olindi.",
    "category_create": "%s muvaffaqiyatli yaratildi.",
    "category_update": "%s muvaffaqiyatli yangilandi.",
    "category_delete": "Category muvaffaqiyatli o'chirildi.",
    "category_info": "Category ma'lumotlari muvaffaqiyatli olindi.",
    "comment_update": "Comment muvaffaqiyatli yangilandi.",
    "comment_delete": "Comment muvaffaqiyatli o'chirildi.",
    "comment_info": "Comment ma'lumotlari muvaffaqiyatli olindi.",
    "desktop_comment_update": "DesktopComment muvaffaqiyatli yangilandi.",
    "desktop_comment_delete": "DesktopComment muvaffaqiyatli o'chirildi.",
    "desktop_comment_info": "DesktopComment ma'lumotlari muvaffaqiyatli olindi.",
    "product_comment_update": "ProductComment muvaffaqiyatli yangilandi.",
    "product_comment_delete": "ProductComment muvaffaqiyatli o'chirildi.",
    "product_comment_info": "ProductComment ma'lumotlari muvaffaqiyatli olindi.",
    "credit_create": "%s muvaffaqiyatli yaratildi.",
    "credit_update": "%s muvaffaqiyatli yangilandi.",
    "credit_delete": "Credit muvaffaqiyatli o'chirildi.",
    "credit_info": "Credit ma'lumotlari muvaffaqiyatli olindi.",
    "delivery_method_create": "%s muvaffaqiyatli yaratildi.",
    "delivery_method_update": "%s muvaffaqiyatli yangilandi.",
    "delivery_method_delete": "DeliveryMethod muvaffaqiyatli o'chirildi.",
    "delivery_method_info": "DeliveryMethod ma'lumotlari muvaffaqiyatli olindi.",
    "desktop_type_create": "%s muvaffaqiyatli yaratildi.",
    "desktop_type_update": "%s muvaffaqiyatli yangilandi.",
    "desktop_type_delete": "DesktopType muvaffaqiyatli o'chirildi.",
    "desktop_type_info": "DesktopType ma'lumotlari muvaffaqiyatli olindi.",
    "desktop_create": "%s muvaffaqiyatli yaratildi.",
    "desktop_update": "%s muvaffaqiyatli yangilandi.",
    "desktop_delete": "Desktop muvaffaqiyatli o'chirildi.",
    "desktop_info": "Desktop ma'lumotlari muvaffaqiyatli olindi.",
    "game_create": "%s muvaffaqiyatli yaratildi.",
    "game_update": "%s muvaffaqiyatli yangilandi.",
    "game_delete": "Game muvaffaqiyatli o'chirildi.",
    "game_info": "Game ma'lumotlari muvaffaqiyatli olindi.",
    "fps_create": "Fps muvaffaqiyatli yaratildi.",
    "fps_update": "Fps muvaffaqiyatli yangilandi.",
    "fps_delete": "Fps muvaffaqiyatli o'chirildi.",
    "fps_info": "Fps ma'lumotlari muvaffaqiyatli olindi.",
    "desktop_image_create": "Desktop image muvaffaqiyatli yaratildi.",
    "desktop_image_update": "Desktop image muvaffaqiyatli yangilandi.",
    "desktop_image_delete": "Desktop image muvaffaqiyatli o'chirildi.",
    "desktop_image_info": "Desktop image ma'lumotlari muvaffaqiyatli olindi.",
    "product_image_create": "Product image muvaffaqiyatli yaratildi.",
    "product_image_update": "Product image muvaffaqiyatli yangilandi.",
    "product_image_delete": "Product image muvaffaqiyatli o'chirildi.",
    "product_image_info": "Product image ma'lumotlari muvaffaqiyatli olindi.",
    "leave_request_create": "Request muvaffaqiyatli yaratildi.",
    "leave_request_update": "Request muvaffaqiyatli yangilandi.",
    "leave_request_delete": "Request muvaffaqiyatli o'chirildi.",
    "leave_request_info": "Request ma'lumotlari muvaffaqiyatli olindi.",
    "new_create": "%s muvaffaqiyatli yaratildi.",
    "new_update": "%s muvaffaqiyatli yangilandi.",
    "new_delete": "New muvaffaqiyatli o'chirildi.",
    "new_info": "New ma'lumotlari muvaffaqiyatli olindi.",
    "order_create": "Order muvaffaqiyatli yaratildi.",
    "order_update": "Order muvaffaqiyatli yangilandi.",
    "order_delete": "Order muvaffaqiyatli o'chirildi.",
    "order_info": "Order ma'lumotlari muvaffaqiyatli olindi.",
    "order_desktop_create": "OrderDesktopItem muvaffaqiyatli yaratildi.",
    "order_desktop_update": "OrderDesktopItem muvaffaqiyatli yangilandi.",
    "order_desktop_delete": "OrderDesktopItem muvaffaqiyatli o'chirildi.",
    "order_desktop_info": "OrderDesktopItem ma'lumotlari muvaffaqiyatli olindi.",
    "order_product_create": "OrderProductItem muvaffaqiyatli yaratildi.",
    "order_product_update": "OrderProductItem muvaffaqiyatli yangilandi.",
    "order_product_delete": "OrderProductItem muvaffaqiyatli o'chirildi.",
    "order_product_info": "OrderProductItem ma'lumotlari muvaffaqiyatli olindi.",
    "payment_type_create": "%s muvaffaqiyatli yaratildi.",
    "payment_type_update": "%s muvaffaqiyatli yangilandi.",
    "payment_type_delete": "PaymentType muvaffaqiyatli o'chirildi.",
    "payment_type_info": "PaymentType ma'lumotlari muvaffaqiyatli olindi.",
    "product_type_create": "%s muvaffaqiyatli yaratildi.",
    "product_type_update": "%s muvaffaqiyatli yangilandi.",
    "product_type_delete": "ProductType muvaffaqiyatli o'chirildi.",
    "product_type_info": "ProductType ma'lumotlari muvaffaqiyatli olindi.",
    "product_create": "%s muvaffaqiyatli yaratildi.",
    "product_update": "%s muvaffaqiyatli yangilandi.",
    "product_delete": "Product muvaffaqiyatli o'chirildi.",
    "product_info": "Product ma'lumotlari muvaffaqiyatli olindi.",
    "service_create": "Service muvaffaqiyatli yaratildi.",
    "service_update": "Service muvaffaqiyatli yangilandi.",
    "service_delete": "Service muvaffaqiyatli o'chirildi.",
    "service_info": "Service ma'lumotlari muvaffaqiyatli olindi.",
    "service_name_create": "%s muvaffaqiyatli yaratildi.",
    "service_name_update": "%s muvaffaqiyatli yangilandi.",
    "service_name_delete": "ServiceName muvaffaqiyatli o'chirildi.",
    "service_name_info": "ServiceName ma'lumotlari muvaffaqiyatli olindi.",
    "status_create": "%s muvaffaqiyatli yaratildi.",
    "status_update": "%s muvaffaqiyatli yangilandi.",
    "status_delete": "Status muvaffaqiyatli o'chirildi.",
    "status_info": "Status ma'lumotlari muvaffaqiyatli olindi.",
    "trade_in_create": "TradeIn muvaffaqiyatli yaratildi.",
    "trade_in_update": "TradeIn muvaffaqiyatli yangilandi.",
    "trade_in_delete": "TradeIn muvaffaqiyatli o'chirildi.",
    "trade_in_info": "TradeIn ma'lumotlari muvaffaqiyatli olindi.",
    "role_create": "%s muvaffaqiyatli yaratildi.",
    "role_update": "%s muvaffaqiyatli yangilandi.",
    "role_delete": "Role muvaffaqiyatli o'chirildi.",
    "role_info": "Role ma'lumotlari muvaffaqiyatli olindi.",
    "login": "Tizimga muvaffaqiyatli kirildi.",
    "refresh": "Token muvaffaqiyatli yangilandi.",
    "brand_list": "Brand lar ro'yxati muvaffaqiyatli olindi.",
    "brand_detail": "Brand malumotlari muvaffaqiyatli olindi.",
    "product_list": "Product lar ro'yxati muvaffaqiyatli olindi.",
    "product_detail": "Product ma'lumotlari muvaffaqiyatli olindi.",
    "category_list": "Category lar ro'yxati muvaffaqiyatli olindi.",
    "category_detail": "Category ma'lumotlari muvaffiqiyatli olindi.",
    "game_list": "Game ro'yxati muvaffaqiyatli olindi.",
    "game_detail": "Game ma'lumotlari muvaffaqiyatli olindi.",
    "desktop_list": "Desktop ro'yxati muvaffaqiyatli olindi.",
    "desktop_detail": "Desktop ma'lumotlari muvaffaqiyatli olindi.",
    "delivery_method_list": "Delivery ro'yxati muvaffaqiyatli olindi.",
    "delivery_method_detail": "Delivery ma'lumotlari muvaffaqiyatli olindi.",
    "payment_type_list": "Payment type ro'yxati muvaffaqiyatli olindi.",
    "payment_type_detail": "Payment type ma'lumotlari muvaffaqiyatli olindi.",
    "banner_list": "Banner ro'yxati muvaffaqiyatli olindi.",
    "banner_detail": "Banner ma'lumotlari muvaffaqiyatli yangilandi.",
    "comment_list": "Comment ro'yxati muvaffaqiyatli olindi.",
    "comment_detail": "Comment ma'lumotlari muvaffaqiyatli olindi.",
    "comment_create": "Comment muvaffaqiyatli yaratildi.",
    "product_comment_list": "ProductComment ro'yxati muvaffaqiyatli olindi.",
    "product_comment_create": "ProductComment muvaffaqiyatli yaratildi.",
    "desktop_comment_list": "DesktopComment ro'yxati muvaffaqiyatli olindi.",
    "desktop_comment_create": "DesktopComment muvaffaqiyatli yaratildi.",
    "new_list": "New ro'yxati muvaffaqiyatli olindi.",
    "new_detail": "New ma'lumotlari muvaffaqiyatli olindi.",
    "catalog_list": "Catalog ro'yxati muvaffaqiyatli olindi.",
    "catalog_detail": "Catalog ma'lumotlari muvaffaqiyatli olindi.",
    "credit_list": "Credit ro'yxati muvaffaqiyatli olindi.",
    "credit_detail": "Credit ma'lumotlari muvaffaqiyatli olindi.",
    "search": "Ma'lumotlar muvaffaqiyatli olindi.",
    "product_type_list": "Product type ro'yxati muvaffaqiyatli olindi.",
    "product_type_detail": "Product type ma'lumotlari muvaffaqiyatli olindi.",
}


def custom_response(mark):
    def decorator(view):
        def inner(self, request, *args, **kwargs):
            response = super(view, self).dispatch(request, *args, **kwargs)
            response_data = response.data
            data = dict(
                status=True,
                message="",
                errors={},
                data={},
            )
            if response.exception:
                data["status"] = False
                if response.status_code == status.HTTP_400_BAD_REQUEST:
                    data["message"] = responses_info["400"]
                if response.status_code == status.HTTP_404_NOT_FOUND:
                    data['message'] = responses_info['404']
                data['errors'] = response_data
                logger.error(f"Error occurred: {response_data}")
            else:
                data["data"] = response_data

                if mark == "login":
                    data['message'] = responses_info['login']

                elif mark == "refresh":
                    data['message'] = responses_info['refresh']

                elif mark == "brand_list":
                    data['message'] = responses_info['brand_list']

                elif mark == "brand_detail":
                    data['message'] = responses_info['brand_detail']

                elif mark == "product_list":
                    data['message'] = responses_info['product_list']

                elif mark == "product_detail":
                    data['message'] = responses_info['product_detail']

                elif mark == "category_list":
                    data['message'] = responses_info['category_list']

                elif mark == "category_detail":
                    data['message'] = responses_info['category_detail']

                elif mark == "comment_detail":
                    data['message'] = responses_info['comment_detail']

                elif mark == "game_list":
                    data['message'] = responses_info['game_list']

                elif mark == "game_detail":
                    data['message'] = responses_info['game_detail']

                elif mark == "desktop_list":
                    data['message'] = responses_info['desktop_list']

                elif mark == "desktop_detail":
                    data['message'] = responses_info['desktop_detail']

                elif mark == "delivery_method_list":
                    data['message'] = responses_info['delivery_method_list']

                elif mark == "delivery_method_detail":
                    data['message'] = responses_info['delivery_method_detail']

                elif mark == "order_create":
                    data['message'] = responses_info['order_create']

                elif mark == "payment_type_list":
                    data['message'] = responses_info['payment_type_list']

                elif mark == "payment_type_detail":
                    data['message'] = responses_info['payment_type_detail']

                elif mark == "banner_list":
                    data['message'] = responses_info["banner_list"]

                elif mark == "banner_detail":
                    data['message'] = responses_info['banner_detail']

                elif mark == "comment_list_create":
                    data['message'] = (responses_info["comment_list"] if request.method == 'GET' else responses_info['comment_create'])

                elif mark == "product_comment_list_create":
                    data['message'] = (responses_info["product_comment_list"] if request.method == 'GET' else responses_info['product_comment_create'])

                elif mark == "desktop_comment_list_create":
                    data['message'] = (responses_info["desktop_comment_list"] if request.method == 'GET' else responses_info["desktop_comment_create"])

                elif mark == "service_create":
                    data['message'] = responses_info["service_create"]

                elif mark == "new_list":
                    data['message'] = responses_info["new_list"]

                elif mark == "new_detail":
                    data['message'] = responses_info["new_detail"]

                elif mark == "trade_in_create":
                    data['message'] = responses_info["trade_in_create"]

                elif mark == "catalog_list":
                    data['message'] = responses_info["catalog_list"]

                elif mark == "catalog_detail":
                    data['message'] = responses_info["catalog_detail"]

                elif mark == "search":
                    data['message'] = responses_info["search"]

                elif mark == "credit_list":
                    data['message'] = responses_info["credit_list"]

                elif mark == "credit_detail":
                    data['message'] = responses_info["credit_detail"]

                elif mark == "product_type_list":
                    data['message'] = responses_info["product_type_list"]

                elif mark == "product_type_detail":
                    data['message'] = responses_info["product_type_detail"]

                elif mark == "leave_request_create":
                    data['message'] = responses_info["leave_request_create"]

                elif mark == "user":
                    data['message'] = (responses_info["user_create"] % f" {response_data.get("last_name")} {response_data.get("first_name")}" if request.method == 'POST'
                                        else responses_info["user_update"] % f" {response_data.get("last_name")} {response_data.get("first_name")}" if request.method in ("PUT", "PATCH")
                                        else responses_info["user_delete"] if request.method == 'DELETE'
                                        else responses_info["user_info"])

                elif mark == "attribute":
                    data['message'] = (responses_info["attribute_create"] % f" << Uz: {response_data.get("type_uz")}, Ru: {response_data.get("type_ru")} >>" if request.method == 'POST'
                                        else responses_info["attribute_update"] % f" << Uz: {response_data.get("type_uz")}, Ru: {response_data.get("type_ru")} >>" if request.method in ("PUT", "PATCH")
                                        else responses_info["attribute_delete"] if request.method == 'DELETE'
                                        else responses_info["attribute_info"])

                elif mark == "banner":
                    data['message'] = (responses_info["banner_create"] % f" << Uz: {response_data.get("name_uz")}, Ru: {response_data.get("name_ru")} >>" if request.method == 'POST'
                                        else responses_info["banner_update"] % f" << Uz: {response_data.get("name_uz")}, Ru: {response_data.get("name_ru")} >>" if request.method in ("PUT", "PATCH")
                                        else responses_info["banner_delete"] if request.method == 'DELETE'
                                        else responses_info["banner_info"])

                elif mark == "brand":
                    data['message'] = (responses_info["brand_create"] % response_data.get("name") if request.method == 'POST'
                                        else responses_info["brand_update"] % response_data.get("name") if request.method in ("PUT", "PATCH")
                                        else responses_info["brand_delete"] if request.method == 'DELETE'
                                        else responses_info["brand_info"])

                elif mark == "catalog":
                    data['message'] = (responses_info["catalog_create"] % f" << Uz: {response_data.get("name_uz")}, Ru: {response_data.get("name_ru")} >>" if request.method == 'POST'
                                        else responses_info["catalog_update"] % f" << Uz: {response_data.get("name_uz")}, Ru: {response_data.get("name_ru")} >>" if request.method in ("PUT", "PATCH")
                                        else responses_info["catalog_delete"] if request.method == 'DELETE'
                                        else responses_info["catalog_info"])

                elif mark == "category":
                    data['message'] = (responses_info["category_create"] % f" << Uz: {response_data.get("name_uz")}, Ru: {response_data.get("name_ru")} >>" if request.method == 'POST'
                                        else responses_info["category_update"] % f" << Uz: {response_data.get("name_uz")}, Ru: {response_data.get("name_ru")} >>" if request.method in ("PUT", "PATCH")
                                        else responses_info["category_delete"] if request.method == 'DELETE'
                                        else responses_info["category_info"])

                elif mark == "comment":
                    data['message'] = (responses_info["comment_create"] if request.method == 'POST'
                                        else responses_info["comment_update"] if request.method in ("PUT", "PATCH")
                                        else responses_info["comment_delete"] if request.method == 'DELETE'
                                        else responses_info["comment_info"])

                elif mark == "desktop_comment":
                    data['message'] = (responses_info["desktop_comment_create"] if request.method == 'POST'
                                        else responses_info["desktop_comment_update"] if request.method in ("PUT", "PATCH")
                                        else responses_info["desktop_comment_delete"] if request.method == 'DELETE'
                                        else responses_info["desktop_comment_info"])

                elif mark == "product_comment":
                    data['message'] = (responses_info["product_comment_create"] if request.method == 'POST'
                                        else responses_info["product_comment_update"] if request.method in ("PUT", "PATCH")
                                        else responses_info["product_comment_delete"] if request.method == 'DELETE'
                                        else responses_info["product_comment_info"])

                elif mark == "credit":
                    data['message'] = (responses_info["credit_create"] % response_data.get("name") if request.method == 'POST'
                                        else responses_info["credit_update"] % response_data.get("name") if request.method in ("PUT", "PATCH")
                                        else responses_info["credit_delete"] if request.method == 'DELETE'
                                        else responses_info["credit_info"])

                elif mark == "delivery_method":
                    data['message'] = (responses_info["delivery_method_create"] % f" << Uz: {response_data.get("name_uz")}, Ru: {response_data.get("name_ru")} >>" if request.method == 'POST'
                                        else responses_info["delivery_method_update"] % f" << Uz: {response_data.get("name_uz")}, Ru: {response_data.get("name_ru")} >>" if request.method in ("PUT", "PATCH")
                                        else responses_info["delivery_method_delete"] if request.method == 'DELETE'
                                        else responses_info["delivery_method_info"])

                elif mark == "desktop_type":
                    data['message'] = (responses_info["desktop_type_create"] % response_data.get("name") if request.method == 'POST'
                                        else responses_info["desktop_type_update"] % response_data.get("name") if request.method in ("PUT", "PATCH")
                                        else responses_info["desktop_type_delete"] if request.method == 'DELETE'
                                        else responses_info["desktop_type_info"])

                elif mark == "desktop":
                    data['message'] = (responses_info["desktop_create"] % f" << Uz: {response_data.get("name_uz")}, Ru: {response_data.get("name_ru")} >>" if request.method == 'POST'
                                        else responses_info["desktop_update"] % f" << Uz: {response_data.get("name_uz")}, Ru: {response_data.get("name_ru")} >>" if request.method in ("PUT", "PATCH")
                                        else responses_info["desktop_delete"] if request.method == 'DELETE'
                                        else responses_info["desktop_info"])

                elif mark == "game":
                    data['message'] = (responses_info["game_create"] % response_data.get("game_name") if request.method == 'POST'
                                        else responses_info["game_update"] % response_data.get("game_name") if request.method in ("PUT", "PATCH")
                                        else responses_info["game_delete"] if request.method == 'DELETE'
                                        else responses_info["game_info"])

                elif mark == "fps":
                    data['message'] = (responses_info["fps_create"] if request.method == 'POST'
                                        else responses_info["fps_update"] if request.method in ("PUT", "PATCH")
                                        else responses_info["fps_delete"] if request.method == 'DELETE'
                                        else responses_info["fps_info"])

                elif mark == "desktop_image":
                    data['message'] = (responses_info["desktop_image_create"] if request.method == 'POST'
                                        else responses_info["desktop_image_update"] if request.method in ("PUT", "PATCH")
                                        else responses_info["desktop_image_delete"] if request.method == 'DELETE'
                                        else responses_info["desktop_image_info"])

                elif mark == "product_image":
                    data['message'] = (responses_info["product_image_create"] if request.method == 'POST'
                                        else responses_info["product_image_update"] if request.method in ("PUT", "PATCH")
                                        else responses_info["product_image_delete"] if request.method == 'DELETE'
                                        else responses_info["product_image_info"])

                elif mark == "leave_request":
                    data['message'] = (responses_info["leave_request_create"] if request.method == 'POST'
                                        else responses_info["leave_request_update"] if request.method in ("PUT", "PATCH")
                                        else responses_info["leave_request_delete"] if request.method == 'DELETE'
                                        else responses_info["leave_request_info"])

                elif mark == "new":
                    data['message'] = (responses_info["new_create"] % f" << Uz: {response_data.get("title_uz")}, Ru: {response_data.get("title_ru")} >>" if request.method == 'POST'
                                        else responses_info["new_update"] % f" << Uz: {response_data.get("title_uz")}, Ru: {response_data.get("title_ru")} >>" if request.method in ("PUT", "PATCH")
                                        else responses_info["new_delete"] if request.method == 'DELETE'
                                        else responses_info["new_info"])

                elif mark == "order":
                    data['message'] = (responses_info["order_create"] if request.method == 'POST'
                                        else responses_info["order_update"] if request.method in ("PUT", "PATCH")
                                        else responses_info["order_delete"] if request.method == 'DELETE'
                                        else responses_info["order_info"])

                elif mark == "order_desktop":
                    data['message'] = (responses_info["order_desktop_create"] if request.method == 'POST'
                                        else responses_info["order_desktop_update"] if request.method in ("PUT", "PATCH")
                                        else responses_info["order_desktop_delete"] if request.method == 'DELETE'
                                        else responses_info["order_desktop_info"])

                elif mark == "order_product":
                    data['message'] = (responses_info["order_product_create"] if request.method == 'POST'
                                        else responses_info["order_product_update"] if request.method in ("PUT", "PATCH")
                                        else responses_info["order_product_delete"] if request.method == 'DELETE'
                                        else responses_info["order_product_info"])

                elif mark == "payment_type":
                    data['message'] = (responses_info["payment_type_create"] % response_data.get("name") if request.method == 'POST'
                                        else responses_info["payment_type_update"] % response_data.get("name") if request.method in ("PUT", "PATCH")
                                        else responses_info["payment_type_delete"] if request.method == 'DELETE'
                                        else responses_info["payment_type_info"])

                elif mark == "product_type":
                    data['message'] = (responses_info["product_type_create"] % response_data.get("name") if request.method == 'POST'
                                        else responses_info["product_type_update"] % response_data.get("name") if request.method in ("PUT", "PATCH")
                                        else responses_info["product_type_delete"] if request.method == 'DELETE'
                                        else responses_info["product_type_info"])

                elif mark == "product":
                    data['message'] = (responses_info["product_create"] % f" << Uz: {response_data.get("name_uz")}, Ru: {response_data.get("name_ru")} >>" if request.method == 'POST'
                                        else responses_info["product_update"] % f" << Uz: {response_data.get("name_uz")}, Ru: {response_data.get("name_ru")} >>" if request.method in ("PUT", "PATCH")
                                        else responses_info["product_delete"] if request.method == 'DELETE'
                                        else responses_info["product_info"])

                elif mark == "service":
                    data['message'] = (responses_info["service_create"] if request.method == 'POST'
                                        else responses_info["service_update"] if request.method in ("PUT", "PATCH")
                                        else responses_info["service_delete"] if request.method == 'DELETE'
                                        else responses_info["service_info"])

                elif mark == "service_name":
                    data['message'] = (responses_info["service_name_create"] % response_data.get("name") if request.method == 'POST'
                                        else responses_info["service_name_update"] % response_data.get("name") if request.method in ("PUT", "PATCH")
                                        else responses_info["service_name_delete"] if request.method == 'DELETE'
                                        else responses_info["service_name_info"])

                elif mark == "status":
                    data['message'] = (responses_info["status_create"] % response_data.get("name") if request.method == 'POST'
                                        else responses_info["status_update"] % response_data.get("name") if request.method in ("PUT", "PATCH")
                                        else responses_info["status_delete"] if request.method == 'DELETE'
                                        else responses_info["status_info"])

                elif mark == "trade_in":
                    data['message'] = (responses_info["trade_in_create"] if request.method == 'POST'
                                        else responses_info["trade_in_update"] if request.method in ("PUT", "PATCH")
                                        else responses_info["trade_in_delete"] if request.method == 'DELETE'
                                        else responses_info["trade_in_info"])

                elif mark == "role":
                    data['message'] = (responses_info["role_create"] % response_data.get("name") if request.method == 'POST'
                                        else responses_info["role_update"] % response_data.get("name") if request.method in ("PUT", "PATCH")
                                        else responses_info["role_delete"] if request.method == 'DELETE'
                                        else responses_info["role_info"])
            response.data = data
            return response

        assert issubclass(view, APIView), (
            "class %s must be subclass of APIView" % view.__class__
        )

        view.dispatch = inner
        return view
    return decorator
