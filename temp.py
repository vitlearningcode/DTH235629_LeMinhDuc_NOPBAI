import matplotlib.pyplot as plt

ascii_diagram = """                MÔ HÌNH THÀNH PHẦN HỆ THỐNG – THE TRIP COFFEE

┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈  PHẠM VI HỆ THỐNG CỬA HÀNG  ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
←  ĐẦU VÀO
   • Nguyên liệu chế biến
   • Nước giải khát
   • Nhân sự
   • Tiền tệ
                                           ĐẦU RA  →
                                           • Thức uống
                                           • Hóa đơn
                                           • Tiền tệ
┌────────────────────────────────────────────────────────────────────────────┐
│ ┌───────────────┬───────────────┬───────────────┐                         │
│ │  KHO XUẤT     │  BỘ PHẬN      │  BỘ PHẬN      │                         │
│ │  NHẬP HÀNG    │  CHẾ BIẾN     │  BÁN HÀNG     │                         │
│ └───────↑───────┴───────↑───────┴───────↑───────┘                         │
│         │               │               │                                  │
│         │    (trao đổi nguyên liệu & sản phẩm)    ←→   (trao đổi SP/bán)  │
│         └───────────────↔───────────────↔──────────────────────────────────│
│ ┌────────────────────────────────────────────────────────────────────────┐ │
│ │                       VĂN PHÒNG QUẢN LÝ                               │ │
│ │        (nhận & gửi thông tin: nhập/xuất, tồn, đơn hàng, báo cáo)      │ │
│ └───────────────↑──────────────────────────↕──────────────────↑──────────┘ │
│                 │                         │                  │            │
│ ┌────────────────────────────────────────────────────────────────────────┐ │
│ │                         BỘ PHẬN GIAO HÀNG                              │ │
│ │ (nhận yêu cầu/đơn từ Bán hàng & VPQL; giao cho khách; phản hồi trạng) │ │
│ └────────────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────────┘

         KHÁCH HÀNG     |   NHÀ CUNG CẤP NVL   |  NHÀ VẬN CHUYỂN  |  NGÂN HÀNG  |  SÀN TMĐT
          (đặt/mua)     |  (cấp nguyên liệu)   | (hỗ trợ logistics)| (thanh toán)| (đặt online)

Ghi chú mũi tên:
  ↔  : luồng 2 chiều giữa các bộ phận (nguyên liệu/sản phẩm/thông tin).
  ↑/↓: luồng nội bộ dọc (báo cáo, điều phối, xác nhận).
  ←/→: đầu vào/đầu ra qua biên hệ thống.
"""

plt.figure(figsize=(14,10))
plt.axis("off")
plt.text(0,1, ascii_diagram, fontsize=9, family="monospace", va="top")
plt.savefig("the_trip_coffee_system.png", bbox_inches="tight", dpi=200)
plt.close()
