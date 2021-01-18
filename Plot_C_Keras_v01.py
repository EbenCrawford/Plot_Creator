# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:30:04 2020

@author: ebenc
"""

from tkinter import *
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter.scrolledtext as scrolledtext
from tkinter import ttk
import ctypes
from sklearn.metrics import *

try:
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.activations import hard_sigmoid
except:
    print("No Keras")
    


import Plot_C_GUI_v01 as pcg
import numpy as np
import Plot_C_dataframe_v01 as pcd

def keras_gui():
    
    back_color = pcg.back_color
    forg_color = pcg.forg_color
    page = pcg.tab5
    
    run_sgd_btn = Button(page, text = "Active Data",
                                         command = run_stochastic_gradient_descent, 
                                         bg = back_color, 
                                         fg = forg_color)
    run_sgd_btn.grid(row=5, column=0, padx=20, pady=3, sticky='w')
    
    #run_sgd_btn = LabelFrame(page, text="SGD Run", padx=1, pady=1, bg=back_color, fg=forg_color, width=130)
    #run_sgd.btn.grid(row=0, column=0, padx=15, pady=5, columnspan=2, sticky='nw')

def run_stochastic_gradient_descent():
    
    
    # ============SELECT DATAFRAME AND SPLIT==================================
    
    df=pcg.df
    df_split = np.array_split(df,2)
    
    # =============SET TEST SET AND TRAINING SET==============================
    
    x=df_split[0]
    y=df_split[1]

    # ==================CREATE MODEL==========================================
    
    model = Sequential()
    model.add(Dense((len(df.columns),), input_shape= (len(df.columns),), activation=hard_sigmoid, kernel_initializer='glorot_uniform'))
    model.compile(loss='binary_crossentropy', optimizer= 'adam', metrics= ['accuracy'])
    model.fit(x, y, epochs=225, batch_size= 25, verbose= 1, validation_split= 0.2)
    model.summary()