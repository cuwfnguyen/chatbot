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
    order_info = order_information.get(order_id)
    return order_info


def check_shipping_time(order_id):
    order_info = order_information.get(order_id)
    return order_info


def check_payment_method(product_name):
    return f"Hình thức thanh toán {product_name} là tiền mặt"


def check_shipping_status(order_id):
    order_info = order_information.get(order_id)
    return order_info


def change_delivery_address(order_id):
    order_info = order_information.get(order_id)
    return order_info


def cancel_order(order_id):
    order_info = order_information.get(order_id)
    return order_info


def send_to_customer_service(order_id):
    return f"Cảm ơn bạn vì phản hồi với đơn hàng {order_id}. Chúng tôi đang xem xét và sớm trả lời."


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
    elif agent_code in [22, 23, 24, 25, 26, 27]:
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


order_information = {
    "Purchase01": {
        "state": "Đang vận chuyển",
        "location": "Ba Dinh LM Hub",
        "shipping_fee": 21000,
    },
    "Purchase02": {
        "state": "Đã hoàn thành",
        "location": "done",
        "shipping_fee": 22000,
    }
    , "Purchase03": {
        "state": "Đang vận chuyển",
        "location": "Bac Ninh LM Hub",
        "shipping_fee": 23000,
    }
}
product_information = {
    "1": {
        "version": "Ba màu xanh vàng trắng",
        "product_qty": 10,
        "payment_method": "cash",
        "description": """
        Máy hút bụi cầm tay SOKANY SK3386 công suất 3500W có 3 đầu hút, giảm tiếng ồn, thiết kế hiện đại lực hút mạnh làm sạch mọi ngóc ngách.
[HÀNG CHÍNH HÃNG - BẢO HÀNH 12 THÁNG - LỖI 1 ĐỔI 1 TRONG 7 NGÀY ĐẦU]
I. THÔNG SỐ KỸ THUẬT CỦA MÁY HÚT BỤI SOKANY SK3386:
1. Thương hiệu: SOKANY
2. Model: SK3386
3. Công suất: 3500W
4. Điện áp: 220V
5. Dung tích túi đựng bụi: 3,5L
6. Chất liệu: Nhựa ABS cao cấp, thép không gỉ
7. Màu sắc: Đen
II. CÁC TÍNH NĂNG ƯU VIỆT CỦA MÁY HÚT BỤI SOKANY SK3386:
1. Công suất hút mạnh mẽ lên đến 30.000Pa:
     Máy hút bụi cầm tay SOKANY là một giải pháp đáng tin cậy với khả năng hút lên đến 30.000Pa. Với độ mạnh này, máy có thể loại bỏ hiệu quả nhiều loại rác thường gặp trong môi trường sống hàng ngày. Không những vậy, lực hút mạnh mẽ này còn giúp loại bỏ các vết bẩn cứng đầu trên sàn nhà một cách dễ dàng và hiệu quả.
2. Thiết kế thông minh, tiện lợi và nhẹ nhàng:
    Máy hút bụi cầm tay SOKANY không chỉ nổi bật với thiết kế hiện đại mà còn là sự kết hợp tuyệt vời giữa tính năng và tiện ích. Với trọng lượng nhẹ nhàng và thiết kế thông minh, máy dễ dàng di chuyển và sử dụng ở mọi góc độ trong nhà. Việc tập trung trọng lượng ở phần cầm giúp người dùng cảm thấy thoải mái hơn khi sử dụng.
3. Đa dạng đầu hút linh hoạt:
   SOKANY cung cấp cho bạn 3 đầu hút khác nhau, bao gồm đầu hút cho sàn nhà và khe hẹp và đầu hút nệm, sofa. Điều này giúp bạn dễ dàng làm sạch mọi góc khuất trong nhà một cách hiệu quả nhất. Đồng thời, ống nhôm Anodized siêu nhẹ giúp bảo vệ máy khỏi trầy xước và đồng thời làm cho việc di chuyển trở nên dễ dàng hơn bao giờ hết.
4. Hoạt động êm ái:
    Với công nghệ tiên tiến, máy hút bụi SOKANY hoạt động một cách êm ái và không gây ra tiếng ồn lớn như các dòng sản phẩm khác. Điều này mang lại sự thoải mái và yên tĩnh trong quá trình làm sạch.
5. Dây cáp dài:
     Với dây cáp dài 6.5m, việc di chuyển trong nhà trở nên thuận tiện hơn bao giờ hết. Bạn có thể dễ dàng di chuyển từ phòng này sang phòng khác mà không cần phải lo lắng về việc tìm kiếm ổ cắm. Điều này giúp tiết kiệm thời gian và năng lượng khi làm sạch.
III. CHẾ ĐỘ BẢO HÀNH:
1. Đổi mới 15 ngày đầu tiên TẠI NHÀ KHÔNG MẤT PHÍ và bảo hành 1 năm.
2. Trong 1 năm sử dụng, máy có lỗi gì do nhà sản xuất khách hàng đều được hỗ trợ bảo hành. Mọi chi phí lắp ráp phụ kiện mới khách hàng được shop hỗ trợ 100%.
        """
    },
    "2": {
        "version": "Hai màu trắng và đen",
        "product_qty": 20,
        "payment_method": "cash",
        "description": """
•	[NHỎ GỌN, TIẾT KIỆM KHÔNG GIAN] Kích thước máy 42,8 x 42,5 x 45,9 cm, có thể đặt được ở nhiều vị trí, hoàn hảo cho gia đình có bếp nhỏ, căn hộ, văn phòng hoặc xe đi du lịch/xe cắm trại. Với sức chứa đến 4 bộ đồ ăn đầy đủ  đáp ứng nhu cầu hàng ngày cho một gia đình 3-4 người bao gồm:  4 chén/bát, 4 tô nhỏ/2 tô lớn, 4 đĩa ăn nhỏ/trung hoặc 3 đĩa lỡn, 4 - 8 muỗng/ dao/ nĩa, 4 - 8 đôi đũa, 4 ly; 
•	[KHÔNG CẦN LẮP ĐẶT] Máy hỗ trợ 2 chế độ cung cấp nước: đổ nước trực tiếp hoặc nối ống dẫn; hộc chứa nước dung tích 5 L cho phép sử dụng ngay lập tức khi đầy đủ nước. Chỉ báo điện tử tự động thông báo khi bạn đã đổ đầy nước và có thể sử dụng.
•	[5 CHƯƠNG TRÌNH RỬA THÔNG MINH] Bình thường, Nhanh, Nhẹ, Đồ dung em bé/Rửa mạnh và Rau quả đáp ứng linh hoạt mọi nhu cầu.
•	[RỬA NHANH TIỆN DỤNG] Chế độ rửa nhanh thông minh chỉ trong 29 áp dụng chén đĩa ít bẩn tiết kiệm thời gian .
•	[ 3 TRONG 1: RỬA, SẤY, LƯU TRỮ] 60 phút sấy nóng tự động bắt đầu sau khi chu kỳ rửa kết thúc, diệt khuẩn và giữ chén đĩa của bạn khô ráo và không mùi. Khả năng lưu trữ chén đĩa, dụng cụ ăn lên đến 72 giờ với tính năng thông gió tự động, đảm bảo chén đĩa luôn sạch sẽ tuyệt đối.
•	[TIẾT KIỆM NĂNG LƯỢNG] Chỉ 5L nước cho 1 lần rửa, tiết kiệm 75% lượng nước so với rửa tay. Với công suất 950W, máy chỉ cần 0.4KW điện cho 1 chu kỳ rửa sấy (hơn 120 phút)
•	[HOẠT ĐỘNG ÊM ÁI, GẦN NHƯ KHÔNG TIẾN ỒN] Thiết kế thông minh vận hành với tiếng ồn cực thấp, không ảnh hưởng đến các hoạt động các nhân của bạn.
•	[ TRỌN BỘ PHỤ KIỆN HOÀN HẢO ]1 khay chính, 1 khay phụ (dung rửa ly hoặc đồ kích thước nhỏ), 1 khay đựng dao muỗng đũa, 1 ống dẫn nước vào, 1 ống thoát nước, 1 giỏ đựng rau quả, 1 bình châm nước.
•	[ MÀN HÌNH ĐIỀU KHIỂN LED] Màn hình cảm ứng LED hiển thị trạng thái và các chương trình của máy, chỉ báo mức nước tự động báo hiệu lượng nước đầy và sẵn sàng để bắt đầu rửa. Cửa kính hai lớp trong suốt, kết hợp với đèn LED tích hợp, cho phép bạn dễ dàng và rõ ràng kiểm tra trạng thái làm việc của máy.
•	[BẢO HÀNH 1 NĂM] An tâm sử dụng với 7 ngày đổi trả (nếu có lỗi từ nhà sản xuất) và 1 năm bảo hành chính hãng.
        """},
    "3": {
        "version": "Titan Đen, Titan Trắng, Titan sa mạc, Titan tự nhiên",
        "product_qty": 40,
        "payment_method": "cash",
        "description": """
        Bộ sản phẩm bao gồm: 
•        iPhone sử dụng iOS 18
•        Cáp Sạc USB‑C (1m)
•        Tài liệu
Thông tin bảo hành:
Bảo hành: 12 tháng kể từ ngày kích hoạt sản phẩm.
Kích hoạt bảo hành tại: https://checkcoverage.apple.com/vn/en/
Hướng dẫn kiểm tra địa điểm bảo hành gần nhất:
Bước 1: Truy cập vào đường link https://getsupport.apple.com/?caller=grl&locale=en_VN 
Bước 2: Chọn sản phẩm.
Bước 3: Điền Apple ID, nhập mật khẩu.
Sau khi hoàn tất, hệ thống sẽ gợi ý những trung tâm bảo hành gần nhất.
Tại Việt Nam, về chính sách bảo hành và đổi trả của Apple, "sẽ được áp dụng chung" theo các điều khoản được liệt kê dưới đây:
1) Chính sách chung: https://www.apple.com/legal/warranty/products/warranty-rest-of-apa-vietnamese.html
2) Chính sách cho phụ kiện: https://www.apple.com/legal/warranty/products/accessory-warr-vietnam.html
3) Các trung tâm bảo hành Apple ủy quyền tại Việt Nam: https://getsupport.apple.com/repai-locations?locale=vi_VN
Qúy khách vui lòng đọc kỹ hướng dẫn và quy định trên các trang được Apple công bố công khai, Shop chỉ có thể hỗ trợ theo đúng chính sách được đăng công khai của thương hiệu Apple tại Việt Nam,
Bài viết tham khảo chính sách hỗ trợ của nhà phân phối tiêu biểu:
https://synnexfpt.com/bao-hanh/chinh-sach-bao-hanh/?agency-group=1&agency-slug=san-pham-apple
Để thuận tiện hơn trong việc xử lý khiếu nại, đơn hàng của Brand Apple thường có giá trị cao, Qúy khách mua hàng vui lòng quay lại Clip khui mở kiện hàng (khách quan nhất có thể, đủ 6 mặt) giúp Shopee có thêm căn cứ để làm việc với các bên và đẩy nhanh tiến độ xử lý giúp Qúy khách mua hàng
        """
    },
    "5": {
        "version": "Titan Đen, Titan Trắng, Titan sa mạc, Titan tự nhiên",
        "product_qty": 50,
        "payment_method": "cash",
        "description": """
        Thông tin chung về Điện thoại Samsung Galaxy S24 Ultra, 12GB/256GB:
- Sản phẩm đã được kích hoạt bảo hành điện tử
- Chip: Snapdragon® 8 Gen 3 for Galaxy
- Màn hình: 6.8 inch, độ phân giải QHD+, Dynamic AMOLED 2X, 120Hz
- RAM: 12GB
- Bộ nhớ trong: 256GB
- Camera: 200MP
- Dung lượng PIN: 5.000mAh
- Công nghệ màn hình: Dynamic AMOLED 2X
- Độ phân giải: 2K+ (1440 x 3120 Pixels)
- Camera sau: Chính 200 MP & Phụ 50 MP, 12 MP, 10 MP
- Camera trước: 12 MP
- Hệ điều hành: Android 14
- Bảo mật nâng cao: Mở khoá vân tay dưới màn hình, Mở khoá khuôn mặt
- Tính năng đặc biệt:Ứng dụng kép (Dual Messenger), Mở rộng bộ nhớ RAM, Màn hình luôn hiển thị AOD, Âm thanh Dolby Atmos, Chặn cuộc gọi, Chặn tin nhắn, Chạm 2 lần tắt/sáng màn hình, Trợ lý ảo Samsung Bixby, Thu nhỏ màn hình sử dụng một tay, Samsung Pay, Âm thanh AKG, Đa cửa sổ (chia đôi màn hình), Samsung DeX (Kết nối màn hình sử dụng giao diện tương tự PC), Trợ lý ảo Google Assistant, Loa kép, Tối ưu game (Game Booster), Phiên dịch trực tiếp, Trợ lý note quyền năng, Trợ lý chat thông minh, Trợ lý chỉnh ảnh, Khoanh vùng search đa năng, Ray Tracing, Vision Booster, Hệ thống tản nhiệt Vapor Chamber, Cử chỉ thông minh, Không gian thứ hai (Thư mục bảo mật)
- Chất liệu: Khung Titan & Mặt lưng kính cường lực
- Bộ sản phẩm gồm: Hộp, Sách hướng dẫn, Cây lấy sim, Cáp Type C
- Thông tin bảo hành: Bảo hành 12 tháng tại các trung tâm bảo hành của Samsung trên toàn quốc
- Về Thiết kế:
Samsung Galaxy S24 Ultra, là phiên bản mới nhất của dòng sản phẩm nổi tiếng, tiếp tục thể hiện vẻ đẹp đẳng cấp và sự hiện đại trong thiết kế.Phần khung này được làm hơi cong, mang lại cảm giác cầm nắm thoải mái và chắc chắn. Kết hợp cùng với đó là mặt lưng kính nhám, nó không chỉ tăng tính thẩm mỹ mà còn đảm bảo độ bền và sang trọng, tạo nên một tổng thể đẳng cấp và lịch lãm.
Phần hệ thống camera của Galaxy S24 Ultra tiếp tục ấn tượng với cụm 4 cảm biến và 1 đèn LED được sắp xếp một cách độc lập. Đây là một kiểu bố trí camera mà người hâm mộ Samsung đã quá quen thuộc, giúp điện thoại giữ vẻ tối giản trong khi vẫn giữ được sự hiện đại và sang trọng. Tổng thể, thiết kế của điện thoại hướng đến đối tượng khách hàng là doanh nhân hoặc những người yêu thích sự lịch lãm và mạnh mẽ.
- Về Màn hình lớn kết hợp cùng độ phân giải Quad HD+:
Galaxy S24 Ultra sử dụng tấm nền Dynamic AMOLED 2X, mở ra một thế giới màu sắc và độ tương phản không giới hạn. Với kích thước màn hình lên đến 6.8 inch, người dùng sẽ được chìm đắm trong những trải nghiệm giải trí và làm việc tuyệt vời nhất. Độ phân giải QHD+ không chỉ làm sắc nét hình ảnh mà còn tạo nên một không gian sống động và chân thực.
- Về Camera 200 MP:
Samsung Galaxy S24 Ultra không chỉ là một bước đột phá trong công nghệ camera trên điện thoại di động mà còn là nguồn động viên cho những người yêu thích nhiếp ảnh và quay video chuyên nghiệp. Với bộ 4 camera đỉnh cao, chiếc điện thoại này đưa trải nghiệm chụp hình và quay video lên một tầm cao mới.
Trang bị camera chính độ phân giải lên tới 200 MP, Galaxy S24 Ultra là một đỉnh cao mới trong thế giới nhiếp ảnh di động. Khả năng chi tiết và sắc nét vượt trội, chiếc điện thoại chụp ảnh, quay phim này là lựa chọn lý tưởng cho những người muốn ghi lại những khoảnh khắc tuyệt vời với độ chính xác cao.
        """
    }
}
