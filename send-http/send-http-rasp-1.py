#### SEND DATA HTTP CONNECTION RASP 1

#---------------------------------------------------------------------------# 
#from pymodbus.client.sync import ModbusTcpClient as ModbusClientTCP
#from pymodbus.client.sync import ModbusUdpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
import requests
import struct
import datetime
from datetime import datetime, date, time
from time import gmtime, strftime, sleep
import json
import urllib
import urllib2
import base64
import time


client = ModbusClient(method='rtu', port='/dev/ttyUSB0', timeout=1, bytesize=8, stopbits=1, baudrate=9600, parity='N')
client.connect()

LmID = 241
jumlahCell = 4
SPB_Lm_ver = "hs-tc-modbus.v1"
SPB_Lm_id = 2411
SPB_Cell_ver = "hs-ta-cellbus.v1"

print "LmID :", LmID
try:
	results = client.read_holding_registers(0003, 2, unit=LmID) 
	Tmod = results.registers[1]
	Tmodf = float(Tmod)/10
	Imod = results.registers[0]
	Imodf = float(Imod)/10
except Exception:
	print "Local Module Modbus ID",Cell, "error, coba cek koneksinya."

for Cell in range(1, jumlahCell+1):
	try:
		time.sleep (0.01)
		result = client.read_holding_registers(0001, 3, unit=Cell) 
		VCell = result.registers[0]
		VCellf = float(VCell)/1000
		TCell = result.registers[1]
		TCellf = float(TCell)/10
		IntRcell = result.registers[2]
		#print IntRcell[Cell]
		IntRcellf = float(IntRcell)/1000
		SOCcell = 100
		SOHcell = 100
		tanggals = datetime.now()
		tanggal = tanggals.strftime("%Y/%m/%d %H:%M:%S")
		payload = {'tanggal':tanggal,'SPB_Lm_id': SPB_Lm_id,'SPB_Lm_ver': SPB_Lm_ver, 'SPB_Cell_id': Cell, 'SPB_Cell_ver': SPB_Cell_ver, 'Vcell': VCellf, 'Tcell': TCellf, 'IntRcell': IntRcellf, 'SOCcell': SOCcell, 'SOHcell': SOHcell, 'Tmod': Tmodf, 'Imod': Imodf}		
		r = requests.get("http://192.168.1.73/capture/database/SPB-put-json.php", params=payload)
		print(r.text)
	except Exception:
		print "Modbus ID",Cell, "error, coba cek koneksinya."

client.close()


client = ModbusClient(method='rtu', port='/dev/ttyUSB1', timeout=1, bytesize=8, stopbits=1, baudrate=9600, parity='N')
client.connect()

LmID = 241
jumlahCell = 4
SPB_Lm_ver = "hs-tc-modbus.v1"
SPB_Lm_id = 2412
SPB_Cell_ver = "hs-ta-cellbus.v1"

print LmID
try:
	results = client.read_holding_registers(0003, 2, unit=LmID) 
	Tmod = results.registers[1]
	Tmodf = float(Tmod)/10
	Imod = results.registers[0]
	Imodf = float(Imod)/10
except Exception:
	print "Local Module Modbus ID",Cell, "error, coba cek koneksinya."

for Cell in range(1, jumlahCell+1):
	try:
		time.sleep (0.01)
		result = client.read_holding_registers(0001, 3, unit=Cell) 
		VCell = result.registers[0]
		VCellf = float(VCell)/1000
		TCell = result.registers[1]
		TCellf = float(TCell)/10
		IntRcell = result.registers[2]
		#print IntRcell[Cell]
		IntRcellf = float(IntRcell)/1000
		SOCcell = 100
		SOHcell = 100
		tanggals = datetime.now()
		tanggal = tanggals.strftime("%Y/%m/%d %H:%M:%S")
		payload = {'tanggal':tanggal,'SPB_Lm_id': SPB_Lm_id,'SPB_Lm_ver': SPB_Lm_ver, 'SPB_Cell_id': Cell, 'SPB_Cell_ver': SPB_Cell_ver, 'Vcell': VCellf, 'Tcell': TCellf, 'IntRcell': IntRcellf, 'SOCcell': SOCcell, 'SOHcell': SOHcell, 'Tmod': Tmodf, 'Imod': Imodf}		
		r = requests.get("http://192.168.1.73/capture/database/SPB-put-json.php", params=payload)
		print(r.text)
	except Exception:
		print "Modbus ID",Cell, "error, coba cek koneksinya."

client.close()