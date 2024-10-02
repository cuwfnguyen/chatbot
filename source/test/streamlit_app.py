import streamlit as st
import requests

st.title("Chatbot Application")
if "messages" not in st.session_state:
    st.session_state.messages = []

agent_options = {
    "Chất lượng sản phẩm": 1,
    "Nguồn gốc sản phẩm": 2,
    "Đặc tính sản phẩm (Kích thước, màu sắc, hình ảnh)": 3,
    "Yêu cầu hình ảnh thật sản phẩm": 4,
    "Công dụng sản phẩm": 5,
    "Hướng dẫn sử dụng sản phẩm": 6,
    "Chương trình khuyến mại, mã giảm giá, flash sale": 7,
    "Tồn kho sản phẩm": 8,
    "Thời gian bảo hành": 9,
    "Hướng dẫn bảo hành": 10,
    "Chính sách đổi trả hàng": 11,
    "Phí vận chuyển": 12,
    "Thời gian giao hàng": 13,
    "Hình thức thanh toán": 14,
    "Hỏi về dịch vụ chăm sóc khách hàng": 15,
    "Yêu cầu hỗ trợ đặt hàng": 16,
    "Kiểm tra trạng thái vận chuyển": 17,
    "Thay đổi sản phẩm trong đơn hàng (trước khi nhận hàng)": 18,
    "Thay đổi phương thức thanh toán": 19,
    "Thay đổi địa chỉ nhận hàng": 20,
    "Yêu cầu hủy đơn hàng": 21,
    "Nhận thiếu hàng": 22,
    "Nhận sai hàng": 23,
    "Sai trạng thái giao hàng": 24,
    "Phàn nàn về đóng gói": 25,
    "Sản phẩm lỗi": 26,
    "Sản phẩm không giống mô tả": 27
}

product_options = {
    "Máy hút bụi": 1,
    "Máy rửa chén": 2,
    "Iphone 16 Promax": 3,
    "Điện thoại samsung galaxy s24 ultra": 5
}
order_options = {
    "Đơn hàng 1": 'Purchase01',
    "Đơn hàng 2": 'Purchase02',
    "Đơn hàng 3": 'Purchase03'
}
selected_agent = st.selectbox("Select a topic:", list(agent_options.keys()))
product_name = st.selectbox("Tên sản phẩm (optional từ api bên ptsp):", list(product_options.keys()))
order_name = st.selectbox("Mã đơn hàng (optional từ api bên ptsp):", list(order_options.keys()))

product_code = product_options[product_name]
agent_code = agent_options[selected_agent]
order_code = order_options[order_name]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Nhập tin nhắn của bạn"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    data = {
        "message": st.session_state.messages,
        "agent_code": agent_code,
        "additional_info": {
            "product_name": product_name,
            "product_code": product_code,
            "order_id": order_code,
        }
    }
    bot_response = requests.post('http://localhost:8181/chatbot', json={'data': data})
    clear = False
    if bot_response.status_code == 200:
        results = bot_response.json()['response_data']
        response = results.get('message')
        if results.get('end_situation') =='t':
            response += ' Kết thúc tình huống / chuyển tình huống'
            clear = True
    else:
        response = ''
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    if clear:
        st.session_state.messages = []  # Reset messages