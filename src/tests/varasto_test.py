import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_palauttaa_oikein_jos_maara_on_0(self):
        self.varasto.lisaa_varastoon(0)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara,0)

    def test_lisays_palauttaa_oikein_jos_maara_pienempi_kuin_0(self):
        self.varasto.lisaa_varastoon(-2)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara,0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tarkista_virheellinen_tilavuus(self):
        varasto = Varasto(-23)

        self.assertAlmostEqual(varasto.tilavuus,0)

    #    
    def test_tarkista_alku_saldo_virheellinen(self):
        varasto = Varasto(0, alku_saldo=-50)

        self.assertAlmostEqual(varasto.saldo, 0)
    
    def test_ota_varastosta_negatiivinen(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-23),0.0)
    
    def test_jos_maara_on_suurempi_kuin_paljonko_mahtuu(self):
        s = self.varasto.lisaa_varastoon(20000)
        self.assertAlmostEqual(self.varasto.saldo,self.varasto.tilavuus)

    def test_oikea_tulostus(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")