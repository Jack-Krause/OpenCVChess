# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:53:46 2025

@author: jackm
"""

import numpy as np
from dataclasses import dataclass

@dataclass
class Line:
    x1: float
    y1: float
    x2: float
    y2: float
    
    def length(self) -> float:
        return np.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)