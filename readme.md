# SỬ DỤNG DATA ĐỌC BÁO TRÊN MÁY TÍNH / LAPTOP DỄ DÀNG VỚI DOCBAO-RESEARCH-CLI TOOL

Công cụ dành cho những người có nhu cầu sử dụng [Theo Dõi Báo Chí](http://theodoibaochi.com) với tần suất cao như phóng viên, nhà nghiên cứu, markerter...Hỗ trợ lấy dữ liệu tự động, thực hiện truy vấn nhanh, và xuất dữ liệu ra file dễ dàng

Version: 1.1.0  
Author: hailoc12  
Email: danghailochp@gmail.com  
Published Date: 15/08/2019  


Note:
Ứng dụng hoàn toàn miễn phí và sẽ luôn miễn phí. Các phiên bản tốt hơn vẫn sẽ liên tục được cập nhật. Nếu ứng dụng này hữu ích với công việc của bạn, rất mong bạn có thể ủng hộ để tác giả tiếp tục đầu tư cải tiến.

Mọi đóng góp xin gửi về:
- Chủ tài khoản: ĐẶNG HẢI LỘC
- Số tài khoản: 0491000010179
- Ngân hàng: Vietcombank chi nhánh Hoàng Quốc Việt 

Và đừng quên star cho mình nhé :d

[Imgur](https://i.imgur.com/9cNOTDr.png)


[Imgur](https://i.imgur.com/9cNOTDr.png)

## Tính năng nổi bật

1. Hoạt động trên cả windows và linux, chỉ cần down đúng bản là chạy được

2. Tự động cập nhật dữ liệu báo chí quét được bởi hệ thống [Theo Dõi Báo Chí](http://github.com/hailoc12/docbao) về máy để xử lý

3. Tập lệnh ngắn gọn, phong phú, hỗ trợ chức năng tương đương trên giao diện web. Ví dụ: hiển thị các từ khóa đang là xu hướng, từ khóa mới xuất hiện, liệt kê toàn bộ các bài báo có chứa một từ khóa xác định, mở link báo trong trình duyệt...

4. Hỗ trợ export kết quả để xử lý bổ sung, ở dạng định dạng rút gọn và đầy đủ thông tin. Hỗ trợ đọc file đã export ngay trong tool

5. Hỗ trợ mở link báo bằng trình duyệt có sẵn trong máy

6. Có thể nhập lệnh thông qua chế độ shell của tool hoặc từ command line



## Hướng dẫn sử dụng

Cú pháp:
~~~
> command [keyword/index/filename]
~~~

Danh sách command được hỗ trợ
~~~
search [keyword/search_string]
:tìm kiếm các bài báo có chứa keyword hoặc search_string
:search_string có dạng "a,b,c; x, y, z" nghĩa là tìm các bài báo thỏa mãn chứa (a or b or c) and (x or y or z)
:tool có chế độ tìm kiếm ở title và tìm kiếm trong toàn bài báo

show [trends/new/growing]
:hiển thị danh sách từ khóa đang là trends, từ khóa mới xuất hiện, từ khóa đang tăng trưởng nhanh:

list [keyword/index]
:liệt kê các bài báo có chứa từ khóa keyword hoặc vị trí của từ khóa trong danh sách trả về của lệnh show:

open index
:mở bài báo ở vị trí index trong danh sách kết quả của lệnh search:
:để dùng lệnh open, cần cài đặt CLI browser như lynx, w3m

export filename
:xuất kết quả của các lệnh show, list, search trước đó ra file text để sử dụng về sau:

read filename
:mở file text đã export:

update
:update dữ liệu

help
:mở danh sách tra cứu lệnh:

quit hoặc exit
:kết thúc chương trình:

~~~

Ví dụ cụ thể
~~~
# Tìm kiếm các bài viết về Trí tuệ nhân tạo
> search "Trí tuệ nhân tạo"

# Tìm kiếm các bài viết về bất động sản ở Hà Nội
> search "bất động sản; Hà Nội"

# Hiển thị các từ khóa đang là xu hướng
> show trends
~~~

~~~
#Liệt kê tất cả các bài viết có chứa từ khóa số 1 trong danh sách trên
list 1
~~~

~~~
# Liệt kê tất cả bài viết có chứa từ khóa "hậu duệ mặt trời"
> list "hậu duệ mặt trời"
~~~

~~~
# Mở bài báo số 5 trong danh sách kết quả bằng trình duyệt trong máy
open 5
~~~

~~~
# Xuất kết quả ra file để lưu trữ / đưa vào ứng dụng khác xử lý
export hau_due_mat_troi.txt
~~~

~~~
# Mở xem lại một file đã export
read hau_due_mat_troi.txt
~~~


## Cài đặt và sử dụng

~~~
git clone http://github.com/hailoc12/docbao-research-cli
cd ~/docbao-research-cli/linux
./docbao
~~~

