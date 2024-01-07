class Node:
    def __init__(self, sku, nama_barang, harga_barang, jumlah_stok):
        self.jumlah_stok = jumlah_stok
        self.nama_barang = nama_barang
        self.harga_barang = harga_barang
        self.sku = sku
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, sku, nama_barang, harga_barang, jumlah_stok):
        if self.root is None:
            self.root = Node(sku, nama_barang, harga_barang, jumlah_stok)
        else:
            self.insert_rec(self.root, sku, nama_barang, harga_barang, jumlah_stok)

    def insert_rec(self, temp, sku, nama_barang, harga_barang, jumlah_stok):
        if sku == temp.sku:
            print("No. SKU sudah tersimpan di BST.")
            return
        elif sku < temp.sku:
            if temp.left is None:
                temp.left = Node(sku, nama_barang, harga_barang, jumlah_stok)
            else:
                self.insert_rec(temp.left, sku, nama_barang, harga_barang, jumlah_stok)
        else:
            if temp.right is None:
                temp.right = Node(sku, nama_barang, harga_barang, jumlah_stok)
            else:
                self.insert_rec(temp.right, sku, nama_barang, harga_barang, jumlah_stok)

    def restock(self, sku, newBarang):
        node = self.find_node(self.root, sku)
        if node is None:
            print("No. SKU belum tersimpan. Silakan input data stok barang terlebih dahulu.")
        else:
            node.jumlah_stok += newBarang
            print("Restok Barang berhasil. Jumlah stok baru:", node.jumlah_stok)

    def find_node(self, temp, sku):
        if temp is None or temp.sku == sku:
            return temp
        elif sku < temp.sku:
            return self.find_node(temp.left, sku)
        else:
            return self.find_node(temp.right, sku)
        
    def delete_node(self, sku):
        self.root, deleted = self.del_node(self.root, sku)
        return deleted

    def del_node(self, node, sku):
        if node is None:
            return node, False

        if sku < node.sku:
            node.left, deleted = self.del_node(node.left, sku)
        elif sku > node.sku:
            node.right, deleted = self.del_node(node.right, sku)
        else:
            if node.left is None and node.right is None:
                del node
                return None, True
            elif node.left is None:
                temp = node.right
                del node
                return temp, True
            elif node.right is None:
                temp = node.left
                del node
                return temp, True
            else:
                successor = self._find_min_node(node.right)
                node.sku = successor.sku
                node.nama_barang = successor.nama_barang
                node.harga_barang = successor.harga_barang
                node.jumlah_stok = successor.jumlah_stok
                node.right, deleted = self.del_node(node.right, successor.sku)

        return node, deleted

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


def menu():
    print("SITORSI (Sistem Informasi Stok dan Transaksi) - Abimanyu Putra Aria - 5220411291")
    print("==========|List Menu: |==========")
    print("[1] Kelola Stok Barang")
    print("[2] Kelola Transaksi Konsumen")
    print("[0] Exit Program")

def submenu1(bins_tree):
    while True:
        print("=====|You Choice 'Kelola Stok Barang'|=====")
        print("[11] Input Data Stok Barang")
        print("[12] Restok Barang")
        print("[13] Tampilkan Data Barang")
        print("[14] Hapus Data Barang")
        print("[0] Back to Main Menu")

        choice1 = input("Select a menu: ")
        if choice1 == "11":
            print("=====|You Choice 'Input Data Stok Barang'|=====")
            while True:
                sku = input("Masukkan SKU: ")
                if not sku.isdigit() or len(sku) != 4:
                    print("Harap masukan SKU dengan benar!")
                    continue
                nama_barang = input("Masukkan Nama Barang: ")
                harga_barang = float(input("Masukkan Harga Satuan: "))
                jumlah_stok = int(input("Masukkan Jumlah Stok: "))
                bins_tree.insert(sku, nama_barang, harga_barang, jumlah_stok)
                tambah_data = input("Apakah Anda ingin memasukkan data lain (Y/N)? ")
                if tambah_data.upper() == "N":
                    break

        elif choice1 == "12":
            def display_data(node):
                if node is not None:
                    display_data(node.left)
                    print(f"{node.sku}\t{node.nama_barang}\t\t{node.harga_barang}\t\t{node.jumlah_stok}")
                    display_data(node.right)

            print("=====|You Choice 'Restok Barang'|=====")
            print("SKU\tNama Barang\tHarga Barang\tJumlah Stok")
            display_data(bins_tree.root)

            sku = input("No. SKU: ")
            jumlah_stok_baru = int(input("Menambahkan Jumlah Stok Baru: "))
            bins_tree.restock(sku, jumlah_stok_baru)

        elif choice1 == "13":
            print("=====|You Choice 'Tampilkan Data Barang'|=====")
            def display_item_details(node):
                if node is None:
                    return
                display_item_details(node.left)
                if node.jumlah_stok > 0:
                    print(f"{node.sku}\t{node.nama_barang}")
                display_item_details(node.right)

            print("SKU\tNama Barang")
            display_item_details(bins_tree.root)

            sku = input("No. SKU: ")
            item_node = bins_tree.find_node(bins_tree.root, sku)
            if item_node is None:
                print("Item not found.")
            else:
                print("=====|Tampilan Rincian Data: |=====")
                print("-----------------------------------")
                print("SKU:", item_node.sku)
                print("Nama Barang:", item_node.nama_barang)
                print("Harga Barang:", item_node.harga_barang)
                print("Jumlah Stok:", item_node.jumlah_stok)
                print("-----------------------------------")

        elif choice1 == "14":
            print("=====|You Choice 'Hapus Data Barang'|=====")
            sku = input("No. SKU: ")
            deleted = bins_tree.delete_node(sku)
            if deleted:
                print("Data barang dengan SKU", sku, "telah dihapus.")
            else:
                print("Data barang dengan SKU", sku, "tidak ditemukan.")

        elif choice1 == "0":
            break

        else:
            print("Sorry, Not Available Yet")

def submenu2(bins_tree, trans_data):
    
    while True:
        print("=====|You Choice 'Kelola Transaksi Konsumen' |=====")
        print("[21] Input Data Transaksi Baru")
        print("[22] Lihat Data Seluruh Transaksi Konsumen")
        print("[23] Lihat Data Transaksi Berdasarkan Subtotal")
        print("[0] Back to Main Menu")

        choice2 = input("Select a menu: ")

        if choice2 == "21":
            print("=====|You Choice 'Input Data Transaksi Baru'|======")

            def display_stock_data(node):
                if node is not None:
                    display_stock_data(node.left)
                    print(f"{node.sku}\t{node.nama_barang}\t\t{node.harga_barang}\t\t{node.jumlah_stok}")
                    display_stock_data(node.right)

            print("SKU\tNama Barang\tHarga Barang\tStok Barang")
            display_stock_data(bins_tree.root)

            nama_konsumen = input("Masukkan Nama Konsumen: ")

            while True:
                sku_barang = input("Masukkan No. SKU barang yang dibeli: ")
                node = bins_tree.find_node(bins_tree.root, sku_barang)

                if node is not None:
                    jumlah_beli = int(input("Masukkan Jumlah Barang yang dibeli: "))

                    if node.jumlah_stok >= jumlah_beli:
                        node.jumlah_stok -= jumlah_beli
                        subtotal = node.harga_barang * jumlah_beli
                        trans_data.append([nama_konsumen, sku_barang, jumlah_beli, subtotal])
                        print("=====|Data Transaksi Konsumen Telah Berhasil Diinputkan|=====")

                        if node.jumlah_stok == 0:
                            print("=====|Peringatan: Jumlah Stok Barang telah habis !!!|=====")

                        tambah_data = input("Apakah Customer ada pembelian lain (Y/N)? ")
                        if tambah_data.upper() == "N":
                            break
                    else:
                        print("=====|Jumlah Stok Barang yang ingin dibeli tidak mencukupi|=====")
                        lanjutkan = input("Apakah Anda ingin melanjutkan transaksi (Y/N)? ")
                        if lanjutkan.upper() == "N":
                            break
                else:
                    print("=====|No.SKU Barang yang diinputkan belum terdaftar|=====")
                    lanjutkan = input("Apakah Anda ingin melanjutkan transaksi (Y/N)? ")
                    if lanjutkan.upper() == "N":
                        break

        elif choice2 == "22":
            print("=====|You Choice 'Lihat Data Seluruh Transaksi Konsumen'|=====")
            if len(trans_data) == 0:
                print("=====|Tidak ada data transaksi konsumen yang tersimpan.|=====")
            else:
                print("=====|Data Seluruh Transaksi Konsumen: |=====")
                print("Nama Konsumen\tNo. SKU\t\tJumlah Beli\tSubtotal")
                for transaksi in trans_data:
                    print(f"{transaksi[0]}\t\t{transaksi[1]}\t\t{transaksi[2]}\t\t{transaksi[3]}")

        elif choice2 == "23":
            print("=====|You Choice 'Lihat Data Transaksi Berdasarkan Subtotal'|=====")
            if len(trans_data) == 0:
                print("=====|Tidak ada data transaksi konsumen yang tersimpan.|=====")
            else:
                for i in range(1, len(trans_data)):
                    key = trans_data[i]
                    j = i - 1
                    while j >= 0 and key[3] < trans_data[j][3]:
                        trans_data[j + 1] = trans_data[j]
                        j -= 1
                    trans_data[j + 1] = key

                print("=====|Data Transaksi Konsumen Berdasarkan Subtotal: |=====")
                print("Nama Konsumen\tNo. SKU\tJumlah Beli\tSubtotal")
                for transaksi in trans_data:
                    print(f"{transaksi[0]}\t\t{transaksi[1]}\t{transaksi[2]}\t\t{transaksi[3]}")

        elif choice2 == "0":
            break
        else:
            print("=====|Sorry, Not Available Yet|=====")

bins_tree = BinarySearchTree()
trans_data = []

while True:
    menu()
    choice = input("Select a menu: ")

    if choice.upper() == "1":
        submenu1(bins_tree)
    elif choice.upper() == "2":
        submenu2(bins_tree, trans_data)
    elif choice == "0":
        print("==========|Thank You <3|==========")
        break
    else:
        print("=====|Sorry, Not Available Yet|=====")