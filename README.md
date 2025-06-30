
# 📘 Format Study Status Today

Tùy chỉnh dòng mô tả học tập hiển thị ở giao diện chính của Anki theo phong cách cá nhân hóa, sinh động hơn, dễ tạo cảm hứng và động lực học tập mỗi ngày.

---

## ✨ Tính năng chính

- Thay đổi nội dung dòng mô tả học tập ở trang chủ Anki.
- Hỗ trợ sử dụng **biến động** như:
  - `{card_text}`: số lượng thẻ đã học hôm nay
  - `{time_text}`: thời gian học hôm nay
  - `{avg_text}`: thời gian trung bình mỗi thẻ
- Hỗ trợ định dạng HTML như in đậm, đổi màu, chèn icon...

---

## 💡 Ví dụ sử dụng

### Mẫu đơn giản:

```
Hôm nay bạn đã học {card_text} trong {time_text}. Trung bình: {avg_text}/thẻ.
```

### Mẫu nâng cao có định dạng:


&lt;span style=&quot;font-size: 24px; color: blue;&quot;&gt;📝Studied &lt;b&gt;{card_text} cards&lt;/b&gt;&lt;/span&gt; in &lt;b&gt;⏰️{time_text}&lt;/b&gt; today. (&lt;b&gt;⏱️{avg_text}s&lt;/b&gt;/card)

---

## 🔧 Cách dùng

1. Vào **Tools → Add-ons → Rewrite Text of Study Cards → Config**.
2. Nhập đoạn văn mong muốn vào ô Text.
3. Bấm **OK** để lưu và quay lại giao diện chính.



## 📎 Ghi chú

- Addon hoạt động tốt trên Anki 2.1.66+ (Qt6).
- Không làm thay đổi dữ liệu học tập hay thẻ flashcard.
- Nếu bạn dùng HTML, đảm bảo đúng cú pháp để hiển thị ổn định.

