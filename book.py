#!/usr/bin/env python
# Copyright (C) 2022 francescoleonetti1234@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""First assignment for the CMEPDA course, 2022/23"""

import argparse
import time
import matplotlib.pyplot as plt

t_iniziale = time.time()

def process(file_path):
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r', encoding = 'utf-8') as input_file:
        text = input_file.read()
    #print(text)
    #print(len(text))
    #
    dictionary_minuscole = {}
    dictionary_maiuscole = {}
    dictionary_finale = {}

    for i in range(ord('a'), ord('z')+1,1):
        dictionary_minuscole[chr(i)] = 0
        dictionary_finale[chr(i)] = 0
        dictionary_maiuscole[chr(i-32)] = 0

    for i in range(len(text)):
        if ord(text[i]) <= ord('z') and ord(text[i]) >= ord('a'):
            dictionary_minuscole[text[i]] += 1

    for i in range(len(text)):
        if ord(text[i]) <= ord('Z') and ord(text[i]) >= ord('A'):
            dictionary_maiuscole[text[i]] += 1

    for i in range (ord('a'), ord('z')+1,1):
        dictionary_finale[chr(i)] = dictionary_minuscole[chr(i)] + dictionary_maiuscole[chr(i-32)]

    width = 0.7
    plt.figure('Grafico')
    plt.title('Istogramma')
    plt.xlabel('Lettera alfabeto latino')
    plt.ylabel('Frequenza')
    plt.bar(dictionary_finale.keys(), dictionary_finale.values(), width,
    align='center', color = 'darkorange')
    plt.show()

    t_finale = time.time()
    intervallo = t_finale - t_iniziale
    print(f'The total elapsed time is {intervallo}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='path to the input file')
    args = parser.parse_args()
    process(args.infile)
