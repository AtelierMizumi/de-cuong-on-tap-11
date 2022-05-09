# Mấy cái bài tin học, làm thử một phát xem
# Bài 1

from tabnanny import check

a=input("Nhập số vào để sort, các số tách nhau bằng dấu cách:")
b=sorted(a.split)
print(b)

# Bài 2 Kiểm tra tính đối xứng của số tự nhiên vừa nhập
n=input("Nhập số để kiểm tra đối xứng:")

def doixung(n):
    # flag = 1 doi xung
    # flag = 0 khong doi xung
    # Ở đây sẽ so sánh và trả giá trị vào biến flag
    flag=0
    if n[::1] == n:
        flag=1
    return flag
check = doixung(n)

if check == 1:
    print("Số ",n," là số đối xứng")
if check == 0:
    print("Số ",n," không phải là số đối xứng")


# Bài 2 ỉa quá làm bài 3 vậy, ít nhất thì nó chạy rồi

x=int(input("Nhập số x:"))
y=int(input("Nhập số y:"))
f=open("tongtich.out","w", encoding="utf-8") # Biêt là encoding utf hơi overkill
new_var = f.writelines("Tổng:",x+y, "Tích", x*y)
new_var
f.close("Đã đóng tệp kkk")

# Đéo hiểu sao không chạy lmao =)))
# Bài 4 Kiểm tra số từ xuất hiện trong chuỗi

a=input("Nhập chuỗi muốn kiểm tra:")
b=input("Nhập đoạn chuỗi muốn kiểm tra số lặp:")
print(a.count(b))


