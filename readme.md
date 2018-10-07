# SỬ DỤNG DATA ĐỌC BÁO TRÊN MÁY TÍNH / LAPTOP DỄ DÀNG VỚI DOCBAO-RESEARCH-CLI TOOL

Công cụ dành cho những người có nhu cầu sử dụng [Đọc Báo Theo Từ Khóa](http://docbao.danghailoc.com) với tần suất cao như phóng viên, nhà nghiên cứu, markerter...Hỗ trợ lấy dữ liệu tự động, thực hiện truy vấn nhanh, và xuất dữ liệu ra file dễ dàng

Version: 1.0.0  
Author: hailoc12  
Email: danghailochp@gmail.com  
Published Date: 7/10/2018  

[Click vào đây để tải bộ cài đặt](http://docbao.danghailoc.com/export/docbao-research-cli.zip)

Note:
Ứng dụng hoàn toàn miễn phí và sẽ luôn miễn phí. Các phiên bản tốt hơn vẫn sẽ liên tục được cập nhật. Nếu ứng dụng này hữu ích với công việc của bạn, rất mong bạn có thể ủng hộ để tác giả tiếp tục đầu tư cải tiến.

Mọi đóng góp xin gửi về:
- Chủ tài khoản: ĐẶNG HẢI LỘC
- Số tài khoản: 0491000010179
- Ngân hàng: Vietcombank chi nhánh Hoàng Quốc Việt 

Và đừng quên star cho mình nhé :d

## Tính năng nổi bật

1. Hoạt động trên cả windows và linux, chỉ cần down đúng bản là chạy được

2. Tự động cập nhật dữ liệu báo chí quét được bởi hệ thống [Đọc Báo Theo Từ Khóa](http://github.com/hailoc12/docbao) về máy để xử lý

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
show [trends/new/growing]	: hiển thị danh sách từ khóa đang là trends, từ khóa mới xuất hiện, từ khóa đang tăng trưởng nhanh

search [keyword/index]		: tìm kiếm các bài báo có chứa từ khóa keyword hoặc vị trí của từ khóa trong danh sách trả về của lệnh show

open index                : mở bài báo ở vị trí index trong danh sách kết quả của lệnh search

export filename           : xuất kết quả của các lệnh show, search ra file text để sử dụng về sau

read filename				      : mở file text đã export

help						          : mở danh sách tra cứu lệnh

quit hoặc exit				    : kết thúc chương trình

~~~

Ví dụ cụ thể

~~~
# Hiển thị các từ khóa đang là xu hướng
> show trends
~~~

~~~
#Liệt kê tất cả các bài viết có chứa từ khóa số 1 trong danh sách trên
search 1
~~~

~~~
# Liệt kê tất cả bài viết có chứa từ khóa "hậu duệ mặt trời"
> search "hậu duệ mặt trời"
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


## Cài đặt

1. Cài đặt trên linux

~~~
git clone http://github.com/hailoc12/docbao-research-cli
cd ~/docbao-research-cli/linux
make install
~~~

2. Cài đặt trên windows: không cần cài đặt, download file từ github hoặc [tại đây](http://docbao.danghailoc.com/export/docbao-research-cli.zip), giải nén là có thể chạy được
