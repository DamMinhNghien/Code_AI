#    BÀI TẬP LỚN TRÍ TUỆ NHÂN TẠO
##    NHÓM 11 - 66PM4
##    Bài Tập: 
```
Sử dụng danh sách móc nối để thực hiện tìm kiếm trên đồ thị
sử dụng thuật toán tìm kiếm đường đi với giá cực tiểu với tri thức bổ sung
```
# Hướng dẫn sử dụng và ý tưởng
## I. Hướng dẫn sử dụng
![image](https://github.com/DamMinhNghien/Code_AI/assets/97715184/5f678f84-87c1-4e3e-b05b-2d4f9e04e8a5)
- Dòng đầu tiên chính là nhập các đỉnh và giá trị dự đoán, ở ví dụ trên A h(A) = 14:
![image](https://github.com/DamMinhNghien/Code_AI/assets/97715184/85d3ebe9-9899-4db1-8409-1f48699d5ff2)
- Dòng thứ 2 nhập khoảng cách giữa 2 cạnh, ở ví dụ trên độ cài A đến B là 5:
![image](https://github.com/DamMinhNghien/Code_AI/assets/97715184/cc09e85e-514f-48b6-9463-6aff59cf1fe3)
- Sau đó chúng ta nhập điểm bắt đầu và điểm kết thúc và enter là ra kết quả:
![image](https://github.com/DamMinhNghien/Code_AI/assets/97715184/bda6bdfd-7c30-4bb1-9f2e-f074f36c54c4)

  *Lưu ý: có thể viết chữ cái là chữ thường*


## II. Ý tưởng
1. Ta tạo 1 class node để lưu thông tin của đỉnh bao gồm tên đỉnh(value) và giá trị dự đoán(h_value):
```python
class Node:
   def __init__(self, value, h_value=0):
        self.value = value
        self.h_value = h_value
        self.next = None
```
2. Tạo 1 class dinh_ke để lưu thông tin các đỉnh kề của node:
```python
 class dinh_ke:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost
        self.next = None
```
3. Tạo class doThi:
- khởi tạo nodes để lưu trữ các đỉnh đã được nhập
```python
class doThi:
    def __init__(self):
        self.nodes = {}
```
- hàm add_node được gọi add node mới vào nodes
```python
    def add_node(self, value, h_value=0):
        self.nodes[value] = Node(value, h_value)
```
- Khi nhập cạnh A,B,5 thì hàm add_canh, hàm này gọi 2 lần hàm add_dinh_ke với thông số ngược nhau
- nhằm tạo ra và trỏ dến đỉnh kề của thằng còn lại, dễ hiểu là:
  
  node A (A,14) -> đỉnh kề B (node B, cost)
  node B (B,10) -> đỉnh kề A (node A, cost)
*trong đó cost là khoảng cách A tới B*
```python
def add_canh(self, node1, node2, cost):
        if node1 not in self.nodes or node2 not in self.nodes:
            print("Đỉnh được nhập không tồn tại! KẾT THÚC BÀI TOÁN")
            sys.exit()
        self.add_dinh_ke(node1, node2, cost)
        self.add_dinh_ke(node2, node1, cost)
def add_dinh_ke(self, node_value, dinh_ke_value, cost):
        dinh_ke_node = self.nodes[dinh_ke_value]
        new_dinh_ke = dinh_ke(dinh_ke_node, cost)

        current_node = self.nodes[node_value]
        if not current_node.next:
            current_node.next = new_dinh_ke
        else:
            temp = current_node.next
            while temp.next:
                temp = temp.next
            temp.next = new_dinh_ke
```
- Đoạn thuật toán  lưu ý 2 cái
- thứ nhât: lưu f_m bằng 1 dictionary với `f_m[tên đỉnh] = giá trị`
  
  - nếu là đỉnh mới thì thêm `f_m[tên đỉnh] = giá trị`
  
  - còn là đỉnh cũ thì xem giá trị f_m mới có bé hơn k, nếu bé hơn thì cập nhật ` f_m[tên đỉnh mới] = giá trị`
- thứ hai: cùng lúc cập nhật f_m ta cũng cập nhật đỉnh dẫn đến nó `node_duong_di[đỉnh đang xét] = đỉnh dẫn đến đỉnh đang xét`

  - từ đó ta đảo ngược lại lần lượt và tìm ra đường đi ngắn nhất và cost thấp nhất
