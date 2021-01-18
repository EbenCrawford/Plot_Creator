# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:12:44 2020

@author: ebenc
"""
from tkinter import *
from tkinter import filedialog
import Plot_C_GUI_v01 as pcg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter.scrolledtext as scrolledtext
from tkinter import ttk

try: 
    import geopandas as gpd
except:
    print("No Geo")

# ===================Map Plots===============================================

def map_plot_fields():
    
    """
    loaded_map_file_name_e = pcg.loaded_map_file_name_e
    loaded_map_file_df_e = pcg.loaded_map_file_df_e
    """
    global loaded_map_file_name_e
    global loaded_map_file_df_e
    #tab3 = pcg.tab3
    page = pcg.tab4
    back_color = pcg.back_color
    forg_color = pcg.forg_color
    
    # ====================Load Data===========================================
    
    select_shape_btn = Button(page, text="Select Shapefile", command=map_shape_select, width=20, bg = back_color, fg = forg_color)
    select_shape_btn.grid(row=0, column=0,padx=15, pady=12, sticky='w')
    
    # =====================File Name==========================================
    
    loaded_map_file_name_e= Entry(page, width=114, bg = back_color, fg = forg_color)
    loaded_map_file_name_e.grid(row=0, column=1, columnspan=4, padx=5, pady=2, sticky='w')
    loaded_map_file_name_e.delete(0, END)
    loaded_map_file_name_e.insert(0, "")

    
    # ========Map Plot Variable Select========================================

    map_plot_var_dd= ttk.Combobox(page, textvariable=pcg.map_plot_var, values=list(pcg.df), width=20, justify='center')
    map_plot_var_dd.grid(row=1, column=0,padx=5, pady=3, sticky='w')
    map_plot_var_dd.delete(0, END)
    map_plot_var_dd.insert(0, "Variable")
    
    # ========Vmin value for colorbar=========================================
    
    v_min_e= Entry(page, textvariable = pcg.v_min, width=15)
    v_min_e.grid(row=1, column=1,padx=10, pady=5, sticky='w')
    v_min_e.delete(0, END)
    v_min_e.insert(0, "Min")
    
    # ========Vmax value for colorbar=========================================
    
    v_max_e= Entry(page, textvariable = pcg.v_max, width=15)
    v_max_e.grid(row=1, column=2,padx=10, pady=5, sticky='w')
    v_max_e.delete(0, END)
    v_max_e.insert(0, "Max")

    # ========Map Color============================================ 
    
    map_color_dd= ttk.Combobox(page, textvariable=pcg.map_color, values=list(pcg.df), width=20, justify='center')
    map_color_dd.grid(row=1, column=3,padx=5, pady=3, sticky='w')
    map_color_dd.delete(0, END)
    map_color_dd.insert(0, "Map Color")
    
        
    # ==================Axis addition=========================================
    
    map_ax_on_c = Checkbutton(page, text="Axis On", variable=pcg.map_ax_on)
    map_ax_on_c.grid(row=1, column=4, sticky='w')
    
    # =========Update map plot===============================================
    
    update_map_plot_btn = Button(page, text="Update Plot", command=map_plot_update, width=20, bg = back_color, fg = forg_color)
    update_map_plot_btn.grid(row=1, column=5,padx=15, pady=12, sticky='w')
    
    # ==============================Map Dataframe View======================
    
    loaded_map_file_df_e= Entry(page, width=60, bg = back_color, fg = forg_color)
    loaded_map_file_df_e.grid(row=2, column=2, columnspan=4, rowspan = 1, padx=5, pady=2, sticky='w')
    loaded_map_file_df_e.delete(0, END)
    loaded_map_file_df_e.insert(0, "")
    
    #with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
                #sub_dir_t = scrolledtext.ScrolledText(meta_data_view_lf,height=8,width=table_width, undo=True)
                #sub_dir_t.insert(END, df_sub.iloc[:,:])
                #sub_dir_t.grid(row=8, column=0, padx=5, pady=2, columnspan=3, sticky='w')

def map_shape_select():
    
    global map_df
    global loaded_map_file_name_e
    global shape_filename
    global loaded_map_file_df_e
    
    shape_filename = filedialog.askopenfilename(initialdir="C:/", title="Select a File", filetypes=(("Shapefile", "*.shp"),("Text files", "*.txt")))
    loaded_map_file_name_e.delete(0, END)
    loaded_map_file_name_e.insert(0, shape_filename)
    
    
    
    map_chart_gen(shape_filename)


    
def map_chart_gen(shape_file):
    
    global ax_map
    global map_df
    page = pcg.tab4
    global shape_filename
    global df_sub
    global loaded_map_file_df_e
    back_color = pcg.back_color
    forg_color = pcg.forg_color
    root = pcg.root
    
    map_df = gpd.read_file(shape_filename)
    # check data type so we can see that this is not a normal dataframe, but a GEOdataframe
    
    # ======================Show Dataframe for plotting ======================
    
    # ==============================Map Dataframe View======================
    
    loaded_map_file_df_e= Entry(page, width=100, bg = back_color, fg = forg_color)
    loaded_map_file_df_e.grid(row=2, column=2, columnspan=4, rowspan = 1, padx=5, pady=2, sticky='w')
    loaded_map_file_df_e.delete(0, END)
    loaded_map_file_df_e.insert(0, list(map_df))
    
    map_figure = plt.Figure(figsize=(root.winfo_width()/170,root.winfo_width()/320), dpi=root.winfo_width()/15)
    
    ax_map = map_figure.add_axes([0.1, 0.23, 0.85, 0.65])
    chart_type = FigureCanvasTkAgg(map_figure, page)
    chart_type.get_tk_widget().grid(row=3, column=0,padx=15, pady=15, columnspan=7, rowspan=7,sticky='ne')

    # ========Map Plot Variable Select========================================

    shape_merge_dd= ttk.Combobox(page, textvariable=pcg.shape_merge, values=list(map_df), width=20, justify='center')
    shape_merge_dd.grid(row=2, column=0,padx=5, pady=3, sticky='w')
    shape_merge_dd.delete(0, END)
    shape_merge_dd.insert(0, "Shape Merge Column")
    
    csv_merge_dd= ttk.Combobox(page, textvariable=pcg.csv_merge, values=list(pcg.df_sub), width=20, justify='center')
    csv_merge_dd.grid(row=2, column=1,padx=5, pady=3, sticky='w')
    csv_merge_dd.delete(0, END)
    csv_merge_dd.insert(0, "CSV Merge Column")
    
    
    map_df.head()
    map_df.plot(ax=ax_map)
    
def map_plot_update():
    
    global ax_map
    global map_df
    page = pcg.tab4
    df_sub = pcg.df_sub
    global shape_filename
    root = pcg.root
    shape_merge = pcg.shape_merge
    csv_merge = pcg.csv_merge
    map_plot_var = pcg.map_plot_var
    
    map_df = gpd.read_file(shape_filename)
    # check data type so we can see that this is not a normal dataframe, but a GEOdataframe
    
    map_figure = plt.Figure(figsize=(root.winfo_width()/170,root.winfo_width()/320), dpi=root.winfo_width()/15)
    
    ax_map = map_figure.add_axes([0.1, 0.23, 0.85, 0.65])
    chart_type = FigureCanvasTkAgg(map_figure, page)
    chart_type.get_tk_widget().grid(row=3, column=0,padx=15, pady=15, columnspan=7, rowspan=7,sticky='ne')

    #print(map_df)

    map_df[shape_merge.get()] = map_df[shape_merge.get()].astype(str)
    df_sub[csv_merge.get()] = df_sub[csv_merge.get()].astype(str)
    
    map_m_df = map_df.set_index(shape_merge.get()).join(df_sub.set_index(csv_merge.get()), how = "outer")
    
    #map_m_df = map_df.merge(df_sub, left_on = shape_merge.get(), right_on = csv_merge.get())
    
    print("THIS IS RIGHT AFTER MERGE")
    #print(map_m_df)
    
    map_m_df.plot(column=map_plot_var.get(), cmap =    
                                'YlGnBu', figsize=(15,9),   
                                 scheme='quantiles', k=3, legend =  
                                  True)
    print(map_m_df.head())
    #print(type(map_m_df))
    
    loaded_map_file_df_e.delete(0, END)
    loaded_map_file_df_e.insert(0, map_m_df)
    
    print(map_m_df)
    print(map_plot_var.get())
    
    #map_m_df.plot(column = map_plot_var.get(), cmap = 'Blues', linewidth=0.8, ax=ax_map, edgecolor='0.8')
    map_m_df.plot(column = map_plot_var.get(), ax=ax_map)

