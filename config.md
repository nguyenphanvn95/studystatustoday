
# Hướng dẫn cấu hình addon

Addon này cho phép bạn tùy chỉnh dòng mô tả quá trình học trên màn hình chính của Anki.

## Cách sử dụng

1. Vào menu cấu hình addon: Rewrite Text of Study Cards
2. Nhập dòng mô tả theo ý muốn. Bạn có thể sử dụng các biến sau:
   - `{card_text}`: số lượng thẻ đã học
   - `{time_text}`: thời gian học
   - `{avg_text}`: thời gian trung bình mỗi thẻ

## Ví dụ

```
Hôm nay bạn đã học {card_text} trong vòng {time_text}. Trung bình: {avg_text}/thẻ.
```
## Ví dụ nâng cao (dùng định dạng HTML)

&lt;span style=&quot;font-size: 24px; color: blue;&quot;&gt;📝Studied &lt;b&gt;{card_text} cards&lt;/b&gt;&lt;/span&gt; in &lt;b&gt;⏰️{time_text}&lt;/b&gt; today. (&lt;b&gt;⏱️{avg_text}s&lt;/b&gt;/card)



## Ghi chú

- Không cần dùng dấu `%` hay `{0}`, chỉ cần viết `{card_text}` đúng cú pháp là được.
- Nếu để trống, Anki sẽ dùng dòng mặc định.
