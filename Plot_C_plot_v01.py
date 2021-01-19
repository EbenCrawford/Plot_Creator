# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:08:12 2020

@author: ebenc
"""
import os
from tkinter import *
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import tkinter.scrolledtext as scrolledtext
from tkinter import ttk
import ctypes
from sklearn.metrics import *
from sklearn.preprocessing import OrdinalEncoder


import Plot_C_GUI_v01 as pcg
import Plot_C_dataframe_v01 as pcd


# ==============Update Plot=================================================

def update_plot_size():
    
    try:
        update_plot()
        
    except:

        print("No Plot")


# ----------------Plot Data-----------------------
def plot_data():
    
    global df_reg_list
    global df_reg_a
    global df_reg_type
    global df_reg_x
    global df_reg_y
    global count
    
    df = pcg.df
    df_sub = pcd.df_sub
    df_2 = pcg.df_2
    df_m = pcd.df_m

    #actvie_data_name = pcd.actvie_data_name
    
    pcg.axis_gui_gen('first')
    pcg.axis_gui_gen('second')
    #chart_opt_gui_gen()
    
    try:
        plt.cla()
    except:
        print("No Chart")
        
    df_select_list = pcg.df_select_list
    df_list = [df, df_sub, df_2, df_m]
    
    for z in range(0,3):
        if pcg.axis_1_dataframe.get() == df_select_list[z]:
            df_1 = df_list[z]    
        if pcg.axis_2_dataframe.get() == df_select_list[z]:
            df_2 = df_list[z] 
    
    var_1 = pcg.Var_Col_1.get()
    var_1_1 = pcg.Var_Col_1_1.get()
    var_x = pcg.Var_Col_x.get()
    
    ent_x_min = pcg.plot_x_axis_min_e
    ent_x_max = pcg.plot_x_axis_max_e
    ent_y_min = pcg.plot_y_axis_min_e
    ent_y_max = pcg.plot_y_axis_max_e
    
    ent_p_name = pcg.plot_name_e
    
    
    if var_1 != "('Y Axis 1',)" and var_x != "('X Axis',)":
        
        ent_x_min.delete(0, END)
        ent_x_max.delete(0, END)
        ent_x_min.insert(0, df_1[var_x].min())
        ent_x_max.insert(0, df_1[var_x].max())


        ent_y_min.delete(0, END)
        ent_y_max.delete(0, END)

        ent_y_min.insert(0, df_1[var_1].min())
        ent_y_max.insert(0, df_1[var_1].max())


        ent_p_name.delete(0, END)
        ent_p_name.insert(0, var_x + " vs " + var_1)
        
        pcg.x_axis_title_e.delete(0, END)
        pcg.x_axis_title_e.insert(0, var_x)
        pcg.y_axis_title_e.delete(0, END)
        pcg.y_axis_title_e.insert(0, var_1)

        pcg.reg_x_axis_dd.delete(0, END)
        pcg.reg_x_axis_dd.insert(0, var_x)
        pcg.reg_y_axis_dd.delete(0, END)
        pcg.reg_y_axis_dd.insert(0, var_1)
        
        if var_1_1 != "('Y Axis 1',)" and var_x != "('X Axis',)":
        
            pcg.y_axis_title_1_e.delete(0, END)
            pcg.y_axis_title_1_e.insert(0, var_1_1)
            
            pcg.plot_y_axis_min_1_e.delete(0, END)
            pcg.plot_y_axis_max_1_e.delete(0, END)
            
            pcg.plot_y_axis_min_1_e.insert(0, df_2[var_1_1].min())
            pcg.plot_y_axis_max_1_e.insert(0, df_2[var_1_1].max())
            
            pcg.reg_x_axis_1_dd.delete(0, END)
            pcg.reg_x_axis_1_dd.insert(0, var_x)
            pcg.reg_y_axis_1_dd.delete(0, END)
            pcg.reg_y_axis_1_dd.insert(0, var_1_1)
        
        count = 0
        df_reg_list = []
        df_reg_a = []
        df_reg_type = []
        df_reg_x = []
        df_reg_y = []
        update_plot()


def update_plot():
    
    global figure
    global ax
    global ax_1
    
    
    root = pcg.root
    tab2 = pcg.tab2
    df = pcg.df
    df_sub = pcd.df_sub
    actvie_data_name = pcd.actvie_data_name
    plot_type = [pcg.graph_type.get(),pcg.graph_type_1.get()]
    
    #Set Min and Max Values
    
    #-------------------Label Names-------------------------------------------
    
    pcg.update_legend_labels()
    
    figure = plt.Figure(figsize=(root.winfo_width()/170,root.winfo_width()/300), dpi=root.winfo_width()/12)
    
    ax = figure.add_axes([0.1, 0.23, 0.75, 0.65])
    chart_type = FigureCanvasTkAgg(figure, tab2)
    chart_type.get_tk_widget().grid(row=0, column=3,padx=15, pady=15, columnspan=4, rowspan=7,sticky='ne')
        
    ax.set_title(pcg.Plot_Name.get(), size=20)
    
    # --------------ADD SECOND AXIS-------------------------------------------
    
    if pcg.Var_Col_1_1.get() != "('Y Axis 1',)":
        ax_1 = ax.twinx()  # instantiate a second axes that shares the same x-axis
        
        if plot_type[1] == "Line":
            cont_x_plot_gen('line',1)
        
        if plot_type[1] == "Plot":
            cont_x_plot_gen('plot',1)
        
        if plot_type[1] == "Scatter":
            cont_x_plot_gen('scatter',1)
        
        if plot_type[1] == "Histogram":
            cont_x_plot_gen('hist',1)
    # -------------Plot Logic-------------------------------------------------
    
    if plot_type[0] == "Line":
        cont_x_plot_gen('line',0)
        
        
    if plot_type[0] == "Plot":
        cont_x_plot_gen('plot',0)
        
    
    if plot_type[0] == "Scatter":
        cont_x_plot_gen('scatter',0)
        
        
    if plot_type[0] == "Histogram":
        cont_x_plot_gen('hist',0)
    
         
    if plot_type[0] == "Pie":
        cont_x_plot_gen('pie',0)
        
    if plot_type[1] == "Pie":
        cont_x_plot_gen('pie',1)
        
        
    if plot_type[0] == "Area":
        cont_x_plot_gen('area',0)
        
    if plot_type[1] == "Area":
        cont_x_plot_gen('area',1)
        
        
    if plot_type[0] == "Hex":
        cont_x_plot_gen('hexbin',0)
        
    if plot_type[1] == "Hex":
        cont_x_plot_gen('hexbin',1)
        
        
    if plot_type[0] == "Density":
        cont_x_plot_gen('density',0)
        
    if plot_type[1] == "Density":
        cont_x_plot_gen('density',1)
        
        
    if plot_type[0] == "Box":
        cont_x_plot_gen('box',0)
        
    if plot_type[1] == "Box":
        cont_x_plot_gen('box',1)
        
        
    if plot_type[0] == "Bar":
        cont_x_plot_gen('bar',0)
        
    if plot_type[1] == "Bar":
        cont_x_plot_gen('bar',1)
        

# ==========================Chart generation=================================

# ========================== Continuous X Chart Gen===========================

def cont_x_plot_gen(p_type,axis):
    

    global figure
    global ax
    global ax_1
    global nul_var_list
    global plot_color_list
    
    df = pcg.df
    df_sub = pcd.df_sub
    df_2 = pcg.df_2
    df_m = pcd.df_m
    
    actvie_data_name = pcd.actvie_data_name
    
    # -----------------------SET STRING LIST OF DATAFRAMES--------------------
    
    df_select_list = pcg.df_select_list
    
    # ----------------------SET OF DATAFRAMES TO PLOT FROM--------------------
    
    df_list = [df, df_sub, df_2, df_m]
    pcg.update_legend_labels()
    
    x_var = pcg.Var_Col_x.get()
    plot_m_size = [pcg.plot_marker_size.get(), pcg.plot_marker_size_1.get()]
    
    plot_symbol_list = [".","o","v","^","<",">","1","2","3","4","8","s","p","*",
                    "h","H","+","x","X","D","d"]
    
    nul_var_list = ["('Y Axis 1',)","('Y Axis 2',)","('Y Axis 3',)",
                "('Y Axis 4',)","('Y Axis 5',)","('Y Axis 6',)",
                "('Y Axis 7',)","('Y Axis 8',)","('Y Axis 9',)",
                "('Y Axis 10',)","('Y Axis 1',)","('Y Axis 2',)",
                "('Y Axis 3',)","('Y Axis 4',)","('Y Axis 5',)",
                "('Y Axis 6',)","('Y Axis 7',)","('Y Axis 8',)",
                "('Y Axis 9',)","('Y Axis 10',)"]

    plot_color_list = ['#b02c00','#c99504','#02c2bb','#48ff00','#237801','#e5ff00',
              '#034c99','#580399','#c204ac','#1942bf','#098a00','#c99504',
              '#02c2bb','#cc0000','#237801','#e5ff00','#034c99','#580399',
              '#c204ac','#c204ac']
    
    axis_df_list = [pcg.axis_1_dataframe.get(), pcg.axis_2_dataframe.get()]

    
    legen_list = [pcg.legend_label_1, pcg.legend_label_2, pcg.legend_label_3,
                  pcg.legend_label_4, pcg.legend_label_5, pcg.legend_label_6,
                  pcg.legend_label_7, pcg.legend_label_8, pcg.legend_label_9,
                  pcg.legend_label_10, pcg.legend_label_1_1, pcg.legend_label_2_1,
                  pcg.legend_label_3_1, pcg.legend_label_4_1, pcg.legend_label_5_1,
                  pcg.legend_label_6_1, pcg.legend_label_7_1, pcg.legend_label_8_1,
                  pcg.legend_label_9_1, pcg.legend_label_10_1]

    var_val_list = [pcg.Var_Col_1.get(), pcg.Var_Col_2.get(), pcg.Var_Col_3.get(),
                    pcg.Var_Col_4.get(), pcg.Var_Col_5.get(), pcg.Var_Col_6.get(),
                    pcg.Var_Col_7.get(), pcg.Var_Col_8.get(), pcg.Var_Col_9.get(),
                    pcg.Var_Col_10.get(), pcg.Var_Col_1_1.get(), pcg.Var_Col_2_1.get(),
                    pcg.Var_Col_3_1.get(), pcg.Var_Col_4_1.get(), pcg.Var_Col_5_1.get(),
                    pcg.Var_Col_6_1.get(), pcg.Var_Col_7_1.get(), pcg.Var_Col_8_1.get(),
                    pcg.Var_Col_9_1.get(), pcg.Var_Col_10_1.get()]
    
    mark_sty = [pcg.plot_symbol_1.get(), pcg.plot_symbol_2.get(), pcg.plot_symbol_3.get(),
                    pcg.plot_symbol_4.get(), pcg.plot_symbol_5.get(), pcg.plot_symbol_6.get(),
                    pcg.plot_symbol_7.get(), pcg.plot_symbol_8.get(), pcg.plot_symbol_9.get(),
                    pcg.plot_symbol_10.get(),pcg.plot_symbol_1_1.get(), pcg.plot_symbol_2_1.get(), 
                    pcg.plot_symbol_3_1.get(), pcg.plot_symbol_4_1.get(), pcg.plot_symbol_5_1.get(),
                    pcg.plot_symbol_6_1.get(), pcg.plot_symbol_7_1.get(), pcg.plot_symbol_8_1.get(), 
                    pcg.plot_symbol_9_1.get(), pcg.plot_symbol_10_1.get()]

    for x in range(0, 9):

        if axis == 1:
            x = x + 10
            axis_var_list = [ax, ax_1]
        else:
            axis_var_list = [ax]
            
        if var_val_list[x] != nul_var_list[x]:

            # ===============Select Dataframe and Chunking====================
            
            for z in range(0, 3):
                if axis_df_list[axis] == df_select_list[z]:
                    df_a = df_list[z]

                        

            if p_type == "scatter":
                if pcg.plot_chunk_name.get() != "Chunk by Column":
                    
                    uniqueValues = pd.unique(df_a[pcg.plot_chunk_name.get()].tolist())
                    uniqueValues = list(uniqueValues)

                    for un in range(0,len(uniqueValues)):  

                        df_chunk = df_a[df_a[pcg.plot_chunk_name.get()]==uniqueValues[un]] 
                        df_chunk.plot(kind=p_type,
                            x=x_var,
                            y=var_val_list[x],
                            ax=axis_var_list[axis],
                            c=plot_color_list[un],
                            label=uniqueValues[un],
                            s=plot_m_size[axis],
                            marker=mark_sty[x])
                else:
                
                    df_a.plot(kind=p_type,
                            x=x_var,
                            y=var_val_list[x],
                            ax=axis_var_list[axis],
                            c=plot_color_list[x],
                            label=legen_list[x],
                            s=plot_m_size[axis],
                            marker=mark_sty[x])
       

                


            elif p_type == "plot":

                df_a.plot(x=x_var,
                          y=var_val_list[x],
                          ax=axis_var_list[axis],
                          color=plot_color_list[x],
                          label=legen_list[x])

            elif p_type == "line":

                df_a.plot(kind=p_type,
                          x=x_var,
                          y=var_val_list[x],
                          ax=axis_var_list[axis],
                          color=plot_color_list[x],
                          label=legen_list[x])

            elif p_type == "area":

                df_a.plot(kind=p_type,
                          x=x_var,
                          y=var_val_list[x],
                          ax=axis_var_list[axis],
                          label=legen_list[x],
                          stacked=True)

            elif p_type == "hexbin":

                df_a.plot(kind=p_type,
                          x=x_var,
                          y=var_val_list[x],
                          ax=axis_var_list[axis],
                          label=legen_list[x],
                          gridsize=plot_m_size[axis])

            elif p_type == "density":

                df_a.plot(kind=p_type,
                          y=var_val_list[x],
                          ax=axis_var_list[axis],
                          label=legen_list[x],
                          alpha=0.5)

            elif p_type == "hist":

                df_a.plot(kind=p_type,
                          y=var_val_list[x],
                          ax=axis_var_list[axis],
                          label=legen_list[x],
                          bins=plot_m_size[axis],
                          alpha=0.5)

            elif p_type == "bar":

                df_a[var_val_list[x]].value_counts().plot(kind=p_type,
                                                          y=var_val_list[x],
                                                          ax=axis_var_list[axis],
                                                          color=plot_color_list[x],
                                                          label=legen_list[x])

                print(np.sum(df[var_val_list[x]].value_counts()))
            elif p_type == "pie":

                df_a[var_val_list[x]].value_counts().plot(kind=p_type,
                                                          ax=axis_var_list[axis],
                                                          label=legen_list[x])

            elif p_type == "box":
                                  
                df_a.plot(kind=p_type,
                          column=var_val_list[x],
                          ax=axis_var_list[axis],
                          label=legen_list[x])


    # =====================FORMAT AXES==========================================================

    if pcg.y_title_1.get() != "('Y Axis 1',)" and pcg.y_title_1_1.get() == "('Y Axis 1',)":    

        ax.legend(bbox_to_anchor=(0.50, -0.15), loc=9, borderaxespad=0.,fancybox=True, shadow=True, ncol=5, fontsize=8)
        ax.set_xlabel(pcg.x_axis_title.get(), size=12)
        ax.set_ylabel(pcg.y_axis_title.get(), size=12)
  
    elif pcg.y_title_1.get() != "('Y Axis 1',)" and pcg.y_title_1_1.get() != "('Y Axis 1',)":
        ax.legend(bbox_to_anchor=(0.25, -0.15), loc=9, borderaxespad=0.,fancybox=True, shadow=True, ncol=5, fontsize=6)
        ax.set_xlabel(pcg.x_axis_title.get(), size=12)
        ax.set_ylabel(pcg.y_axis_title.get(), size=12)
        
        ax_1.legend(bbox_to_anchor=(0.75, -0.15), loc=9, borderaxespad=0.,fancybox=True, shadow=True, ncol=5, fontsize=6)
        ax_1.set_ylabel(pcg.y_axis_title_1.get(), size=12)
        
    
    if p_type == "scatter" or p_type == 'line' or p_type == 'plot' or p_type == 'hexbin' or p_type == 'area':
        
        if pcg.y_title_1.get() != "('Y Axis 1',)":
            
            ax.set_xlim([float(pcg.plot_x_axis_min.get()),float(pcg.plot_x_axis_max.get())])
            ax.set_ylim([float(pcg.plot_y_axis_min.get()),float(pcg.plot_y_axis_max.get())])
        
        if pcg.y_title_1.get() != "('Y Axis 1',)" and pcg.y_title_1_1.get() != "('Y Axis 1',)":
            
            #ax.set_xlim([float(pcg.plot_x_axis_min.get()),float(pcg.plot_x_axis_max.get())])
            #ax.set_ylim([float(pcg.plot_y_axis_min.get()),float(pcg.plot_y_axis_max.get())])
            ax_1.set_ylim([float(pcg.plot_y_axis_min_1.get()),float(pcg.plot_y_axis_max_1.get())])
        
    elif p_type =="bar":
        
        if pcg.y_title_1.get() != "('Y Axis 1',)":
            ax.set_ylim([float(pcg.plot_y_axis_min.get()),float(pcg.plot_y_axis_max.get())])
            
        if pcg.y_title_1.get() != "('Y Axis 1',)" and pcg.y_title_1_1.get() != "('Y Axis 1',)":
            ax_1.set_ylim([float(pcg.plot_y_axis_min_1.get()),float(pcg.plot_y_axis_max_1.get())])
        
        print("None Cont")
    
    # ======================ADD ANNOTATIONS===================================
    
    annot_text_v = [pcg.annot_1.get(), pcg.annot_2.get(), pcg.annot_3.get(), pcg.annot_4.get(), pcg.annot_5.get()]
    annot_text_t = ["Annotation (1)", "Annotation (2)", "Annotation (3)", "Annotation (4)", "Annotation (5)"]
    annot_x_coord_v = [pcg.annot_x_1.get(), pcg.annot_x_2.get(), pcg.annot_x_3.get(), pcg.annot_x_4.get(), pcg.annot_x_5.get()]
    annot_y_coord_v = [pcg.annot_y_1.get(), pcg.annot_y_2.get(), pcg.annot_y_3.get(), pcg.annot_y_4.get(), pcg.annot_y_5.get()]

    annot_x_coord_t = [pcg.annot_x_t_1.get(), pcg.annot_x_t_2.get(), pcg.annot_x_t_3.get(), pcg.annot_x_t_4.get(), pcg.annot_x_t_5.get()]
    annot_y_coord_t = [pcg.annot_y_t_1.get(), pcg.annot_y_t_2.get(), pcg.annot_y_t_3.get(), pcg.annot_y_t_4.get(), pcg.annot_y_t_5.get()]
    annot_arrow_t = [pcg.annot_arrow_1.get(), pcg.annot_arrow_2.get(), pcg.annot_arrow_3.get(), pcg.annot_arrow_4.get(), pcg.annot_arrow_5.get()]
    
    for w in range(0,4):
        if annot_text_t[w] != annot_text_v[w]:
            ax.annotate(annot_text_v[w], xy= (float(annot_x_coord_v[w]),float(annot_y_coord_v[w])), 
                          textcoords = "data", 
                          xytext=(float(annot_x_coord_t[w]),float(annot_y_coord_t[w])), 
                          arrowprops=dict(arrowstyle=annot_arrow_t[w], facecolor='black'),
                          xycoords='data')

def add_regression(x_axis,x_min,x_max,y_axis,r_s_axis,reg_t):

    global ax
    global ax_1
    global figure
    global df_reg_list
    global df_reg_a
    global df_reg_type
    global df_reg_x
    global df_reg_y

    
    df = pcg.df
    df_sub = pcd.df_sub
    actvie_data_name = pcd.actvie_data_name
    global count
    #Set Min and Max Values
    
    # ===================AXIS SELECTION=======================================
    
    if r_s_axis == 0:
        df_reg_a.append(0)

        
    elif r_s_axis == 1:
        df_reg_a.append(1)
 
        
    df_reg_x.append(x_axis)
    df_reg_y.append(y_axis)
    df_reg_type.append(reg_t)    
    
    
    
    # =======================Label Names======================================
    update_plot_size()
    pcg.update_legend_labels()
       
    
    if pcd.actvie_data_name == "dataframe":
    
        if x_min != "Min" and x_max == "Max":
            df_reg_list.append(df[df[x_axis] > float(x_min)])
        
        elif x_min == "Min" and x_max != "Max":
            df_reg_list.append(df[df[x_axis] < float(x_max)])
        
        elif x_min != "Min" and x_max != "Max":
        
            holder = df[float(x_min) < df[x_axis]]
            holder1 = holder[float(x_max) > holder[x_axis]]
        
            df_reg_list.append(holder1)
        
        else:
            
            df_reg_list.append(df.iloc[:,:])
    
    else:
        
        if x_min != "Min" and x_max == "Max":
            df_reg_list.append(df_sub[df_sub[x_axis] > float(x_min)])
        
        elif x_min == "Min" and x_max != "Max":
            df_reg_list.append(df_sub[df_sub[x_axis] < float(x_max)])
        
        elif x_min != "Min" and x_max != "Max":
        
            holder = df_sub[float(x_min) < df_sub[x_axis]]
            holder1 = holder[float(x_max) > holder[x_axis]]
        
            df_reg_list.append(holder1)
        
        else:
            
            df_reg_list.append(df.iloc[:,:])

    # ========================CREATE REGRESSION LINE==========================

    count+=1 
    
    #c=count
    for c in range(count):

        x = df_reg_list[c][df_reg_x[c]]
        y = df_reg_list[c][df_reg_y[c]]
        
        z = np.polyfit(x, y, int(df_reg_type[c]))
        y_hat = np.poly1d(z)(x)
    
        df_reg_list[c]['y_hat_'+str(c+1)] = y_hat
        
        y_hat_t = df_reg_list[c]['y_hat_'+str(c+1)]
        
        if df_reg_a[c] == 0:
        
            #df_reg_list[c].plot(kind='line',x=x_axis, y="y_hat_"+str(int(c)+1), ax=ax, c='black', label="Trend "+str(c+1))
            df_reg_list[c].plot(kind='line',x=x_axis, y="y_hat_"+str(int(c)+1), ax=ax, c='black', label="_Hidden")
            
            #ax.legend(bbox_to_anchor=(0.5, -0.15), loc=9, borderaxespad=0.,fancybox=True, shadow=True, ncol=5)
            text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat_t):0.3f}$"
            ax.text(0.05+(c*0.2), -0.25, text,transform=ax.transAxes,fontsize=6, verticalalignment='top')
        
        elif df_reg_a[c] == 1:
        #if Var_Col_1_1.get() != "('Y Axis 1',)":
    
            df_reg_list[c].plot(kind='line',x=x_axis, y="y_hat_"+str(int(c)+1), ax=ax_1, c='blue', label="_Hidden")
        
            #ax.legend(bbox_to_anchor=(0.5, -0.15), loc=9, borderaxespad=0.,fancybox=True, shadow=True, ncol=5)
            text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat_t):0.3f}$"
            ax.text(0.05+(c*0.2), -0.25, text,transform=ax_1.transAxes,fontsize=6, verticalalignment='top', c='blue')
                
                
    # ============================UPDATE LEGEND ==============================
    if pcg.plot_chunk_name == "Chunk by Column":
        if pcg.y_title_1.get() != "('Y Axis 1',)" and pcg.y_title_1_1.get() == "('Y Axis 1',)":    
                
            ax.legend(bbox_to_anchor=(0.50, -0.15), loc=9, borderaxespad=0.,fancybox=True, shadow=True, ncol=5, fontsize=8)
            ax.set_xlabel(pcg.x_axis_title.get(), size=12)
            ax.set_ylabel(pcg.y_axis_title.get(), size=12)
        #else:    
        elif pcg.y_title_1.get() != "('Y Axis 1',)" and pcg.y_title_1_1.get() != "('Y Axis 1',)":
            ax.legend(bbox_to_anchor=(0.25, -0.15), loc=9, borderaxespad=0.,fancybox=True, shadow=True, ncol=5, fontsize=6)
            ax.set_xlabel(pcg.x_axis_title.get(), size=12)
            ax.set_ylabel(pcg.y_axis_title.get(), size=12)
            
            ax_1.legend(bbox_to_anchor=(0.75, -0.15), loc=9, borderaxespad=0.,fancybox=True, shadow=True, ncol=5, fontsize=6)
            ax_1.set_ylabel(pcg.y_axis_title_1.get(), size=12)
            ax_1.set_ylim([float(pcg.plot_y_axis_min_1.get()),float(pcg.plot_y_axis_max_1.get())])
        
# ===========================================================================


# =================================END========================================        
