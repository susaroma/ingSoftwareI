'''

Created on 22/4/2015
@author: susyroma

'''
from calcularPrecio import *
import unittest
from datetime import *


class CasosDePrueba(unittest.TestCase):
    
    def testTiempo0(self):
        # Caso de prueba tiempo de reservacion = (0) minutos
        tarifaPrueba = Tarifa(15,17)
        reservaIni = datetime(2015, 4, 23, 9, 20, 0, 0)
        reservaFin = datetime(2015, 4, 23, 9, 20, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        try:
            calcularPrecio(tarifaPrueba, tiempoReserva)
        except:
            pass
    
    def testMin15minutos(self):
        # Caso de prueba tiempo de reservacion = (15) minutos, tarifa pequena
        tarifaPrueba = Tarifa(50,100)
        reservaIni = datetime(2015, 4, 21, 6, 15, 0, 0)
        reservaFin = datetime(2015, 4, 21, 6, 30, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio, 12.50) 

    def test7Dias(self):
        # Caso de prueba tiempo de reservacion = (7) dias con tarifa decimal
        tarifaPrueba = Tarifa(5.50,7.25)
        reservaIni = datetime(2015, 4, 19, 6, 0, 0, 0)
        reservaFin = datetime(2015, 4, 26, 6, 0, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio,((5.50*7200)+(7.25*2880))/ 60)
        
    def testTarifaGrande(self):
        # Caso de prueba de una tarifa muy grande
        tarifaPrueba = Tarifa(3**21,3**32)
        reservaIni = datetime(2015, 4, 19, 6, 0, 0, 0)
        reservaFin = datetime(2015, 4, 26, 6, 0, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio, (((3**21)*7200 + (3**32)*2880)/ 60))
        
    def testTarifaNegativa(self):
        tarifaPrueba = Tarifa(-2, -3)
        reservaIni = datetime(2015, 4, 19, 12, 15, 0, 0)
        reservaFin = datetime(2015, 4, 19, 12, 45, 0, 0)
        tiempoReserva = [reservaIni, reservaFin]
        self.assertRaises(Exception, calcularPrecio,tarifaPrueba, tiempoReserva)
        
    def testFechaInvalida(self):
        tarifaPrueba = Tarifa(4, 6)
        reservaIni = datetime(2015, 4, 30, 12, 15, 0, 0)
        reservaFin = datetime(2015, 4, 19, 12, 45, 0, 0)
        tiempoReserva = [reservaIni, reservaFin]
        self.assertRaises(Exception, calcularPrecio,tarifaPrueba, tiempoReserva)
        
    def testTiempoMenor14Min(self):
        tarifaPrueba = Tarifa(4, 6)
        reservaIni = datetime(2015, 6, 29, 12, 0, 0, 0)
        reservaFin = datetime(2015, 6, 29, 12, 14, 0, 0)
        tiempoReserva = [reservaIni, reservaFin]
        self.assertRaises(Exception, calcularPrecio,tarifaPrueba, tiempoReserva)

if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()