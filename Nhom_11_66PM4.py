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
    def cucTieuChiThucBoSung(self, start, end):
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
                return path
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
                elif g_m_node < g_m.get(node.value, float('inf')):
                    g_m[node.value] = g_m_node
                    f_m[node.value] = g_m_node + node.h_value
                    node_duong_di[node.value] = dinh_hien_tai
            print("{:<20} {:<20} {:<30} {:<30} {:<30}".format(N,
                                                              ' '.join(str(x) for x in dinh_hien_tai),
                                                              ' '.join(str(x) for x in children),
                                                              ' '.join(str(x) + str(f_m[x]) for x in MO),
                                                              ' '.join(str(x) for x in DONG)))


            children.clear()
        return "Không tìm thấy đường đi"

def nhap_node():
    nhap = input("Nhập đỉnh và giá trị dự đoán (ví dụ: A,14 B,10 ...): ")
    nodes = nhap.split()
    node_values = [x.split(",") for x in nodes]
    return node_values

def nhap_canh():
    nhap = input("Nhập cạnh giữa 2 đỉnh (ví dụ: A,B,5 A,C,3 ... ): ")
    edges = nhap.split()
    edges_values = [x.split(",") for x in edges]
    return edges_values

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

path = newDoThi.cucTieuChiThucBoSung(start_node, end_node)
if path == "Không tìm thấy đường đi":
    print("Không tìm thấy đường đi giữa {} và {}".format(start_node,end_node))
else:
    print("Đường đi có giá ngắn nhất kết hợp tri thức bổ sung:")
    print(" -> ".join(path))

