# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:11:35 2020

@author: lourd
"""

import serial

def main():
    #declare port, baud, and file path
    serial_port = '/dexy/ttyACME'
    baud_rate = 9600
    write_to_file_path = "waterquality.csv"
    
    #open file for writing and get serial feed
    output_file = open(write_to_file_path, 'w+')
    ser = serial.serial(serial_port, baud_rate)
    
    
    #write serial output to a csv file 
    output_file.write('distance\n')
    n = 0
    while n < 20: #amount of iterations and typing onto csv
        line = ser.readline()
        line = line.decode('utf-8')
        output_file.write(line)
        n += 1
        
    output_file.close()
        
if __name__ == "main":
    main()