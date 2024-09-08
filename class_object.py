class NhanVien:
    def __init__(self, ma_nhan_vien: int, ten: str, tuoi: int, dia_chi: str, luong: int, gio_lam: float):
        self.ma_nhan_vien = ma_nhan_vien
        self.ten = ten
        self.tuoi = tuoi
        self.dia_chi = dia_chi
        self.luong = luong
        self.gio_lam = gio_lam


    def printInfor(self):
        print(self.ma_nhan_vien, self.ten, self.tuoi, self.dia_chi, self.luong, self.gio_lam)

    def tinhThuong(self):
        if self.gio_lam >= 200:
            thuong = self.luong * 20 / 100
        elif 100 <= self.gio_lam < 200:
            thuong = self.luong * 10 / 100
        elif self.gio_lam < 100:
            thuong = 0

        print(f'So tien thuong la: {thuong}')

thong_tin = NhanVien("001", "Tran Van Cong", 45, "30 Loseby", 1200000, 210.5)
thong_tin.printInfor()
thong_tin.tinhThuong()


class Vehicle():
    def __init__(self, ten, toc_do, so_km_da_di):
        self.ten = ten
        self.toc_do = toc_do
        self.so_km_da_di = so_km_da_di

    def __str__(self):
        return f"{self.ten}, {self.toc_do}, {self.so_km_da_di}"

class Bus(Vehicle):
    pass


thong_tin_xe_bus = Bus("City Bus", "120 km/h", 2000)
print(thong_tin_xe_bus)





