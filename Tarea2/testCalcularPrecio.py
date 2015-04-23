'''
Created on 22/4/2015
ll
@author: susyroma
'''
import unittest
from calcularPrecio import *
from datetime import *

class Test(unittest.TestCase):

    
    def testSieteDias(self):
        # Caso de prueba de tiempo de reservacion (7) dias
        tarifa = Tarifa (90,180)
        inicioDeReservacion = datetime(2015,7,20,20,30,0,0)
        finDeReservacion = datetime(2015,7,27,20,30,0,0)
        tiempoDeReservacionr = [inicioDeReservacion, finDeReservacion]
        self.assertTrue(19440.00 == calcularPrecio(tarifa,tiempoDeReservacionr))
        
    def testFinSemana(self):
        # Caso de prueba de dias de reservacion (fin de semana)
        tarifa = Tarifa (25,45)
        inicioDeReservacion = datetime(2015,4,25,12,30,0,0)
        finDeReservacion = datetime(2015,4,26,12,30,0,0)
        tiempoDeReservacionr = [inicioDeReservacion, finDeReservacion]
        self.assertTrue(1080 == calcularPrecio(tarifa,tiempoDeReservacionr))
                        
    def testSemana(self):
        # Caso de prueba de dias de reservacion (dias de semana)
        tarifa = Tarifa(50,75)
        inicioDeReservacion = datetime(2015,4,28,18,45,0,0)
        finDeReservacion = datetime(2015,4,30,20,00,0,0)
        tiempoDeReservacionr = [inicioDeReservacion, finDeReservacion]
        self.assertTrue(2462 == calcularPrecio(tarifa,tiempoDeReservacionr))
        
    def testFechaErronea(self):
        # Caso de falla para entrada de fecha invalida
        tarifa = Tarifa(31,77)
        inicioDeReservacion = datetime(2015,4,28,18,45,0,0)
        finDeReservacion = datetime(2014,4,30,20,00,0,0)
        tiempoDeReservacionr = [inicioDeReservacion, finDeReservacion]
        self.assertRaises(Exception,calcularPrecio,tarifa,tiempoDeReservacionr)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()