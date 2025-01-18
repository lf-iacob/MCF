import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Hit():
  def __init__(self, modulo, sensore, tempo):
    self.id_module=modulo
    self.id_sensor=sensore
    self.time_stamp=tempo
  def __repr__(self):
    return 'Modulo: {:}, Sensore: {:}, Time Stamp: {:}'.format(self.id_module, self.id_sensor, self.time_stamp)
  def __str__(self):
    return 'Modulo: {:}, Sensore: {:}, Time Stamp: {:}'.format(self.id_module, self.id_sensor, self.time_stamp)
  def __lt__(self, other):
    if(self.time_stamp!=other.time_stamp):
      return self.time_stamp<other.time_stamp
    elif(self.id_module!=other.id_module):
      return self.id_module<other.id_module
    else:
      return self.id_sensor<other.id_sensor
  def __sub__(self, other):
    return abs(self.time_stamp-other.time_stamp)
