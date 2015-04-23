'''
Created on 22/4/2015
ll
@author: susyroma
'''
import unittest
from calcularPrecio import *
from datetime import *

class Test(unittest.TestCase):


    def testFinSemana(self):
        tarifa = Tarifa (25,45)
        inicioDeReservacion = datetime(2015,4,25,12,30,0,0)
        finDeReservacion = datetime(2015,4,26,12,30,0,0)
        tiempoDeReservacionr = [inicioDeReservacion, finDeReservacion]
        self.assertTrue(1080 == self.calcularPrecio(tarifa,tiempoDeReservacionr)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()