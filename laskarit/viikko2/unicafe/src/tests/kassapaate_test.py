import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_rahamaara_ja_lounasmaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    

    def test_riittava_edullinen_kateismaksu_kasvattaa_kassaa_oikein_ja_palauttaa_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_riittava_maukas_kateismaksu_kasvattaa_kassaa_oikein_ja_palauttaa_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_riittava_edullinen_kateismaksu_kasvattaa_myyntien_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_riittava_maukas_kateismaksu_kasvattaa_myyntien_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_riittamaton_edullinen_kateismaksu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_riittamaton_maukas_kateismaksu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_jos_kortilla_tarpeeksi_rahaa_edullinen_veloitetaan_ja_palutetaan_true(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)

    def test_jos_kortilla_tarpeeksi_rahaa_maukas_veloitetaan_ja_palutetaan_true(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)

    def test_jos_kortilla_tarpeeksi_rahaa_edulliset_kasvavat(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_jos_kortilla_tarpeeksi_rahaa_maukkaat_kasvavat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_riittamaton_edullinen_korttimaksu(self):
        kortti = Maksukortti(230)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(kortti.saldo_euroina(), 2.3)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_riittamaton_maukas_korttimaksu(self):
        kortti = Maksukortti(230)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(kortti.saldo_euroina(), 2.3)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassan_rahamaara_ei_muutu_kortilla_ostaessa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahan_lataaminen_muuttaa_saldoa_ja_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 11.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_negatiivisen_maaran_lataaminen_ei_onnistu(self):
        self.assertIsNone(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -4))
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_rahaa_euroina_palauttaa_oikean_summan(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        

    

    
