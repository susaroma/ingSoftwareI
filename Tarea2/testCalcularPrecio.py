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
        # Caso de prueba dias de reservacion (fin de semana) con tarifa entera
        tarifaPrueba = Tarifa(10,15)
        reservaIni = datetime(2015, 4, 25, 12, 30, 0, 0)
        reservaFin = datetime(2015, 4, 26, 12, 30, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio,((10*0)+(15*1440))/ 60)
        
    def testSemana(self):
        # Caso de prueba dias de reservacion (semana) con tarifa entera
        tarifaPrueba = Tarifa(8,12)
        reservaIni = datetime(2015, 6, 23, 7, 30, 0, 0)
        reservaFin = datetime(2015, 6, 25, 7, 30, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio,((8*2880)+(12*0))/ 60)
        
    def testSemanaAFin(self):
        # Caso de prueba dias de reservacion (empieza en semana y termina fin de semana) con tarifa decimal
        tarifaPrueba = Tarifa(10.12,15.3)
        reservaIni = datetime(2015, 5, 21, 7, 30, 0, 0)
        reservaFin = datetime(2015, 5, 24, 7, 30, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(round(precio,2),round(((((10.12)*2430)+((15.3)*1890))/ 60),2))
        
    def testFinASemana(self):
        # Caso de prueba dias de reservacion (empieza fin de semana y termina en semana) con tarifa entera
        tarifaPrueba = Tarifa(17,23)
        reservaIni = datetime(2015, 5, 16, 5, 0, 0, 0)
        reservaFin = datetime(2015, 5, 18, 5, 0, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio,((17*300)+(23*2580))/ 60)
        
    '''
    def testHoraMinSemana(self):
        # Caso de prueba tiempo de reservacion (1h y 1m) con tarifa decimal
        tarifaPrueba = Tarifa(17,23)
        reservaIni = datetime(2015, 4, 29, 5, 0, 0, 0)
        reservaFin = datetime(2015, 4, 29, 6, 1, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio,((17*120)+(23*0))/ 60)
    
    def testHoraMinFinSemana(self):
        # Caso de prueba tiempo de reservacion (1h y 1m) con tarifa decimal
        tarifaPrueba = Tarifa(17,23)
        reservaIni = datetime(2015, 4, 26, 5, 0, 0, 0)
        reservaFin = datetime(2015, 4, 26, 6, 1, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio,((17*0)+(23*120))/ 60)
    '''    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()