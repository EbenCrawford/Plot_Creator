# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:05:47 2020

@author: ebenc
"""

import os
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
from scipy.signal import savgol_filter

import Plot_C_GUI_v01 as pcg
#import Plot_C_plot_v01 as pcp



#global dataframe_select_count
dataframe_select_count = 0
global actvie_data_name
actvie_data_name = "dataframe"



# ======================Update Table==========================================

def update_table():
    global df
    global file_table_lf
    df = pcg.df
    tab_loc = pcg.df_1_tab
    tv_dim = pcg.df_dir_dim
    #file_table_lf = pcg.file_table_lf
    
    table_width = int(pcg.root.winfo_width()/21)
    
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  
        loaded_prev_name_t = scrolledtext.ScrolledText(tab_loc,height=16,width=table_width, undo=True)
        if len(df.index) < 100:
            loaded_prev_name_t.insert(END, df.iloc[:,:])
        
        else:
            df_print = df.iloc[:50,:]
            df_print = df_print.append(df.iloc[-50,:])
            
            loaded_prev_name_t.insert(END, df_print.iloc[:,:])
        loaded_prev_name_t.grid(row=0, column=0, padx=15, pady=15, columnspan=4, sticky='n')
        
    # ========DATAFRAME DIMENSIONS========================================
    
    df_dir_dim_e = Entry(tab_loc, textvariable = tv_dim, width=40)
    df_dir_dim_e.grid(row=3, column=0,padx=10, pady=5, sticky='e', columnspan=2)
    df_dir_dim_e.delete(0, END)
    df_dir_dim_e.insert(0, str(len(df.index))+ " Rows x " + str(len(df.columns)))

    pcg.reset_dd_menus()

#----------Create Subset view-------------------------------------------------

def create_subset_view():
    
    global df
    df = pcg.df
    global df_sub
    global df_2
    root= pcg.root
    global df_m
    tab_loc = pcg.df_s_tab
    tv_dim = pcg.sub_dir_dim
    
    df_sub = df.iloc[:,:]
    df_2 = []
    df_m = []
    
    table_width = int(root.winfo_width()/21)
    
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        sub_dir_t = scrolledtext.ScrolledText(tab_loc, height=16, width=table_width, undo=True)
                
        if len(df_sub.index) < 100:
            sub_dir_t.insert(END, df_sub.iloc[:,:])
        
        else:
            df_print = df_sub.iloc[:50,:]
            df_print = df_print.append(df_sub.iloc[-50,:])
            
            sub_dir_t.insert(END, df_print.iloc[:,:])
                    
        sub_dir_t.grid(row=0, column=0, padx=15, pady=15, columnspan=4, sticky='w')

    # ========SUB DATAFRAME DIMENSIONS========================================
    
    sub_dir_dim_e= Entry(tab_loc, textvariable = tv_dim, width=40)
    sub_dir_dim_e.grid(row=3, column=0,padx=10, pady=5, sticky='e', columnspan=2)
    sub_dir_dim_e.delete(0, END)
    sub_dir_dim_e.insert(0, str(len(df_sub.index))+ " Rows x " + str(len(df_sub.columns)))


# ===================Update Sub set of data===================================
def update_subset_view(df_sub):
    
    #df_sub = pcg.df_sub
    #global meta_data_view_lf
    tv_dim = pcg.sub_dir_dim
    tab_loc = pcg.df_s_tab
    
    table_width = int(pcg.root.winfo_width()/21)
    
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  
        sub_dir_t = scrolledtext.ScrolledText(tab_loc,height=15,width=table_width, undo=True)
        
        if len(df_sub.index) < 100:
            sub_dir_t.insert(END, df_sub.iloc[:,:])
        
        else:
            df_print = df_sub.iloc[:50,:]
            
            df_print = df_print.append(df_sub.iloc[-50,:])
            
            sub_dir_t.insert(END, df_print.iloc[:,:])
            
        sub_dir_t.grid(row=0, column=0, padx=15, pady=15, columnspan=4, sticky='n')
    
    
    # ========SUB DATAFRAME DIMENSIONS========================================
    
    sub_dir_dim_e= Entry(tab_loc, textvariable = tv_dim, width=40)
    sub_dir_dim_e.grid(row=3, column=0,padx=10, pady=5, sticky='e', columnspan=2)
    sub_dir_dim_e.delete(0, END)
    sub_dir_dim_e.insert(0, str(len(df_sub.index))+ " Rows x " + str(len(df_sub.columns)))

# =====================UPLOAD SECOND DATAFRAME================================

def upload_2nd_dataframe_view():
    

    global df_2
    global file_table_lf
    df_2 = pcg.df_2
    df_2_table_loc = pcg.df_2_tab
    tv_dim = pcg.sec_dir_dim
    #file_table_lf = pcg.file_table_lf
    
    table_width = int(pcg.root.winfo_width()/21)
    
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  
        df_2_t = scrolledtext.ScrolledText(df_2_table_loc,height=16,width=table_width, undo=True)
        if len(df_2.index) < 100:
            df_2_t.insert(END, df_2.iloc[:,:])
        
        else:
            df_print = df_2.iloc[:50,:]
            df_print = df_print.append(df_2.iloc[-50,:])
            
            df_2_t.insert(END, df_print.iloc[:,:])
            
        df_2_t.grid(row=0, column=0, padx=15, pady=15, columnspan=4, sticky='n')
    
    # ========2nd DATAFRAME DIMENSIONS========================================
    
    sec_dir_dim_e = Entry(df_2_table_loc, textvariable = tv_dim, width=40)
    sec_dir_dim_e.grid(row=3, column=0,padx=10, pady=5, sticky='e', columnspan=2)
    sec_dir_dim_e.delete(0, END)
    sec_dir_dim_e.insert(0, str(len(df_2.index))+ " Rows x " + str(len(df_2.columns)))
    
    pcg.reset_dd_menus()
    

def merge_dataframe_view():
    
    global df_m
    global file_table_lf
    global df_sub
    global df_2
    
    df_int_type_table = pcg.df_int_type_table
    merge_pos_table =  pcg.merge_pos_table
    tv_dim = pcg.m_dir_dim

    
    right_dataframe = pcg.right_dataframe.get()
    left_dataframe = pcg.left_dataframe.get()
    merge_position = pcg.merge_position.get()
    data_int_method = pcg.data_int_method.get()
    
    df_m_table_loc = pcg.df_m_tab

    
    table_width = int(pcg.root.winfo_width()/21)
    
    if data_int_method == 'Join':
        
        df_m = df_sub.join(df_2)
        
    else:
        
        df_m = df_sub.merge(df_2, how=merge_position, left_on=left_dataframe, right_on=right_dataframe)
            
    
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  
        df_m_t = scrolledtext.ScrolledText(df_m_table_loc,height=16,width=table_width, undo=True)
        if len(df_m.index) < 100:
            df_m_t.insert(END, df_m.iloc[:,:])
        
        else:
            df_print = df_m.iloc[:50,:]
            df_print = df_print.append(df_m.iloc[-50,:])
            
            df_m_t.insert(END, df_print.iloc[:,:])
            
        df_m_t.grid(row=1, column=0, padx=15, pady=15, columnspan=4, sticky='n')
    
    # ========MERGE DATAFRAME DIMENSIONS=======================================
    
    m_dir_dim_e = Entry(df_m_table_loc, textvariable = tv_dim, width=40)
    m_dir_dim_e.grid(row=3, column=0,padx=10, pady=5, sticky='e', columnspan=2)
    m_dir_dim_e.delete(0, END)
    m_dir_dim_e.insert(0, str(len(df_m.index))+ " Rows x " + str(len(df_m.columns)))

    #pcg.reset_dd_menus()

def melt_subset():

    print("dataframe 2")

def smooth_signal():
    
    smooth_col = pcg.col_value_1.get()
    smooth_range = int(pcg.col_value_2.get())
    smooth_col_name = pcg.new_col_name.get()
    smooth_poly = int(pcg.col_operator.get())
    df_sub = pcg.df_sub
    
    df_sub[smooth_col_name] = savgol_filter(df_sub[smooth_col], smooth_range, 2, mode='nearest')
    


# =====================Reset subset filter options============================

def update_sub_set():
    global df_sub
    #df_sub = pcg.df_sub
    df = pcg.df
    
    sub_v1 = pcg.sub_set_value_1.get()
    sub_v2 = pcg.sub_set_value_2.get()
    sub_v3 = pcg.sub_set_value_3.get()
    sub_v4 = pcg.sub_set_value_4.get()
    sub_v5 = pcg.sub_set_value_5.get()
    sub_v6 = pcg.sub_set_value_6.get()
    sub_v7 = pcg.sub_set_value_7.get()
    sub_v8 = pcg.sub_set_value_8.get()
    sub_v9 = pcg.sub_set_value_9.get()
    
    sub_op1 = pcg.sub_set_operator_1.get()
    sub_op2 = pcg.sub_set_operator_2.get()
    sub_op3 = pcg.sub_set_operator_3.get()
    sub_op4 = pcg.sub_set_operator_4.get()
    sub_op5 = pcg.sub_set_operator_5.get()
    sub_op6 = pcg.sub_set_operator_6.get()


    if sub_op2 == "Op (2)":
        single_op_subset(sub_v1, sub_v2, sub_op1)
    else:
        double_op_subset(sub_v1, sub_v2, sub_v3, sub_op1, sub_op2)
        
        
    if sub_op3 == "Op (3)":  
        return
    elif sub_op4 == "Op (4)":
        single_op_subset(sub_v4, sub_v5, sub_op3)  
    else:
        double_op_subset(sub_v4, sub_v5, sub_v6, sub_op3, sub_op4)
    
    if sub_op5 == "Op (5)":  
        return
    elif sub_op6 == "Op (6)":
        single_op_subset(sub_v7, sub_v8, sub_op5)  
    else:
        double_op_subset(sub_v7, sub_v8, sub_v9, sub_op5, sub_op6)




# ===================Subset gen single========================================

def single_op_subset(value_1, value_2, op_1):
    df = pcg.df
    global df_sub
    #df_sub = pcg.df_sub
    
    try:
        float(value_2)/2
        if op_1 == '>':
            df_sub = df[df[value_1] > float(value_2)]
        elif op_1 == '<':
            df_sub = df[df[value_1] < float(value_2)]
        elif op_1 == '==':
            df_sub = df[df[value_1] == float(value_2)]
        elif op_1 == '!=':
            df_sub = df[df[value_1] != float(value_2)]
        elif op_1 == '<=':
            df_sub = df[df[value_1] <= float(value_2)]
        elif op_1 == '>=':
            df_sub = df[df[value_1] >= float(value_2)]
        
        
    except:

        try:
            if op_1 == '>':
                df_sub = df[df[value_1] > df[value_2]]   
            elif op_1 == '<':
                df_sub = df[df[value_1] < df[value_2]]  
            elif op_1 == '==':
                df_sub = df[df[value_1] == df[value_2]]
            elif op_1 == '!=':
                df_sub = df[df[value_1] != df[value_2]]
            elif op_1 == '<=':
                df_sub = df[df[value_1] <= df[value_2]]
            elif op_1 == '>=':
                df_sub = df[df[value_1] >= df[value_2]]
            
        except KeyError:
            if op_1 == '>':
                df_sub = df[df[value_1] > value_2]
                
            elif op_1 == '<':
                df_sub = df[df[value_1] < value_2]
                
            elif op_1 == '==':
                df_sub = df[df[value_1].str.contains(value_2)]
                
            elif op_1 == '!=':
                df_sub = df[df[value_1] != value_2]
                
            elif op_1 == '<=':
                df_sub = df[df[value_1] <= value_2]
                
            elif op_1 == '>=':
                df_sub = df[df[value_1] >= value_2]
            print(value_1 + " 2")
            print(value_2 + " 2")
    update_subset_view(df_sub)    
    
# ---------Double Operation subset gen=---------------------------------------
    
    
def double_op_subset(value_1, value_2, value_3, op_1, op_2):
    global df_sub
    #df_sub = pcg.df_sub
    df = pcg.df
    
    try:
        
        float(value_1)/2
        if op_1 == '>':
            df_sub = df[float(value_1) > df[value_2]]
            
        elif op_1 == '<':
            df_sub = df[float(value_1) < df[value_2]]
            
        elif op_1 == '==':
            df_sub = df[float(value_1) == df[value_2]]
            
        elif op_1 == '!=':
            df_sub = df[float(value_1) != df[value_2]]
            
        elif op_1 == '<=':
            df_sub = df[float(value_1) <= df[value_2]]
            
        elif op_1 == '>=':
            df_sub = df[float(value_1) >= df[value_2]]
        
    except ValueError:
        
        if op_1 == '>':
            df_sub = df[df[value_1] > df[value_2]]
            
        elif op_1 == '<':
            df_sub = df[df[value_1] < df[value_2]]
            
        elif op_1 == '==':
            df_sub = df[df[value_1] == df[value_2]]
            
        elif op_1 == '!=':
            df_sub = df[df[value_1] != df[value_2]]
            
        elif op_1 == '<=':
            df_sub = df[df[value_1] <= df[value_2]]
            
        elif op_1 == '>=':
            df_sub = df[df[value_1] >= df[value_2]]
            
    except KeyError:
        if op_1 == '>':
            df_sub = df[df[value_1] > value_2]
            
        elif op_1 == '<':
            df_sub = df[df[value_1] < value_2]
            
        elif op_1 == '==':
            df_sub = df[df[value_1] == value_2]
            
        elif op_1 == '!=':
            df_sub = df[df[value_1] != value_2]
            
        elif op_1 == '<=':
            df_sub = df[df[value_1] <= value_2]
            
        elif op_1 == '>=':
            df_sub = df[df[value_1] >= value_2]
    try:
        
        float(value_3)/2
        if op_1 == '>':
            df_sub = df_sub[df_sub[value_2] > float(value_3)]
            
        elif op_1 == '<':
            df_sub = df_sub[df_sub[value_2] < float(value_3)]
            
        elif op_1 == '==':
            df_sub = df_sub[df_sub[value_2] == float(value_3)]
            
        elif op_1 == '!=':
            df_sub = df_sub[df_sub[value_2] != float(value_3)]
            
        elif op_1 == '<=':
            df_sub = df_sub[df_sub[value_2] <= float(value_3)]
            
        elif op_1 == '>=':
            df_sub = df_sub[df_sub[value_2] >= float(value_3)]
        
    except ValueError:
        
        if op_1 == '>':
            df_sub = df[df[value_2] > df[value_3]]
            
        elif op_1 == '<':
            df_sub = df[df[value_2] < df[value_3]]
            
        elif op_1 == '==':
            df_sub = df[df[value_2] == df[value_3]]
            
        elif op_1 == '!=':
            df_sub = df[df[value_2] != df[value_3]]
            
        elif op_1 == '<=':
            df_sub = df[df[value_2] <= df[value_3]]
            
        elif op_1 == '>=':
            df_sub = df[df[value_2] >= df[value_3]]
            
    except KeyError:
        if op_1 == '>':
            df_sub = df[df[value_2] > value_3]
            
        elif op_1 == '<':
            df_sub = df[df[value_2] < value_3]
            
        elif op_1 == '==':
            df_sub = df[df[value_2] == value_3]
            
        elif op_1 == '!=':
            df_sub = df[df[value_2] != value_3]
            
        elif op_1 == '<=':
            df_sub = df[df[value_2] <= value_3]
            
        elif op_1 == '>=':
            df_sub = df[df[value_2] >= value_3]
            
            
    update_subset_view()
    
    

# ---------Create New Calculated Column----------------

def new_calc_col():
    global df_sub
    df = pcg.df
    df_sub = pcg.df_sub

    try:

        col_to_col_op()

    except KeyError:

        col_to_num_op()

    pcg.update_data_fields()
    update_subset_view(df_sub)
    #update_table()

# -----Column to column operation-------------------------------------------


def col_to_col_op():
    global df_sub
    df = pcg.df
    #df_sub = pcg.df_sub
    col_name = pcg.new_col_name.get()
    col_op = pcg.col_operator.get()
    col_v_1 = pcg.col_value_1.get()
    col_v_2 = pcg.col_value_2.get()
    

    if col_op == "-":
        df_sub[col_name] = df[col_v_1] - df[col_v_2]

    if col_op == "+":
        df_sub[col_name] = df[col_v_1] + df[col_v_2]

    if col_op == "*":
        df_sub[col_name] = df[col_v_1] * df[col_v_2]

    if col_op == "/":
        df_sub[col_name] = df[col_v_1] / df[col_v_2]

    if col_op == "**":
        df_sub[col_name] = df[col_v_1] ** df[col_v_2]

    if col_op == "sqrt()":
        df_sub[col_name] = sqrt(df[col_v_1])


# ------Column to num operations ------------------------------------------


def col_to_num_op():
    global df_sub
    df = pcg.df
    #df_sub = pcg.df_sub
    col_name = pcg.new_col_name.get()
    col_op = pcg.col_operator.get()
    col_v_1 = pcg.col_value_1.get()
    col_v_2 = pcg.col_value_2.get()

    if col_op == "-":
        df_sub[col_name] = df[col_v_1] - float(col_v_2)

    if col_op == "+":
        df_sub[col_name] = df[col_v_1] + float(col_v_2)

    if col_op == "*":
        df_sub[col_name] = df[col_v_1] * float(col_v_2)

    if col_op == "/":
        df_sub[col_name] = df[col_v_1] / float(col_v_2)

    if col_op == "**":
        df_sub[col_name] = df[col_v_1] ** float(col_v_2)

    if col_op == "sqrt()":
        df_sub[col_name] = sqrt(df[col_v_1])

