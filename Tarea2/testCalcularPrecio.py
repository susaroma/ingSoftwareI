'''

Created on 22/4/2015
@author: susyroma

'''
from calcularPrecio import *
import unittest
from datetime import *


class CasosDePrueba(unittest.TestCase):
    
    def test0Timer(self):
        # Caso de prueba tiempo de reservacion = (0) minutos
        tarifaPrueba = Tarifa(15,17)
        reservaIni = datetime(2015, 4, 23, 9, 20, 0, 0)
        reservaFin = datetime(2015, 4, 23, 9, 20, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        try:
            calcularPrecio(tarifaPrueba, tiempoReserva)
        except:
            pass
    
    def test15MTimeSmallT(self):
        # Caso de prueba tiempo de reservacion = (15) minutos, tarifa pequenia
        tarifaPrueba = Tarifa(1.75, 7)
        reservaIni = datetime(2015, 4, 21, 6, 15, 0, 0)
        reservaFin = datetime(2015, 4, 21, 6, 30, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio, 1.75) 
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()