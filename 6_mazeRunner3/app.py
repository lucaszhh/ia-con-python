from entities import *

""" import laberintos """
laberintoTxt = "./laberintos/laberinto.txt"
laberintoTxt1 = "./laberintos/laberinto1.txt"
laberintoTxt2 = "./laberintos/laberinto2.txt"
laberintoTxt3 = "./laberintos/laberinto3.txt"

""" Posibles algoritmos BFS DFS GBFS A* """

Laberinto("BFS", laberintoTxt3).resolver()
Laberinto("DFS", laberintoTxt3).resolver()
Laberinto("GBFS", laberintoTxt3).resolver()
Laberinto("A*", laberintoTxt3).resolver()
