# coding: utf-8

class Otomobil(object):
    def __init__(self, hiz = 0):
        """
        Eğer sınıf çağırılırken başlangıç hızı belirtilmediyse sıfır alınacak.
        """        
        self.hiz_km = {0: 0, 10: 1, 20: 3, 30: 5, 40: 8, 50: 11, 60: 14, 70: 17, 80: 20, 90: 23, 100: 26}
        self.hiz = hiz
        self.mesafe = 0

    def calistir(self):
        print 'Otomobil çalıştırıldı. Gitmeye hazır.'


    def durdur(self):
        print 'Otomobilin kontağı kapatıldı. Yapılan toplam mesafe: %dkm.' % (self.mesafe)


    def hizlan(self):
        if self.hiz % 10 == 0:
            self.hiz += 10
            self.mesafe += self.hiz_km[self.hiz]
            print 'Gaza basıldı. Soz hız: %dkm/s' % (self.hiz)


    def yavasla(self):
        if self.hiz == 0:
            print 'Otomobil zaten duruyor.'
        elif self.hiz % 10 == 0:
            self.hiz -= 10
            self.mesafe += self.hiz_km[self.hiz]
            print 'Frene basıldı. Soz hız: %dkm/s' % (self.hiz)            
