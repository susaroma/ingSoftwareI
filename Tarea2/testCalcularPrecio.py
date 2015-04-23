'''

Created on 22/4/2015
@author: susyroma

'''
from calcularPrecio import *
import unittest
<<<<<<< HEAD
=======
from calcularPrecio import *
>>>>>>> 23cc3419d9c8fb3d04e03b5517c53313ca54dc57
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
        # Caso de prueba tiempo de reservacion = (15) minutos, tarifa pequena
        tarifaPrueba = Tarifa(50,100)
        reservaIni = datetime(2015, 4, 21, 6, 15, 0, 0)
        reservaFin = datetime(2015, 4, 21, 6, 30, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio, 12.50) 

    def test7DaysTimer(self):
        # Caso de prueba tiempo de reservacion = (7) dias con tarifa decima
        tarifaPrueba = Tarifa(5.50,7.25)
        reservaIni = datetime(2015, 4, 21, 6, 15, 0, 0)
        reservaFin = datetime(2015, 4, 28, 6, 15, 0, 0)
        tiempoReserva = [reservaIni,reservaFin]
        precio = calcularPrecio(tarifaPrueba, tiempoReserva)
        self.assertEqual(precio,((5.50*5)+(7.25*2)))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()