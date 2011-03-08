# coding: utf-8

class MotorYandi(RuntimeError):
    pass

class BenzinBitti(Exception):
    pass


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
        raise BenzinBitti


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


    def depo_kapagini_ac(self, miktar = 20):
        for i in (self.hiz / 10):
            self.yavasla()

        return Depo(miktar)


    class Depo(object):
        def __init__(self, miktar):
            self.miktar = miktar


        def koy(self, miktar):
            self.miktar += miktar
            print '%dlt benzin konuldu. Yeni miktar: %dlt.' % (miktar, self.miktar)


        def cek(self, miktar):
            if miktar > self.miktar:
                miktar_cache = self.miktar                
                print '%dlt benzin istendi ancak depoda %dlt benzin olduğundan %dlt çekildi.' % (miktar, miktar_cache, miktar_cache)
                self.miktar = 0
                return miktar_cache

            self.miktar -= miktar
            print '%dlt benzin çekildi. Yeni miktar: %dlt.' % (miktar, self.miktar)


    class Motor(object):
        def __init__(self, depo):
            self.depo = depo
            self.asiri_yuklenme = 0

        def calis(self):
            if Otomobil.hiz > 100 and self.asiri_yuklenme == 3:
                pass

    class BenzinIstasyonu(object):
        def benzin_doldur(self, otomobil, miktar):
            pass
