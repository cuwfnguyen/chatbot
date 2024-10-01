
def check_product_quality(product_name):
    return f"Chất lượng sản phẩm {product_name} được đánh giá rất cao"

def check_product_origin(product_name):
    return f"Sản phẩm {product_name} với nguồn gốc tự nhiên"

def check_product_features(product_name):
    return f"Sản phẩm {product_name} có tất cả 9 màu sắc và kích cỡ"

def check_product_uses(product_name):
    return f"Sản phẩm {product_name} sẽ giúp bạn dọn sạch nhà trong 30 phút"

def check_user_guide(product_name):
    return f"Vui lòng xem hướng dẫn sử dụng sản phẩm {product_name} tại phần mô tả sản phẩm"

def check_promotion_coupon(tenant_id):
    return f"Hiện {tenant_id} không có CTKM"

def check_product_quantity(product_name):
    return f"Sản phẩm {product_name} hiện số lượng còn 123 chiếc"

def check_warranty_period(product_name):
    return f"Thời gian bảo hành sản phẩm {product_name} từ 12 tháng"

def check_warranty_guide(product_name):
    return f"Hướng dẫn bảo hành sp {product_name} có tại phần mô tả sản phẩm"

def check_return_policy(product_name):
    return f"Hiện chưa có chính sách đổi trả với sp {product_name}"

def check_shipping_price(order_id):
    return f"Đơn hàng {order_id} có phí giao hàng là 12000đ"

def check_shipping_time(order_id):
    return f"Đơn hàng {order_id} sẽ được giao vào 2 ngày làm việc"

def check_payment_method(product_name):
    return f"Hình thức thanh toán {product_name} là tiền mặt"

def check_shipping_status(order_id):
    return f"Đơn hàng {order_id} của bạn hiện đang ở 'Ba Dinh LM Hub'"

def change_delivery_address(order_id):
    return f"Đơn hàng {order_id} đang vận chuyển, không thể thay đổi"

def cancel_order(order_id):
    return f"Đơn hàng {order_id} của bạn không thể hủy do đang vận chuyển"

def send_to_customer_service(order_id):
    return f"Cảm ơn bạn vì phản hồi với đơn hàng {order_id}. Chúng tôi đang xem xét và sớm trả lời."

def get_additional_info(agent_code, additional_info):
    if agent_code == 4:
        return f"\nBạn có thể xem hình ảnh thật của sản phẩm {additional_info.get('product_name', '')} trên trang mua hàng."
    else: return ''


def define_function(agent_code):
    function = {}
    if agent_code == 1:
        function = {
                "name": "check_product_quality",
                "description": "Kiểm tra chất lượng sản phẩm",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_name": {
                            "type": "string",
                            "description": "Tên sản phẩm"
                        }
                    },
                    "required": ["product_name"]
                }
            }
    elif agent_code == 2:
        function = {
            "name": "check_product_origin",
            "description": "Kiểm tra nguồn gốc sản phẩm",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "Tên sản phẩm"
                    }
                },
                "required": ["product_name"]
            }
        }
    elif agent_code == 3:
        function = {
            "name": "check_product_features",
            "description": "Kiểm tra đặc tính sản phẩm",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "Tên sản phẩm"
                    }
                },
                "required": ["product_name"]
            }
        }
    elif agent_code == 5:
        function = {
            "name": "check_product_uses",
            "description": "Check công dụng sản phẩm",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "Tên sản phẩm"
                    }
                },
                "required": ["product_name"]
            }
        }
    elif agent_code == 6:
        function = {
            "name": "check_user_guide",
            "description": "Kiểm tra hướng dẫn sử dụng sản phẩm",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "Tên sản phẩm"
                    }
                },
                "required": ["product_name"]
            }
        }
    elif agent_code == 7:
        function = {
            "name": "check_promotion_coupon",
            "description": "Kiểm tra mã giảm giá, khuyến mãi",
            "parameters": {
                "type": "object",
                "properties": {
                    "tenant_id": {
                        "type": "string",
                        "description": "Mã shop"
                    }
                }
            }
        }
    elif agent_code == 8:
        function = {
            "name": "check_product_quantity",
            "description": "Kiểm tra sản phẩm còn lại",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "Tên sản phẩm"
                    }
                },
                "required": ["product_name"]
            }
        }
    elif agent_code == 9:
        function = {
            "name": "check_warranty_period",
            "description": "Kiểm tra thời gian bảo hành",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "Tên sản phẩm"
                    }
                },
                "required": ["product_name"]
            }
        }
    elif agent_code == 10:
        function = {
            "name": "check_warranty_guide",
            "description": "Kiểm tra hướng dẫn bảo hành",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "Tên sản phẩm"
                    }
                },
                "required": ["product_name"]
            }
        }
    elif agent_code == 11:
        function = {
            "name": "check_return_policy",
            "description": "Kiểm tra chính sách đổi trả hàng",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "Tên sản phẩm"
                    }
                },
                "required": ["product_name"]
            }
        }
    elif agent_code == 12:
        function = {
            "name": "check_shipping_price",
            "description": "Kiểm tra phí giao hàng",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "Mã đơn hàng"
                    }
                },
                "required": ["order_id"]
            }
        }
    elif agent_code == 13:
        function = {
            "name": "check_shipping_time",
            "description": "Kiểm tra thời gian giao hàng",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "Mã đơn hàng"
                    }
                },
                "required": ["order_id"]
            }
        }
    elif agent_code == 14:
        function = {
            "name": "check_payment_method",
            "description": "Kiểm tra hình thức thanh toán",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "Tên sản phẩm"
                    }
                },
                "required": ["product_name"]
            }
        }

    elif agent_code == 17:
        function = {
            "name": "check_shipping_status",
            "description": "Kiểm tra trạng thái vận chuyển",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "Mã đơn hàng"
                    }
                },
                "required": ["order_id"]
            }
        }
    elif agent_code == 20:
        function = {
            "name": "change_delivery_address",
            "description": "Thay đổi địa chỉ nhận hàng",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "Mã đơn hàng"
                    }
                },
                "required": ["order_id"]
            }
        }
    elif agent_code == 21:
        function = {
            "name": "cancel_order",
            "description": "Huỷ đơn hàng",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "Mã đơn hàng"
                    }
                },
                "required": ["order_id"]
            }
        }
    elif agent_code in [22,23,24,25,26,27]:
        function = {
            "name": "send_to_customer_service",
            "description": "Gửi thông tin đến nhân viên tư vấn",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "Mã đơn hàng"
                    }
                },
                "required": ["order_id"]
            }
        }
    return function