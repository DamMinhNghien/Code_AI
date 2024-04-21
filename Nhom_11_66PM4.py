import sys
class Node:
    def __init__(self, value, h_value=0):
        self.value = value
        self.h_value = h_value
        self.next = None
class dinh_ke:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost
        self.next = None
class doThi:
    def __init__(self):
        self.nodes = {}
    def add_node(self, value, h_value=0):
        self.nodes[value] = Node(value, h_value)
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

    def get_cost(self, node1, node2):
        first_node = self.nodes[node1]
        second_node = self.nodes[node2]
        current_node = first_node.next
        while current_node:
            if current_node.node == second_node:
                return current_node.cost
            current_node = current_node.next

        print("Không tìm thấy cạnh giữa {} và {}".format(node1, node2))
        return None
    def cucTieuChiThucBoSung(self, start, end):
        if start not in self.nodes or end not in self.nodes:
            print("START hoặc END không tồn tại! KẾT THÚC BÀI TOÁN !")
            sys.exit()
        N=0
        children = []
        MO = {start}
        DONG = set()
        g_m = {start: 0}
        f_m = {start: self.nodes[start].h_value}
        node_duong_di = {}

        empty_MO = "[]"
        empty_dong = "[]"
        print("{:<20} {:<20} {:<30} {:<30} {:<30}".format(N, "[]", empty_MO, ' '.join(str(x) + str(f_m[x]) for x in MO),empty_dong))

        while MO:
            N += 1
            dinh_hien_tai = min(MO, key=lambda node: f_m.get(node, float('inf')))
            if dinh_hien_tai == end:
                path = []
                while dinh_hien_tai in node_duong_di:
                    path.append(dinh_hien_tai)
                    dinh_hien_tai = node_duong_di[dinh_hien_tai]
                path.append(start)
                path.reverse()

                cost = self.get_cost(path[-2], path[-1])
                dinh_end = self.nodes[path[-1]]
                cost_end = cost + g_m[path[-2]] + dinh_end.h_value

                return path, cost_end
            MO.remove(dinh_hien_tai)
            DONG.add(dinh_hien_tai)
            dinh_ke_hien_tai = self.nodes[dinh_hien_tai].next
            while dinh_ke_hien_tai:
                children.append(dinh_ke_hien_tai.node.value)
                node = dinh_ke_hien_tai.node
                cost = dinh_ke_hien_tai.cost
                dinh_ke_hien_tai = dinh_ke_hien_tai.next
                g_m_node = g_m[dinh_hien_tai] + cost
                if node.value not in MO and node.value not in DONG:
                    node_duong_di[node.value] = dinh_hien_tai
                    g_m[node.value] = g_m_node
                    f_m[node.value] = g_m_node + node.h_value
                    MO.add(node.value)
                elif node.value in MO:
                    f_m_cu = f_m[node.value]
                    f_m_moi = g_m_node + node.h_value
                    if f_m_moi < f_m_cu:
                        g_m[node.value] = g_m_node
                        f_m[node.value] = f_m_moi
                        node_duong_di[node.value] = dinh_hien_tai
            print("{:<20} {:<20} {:<30} {:<30} {:<30}".format(N,
                                                              ' '.join(str(x) for x in dinh_hien_tai),
                                                              ' '.join(str(x) for x in children),
                                                              ' '.join(str(x) + str(f_m[x]) for x in MO),
                                                              ' '.join(str(x) for x in DONG)))


            children.clear()
        return "Không tìm thấy đường đi"

def nhap_node():
    while True:
        nhap = input("Nhập đỉnh và giá trị dự đoán (ví dụ: A,14 B,10 ...): ")
        nodes = nhap.split()
        node_values = [x.split(",") for x in nodes]
        if all(len(node) == 2 and node[0].isalpha() and node[1].isdigit() for node in node_values):
            return node_values
        else:
            print("Định dạng đầu vào không chính xác. Vui lòng nhập lại.")
def nhap_canh():
    while True:
        nhap = input("Nhập cạnh giữa 2 đỉnh (ví dụ: A,B,5 A,C,3 ... ): ")
        edges = nhap.split()
        edges_values = [x.split(",") for x in edges]
        if all(len(edge) == 3 and edge[0].isalpha() and edge[1].isalpha() and edge[2].isdigit() for edge in edges_values):
            return edges_values
        else:
            print("Định dạng đầu vào không chính xác. Vui lòng nhập lại.")

newDoThi = doThi()

# Nhập và thêm các node
node_input = nhap_node()
for node in node_input:
    newDoThi.add_node(node[0].upper(), int(node[1]))

# Nhập và thêm các cạnh
edge_input = nhap_canh()
for edge in edge_input:
    newDoThi.add_canh(edge[0].upper(), edge[1].upper(), int(edge[2]))

start_node = input("Nhập node bắt đầu: ").upper()
end_node = input("Nhập node kết thúc: ").upper()

path, cost = newDoThi.cucTieuChiThucBoSung(start_node, end_node)
if path == "Không tìm thấy đường đi":
    print("Không tìm thấy đường đi giữa {} và {}".format(start_node,end_node))
else:
    print("Đường đi có giá ngắn nhất kết hợp tri thức bổ sung:")
    print(" -> ".join(path))
    print("Cost: {}".format(cost))

