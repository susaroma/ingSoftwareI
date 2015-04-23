'''

Created on 22/4/2015
@author: Susana Rodriguez 11-10893
        Marisela Del Valle 11-10267

'''
import unittest
from calcularPrecio import *
from datetime import *
from decimal import *


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
        self.assertEqual(precio,round(Decimal(((((10.12)*2430)+((15.3)*1890))/ 60)),2))
        
    def testFinASemana(self):
        # Caso de prueba dias de reservacion (empieza fin de semana y termina en semana) con tarifa entera
        tarifaPrueba = Tarifa(17,23)
        reservaIni = datetime(2015, 5, 16, 5, 0, 0, 0)
        reservaFin = datetime(2015, 5, 18, 5, 0, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio,Decimal(((17*300)+(23*2580))/60))
        
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
        # Caso de prueba con tarifa negativa
        tarifaPrueba = Tarifa(-2, -3)
        reservaIni = datetime(2015, 4, 19, 12, 15, 0, 0)
        reservaFin = datetime(2015, 4, 19, 12, 45, 0, 0)
        tiempoReserva = [reservaIni, reservaFin]
        self.assertRaises(Exception, calcularPrecio,tarifaPrueba, tiempoReserva)
        
    def testFechaInvalida(self):
        # Caso de prueba con tiempo de reservacion invalido
        tarifaPrueba = Tarifa(4, 6)
        reservaIni = datetime(2015, 4, 30, 12, 15, 0, 0)
        reservaFin = datetime(2015, 4, 19, 12, 45, 0, 0)
        tiempoReserva = [reservaIni, reservaFin]
        self.assertRaises(Exception, calcularPrecio,tarifaPrueba, tiempoReserva)
        
    def testTiempoMenor14Min(self):
        # Caso de prueba tiempo menor a (14) minutos
        tarifaPrueba = Tarifa(4, 6)
        reservaIni = datetime(2015, 6, 29, 12, 0, 0, 0)
        reservaFin = datetime(2015, 6, 29, 12, 14, 0, 0)
        tiempoReserva = [reservaIni, reservaFin]
        self.assertRaises(Exception, calcularPrecio,tarifaPrueba, tiempoReserva)
        
    def testTiempoExcedido(self):
        # Caso de prueba tiempo de reservacion excedido
        tarifaPrueba = Tarifa(4, 6)
        reservaIni = datetime(2015, 2, 20, 6, 0, 0, 0)
        reservaFin = datetime(2015, 2, 27, 6, 1, 0, 0)
        tiempoReserva = [reservaIni, reservaFin]
        self.assertRaises(Exception, calcularPrecio,tarifaPrueba, tiempoReserva)
        
    def testTiempo60minutosDiaSem (self):
        # Caso de prueba tiempo de (60) minutos en un dia de la semana
        tarifaPrueba = Tarifa(12,23)
        reservaIni = datetime(2015, 6, 29, 12, 0, 0, 0)
        reservaFin = datetime(2015, 6, 29, 13, 0, 0, 0)
        tiempoReserva = [reservaIni, reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio, ((12*60 / 60)))
        
    def testTiempo60minutosFinSem (self):
        # Caso de prueba tiempo de (60) minutos en un dia del fin de semana
        tarifaPrueba = Tarifa(12,23)
        reservaIni = datetime(2015, 4, 19, 12, 0, 0, 0)
        reservaFin = datetime(2015, 4, 19, 13, 0, 0, 0)
        tiempoReserva = [reservaIni, reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio, ((23*60 / 60)))
        
if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
