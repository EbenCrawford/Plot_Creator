# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:58:08 2020

@author: ebenc
"""


# =========================IMPORT SECTION====================================
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
import csv

import Plot_C_dataframe_v01 as pcd
import Plot_C_plot_v01 as pcp
import Plot_C_M_v01 as pcm
import Plot_C_Keras_v01 as pck

global root
root = Tk()
root.title("Plot Creator")
root.state('zoomed')
root.geometry("1500x800")
root.grid()
    
csv.field_size_limit(15000000)
count = 0

# ===============CREATE ROOT==================================================


# -------------Formatting ----------------------------------------------------
# 'Blue -'#5ae3f2' 
# ---------------Colors-----------------------------------

purple_opt = '#bf87ff'
blue_opt = '#5eefff'
orange_opt = "#ffc342"
red_opt = '#ff8066'
green_opt = '#aeff78'
gamboge_opt = '#e49b0f'
gray_1_opt = '#27313d'
gray_2_opt = '#3d3f54'


back_color = gray_1_opt
text_back_color = gray_2_opt
forg_color = gamboge_opt


root.configure(background=back_color)


# ==========Tabs =============================================================
# ----------ttk Style Setting-------------------------------------------------

tabControl = ttk.Notebook(root)  

ttk_sty = ttk.Style()
ttk_sty.configure('TNotebook', background= back_color)
ttk_sty.configure('TFrame', background= back_color)

# -------------CREATE TABS----------------------------------------------------

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6 = ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Data')
tabControl.add(tab2, text='Plot')
tabControl.add(tab3, text='Multi Plot')
tabControl.add(tab4, text='Map Plot')
tabControl.add(tab5, text='PyTorch')
tabControl.add(tab6, text='TensorFlow')
tabControl.add(tab7, text='Relief Regression')
tabControl.grid(row=0, column=0, sticky='nw')




# ==========Start Label Frames================================================


start_lf = LabelFrame(tab1, text="Data Options", padx=1, pady=1, bg=back_color, fg=forg_color, width=130)
start_lf.grid(row=0, column=0, padx=15, pady=5, columnspan=2, sticky='nw')


#=============Tables==========================================================

graph_options = ["Plot", "Line", "Scatter", "Density", "Area", 
                 "Histogram", "Pie", "Bar", "Hex", 'Box']
meta_data_operators = ["-", "+", "*", "/", "**", "sqrt()"]
values=sub_set_operators = ['>','<','==','!=','<=','>=']
plot_symbol_list = [".","o","v","^","<",">","1","2","3","4","8","s","p","*",
                    "h","H","+","x","X","D","d"]
nul_var_list = ["('Y Axis 1',)","('Y Axis 2',)","('Y Axis 3',)",
                "('Y Axis 4',)","('Y Axis 5',)","('Y Axis 6',)",
                "('Y Axis 7',)","('Y Axis 8',)","('Y Axis 9',)",
                "('Y Axis 10',)"]
                
nul_var_list_1 = ["('Y Axis 1',)","('Y Axis 2',)",
                "('Y Axis 3',)","('Y Axis 4',)","('Y Axis 5',)",
                "('Y Axis 6',)","('Y Axis 7',)","('Y Axis 8',)",
                "('Y Axis 9',)","('Y Axis 10',)"]

plot_color_list = ['#b02c00','#c99504','#02c2bb','#48ff00','#237801','#e5ff00',
              '#034c99','#580399','#c204ac','#c204ac','#c204ac','#c99504',
              '#02c2bb','#48ff00','#237801','#e5ff00','#034c99','#580399',
              '#c204ac','#c204ac']

df_select_list = ['Dataframe (1)','Dataframe (1) Subset','Dataframe (2)', 'Merged Dataframe']

dtype_list = ["Date","int64","float64","object"]

annot_arrow_table = ["-","->","-[","<-","fancy","simple","wedge"]

# =========Variables==========================================================

# --------------Dataframe Variables-------------------------------------------

cur_folder_name = StringVar()
dataframe_col_sel = StringVar()

sub_dir_dim = StringVar()
df_dir_dim = StringVar()
sec_dir_dim = StringVar()
m_dir_dim = StringVar()

h1_v = StringVar()
h2_v = StringVar()
h3_v = StringVar()
h4_v = StringVar()
h5_v = StringVar()
h6_v = StringVar()
h7_v = StringVar()
h8_v = StringVar()
h9_v = StringVar()
h10_v = StringVar()

ct1_v = StringVar()
ct2_v = StringVar()
ct3_v = StringVar()
ct4_v = StringVar()
ct5_v = StringVar()
ct6_v = StringVar()
ct7_v = StringVar()
ct8_v = StringVar()
ct9_v = StringVar()
ct10_v = StringVar()

# ------------Annotations-----------------------------------------------------

annot_1 = StringVar()
annot_2 = StringVar()
annot_3 = StringVar()
annot_4 = StringVar()
annot_5 = StringVar()

annot_arrow_1 = StringVar()
annot_arrow_2 = StringVar()
annot_arrow_3 = StringVar()
annot_arrow_4 = StringVar()
annot_arrow_5 = StringVar()

annot_x_1 = StringVar()
annot_x_2 = StringVar()
annot_x_3 = StringVar()
annot_x_4 = StringVar()
annot_x_5 = StringVar()

annot_y_1 = StringVar()
annot_y_2 = StringVar()
annot_y_3 = StringVar()
annot_y_4 = StringVar()
annot_y_5 = StringVar()

annot_x_t_1 = StringVar()
annot_x_t_2 = StringVar()
annot_x_t_3 = StringVar()
annot_x_t_4 = StringVar()
annot_x_t_5 = StringVar()

annot_y_t_1 = StringVar()
annot_y_t_2 = StringVar()
annot_y_t_3 = StringVar()
annot_y_t_4 = StringVar()
annot_y_t_5 = StringVar()

# ------------First Axis------------------------------------------------------

graph_type = StringVar()
axis_1_dataframe = StringVar()
plot_marker_size = IntVar()

Var_Col_1 = StringVar()
Var_Col_2 = StringVar()
Var_Col_3 = StringVar()
Var_Col_4 = StringVar()
Var_Col_5 = StringVar()
Var_Col_6 = StringVar()
Var_Col_7 = StringVar()
Var_Col_8 = StringVar()
Var_Col_9 = StringVar()
Var_Col_10 = StringVar()

y_title_1 = StringVar()
y_title_2 = StringVar()
y_title_3 = StringVar()
y_title_4 = StringVar()
y_title_5 = StringVar()
y_title_6 = StringVar()
y_title_7 = StringVar()
y_title_8 = StringVar()
y_title_9 = StringVar()
y_title_10 = StringVar()

plot_symbol_1 = StringVar()
plot_symbol_2 = StringVar()
plot_symbol_3 = StringVar()
plot_symbol_4 = StringVar()
plot_symbol_5 = StringVar()
plot_symbol_6 = StringVar()
plot_symbol_7 = StringVar()
plot_symbol_8 = StringVar()
plot_symbol_9 = StringVar()
plot_symbol_10 = StringVar()

plot_color_1 = StringVar()
plot_color_2 = StringVar()
plot_color_3 = StringVar()
plot_color_4 = StringVar()
plot_color_5 = StringVar()
plot_color_6 = StringVar()
plot_color_7 = StringVar()
plot_color_8 = StringVar()
plot_color_9 = StringVar()
plot_color_10 = StringVar()

# ------------Second Axis Variables-------------------------------------------

graph_type_1 = StringVar()
axis_2_dataframe = StringVar()
plot_marker_size_1 = IntVar()

Var_Col_1_1 = StringVar()
Var_Col_2_1 = StringVar()
Var_Col_3_1 = StringVar()
Var_Col_4_1 = StringVar()
Var_Col_5_1 = StringVar()
Var_Col_6_1 = StringVar()
Var_Col_7_1 = StringVar()
Var_Col_8_1 = StringVar()
Var_Col_9_1 = StringVar()
Var_Col_10_1 = StringVar()

y_title_1_1 = StringVar()
y_title_2_1 = StringVar()
y_title_3_1 = StringVar()
y_title_4_1 = StringVar()
y_title_5_1 = StringVar()
y_title_6_1 = StringVar()
y_title_7_1 = StringVar()
y_title_8_1 = StringVar()
y_title_9_1 = StringVar()
y_title_10_1 = StringVar()

plot_symbol_1_1 = StringVar()
plot_symbol_2_1 = StringVar()
plot_symbol_3_1 = StringVar()
plot_symbol_4_1 = StringVar()
plot_symbol_5_1 = StringVar()
plot_symbol_6_1 = StringVar()
plot_symbol_7_1 = StringVar()
plot_symbol_8_1 = StringVar()
plot_symbol_9_1 = StringVar()
plot_symbol_10_1 = StringVar()

plot_color_1_1 = StringVar()
plot_color_2_1 = StringVar()
plot_color_3_1 = StringVar()
plot_color_4_1 = StringVar()
plot_color_5_1 = StringVar()
plot_color_6_1 = StringVar()
plot_color_7_1 = StringVar()
plot_color_8_1 = StringVar()
plot_color_9_1 = StringVar()
plot_color_10_1 = StringVar()

# ------------X Axis Variables-----------------------------------------------

Var_Col_x = StringVar()

# ------------Plot Variables--------------------------------------------------

Plot_Name = StringVar()
Save_Name = StringVar()

x_axis_title = StringVar()
y_axis_title = StringVar()
y_axis_title_1 = StringVar()

plot_x_axis_min = StringVar()
plot_x_axis_max = StringVar()

plot_y_axis_min = StringVar()
plot_y_axis_max = StringVar()

plot_y_axis_min_1 = StringVar()
plot_y_axis_max_1 = StringVar()

# -----------Save Variables---------------------------------------------------

save_plot = StringVar()
save_name_csv = StringVar()
save_subset_csv = StringVar()

# ----------Metadata Variables------------------------------------------------

new_col_name = StringVar()
col_value_1 = StringVar()
col_value_2 = StringVar()
col_operator = StringVar()




active_data_select = StringVar(value="off")

MessageBox = ctypes.windll.user32.MessageBoxW
"""
global actvie_data_name
actvie_data_name = "dataframe"
"""
# -------------Merge Dataframes-----------------------------------------------

right_dataframe = StringVar()
left_dataframe = StringVar()
merge_position = StringVar()
data_int_method = StringVar()


# -------------Sub Set Data Variables-----------------------------------------

sub_set_name = StringVar()
sub_set_value_1 = StringVar()
sub_set_value_2 = StringVar()
sub_set_value_3 = StringVar()
sub_set_value_4 = StringVar()
sub_set_value_5 = StringVar()
sub_set_value_6 = StringVar()
sub_set_value_7 = StringVar()
sub_set_value_8 = StringVar()
sub_set_value_9 = StringVar()

sub_set_operator_1 = StringVar()
sub_set_operator_2 = StringVar()
sub_set_operator_3 = StringVar()
sub_set_operator_4 = StringVar()
sub_set_operator_5 = StringVar()
sub_set_operator_6 = StringVar()

# ------------Regression Variables--------------------------------------------

reg_x_axis = StringVar()
reg_x_min = StringVar()
reg_x_max = StringVar()
reg_y_axis = StringVar()
reg_type = StringVar()

reg_x_axis_1 = StringVar()
reg_x_min_1 = StringVar()
reg_x_max_1 = StringVar()
reg_y_axis_1 = StringVar()
reg_type_1 = StringVar()

# ------------Map Plot Variables----------------------------------------------

map_ax_on = IntVar()
map_plot_var = StringVar()
v_max = StringVar()
v_min = StringVar()
map_color = StringVar()
shape_merge = StringVar()
csv_merge = StringVar()

# ============================================================================
# ==========================DATA MANAGMENT====================================
# ============================================================================

#-------------Load Data------------------------------------------------------

def open_file(df_num):
    
    global root
    root.state('zoomed')
    root.geometry(str(root.winfo_width())+ "x" + str(root.winfo_width()))
    global df
    global df_2

    #----------Create dataframe manager---------------------------------------

    rows_to_skip = "How many rows of the dataframe should \n be skipped after the header?"
    header_row = "Which row is the header located?"

    open_dataframe_window(header_row, rows_to_skip, df_num)

# ------------Open dataframe Window-------------------------------------------

def open_dataframe_window(text1, text2, df_num):

    global top
    global text_var_1_f
    global text_var_2_f
    global dataframe_col_sel

    top = Toplevel()
    top.configure(bg=back_color)
    top.title("Filter Dataframe")

    text_var_1_f = IntVar()
    text_var_1_f.set(1)
    text_var_2_f = IntVar()
    text_var_2_f.set(0)
    
    dataframe_col_sel.set("All Headers")
     

    label_1_text = text1
    label_2_text = text2
    
    # --------------SELECT TOTAL NUMBER OF ROWS ------------------------------
    
    
    # ---------------CREATE HEADER LOGIC SELECTION----------------------------
    
    col_log_list = ["All Headers","Subset Headers"]
    
    col_upload_dd = OptionMenu(top, dataframe_col_sel,*col_log_list)
    col_upload_dd.config(bg = back_color, fg = forg_color, borderwidth=0, 
                         highlightcolor= text_back_color, 
                         activebackground= back_color, 
                         activeforeground= forg_color)
    
    col_upload_dd.grid(row=1, column=0,padx=10, pady=20, columnspan=2)
    
    # --------------SELECT HEADER ROW AND SKIP OTHER ROWS AFTER HEADER--------

    x = list(np.arange(0,30,1))

    top_1_label = Label(top, text=label_1_text,bg = back_color, fg = forg_color).grid(row=2, column=0,padx=10, pady=5, columnspan=2)

    top_1_dd = OptionMenu(top, text_var_1_f,*x)
    top_1_dd.config(bg = back_color, fg = forg_color, borderwidth=0, highlightcolor= text_back_color, activebackground=back_color, activeforeground=forg_color)
    top_1_dd.grid(row=3, column=0,padx=10, pady=5, columnspan=2)

    top_2_label = Label(top, text=label_2_text, bg = back_color, fg = forg_color).grid(row=4, column=0,padx=10, pady=5, columnspan=2)

    top_2_dd = OptionMenu(top, text_var_2_f, *x)
    top_2_dd.config(bg = back_color, fg = forg_color, borderwidth=0, highlightcolor= text_back_color, activebackground=back_color, activeforeground=forg_color)
    top_2_dd.grid(row=5, column=0, padx=10, pady=5, columnspan=2)
  
    
    ok_top_btn = Button(top, text='Select File', command=lambda: open_dataframe(df_num), width = 10, bg = back_color, fg = forg_color).grid(row=6, column=0,padx=10, pady=5)
    exit_top_btn = Button(top, text="Cancel", command=top.destroy, width=10, bg = back_color, fg = forg_color, bd=4).grid(row=6, column=1,padx=10, pady=5)

# -----Open Dataframe from CSV-------------------------------------------------


def open_dataframe(df_num):

    global df
    global df_2
    global filename
    global top
    df_2 = []

    
    filename = filedialog.askopenfilename(initialdir="C:/", title="Select a File", filetypes=(("CSV files", "*.csv"),("DAT files", "*.dat")))
    
    if df_num==0:
            
        if dataframe_col_sel.get() == "All Headers":
            
            try:
                df = pd.read_csv (filename,header=text_var_1_f.get()-1, engine='c')
                df = pd.read_csv (filename,skiprows=text_var_1_f.get() + text_var_2_f.get(),names = list(df), engine='c')
            except:
                df = pd.read_csv (filename,header=text_var_1_f.get()-1, engine='python')
                df = pd.read_csv (filename,skiprows=text_var_1_f.get() + text_var_2_f.get(),names = list(df), engine='python')
            
            top.destroy()
            create_gui()
            
        else:
            
            df_header = pd.read_csv (filename,nrows=1)
            top.destroy()
            select_header_window(df_header,df_num)
    
    else:
        
        if dataframe_col_sel.get() == "All Headers":
            try:
                
                df_2 = pd.read_csv (filename,header=text_var_1_f.get()-1, engine='c')
                df_2 = pd.read_csv (filename,skiprows=text_var_1_f.get() + text_var_2_f.get(),names = list(df_2), engine='c')
            except:
                df_2 = pd.read_csv (filename,header=text_var_1_f.get()-1, engine='python')
                df_2 = pd.read_csv (filename,skiprows=text_var_1_f.get() + text_var_2_f.get(),names = list(df_2), engine='python')
            top.destroy()
            pcd.upload_2nd_dataframe_view()
            
        else:
            
            df_header = pd.read_csv (filename,nrows=1)
            top.destroy()
            select_header_window(df_header,df_num)
        

# ------------Open Save dataframe CSV Window--------------------------------------------

def select_header_window(header_list,df_num):
    
    global df
    global filename 
    global header_var
    global col_dtype_var
    
    top = Toplevel()
    top.configure(bg=back_color)
    top.title("Column Selection")
    
    col_sel_label = Label(top, text="Select Column Headers to Import", 
                          bg = back_color, 
                          fg = forg_color).grid(row=0, 
                                                column=0,
                                                padx=10, 
                                                pady=5, 
                                                columnspan=2)

    
    header_dd = ["h1",'h2','h3','h4','h5','h6','h7','h8','h9','h10']
    header_var = [h1_v, h2_v, h3_v, h4_v, h5_v, h6_v, h7_v, h8_v, h9_v, h10_v]
    
    col_dtype_dd = ["ct1","ct2","ct3","ct4","ct5","ct6","ct7","ct8","ct9","ct10"]
    col_dtype_var = [ct1_v, ct2_v, ct3_v, ct4_v, ct5_v, ct6_v, ct7_v, ct8_v, ct9_v, ct10_v]
    
    for x in range(0,9):
        
        header_dd[x]= ttk.Combobox(top, textvariable=header_var[x], values=list(header_list), width=30)
        header_dd[x].grid(row=x+1, column=0,padx=15, pady=10, sticky='e', columnspan=1)
        header_dd[x].delete(0, END)
        header_dd[x].insert(0, "Column (" + str(x) +")")
        
        col_dtype_dd[x]= ttk.Combobox(top, textvariable=col_dtype_var[x], values=dtype_list, width=15)
        col_dtype_dd[x].grid(row=x+1, column=1,padx=15, pady=10, sticky='e', columnspan=1)
        col_dtype_dd[x].delete(0, END)
        col_dtype_dd[x].insert(0, "Data Type (" + str(x) +")")
        
        
    ok_top_btn = Button(top, text='Create df', command=lambda:open_subset_dataframe(df_num), width = 10, bg = back_color, fg = forg_color).grid(row=12, column=0,padx=10, pady=5)
    exit_top_btn = Button(top, text="Cancel", command=top.destroy, width=10, bg = back_color, fg = forg_color, bd=4).grid(row=12, column=1,padx=10, pady=5)  
    
def open_subset_dataframe(df_num):
    
    global filename
    global header_var
    global col_dtype_var
    global df
    global df_2
    global top
    global dtype_list
    
    if df_num == 0:
        
        if col_dtype_var[0].get()== "Data Type (" + str(0) +")":
            df = pd.read_csv (filename, usecols = [header_var[0].get()], engine='c', quoting=csv.QUOTE_NONE, error_bad_lines=False, skip_blank_lines=False)
        elif col_dtype_var[0].get()== "Date":
            df = pd.read_csv (filename, usecols = [header_var[0].get()], parse_dates=True, engine='c', quoting=csv.QUOTE_NONE, error_bad_lines=False, skip_blank_lines=False)
        else:
            df = pd.read_csv (filename, usecols = [header_var[0].get()], dtype=col_dtype_var[0].get(), engine='c', quoting=csv.QUOTE_NONE, error_bad_lines=False, skip_blank_lines=False)

        for  x in range(1,9):
            
            if header_var[x].get() != "Column (" + str(x) +")":
                
                if col_dtype_var[x].get()== "Data Type (" + str(x) +")":
                    df_col = pd.read_csv (filename, usecols = [header_var[x].get()], engine='c', quoting=csv.QUOTE_NONE, error_bad_lines=False, skip_blank_lines=False)
                elif col_dtype_var[x].get()== "Date":
                    df_col = pd.read_csv (filename, usecols = [header_var[x].get()], parse_dates=True, engine='c', quoting=csv.QUOTE_NONE, error_bad_lines=False, skip_blank_lines=False)
                else:
                    df_col = pd.read_csv (filename, usecols = [header_var[x].get()], dtype=col_dtype_var[x].get(), engine='c', quoting=csv.QUOTE_NONE, error_bad_lines=False, skip_blank_lines=False)
    
    
                df = df.join(df_col)
        top.destroy()
        create_gui() 
    else:
        
        if col_dtype_var[0].get()== "Data Type (" + str(0) +")":
            df_2 = pd.read_csv (filename, usecols = [header_var[0].get()], engine='c', quoting=csv.QUOTE_NONE, error_bad_lines=False, skip_blank_lines=False)
        elif col_dtype_var[0].get()== "Date":
            df_2 = pd.read_csv (filename, usecols = [header_var[0].get()], parse_dates=True, engine='c', quoting=csv.QUOTE_NONE, error_bad_lines=False, skip_blank_lines=False)
        else:
            df_2 = pd.read_csv (filename, usecols = [header_var[0].get()], dtype=col_dtype_var[0].get(), engine='c', quoting=csv.QUOTE_NONE, error_bad_lines=False, skip_blank_lines=False)

        for  x in range(1,9):
            
            if header_var[x].get() != "Column (" + str(x) +")":
                
                if col_dtype_var[x].get()== "Data Type (" + str(x) +")":
                    df_col = pd.read_csv (filename, usecols = [header_var[x].get()], engine='c', quoting=csv.QUOTE_NONE, error_bad_lines=False, skip_blank_lines=False)
                elif col_dtype_var[x].get()== "Date":
                    df_col = pd.read_csv (filename, usecols = [header_var[x].get()], parse_dates=True, engine='c', quoting=csv.QUOTE_NONE, error_bad_lines=False, skip_blank_lines=False)
                else:
                    df_col = pd.read_csv (filename, usecols = [header_var[x].get()], dtype=col_dtype_var[x].get(), engine='c', quoting=csv.QUOTE_NONE, error_bad_lines=False, skip_blank_lines=False)
    
                    
                df_2 = df_2.join(df_col)
        top.destroy()  
        pcd.upload_2nd_dataframe_view()
            
    

def create_folder_window():

    global top

    top = Toplevel()
    top.configure(bg='#27313d')
    top.title("Data Directory")

    save_folder_label = Label(top, text="Change active directory or create new directory", bg = back_color, fg = forg_color).grid(row=0, column=0,padx=10, pady=20, columnspan=2)
    save_folder_name_e = Entry(top,textvariable = cur_folder_name, width=50, bg = back_color, fg = forg_color)
    save_folder_name_e.grid(row=0, column=0, padx=10, pady=20, columnspan=2)
    save_folder_name_e.delete(0, END)
    save_folder_name_e.insert(0, Plot_Name.get())

    ok_save_btn = Button(top, text='Save', command=create_new_folder, width = 10, bg = back_color, fg = forg_color).grid(row=2, column=0,padx=10, pady=5)
    exit_btn = Button(top, text="Cancel", command=top.destroy, width=10, bg = back_color, fg = forg_color, bd=4).grid(row=2, column=1,padx=10, pady=5)


#-----------Create New Folder------------------------------------------------

def create_new_folder():
    
    #path=os.path.abspath(__file__)
    path=cur_folder_name.get()
    try:
        os.mkdir(path)
        top.destroy()
        os.chdir(cur_folder_name.get())
        MessageBox(None, "Success! ", cur_folder_name.get() + " has been created")
    except OSError:
        top.destroy()
        os.chdir(cur_folder_name.get())
        MessageBox(None, "Switched active directory to \n" + cur_folder_name.get())
        

# ------------Open Save Plot Window-------------------------------------------


def save_plot_window():

    global top

    top = Toplevel()
    top.configure(bg='#27313d')

    top.title("Name Plot")
    save_plot_label = Label(top, text="Name your plot", bg = back_color, fg = forg_color).grid(row=0, column=0,padx=10, pady=20, columnspan=2)
    save_plot_name_e = Entry(top,textvariable = save_plot, width=50, bg = back_color, fg = forg_color)
    save_plot_name_e.grid(row=0, column=0,padx=10, pady=20, columnspan=2)
    save_plot_name_e.delete(0, END)
    save_plot_name_e.insert(0, Plot_Name.get())

    ok_save_btn = Button(top, text='Save', command=save_plot_f, width = 10, bg = back_color, fg = forg_color).grid(row=2, column=0,padx=10, pady=5)
    exit_btn = Button(top, text="Cancel", command=top.destroy, width=10, bg = back_color, fg = forg_color,bd=4).grid(row=2, column=1,padx=10, pady=5)



def save_dataframe_csv_window():

    global top

    top = Toplevel()
    top.configure(bg='#27313d')
    top.title("Name File")

    save_label = Label(top, text="Save dataframe as...",bg = back_color, fg = forg_color).grid(row=0, column=0,padx=10, pady=20, columnspan=2)
    save_Name_e = Entry(top,textvariable = save_name_csv, width=50, bg = back_color, fg = forg_color)
    save_Name_e.grid(row=1, column=0,padx=10, pady=20, columnspan=2)
    save_Name_e.delete(0, END)
    save_Name_e.insert(0, Plot_Name.get())

    ok_save_btn = Button(top, text='Save', command=save_dataframe_csv, width = 10, bg = back_color, fg = forg_color).grid(row=2, column=0,padx=10, pady=5)
    exit_btn = Button(top, text="Cancel", command=top.destroy, width=10, bg = back_color, fg = forg_color, bd=4).grid(row=2, column=1,padx=10, pady=5)

# ------------Open Save subset CSV Window--------------------------------------------


def save_subset_csv_window():

    global top

    top = Toplevel()
    top.configure(bg='#27313d')
    top.title("Name File")

    save_label = Label(top, text="Save subset as...",bg = back_color, fg = forg_color).grid(row=0, column=0,padx=10, pady=20, columnspan=2)
    save_Name_e = Entry(top,textvariable = save_name_csv, width=50, bg = back_color, fg = forg_color)
    save_Name_e.grid(row=1, column=0,padx=10, pady=20, columnspan=2)
    save_Name_e.delete(0, END)
    save_Name_e.insert(0, Plot_Name.get())

    ok_save_btn = Button(top, text='Save', command=save_subset_csv, width = 10, bg = back_color, fg = forg_color).grid(row=2, column=0,padx=10, pady=5)
    exit_btn = Button(top, text="Cancel", command=top.destroy, width=10, bg = back_color, fg = forg_color).grid(row=2, column=1,padx=10, pady=5)

# ------------Save Plot-------------------------------------------------------


def save_plot_f():
    
    pcp.figure.savefig(save_plot.get() +'.png')
    top.destroy()
    MessageBox(None, "Save Complete! ", save_plot.get() + " has saved successfully")

# ------------Save dataframe CSV--------------------------------------------------------


def save_dataframe_csv():
    
    #figure.savefig(save_name_csv.get() + '.csv')
    df.to_csv(save_name_csv.get() + '.csv')
    top.destroy()
    MessageBox(None, "Save Complete! ", save_name_csv.get() + " has saved successfully")
    
    
# ------------Save subset CSV--------------------------------------------------------

def save_subset_csv():
    df_sub  = pcd.df_sub
    #figure.savefig(save_name_csv.get() + '.csv')
    df_sub.to_csv(save_name_csv.get() + '.csv')
    top.destroy()
    MessageBox(None, "Save Complete! ", save_name_csv.get() + " has saved successfully")

def exit_program():
    
    top = Toplevel()
    top.configure(bg='#27313d')
    top.title("Exit")

    exit_label = Label(top, text="Would you like to close Plot Creator?",bg = back_color, fg = forg_color).grid(row=0, column=0,padx=10, pady=20, columnspan=2)

    ok_exit_btn = Button(top, text='Ok', command=root.destroy, width = 10, bg = back_color, fg = forg_color).grid(row=2, column=0,padx=10, pady=5)
    cancel_btn = Button(top, text="Cancel", command=top.destroy, width=10, bg = back_color, fg = forg_color).grid(row=2, column=1,padx=10, pady=5)

# ============================================================================
# =========================END DATA MANAGMENT=================================
# ============================================================================


# =============Create GUI Function============================================

def create_gui():

    # -------------------Frames-----------------------------------------------
    
    global annot_tab
    global df_1_tab
    global df_s_tab
    global df_2_tab
    global df_m_tab
    
    
    
    # ====================LABEL FRAMES========================================
    
    # ------------------Set LabelFrame Width----------------------------------
    
    lf_width = int(root.winfo_width()/100)
    
   
    # ==============TAB 1 COLUMN 0============================================
    
    # --------------BOTTOM SPACER---------------------------------------------
    
    # ---------------ROW 1----------------------------------------------------
    
    # ------------------DATAFRAME NOTEBOOK------------------------------------    
    
    dataframe_nb = ttk.Notebook(tab1)
    
    df_1_tab = ttk.Frame(dataframe_nb)
    df_s_tab = ttk.Frame(dataframe_nb)
    df_2_tab = ttk.Frame(dataframe_nb)
    df_m_tab = ttk.Frame(dataframe_nb)
    
    dataframe_nb.add(df_1_tab, text='Dataframe (1)')
    dataframe_nb.add(df_s_tab, text='Dataframe Subset')
    dataframe_nb.add(df_2_tab, text='Dataframe (2)')
    dataframe_nb.add(df_m_tab, text='Dataframe Merged')
    
    dataframe_nb.grid(row=1, column=0, rowspan=7, columnspan=2, sticky='nw', padx=15, pady=5)
    
    # =======================DATAFRAME TABS===================================

    global file_table_lf

    file_table_lf = LabelFrame(df_1_tab, text="Loaded Dataframe", padx=2, pady=2, bg=back_color, fg=forg_color, width=lf_width)
    file_table_lf.grid(row=2, column=0, padx=15, pady=5, columnspan=3, sticky='nnw')
    
    global meta_data_view_lf
    
    meta_data_view_lf = LabelFrame(df_1_tab, text="Dataframe Subset", padx=2, pady=2, bg=back_color, fg=forg_color, width=lf_width)
    meta_data_view_lf.grid(row=3, column=0, padx=15, pady=5, columnspan=3,rowspan=1, sticky='nw')

    # -----------------ROW 7--------------------------------------------------    

    global data_functions_lf
    
    data_functions_lf = LabelFrame(tab1, text="Dataframe Functions", padx=2, pady=2, bg=back_color, fg=forg_color, width=lf_width)
    data_functions_lf.grid(row=8, column=0, padx=15, pady=5, columnspan=3,rowspan=1, sticky='nw')

    # -----------------ROW 8--------------------------------------------------
    
    global add_data_lf
    
    add_data_lf = LabelFrame(tab1, text="Add Meta Data", padx=2, pady=2, bg=back_color, fg=forg_color, width=lf_width)
    add_data_lf.grid(row=9, column=0, padx=15, pady=5, columnspan=2,rowspan=1, sticky='nnw')
    
    # -----------------ROW 9--------------------------------------------------
    
    global add_subset_lf

    add_subset_lf = LabelFrame(tab1, text="Subset Data", padx=2, pady=2, bg=back_color, fg=forg_color, width=lf_width)
    add_subset_lf.grid(row=10, column=0, padx=15, pady=5, columnspan=2,rowspan=1, sticky='nnw')
    
    # -----------------ROW 15--------------------------------------------------
    
    bottom_spacer_lf = LabelFrame(tab1, text="", padx=2, pady=2, bg=back_color, fg=forg_color)
    bottom_spacer_lf.grid(row=15, column=0, padx=15, pady=5, columnspan=6,rowspan=1, sticky='sw')

    s = ' '*int(np.round(root.winfo_width()/3))
    bottom_spacer = Label(bottom_spacer_lf, bg = back_color, fg = forg_color, text=s+" ")
    bottom_spacer.grid(row=0,column=0)
    
    
    # ==================TAB 1 COLUMN 1========================================
    
    # ------------------ROW 0-------------------------------------------------
    global file_name_lf
    file_name_lf = LabelFrame(tab1, text="Loaded File", padx=2, pady=2,bg=back_color, fg=forg_color, width=lf_width)
    file_name_lf.grid(row=0, column=2, padx=15, pady=5, columnspan=3, sticky='nnw')

    # ------------------ROW 1-------------------------------------------------
    global plot_btn_lf
    plot_btn_lf = LabelFrame(tab1, padx=2, pady=2,bg=back_color, fg=forg_color, width=lf_width)
    plot_btn_lf.grid(row=2, column=2, padx=15, pady=5, columnspan=3, sticky='nnw')

    # ------------------ROW 2-------------------------------------------------
    global chart_opt_lf
    chart_opt_lf = LabelFrame(tab1, text="Chart Options", padx=2, pady=2, bg=back_color, fg=forg_color, width=lf_width)
    chart_opt_lf.grid(row=1, column=2, padx=15, pady=5, columnspan=3, sticky='nnw')
    
    # ------------------ROW 3-------------------------------------------------
    global x_axis_lf
    x_axis_lf = LabelFrame(tab1, text="X-Axis Values", padx=2, pady=2, bg=back_color, fg=forg_color, width=lf_width)
    x_axis_lf.grid(row=3, column=2, padx=15, pady=5, columnspan=3, sticky='nnw')

    # ------------------ROW 4-------------------------------------------------
    # ----------------AXIS PLOTTING NOTEBOOK----------------------------------
    
    axis_nb = ttk.Notebook(tab1)

    axis_1_tab = ttk.Frame(axis_nb)
    axis_2_tab = ttk.Frame(axis_nb)
    annot_tab = ttk.Frame(axis_nb)

    axis_nb.add(axis_1_tab, text='First Axis')
    axis_nb.add(axis_2_tab, text='Second Axis')
    axis_nb.add(annot_tab, text='Annotations')
    
    axis_nb.grid(row=4, column=2, rowspan=8, columnspan=3, sticky='nw', padx=15, pady=5)



    # =======================AXIS 1-2 TAB FRAMES==============================
    
    # ----------------AXIS_1_TAB----------------------------------------------

    global plot_edit_lf

    plot_edit_lf = LabelFrame(axis_1_tab, text="Edit Plot", padx=2, pady=2, width=100, bg=back_color, fg=forg_color)
    plot_edit_lf.grid(row=0, column=0, padx=15, pady=5, columnspan=3,rowspan=1, sticky='nw')
    
    global yaxis_lf

    yaxis_lf = LabelFrame(axis_1_tab, text="Y-Axis Variables", padx=2, pady=2, width=100, bg=back_color, fg=forg_color)
    yaxis_lf.grid(row=1, column=0, padx=15, pady=5, columnspan=3,rowspan=1, sticky='nw')
    
    global add_regression_lf
    
    add_regression_lf = LabelFrame(axis_1_tab, text="Add Regression Lines", padx=2, pady=2, width=100, bg=back_color, fg=forg_color)
    add_regression_lf.grid(row=5, column=0, padx=15, pady=5, columnspan=3,rowspan=1, sticky='nw')
    
    # ----------------AXIS_2_TAB----------------------------------------------
    
    global plot_edit_lf_1

    plot_edit_lf_1 = LabelFrame(axis_2_tab, text="Edit Plot", padx=2, pady=2, width=100, bg=back_color, fg=forg_color)
    plot_edit_lf_1.grid(row=0, column=0, padx=15, pady=5, columnspan=3,rowspan=1, sticky='nw')

    global yaxis_lf_1

    yaxis_lf_1 = LabelFrame(axis_2_tab, text="Y-Axis Variables", padx=2, pady=2, width=100, bg=back_color, fg=forg_color)
    yaxis_lf_1.grid(row=1, column=0, padx=15, pady=5, columnspan=3,rowspan=1, sticky='nw')

    global add_regression_lf_1
    
    add_regression_lf_1 = LabelFrame(axis_2_tab, text="Add Regression Lines", padx=2, pady=2, width=100, bg=back_color, fg=forg_color)
    add_regression_lf_1.grid(row=5, column=0, padx=15, pady=5, columnspan=3,rowspan=1, sticky='nw')
    

    # =======================END FRAMES=======================================
    

    # ==========================LOADED FILE NAME==============================


    loaded_file_name_e= Entry(file_name_lf, width=80, bg = back_color, fg = forg_color, font= ("Calibri", 14))
    loaded_file_name_e.grid(row=0, column=0, padx=5, pady=10, sticky='w')
    loaded_file_name_e.delete(0, END)
    loaded_file_name_e.insert(0, filename)

    # ================Update Data Feilds with function========================
    
    
    #update_table()
    pcd.create_subset_view()
    
    # update_data_fields()
    reset_dd_menus()
    #plot_variable_fields()
    data_functions_feilds()
    meta_data_gen_fields()
    sub_set_fields()
    chart_btn_fields()
    chart_edit_fields()
    chart_edit_fields_1()
    pcd.update_table()
    pcd.update_sub_set()
    #pcd.frame_or_sub_select()
    dataframe_integration_fields()
    chart_opt_gui_gen()
    x_axis_fields()
    axis_gui_gen('first')
    axis_gui_gen('second')
    annot_fields()
    plot_regression_fields()
    plot_regression_fields_1()
    #sub_set_btns()
    pck.keras_gui()
    pcm.map_plot_fields()
    
    
    
# ===============DATA FUNCTION FEILDS=========================================

def dataframe_integration_fields():
    
    
    df_sub  = pcd.df_sub
    df_2 = pcd.df_2
    global df_int_type_table
    global merge_pos_table
    
    df_int_type_table = ["Join","Merge"]
    merge_pos_table = ["left",'right','outer','inner']
    frame = df_m_tab
    

    # ----------------DATA INTEGRATION TYPE------------------------------------
    
    data_int_type_dd = ttk.Combobox(frame, textvariable=data_int_method, values=df_int_type_table)
    data_int_type_dd.configure(width=20)
    data_int_type_dd.insert(0, "Integration")
    data_int_type_dd.grid(row=0, column=0,padx=5, pady=10)
    
    # ----------------RIGHT DATAFRAME-----------------------------------------
    
    right_df_dd = ttk.Combobox(frame, textvariable=right_dataframe, values=list(df_sub))
    right_df_dd.configure(width=20)
    right_df_dd.insert(0, "Right Dataframe")
    right_df_dd.grid(row=0, column=1,padx=5, pady=10)
    
    # ----------------LEFT DATAFRAME------------------------------------------
    
    left_df_dd = ttk.Combobox(frame, textvariable=left_dataframe, values=list(df_2))
    left_df_dd.configure(width=20)
    left_df_dd.insert(0, "Left Dataframe")
    left_df_dd.grid(row=0, column=2,padx=5, pady=10)
    
    # ----------------MERGE POSITION-------------------------------------------
    
    merge_pos_dd = ttk.Combobox(frame, textvariable=merge_position, values=merge_pos_table)
    merge_pos_dd.configure(width=20)
    merge_pos_dd.insert(0, "Merge Position")
    merge_pos_dd.grid(row=0, column=3,padx=5, pady=10)


def data_functions_feilds():

    global data_functions_lf


    #-------------------Filter SUBSET BUTTON----------------------------------
    
    add_sub_set_btn = Button(data_functions_lf, text="Subset Dataframe", 
                             command=pcd.update_sub_set, 
                             width=20, 
                             bg = back_color, 
                             fg = forg_color)
    add_sub_set_btn.grid(row=0, column=0 ,padx=3, pady=3, sticky='w')

    # ------------------ADD META DATA COLUMN BUTTON---------------------------
    
    add_col_btn = Button(data_functions_lf, text="Add Meta Data", 
                         command=pcd.new_calc_col, 
                         width=20, 
                         bg = back_color, 
                         fg = forg_color)
    add_col_btn.grid(row=0, column=1, padx=3, pady=3, sticky='w')
    
    # -------------------Load 2nd Data Set Button-------------------------------

    add_dataframe_btn = Button(data_functions_lf, text = "Load Dataframe(2)",
                                         command = lambda: open_file(1), 
                                         width = 20,
                                         bg = back_color,
                                         fg = forg_color)
    add_dataframe_btn.grid(row=0, column=2, padx=3, pady=3, sticky='w')


    # -----------------MERGE DATAFRAMES BUTTON--------------------------------
    
    merge_data_btn = Button(data_functions_lf, text="Merge Data", 
                             command=pcd.merge_dataframe_view, 
                             width=20, 
                             bg = back_color, 
                             fg = forg_color)
    merge_data_btn.grid(row=0, column=3,padx=3, pady=3, sticky='w')
    
    
    
    # -----------------RENAME COLUMNS BUTTON----------------------------------
    
    rename_col_btn = Button(data_functions_lf, text="Rename Column", 
                             command=pcd.update_sub_set, 
                             width=20, 
                             bg = back_color, 
                             fg = forg_color)
    rename_col_btn.grid(row=1, column=0,padx=3, pady=3, sticky='w')
    
    
    # -----------------DELETE COLUMN BUTTON-----------------------------------
    
    delete_col_btn = Button(data_functions_lf, text="Delete Column", 
                             command=pcd.update_sub_set, 
                             width=20, 
                             bg = back_color, 
                             fg = forg_color)
    delete_col_btn.grid(row=1, column=1,padx=3, pady=3, sticky='w')
    
    #-------------------NEW FUNCTION  Button--------------------------------
    
    active_data_select_btn = Button(data_functions_lf,
                                    text = "Smooth Column",
                                    command = pcd.smooth_signal,
                                    width = 20,
                                    bg = back_color,
                                    fg = forg_color)
    active_data_select_btn.grid(row=1, column=2, padx=3, pady=3, sticky='w')
    
    # -----------------CLEAR FIELDS BUTTON------------------------------------
    
    rest_subset_btn = Button(data_functions_lf,
                             text="Clear Fields", 
                             command=reset_subset_op, 
                             width=20, 
                             bg = back_color, 
                             fg = forg_color)
    rest_subset_btn.grid(row=1, column=3,padx=3, pady=3, sticky='w')
    
   
# ===============CHART BUTTONS================================================

def chart_btn_fields():
    
    global plot_btn_lf
    
    # --------------Plot Data Button-----------------------------

    plot_data_btn = Button(plot_btn_lf, text="Create Plot", command=pcp.plot_data, 
                           width=22, bg = back_color, fg = forg_color)
    plot_data_btn.grid(row=0, column=0, padx=17, pady=5)
    
    # --------------Update Plots btb----------------------------------

    update_plots_dd_btn = Button(plot_btn_lf, text="Update Plot", 
                                 command=pcp.update_plot_size, width=22, 
                                 bg = back_color, fg = forg_color)
    update_plots_dd_btn.grid(row=0, column=1,padx=17, pady=5)
    
    # --------------Plot Data Button-----------------------------

    plot_update_dd_btn = Button(plot_btn_lf, text="Update Dropdowns", command=plot_update_dd, 
                           width=22, bg = back_color, fg = forg_color)
    plot_update_dd_btn.grid(row=0, column=2, padx=17, pady=5)

    # ---------------Reset Variable fields Button----------------

    reset_dd_btn = Button(plot_btn_lf, text="Reset", command=reset_dd_menus, 
                          width=22, bg = back_color, fg = forg_color)
    reset_dd_btn.grid(row=0, column=3,padx=17, pady=5)

# =================   
def plot_update_dd():
    
    axis_gui_gen('first')
    axis_gui_gen('second')
    x_axis_fields()
    plot_regression_fields()
    plot_regression_fields_1()
    
# ====================X AXIS VALUE FIELDS======================================

def x_axis_fields():
    
    global df
    global df_sub
    global df_m
    global df_select_list
    global df_2 
    df_sub = pcd.df_sub
    df_m = pcd.df_m
    
    df_axis = [df, df_sub, df_2, df_m]
    
    for x in range(0,3):
            if axis_1_dataframe.get()==df_select_list[x]:
                df_ax_1 = df_axis[x]
                
    # ----------------X AXIS TITLE--------------------------------------------

    global x_axis_title_e
    x_axis_title_e = Entry(x_axis_lf, textvariable = x_axis_title, width=30, font= ("Calibri", 12))
    x_axis_title_e.grid(row=0, column=0,padx=15, pady=3, sticky='e')
    x_axis_title_e.delete(0, END)
    x_axis_title_e.insert(0, "X-Axis-Title")

    # ----------------X Axis Dropdown-----------------------------------------
    
    dd_box_x = ttk.Combobox(x_axis_lf, textvariable=Var_Col_x, values=list(df_ax_1))
    dd_box_x.configure(width=22, font= ("Calibri", 12))
    dd_box_x.grid(row=0, column=1,padx=10, pady=3)
    
    # ----------------X Min Max-----------------------------------------------
    
    x_axis_min_label =Label(x_axis_lf, text="X Min", bg = back_color,fg = forg_color, font= ("Calibri", 12))
    x_axis_min_label.grid(row=0, column=2, padx=5, pady=5, sticky='nesw')
    
    global plot_x_axis_min_e
    plot_x_axis_min_e = Entry(x_axis_lf, textvariable = plot_x_axis_min, width=10,justify='center', font= ("Calibri", 12))
    plot_x_axis_min_e.grid(row=0, column=3, padx=5, pady=5, sticky='nesw')
    plot_x_axis_min_e.delete(0, END)
    plot_x_axis_min_e.insert(0, "0")

    x_axis_max_label =Label(x_axis_lf, text="X Max", bg = back_color,fg = forg_color, font= ("Calibri", 12))
    x_axis_max_label.grid(row=0, column=4, padx=5, pady=5, sticky='nesw')
    
    global plot_x_axis_max_e
    plot_x_axis_max_e = Entry(x_axis_lf, textvariable = plot_x_axis_max, width=10,justify='center', font= ("Calibri", 12))
    plot_x_axis_max_e.grid(row=0, column=5, padx=5, pady=5, sticky='nesw')
    plot_x_axis_max_e.delete(0, END)
    plot_x_axis_max_e.insert(0, "25")


# ===============Update-Data-Fields===========================================

def update_data_fields():

    meta_data_gen_fields()
    sub_set_fields()
    plot_regression_fields()
    plot_regression_fields_1()

# ===================Chart Edit options=======================================

def chart_edit_fields():
    
    global plot_y_axis_min_e
    global plot_y_axis_max_e
    global y_axis_title_e
    global df_select_list
    
    y_axis_title_e = Entry(plot_edit_lf, textvariable = y_axis_title, width=30, font= ("Calibri", 12),justify='center')
    y_axis_title_e.grid(row=0, column=0,padx=5, pady=5, sticky='e')
    y_axis_title_e.delete(0, END)
    y_axis_title_e.insert(0, "Y-Axis-Title")
    
    # ---------------Plot Point-----------------------------------------------
    
    plot_marker_label =Label(plot_edit_lf, text="Plot Point Size", bg = back_color,fg = forg_color, font= ("Calibri", 12))
    plot_marker_label.grid(row=0, column=2, padx=5, pady=5, sticky='e')
    
    
    plot_marker_size_e = Entry(plot_edit_lf, textvariable = plot_marker_size, width=7,justify='center', font= ("Calibri", 12))
    plot_marker_size_e.grid(row=0, column=3, padx=5, pady=5, sticky='e')
    plot_marker_size_e.delete(0, END)
    plot_marker_size_e.insert(0, "25")
    
    # ---------------Y MIN AND MAX--------------------------------------------

    y_axis_min_label =Label(plot_edit_lf, text="Y Min", bg = back_color,fg = forg_color, font= ("Calibri", 12))
    y_axis_min_label.grid(row=0, column=4, padx=10, pady=5, sticky='e')
    
    plot_y_axis_min_e = Entry(plot_edit_lf, textvariable = plot_y_axis_min, width=10,justify='center', font= ("Calibri", 12))
    plot_y_axis_min_e.grid(row=0, column=5, padx=5, pady=5, sticky='e')
    plot_y_axis_min_e.delete(0, END)
    plot_y_axis_min_e.insert(0, "0")

    y_axis_max_label =Label(plot_edit_lf, text="Y Max", bg =back_color,fg = forg_color, font= ("Calibri", 12))
    y_axis_max_label.grid(row=0, column=6, padx=10, pady=5, sticky='e')
    
    plot_y_axis_max_e = Entry(plot_edit_lf, textvariable = plot_y_axis_max, width=10,justify='center', font= ("Calibri", 12))
    plot_y_axis_max_e.grid(row=0, column=7, padx=5, pady=5, sticky='e')
    plot_y_axis_max_e.delete(0, END)
    plot_y_axis_max_e.insert(0, "25")
    
    

def chart_edit_fields_1():
    

    global plot_y_axis_min_1_e
    global plot_y_axis_max_1_e
    global y_axis_title_1_e
    global df_select_list
    
    y_axis_title_1_e = Entry(plot_edit_lf_1, textvariable = y_axis_title_1, width=30, font= ("Calibri", 12))
    y_axis_title_1_e.grid(row=0, column=0,padx=5, pady=3, sticky='e')
    y_axis_title_1_e.delete(0, END)
    y_axis_title_1_e.insert(0, "Y-Axis-Title")
    
    # ---------------Plot Point-----------------------------------------------

    plot_marker_label =Label(plot_edit_lf_1, text="Plot Point Size", bg = back_color,fg = forg_color, font= ("Calibri", 12))
    plot_marker_label.grid(row=0, column=2, padx=5, pady=5, sticky='e')

    plot_marker_size_e = Entry(plot_edit_lf_1, textvariable = plot_marker_size_1, width=7,justify='center', font= ("Calibri", 12))
    plot_marker_size_e.grid(row=0, column=3, padx=5, pady=5, sticky='e')
    plot_marker_size_e.delete(0, END)
    plot_marker_size_e.insert(0, "25")
    
    # ---------------Y MIN AND MAX--------------------------------------------
    
    y_axis_min_label =Label(plot_edit_lf_1, text="Y Min", bg = back_color,fg = forg_color, font= ("Calibri", 12))
    y_axis_min_label.grid(row=0, column=4, padx=5, pady=5, sticky='e')

    plot_y_axis_min_1_e = Entry(plot_edit_lf_1, textvariable = plot_y_axis_min_1, width=10,justify='center', font= ("Calibri", 12))
    plot_y_axis_min_1_e.grid(row=0, column=5, padx=12, pady=5, sticky='e')
    plot_y_axis_min_1_e.delete(0, END)
    plot_y_axis_min_1_e.insert(0, "0")

    y_axis_max_label =Label(plot_edit_lf_1, text="Y Max", bg =back_color,fg = forg_color, font= ("Calibri", 12))
    y_axis_max_label.grid(row=0, column=6, padx=5, pady=5, sticky='e')
    
    plot_y_axis_max_1_e = Entry(plot_edit_lf_1, textvariable = plot_y_axis_max_1, width=10,justify='center', font= ("Calibri", 12))
    plot_y_axis_max_1_e.grid(row=0, column=7, padx=12, pady=5, sticky='e')
    plot_y_axis_max_1_e.delete(0, END)
    plot_y_axis_max_1_e.insert(0, "25")

# ====================ANNOTATION FIELDS=======================================

def annot_fields():
    
    #global annot_tab
    global annot_arrow_table
    
    # =====================Annoation 1========================================
    
    annot_1_label =Label(annot_tab, text="Annotation (1)", bg = back_color,fg = forg_color)
    annot_1_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
    
    annot_1_e = Entry(annot_tab, textvariable = annot_1, width=15,justify='center')
    annot_1_e.grid(row=0, column=1, padx=5, pady=5, sticky='e')
    annot_1_e.delete(0, END)
    annot_1_e.insert(0, "Annotation (1)")
    
    annot_arrow_1_dd = ttk.Combobox(annot_tab, textvariable=annot_arrow_1, values=annot_arrow_table)
    annot_arrow_1_dd.configure(width=5, font= ("Calibri", 12))
    annot_arrow_1_dd.delete(0, END)
    annot_arrow_1_dd.insert(0, "->")
    annot_arrow_1_dd.grid(row=0, column=2,padx=5, pady=10)
    
    # -----------------DATA POINT ENTRY FORM----------------------------------
    
    annot_x_1_e = Entry(annot_tab, textvariable = annot_x_1, width=15,justify='center')
    annot_x_1_e.grid(row=0, column=3, padx=5, pady=5, sticky='e')
    annot_x_1_e.delete(0, END)
    annot_x_1_e.insert(0, "x-coord")
    
    annot_y_1_e = Entry(annot_tab, textvariable = annot_y_1, width=15,justify='center')
    annot_y_1_e.grid(row=0, column=4, padx=5, pady=5, sticky='e')
    annot_y_1_e.delete(0, END)
    annot_y_1_e.insert(0, "y-coord")
    
    # --------------------TEXT ENTRY FORMS------------------------------------
    
    annot_x_1_t_e = Entry(annot_tab, textvariable = annot_x_t_1, width=15,justify='center')
    annot_x_1_t_e.grid(row=0, column=5, padx=5, pady=5, sticky='e')
    annot_x_1_t_e.delete(0, END)
    annot_x_1_t_e.insert(0, "x-text-coord")
    
    annot_y_1_t_e = Entry(annot_tab, textvariable = annot_y_t_1, width=15,justify='center')
    annot_y_1_t_e.grid(row=0, column=6, padx=5, pady=5, sticky='e')
    annot_y_1_t_e.delete(0, END)
    annot_y_1_t_e.insert(0, "y-text-coord")
    
    # =====================Annoation 2========================================
    
    annot_2_label =Label(annot_tab, text="Annotation (2)", bg = back_color,fg = forg_color)
    annot_2_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
    
    annot_2_e = Entry(annot_tab, textvariable = annot_2, width=15,justify='center')
    annot_2_e.grid(row=1, column=1, padx=5, pady=5, sticky='e')
    annot_2_e.delete(1, END)
    annot_2_e.insert(1, "Annotation (2)")
    
    annot_arrow_2_dd = ttk.Combobox(annot_tab, textvariable=annot_arrow_2, values=annot_arrow_table)
    annot_arrow_2_dd.configure(width=5, font= ("Calibri", 12))
    annot_arrow_2_dd.delete(0, END)
    annot_arrow_2_dd.insert(0, "->")
    annot_arrow_2_dd.grid(row=1, column=2,padx=5, pady=10)
    
    annot_x_2_e = Entry(annot_tab, textvariable = annot_x_2, width=15,justify='center')
    annot_x_2_e.grid(row=1, column=3, padx=5, pady=5, sticky='e')
    annot_x_2_e.delete(0, END)
    annot_x_2_e.insert(0, "x-coord")
    
    annot_y_2_e = Entry(annot_tab, textvariable = annot_y_2, width=15,justify='center')
    annot_y_2_e.grid(row=1, column=4, padx=5, pady=5, sticky='e')
    annot_y_2_e.delete(0, END)
    annot_y_2_e.insert(0, "y-coord")
    
    # --------------------TEXT ENTRY FORMS------------------------------------
    
    annot_x_2_t_e = Entry(annot_tab, textvariable = annot_x_t_2, width=15,justify='center')
    annot_x_2_t_e.grid(row=1, column=5, padx=5, pady=5, sticky='e')
    annot_x_2_t_e.delete(0, END)
    annot_x_2_t_e.insert(0, "x-text-coord")
    
    annot_y_2_t_e = Entry(annot_tab, textvariable = annot_y_t_2, width=15,justify='center')
    annot_y_2_t_e.grid(row=1, column=6, padx=5, pady=5, sticky='e')
    annot_y_2_t_e.delete(0, END)
    annot_y_2_t_e.insert(0, "y-text-coord")
    
    # =====================Annoation 3========================================
    
    annot_3_label =Label(annot_tab, text="Annotation (3)", bg = back_color,fg = forg_color)
    annot_3_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
    
    annot_3_e = Entry(annot_tab, textvariable = annot_3, width=15,justify='center')
    annot_3_e.grid(row=2, column=1, padx=5, pady=5, sticky='e')
    annot_3_e.delete(0, END)
    annot_3_e.insert(0, "Annotation (3)")
    
    annot_arrow_3_dd = ttk.Combobox(annot_tab, textvariable=annot_arrow_3, values=annot_arrow_table)
    annot_arrow_3_dd.configure(width=5, font= ("Calibri", 12))
    annot_arrow_3_dd.delete(0, END)
    annot_arrow_3_dd.insert(0, "->")
    annot_arrow_3_dd.grid(row=2, column=2,padx=5, pady=10)
    
    annot_x_3_e = Entry(annot_tab, textvariable = annot_x_3, width=15,justify='center')
    annot_x_3_e.grid(row=2, column=3, padx=5, pady=5, sticky='e')
    annot_x_3_e.delete(0, END)
    annot_x_3_e.insert(0, "x-coord")
    
    annot_y_3_e = Entry(annot_tab, textvariable = annot_y_3, width=15,justify='center')
    annot_y_3_e.grid(row=2, column=4, padx=5, pady=5, sticky='e')
    annot_y_3_e.delete(0, END)
    annot_y_3_e.insert(0, "y-coord")
    
    # --------------------TEXT ENTRY FORMS------------------------------------
    
    annot_x_3_t_e = Entry(annot_tab, textvariable = annot_x_t_3, width=15,justify='center')
    annot_x_3_t_e.grid(row=2, column=5, padx=5, pady=5, sticky='e')
    annot_x_3_t_e.delete(0, END)
    annot_x_3_t_e.insert(0, "x-text-coord")
    
    annot_y_3_t_e = Entry(annot_tab, textvariable = annot_y_t_3, width=15,justify='center')
    annot_y_3_t_e.grid(row=2, column=6, padx=5, pady=5, sticky='e')
    annot_y_3_t_e.delete(0, END)
    annot_y_3_t_e.insert(0, "y-text-coord")
    
    # =====================Annoation 4========================================
    
    annot_4_label =Label(annot_tab, text="Annotation (4)", bg = back_color,fg = forg_color)
    annot_4_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
    
    annot_4_e = Entry(annot_tab, textvariable = annot_4, width=15,justify='center')
    annot_4_e.grid(row=3, column=1, padx=5, pady=5, sticky='e')
    annot_4_e.delete(0, END)
    annot_4_e.insert(0, "Annotation (4)")
    
    annot_arrow_4_dd = ttk.Combobox(annot_tab, textvariable=annot_arrow_4, values=annot_arrow_table)
    annot_arrow_4_dd.configure(width=5, font= ("Calibri", 12))
    annot_arrow_4_dd.delete(0, END)
    annot_arrow_4_dd.insert(0, "->")
    annot_arrow_4_dd.grid(row=3, column=2,padx=5, pady=10)
    
    annot_x_4_e = Entry(annot_tab, textvariable = annot_x_4, width=15,justify='center')
    annot_x_4_e.grid(row=3, column=3, padx=5, pady=5, sticky='e')
    annot_x_4_e.delete(0, END)
    annot_x_4_e.insert(0, "x-coord")
    
    annot_y_4_e = Entry(annot_tab, textvariable = annot_y_4, width=15,justify='center')
    annot_y_4_e.grid(row=3, column=4, padx=5, pady=5, sticky='e')
    annot_y_4_e.delete(0, END)
    annot_y_4_e.insert(0, "y-coord")
    
    # --------------------TEXT ENTRY FORMS------------------------------------
    
    annot_x_4_t_e = Entry(annot_tab, textvariable = annot_x_t_4, width=15,justify='center')
    annot_x_4_t_e.grid(row=3, column=5, padx=5, pady=5, sticky='e')
    annot_x_4_t_e.delete(0, END)
    annot_x_4_t_e.insert(0, "x-text-coord")
    
    annot_y_4_t_e = Entry(annot_tab, textvariable = annot_y_t_4, width=15,justify='center')
    annot_y_4_t_e.grid(row=3, column=6, padx=5, pady=5, sticky='e')
    annot_y_4_t_e.delete(0, END)
    annot_y_4_t_e.insert(0, "y-text-coord")
    
    # =====================Annoation 5========================================
    
    annot_5_label =Label(annot_tab, text="Annotation (5)", bg = back_color,fg = forg_color)
    annot_5_label.grid(row=4, column=0, padx=5, pady=5, sticky='e')
    
    annot_5_e = Entry(annot_tab, textvariable = annot_5, width=15,justify='center')
    annot_5_e.grid(row=4, column=1, padx=5, pady=5, sticky='e')
    annot_5_e.delete(0, END)
    annot_5_e.insert(0, "Annotation (5)")
    
    annot_arrow_5_dd = ttk.Combobox(annot_tab, textvariable=annot_arrow_5, values=annot_arrow_table)
    annot_arrow_5_dd.configure(width=5, font= ("Calibri", 12))
    annot_arrow_5_dd.delete(0, END)
    annot_arrow_5_dd.insert(0, "->")
    annot_arrow_5_dd.grid(row=4, column=2,padx=5, pady=10)
    
    annot_x_5_e = Entry(annot_tab, textvariable = annot_x_5, width=15,justify='center')
    annot_x_5_e.grid(row=4, column=3, padx=5, pady=5, sticky='e')
    annot_x_5_e.delete(0, END)
    annot_x_5_e.insert(0, "x-coord")
    
    annot_y_5_e = Entry(annot_tab, textvariable = annot_y_5, width=15,justify='center')
    annot_y_5_e.grid(row=4, column=4, padx=5, pady=5, sticky='e')
    annot_y_5_e.delete(0, END)
    annot_y_5_e.insert(0, "y-coord")
    
    # --------------------TEXT ENTRY FORMS------------------------------------
    
    annot_x_5_t_e = Entry(annot_tab, textvariable = annot_x_t_5, width=15,justify='center')
    annot_x_5_t_e.grid(row=4, column=5, padx=5, pady=5, sticky='e')
    annot_x_5_t_e.delete(0, END)
    annot_x_5_t_e.insert(0, "x-text-coord")
    
    annot_y_5_t_e = Entry(annot_tab, textvariable = annot_y_t_5, width=15,justify='center')
    annot_y_5_t_e.grid(row=4, column=6, padx=5, pady=5, sticky='e')
    annot_y_5_t_e.delete(0, END)
    annot_y_5_t_e.insert(0, "y-text-coord")

    
def meta_data_gen_fields():
    
    dd_y_width = int(root.winfo_width()/120)
    dd_padx  = int(root.winfo_width()/300)
    dd_pady = int(root.winfo_width()/1000)
    op_width = 10
    
    
    new_col_name_e= Entry(add_data_lf, textvariable = new_col_name, width=25)
    new_col_name_e.grid(row=0, column=1,padx=10, pady=5, sticky='e')
    new_col_name_e.delete(0, END)
    new_col_name_e.insert(0, "New Column Name")

    col_value_1.set(["First Variable"])
    col_value_2.set(["Second Variable"])

    col_value_1_dd= ttk.Combobox(add_data_lf, textvariable=col_value_1, values=list(df), width=2*dd_y_width)
    col_value_1_dd.grid(row=0, column=2,padx=dd_padx, pady=dd_pady, sticky='e')
    col_value_1_dd.delete(0, END)
    col_value_1_dd.insert(0, "New Value Equation (1)")

    col_value_2_dd= ttk.Combobox(add_data_lf, textvariable=col_value_2, values=list(df), width=2*dd_y_width)
    col_value_2_dd.grid(row=0, column=4,padx=dd_padx, pady=dd_pady, sticky='e')
    col_value_2_dd.delete(0, END)
    col_value_2_dd.insert(0, "New Value Equation (2)")

    col_operator_dd= ttk.Combobox(add_data_lf, textvariable=col_operator, values=meta_data_operators, width=op_width)
    col_operator_dd.grid(row=0, column=3,padx=dd_padx, pady=dd_pady, sticky='e')
    col_operator_dd.delete(0, END)
    col_operator_dd.insert(0, "Operator")

    
def sub_set_fields():

    value_dd_width = 20
    operator_dd_width = 9
    sub_set_pady = int(root.winfo_width()/800)
    sub_set_padx = int(root.winfo_width()/270)
    

    sub_set_value_1_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_value_1, values=list(df), width=value_dd_width, justify='center')
    sub_set_value_1_dd.grid(row=1, column=0,padx=sub_set_padx, pady=sub_set_pady, sticky='e')
    sub_set_value_1_dd.delete(0, END)
    sub_set_value_1_dd.insert(0, "Value (1)")
    
    sub_set_operator_1_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_operator_1, values=sub_set_operators, width=operator_dd_width, justify='center')
    sub_set_operator_1_dd.grid(row=1, column=1,padx=sub_set_padx/2, pady=sub_set_pady, sticky='e')
    sub_set_operator_1_dd.delete(0, END)
    sub_set_operator_1_dd.insert(0, "Op (1)")

    sub_set_value_2_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_value_2, values=list(df), width=value_dd_width, justify='center')
    sub_set_value_2_dd.grid(row=1, column=2,padx=sub_set_padx, pady=sub_set_pady, sticky='e')
    sub_set_value_2_dd.delete(0, END)
    sub_set_value_2_dd.insert(0, "Value (2)")
    
    sub_set_operator_2_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_operator_2, values=sub_set_operators, width=operator_dd_width, justify='center')
    sub_set_operator_2_dd.grid(row=1, column=3,padx=sub_set_padx/2, pady=sub_set_pady, sticky='e')
    sub_set_operator_2_dd.delete(0, END)
    sub_set_operator_2_dd.insert(0, "Op (2)")
    
    sub_set_value_3_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_value_3, values=list(df), width=value_dd_width, justify='center')
    sub_set_value_3_dd.grid(row=1, column=4,padx=sub_set_padx, pady=sub_set_pady, sticky='e')
    sub_set_value_3_dd.delete(0, END)
    sub_set_value_3_dd.insert(0, "Value (3)")
    
    # Second row of subplot
    
    sub_set_value_4_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_value_4, values=list(df), width=value_dd_width, justify='center')
    sub_set_value_4_dd.grid(row=2, column=0,padx=sub_set_padx, pady=sub_set_pady, sticky='e')
    sub_set_value_4_dd.delete(0, END)
    sub_set_value_4_dd.insert(0, "Value (4)")
    
    sub_set_operator_3_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_operator_3, values=sub_set_operators, width=operator_dd_width, justify='center')
    sub_set_operator_3_dd.grid(row=2, column=1,padx=sub_set_padx/2, pady=sub_set_pady, sticky='e')
    sub_set_operator_3_dd.delete(0, END)
    sub_set_operator_3_dd.insert(0, "Op (3)")
    
    sub_set_value_5_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_value_5, values=list(df), width=value_dd_width, justify='center')
    sub_set_value_5_dd.grid(row=2, column=2,padx=sub_set_padx, pady=sub_set_pady, sticky='e')
    sub_set_value_5_dd.delete(0, END)
    sub_set_value_5_dd.insert(0, "Value (5)")
    
    sub_set_operator_4_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_operator_4, values=sub_set_operators, width=operator_dd_width, justify='center')
    sub_set_operator_4_dd.grid(row=2, column=3,padx=sub_set_padx/2, pady=sub_set_pady, sticky='e')
    sub_set_operator_4_dd.delete(0, END)
    sub_set_operator_4_dd.insert(0, "Op (4)")
    
    sub_set_value_6_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_value_6, values=list(df), width=value_dd_width, justify='center')
    sub_set_value_6_dd.grid(row=2, column=4,padx=sub_set_padx, pady=sub_set_pady, sticky='e')
    sub_set_value_6_dd.delete(0, END)
    sub_set_value_6_dd.insert(0, "Value (6)")

    
    # Third row of subplot
    
    sub_set_value_7_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_value_7, values=list(df), width=value_dd_width, justify='center')
    sub_set_value_7_dd.grid(row=3, column=0,padx=sub_set_padx, pady=sub_set_pady, sticky='e')
    sub_set_value_7_dd.delete(0, END)
    sub_set_value_7_dd.insert(0, "Value (7)")
    
    sub_set_operator_5_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_operator_5, values=sub_set_operators, width=operator_dd_width, justify='center')
    sub_set_operator_5_dd.grid(row=3, column=1,padx=sub_set_padx/2, pady=sub_set_pady, sticky='e')
    sub_set_operator_5_dd.delete(0, END)
    sub_set_operator_5_dd.insert(0, "Op (5)")
    
    sub_set_value_8_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_value_8, values=list(df), width=value_dd_width, justify='center')
    sub_set_value_8_dd.grid(row=3, column=2,padx=sub_set_padx, pady=sub_set_pady, sticky='e')
    sub_set_value_8_dd.delete(0, END)
    sub_set_value_8_dd.insert(0, "Value (8)")
    
    sub_set_operator_6_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_operator_6, values=sub_set_operators, width=operator_dd_width, justify='center')
    sub_set_operator_6_dd.grid(row=3, column=3,padx=sub_set_padx/2, pady=sub_set_pady, sticky='e')
    sub_set_operator_6_dd.delete(0, END)
    sub_set_operator_6_dd.insert(0, "Op (6)")
    
    sub_set_value_9_dd= ttk.Combobox(add_subset_lf, textvariable=sub_set_value_9, values=list(df), width=value_dd_width, justify='center')
    sub_set_value_9_dd.grid(row=3, column=4,padx=sub_set_padx, pady=sub_set_pady, sticky='e')
    sub_set_value_9_dd.delete(0, END)
    sub_set_value_9_dd.insert(0, "Value (9)")
    
    
# ================REGRESSION=================================================

def plot_regression_fields():

    global ax
    global ax_1
    global reg_x_axis_dd
    global reg_y_axis_dd 
    df_sub  = pcd.df_sub
    
    global df
    global df_m
    global df_select_list
    global df_2 
    df_m = pcd.df_m
    
    df_axis = [df, df_sub, df_2, df_m]
    
    for x in range(0,3):
            if axis_1_dataframe.get()==df_select_list[x]:
                df_ax_1 = df_axis[x]

    reg_equ_list = ['1','2','3','4']    

    # ========Regression X Select============================================

    reg_x_axis_dd= ttk.Combobox(add_regression_lf, textvariable=reg_x_axis, values=list(df_ax_1), width=20, justify='center')
    reg_x_axis_dd.grid(row=0, column=0,padx=5, pady=3, sticky='e')
    reg_x_axis_dd.delete(0, END)
    reg_x_axis_dd.insert(0, "X-Axis")
    
    # ========Regression X Minimum============================================
    
    reg_x_min_e= Entry(add_regression_lf, textvariable = reg_x_min, width=10)
    reg_x_min_e.grid(row=0, column=1,padx=10, pady=5, sticky='e')
    reg_x_min_e.delete(0, END)
    reg_x_min_e.insert(0, "Min")
    
    # ========Regression X Maximum============================================
    
    reg_x_max_e= Entry(add_regression_lf, textvariable = reg_x_max, width=10)
    reg_x_max_e.grid(row=0, column=2,padx=10, pady=5, sticky='e')
    reg_x_max_e.delete(0, END)
    reg_x_max_e.insert(0, "Max")

    # ========Regression Y Select============================================ 
    
    reg_y_axis_dd= ttk.Combobox(add_regression_lf, textvariable=reg_y_axis, values=list(df_ax_1), width=20, justify='center')
    reg_y_axis_dd.grid(row=0, column=3,padx=5, pady=3, sticky='e')
    reg_y_axis_dd.delete(0, END)
    reg_y_axis_dd.insert(0, "Y-Axis")
    
    # ========Regression Method Select=======================================

    reg_type_dd= ttk.Combobox(add_regression_lf, textvariable=reg_type, values=reg_equ_list, width=20, justify='center')
    reg_type_dd.grid(row=0, column=4,padx=5, pady=3, sticky='e')
    reg_type_dd.delete(0, END)
    reg_type_dd.insert(0, "Line Type")

    # ===========Regression button===========================================

    add_regression_btn = Button(add_regression_lf, text="Add Regression", 
                                command=lambda:pcp.add_regression(reg_x_axis.get(), 
                                                                  reg_x_min.get(), 
                                                                  reg_x_max.get(), 
                                                                  reg_y_axis.get(), 
                                                                  0, 
                                                                  reg_type.get()),
                                width=15, bg = back_color, fg = forg_color)
    
    add_regression_btn.grid(row=0, column=5,padx=5, pady=2, sticky='w')

def plot_regression_fields_1():
    
    global ax
    global ax_1
    global reg_x_axis_1_dd
    global reg_y_axis_1_dd
    df_sub  = pcd.df_sub
    
    global df
    global df_m
    global df_select_list
    global df_2 
    df_m = pcd.df_m
    
    df_axis = [df, df_sub, df_2, df_m]
    
    for x in range(0,3):
            if axis_2_dataframe.get()==df_select_list[x]:
                df_ax_2 = df_axis[x]
    
    reg_equ_list = ['1','2','3','4']    

    # ========Regression X Select============================================

    reg_x_axis_1_dd= ttk.Combobox(add_regression_lf_1, textvariable=reg_x_axis_1, values=list(df_ax_2), width=20, justify='center')
    reg_x_axis_1_dd.grid(row=0, column=0,padx=5, pady=3, sticky='e')
    reg_x_axis_1_dd.delete(0, END)
    reg_x_axis_1_dd.insert(0, "X-Axis")
    
    # ========Regression X Minimum============================================
    
    reg_x_min_1_e= Entry(add_regression_lf_1, textvariable = reg_x_min_1, width=10)
    reg_x_min_1_e.grid(row=0, column=1,padx=10, pady=5, sticky='e')
    reg_x_min_1_e.delete(0, END)
    reg_x_min_1_e.insert(0, "Min")
    
    # ========Regression X Maximum============================================
    
    reg_x_max_1_e= Entry(add_regression_lf_1, textvariable = reg_x_max_1, width=10)
    reg_x_max_1_e.grid(row=0, column=2,padx=10, pady=5, sticky='e')
    reg_x_max_1_e.delete(0, END)
    reg_x_max_1_e.insert(0, "Max")

    # ========Regression Y Select============================================ 
    
    reg_y_axis_1_dd= ttk.Combobox(add_regression_lf_1, textvariable=reg_y_axis_1, values=list(df_ax_2), width=20, justify='center')
    reg_y_axis_1_dd.grid(row=0, column=3,padx=5, pady=3, sticky='e')
    reg_y_axis_1_dd.delete(0, END)
    reg_y_axis_1_dd.insert(0, "Y-Axis")
    
    # ========Regression Method Select=======================================

    reg_type_1_dd= ttk.Combobox(add_regression_lf_1, textvariable=reg_type_1, values=reg_equ_list, width=20, justify='center')
    reg_type_1_dd.grid(row=0, column=4,padx=5, pady=3, sticky='e')
    reg_type_1_dd.delete(0, END)
    reg_type_1_dd.insert(0, "Line Type")

    # ===========Regression button===========================================

    add_regression_1_btn = Button(add_regression_lf_1, text="Add Regression", 
                                  command=lambda:pcp.add_regression(reg_x_axis_1.get(), 
                                                                    reg_x_min_1.get(), 
                                                                    reg_x_max_1.get(),
                                                                    reg_y_axis_1.get(), 
                                                                    1, 
                                                                    reg_type_1.get()), 
                                  width=15, bg = back_color, fg = forg_color)
    add_regression_1_btn.grid(row=0, column=5,padx=5, pady=2, sticky='w')


# -------------------Legend Labels------------------------------------------

def update_legend_labels():
    
    global legend_label_1
    global legend_label_2
    global legend_label_3
    global legend_label_4
    global legend_label_5
    global legend_label_6
    global legend_label_7
    global legend_label_8
    global legend_label_9
    global legend_label_10
    
    global legend_label_1_1
    global legend_label_2_1
    global legend_label_3_1
    global legend_label_4_1
    global legend_label_5_1
    global legend_label_6_1
    global legend_label_7_1
    global legend_label_8_1
    global legend_label_9_1
    global legend_label_10_1
    
    legend_label_1= y_title_1.get()
    legend_label_2= y_title_2.get()
    legend_label_3= y_title_3.get()
    legend_label_4= y_title_4.get()
    legend_label_5= y_title_5.get()
    legend_label_6= y_title_6.get()
    legend_label_7= y_title_7.get()
    legend_label_8= y_title_8.get()
    legend_label_9= y_title_9.get()
    legend_label_10= y_title_10.get()
    
    legend_label_1_1= y_title_1_1.get()
    legend_label_2_1= y_title_2_1.get()
    legend_label_3_1= y_title_3_1.get()
    legend_label_4_1= y_title_4_1.get()
    legend_label_5_1= y_title_5_1.get()
    legend_label_6_1= y_title_6_1.get()
    legend_label_7_1= y_title_7_1.get()
    legend_label_8_1= y_title_8_1.get()
    legend_label_9_1= y_title_9_1.get()
    legend_label_10_1= y_title_10_1.get()

def reset_subset_op():
    
    global sub_set_value_1
    global sub_set_value_2
    global sub_set_value_3
    global sub_set_operator_1
    global sub_set_operator_2
    global sub_set_value_4_
    global sub_set_value_5
    global sub_set_value_6
    global sub_set_operator_3
    global sub_set_operator_4
    global sub_set_value_7
    global sub_set_value_8
    global sub_set_value_9
    global sub_set_operator_5
    global sub_set_operator_6
    
    sub_set_fields()

# ------------reset y axis dropdown menus-------------------------------------

def reset_dd_menus():
    
    Var_Col_x.set(["X Axis"])
    Var_Col_1.set(["Y Axis 1"])
    Var_Col_2.set(["Y Axis 2"])
    Var_Col_3.set(["Y Axis 3"])
    Var_Col_4.set(["Y Axis 4"])
    Var_Col_5.set(["Y Axis 5"])
    Var_Col_6.set(["Y Axis 6"])
    Var_Col_7.set(["Y Axis 7"])
    Var_Col_8.set(["Y Axis 8"])
    Var_Col_9.set(["Y Axis 9"])
    Var_Col_10.set(["Y Axis 10"])
    
    Var_Col_1_1.set(["Y Axis 1"])
    Var_Col_2_1.set(["Y Axis 2"])
    Var_Col_3_1.set(["Y Axis 3"])
    Var_Col_4_1.set(["Y Axis 4"])
    Var_Col_5_1.set(["Y Axis 5"])
    Var_Col_6_1.set(["Y Axis 6"])
    Var_Col_7_1.set(["Y Axis 7"])
    Var_Col_8_1.set(["Y Axis 8"])
    Var_Col_9_1.set(["Y Axis 9"])
    Var_Col_10_1.set(["Y Axis 10"])
    
    graph_type.set(["1st Chart Type"])
    graph_type_1.set(['2nd Chart Type'])

def reset_legend_titles():
    
    y_title_1.set([Var_Col_1.get()])
    y_title_2.set([Var_Col_2.get()])
    y_title_3.set([Var_Col_3.get()])
    y_title_4.set([Var_Col_4.get()])
    y_title_5.set([Var_Col_5.get()])
    y_title_6.set([Var_Col_6.get()])
    y_title_7.set([Var_Col_7.get()])
    y_title_8.set([Var_Col_8.get()])
    y_title_9.set([Var_Col_9.get()])
    y_title_10.set([Var_Col_10.get()])

# ==============CHART OPTIONS GUI GEN=========================================

def chart_opt_gui_gen():

    dd_y_width = int(root.winfo_width()/120)
    dd_set_pady = int(root.winfo_width()/1000)
    dd_set_padx = int(root.winfo_width()/300)
    
    global df_select_lis
    
    # ------------Chart Axis and Title Naming---------------------------------
    
    global plot_name_e
    plot_name_e = Entry(chart_opt_lf, textvariable = Plot_Name, width=25, font= ("Calibri", 12))
    plot_name_e.grid(row=0, column=0,padx=5, pady=3, sticky='e')
    plot_name_e.delete(0, END)
    plot_name_e.insert(0, "Plot Name")
    
    # ========================== Graph Type 1===================================

    dd_box_graph_type = ttk.Combobox(chart_opt_lf, textvariable=graph_type, values=graph_options)
    dd_box_graph_type.config(width=12, font= ("Calibri", 12))
    dd_box_graph_type.grid(row=0, column=1,padx=5, pady=3)
    
    # ----------------AXIS 1 Dropdown-----------------------------------------
    
    axis_1_dataframe_dd = ttk.Combobox(chart_opt_lf, textvariable=axis_1_dataframe, values=df_select_list)
    axis_1_dataframe_dd.configure(width=17, font= ("Calibri", 12))
    axis_1_dataframe_dd.delete(0, END)
    axis_1_dataframe_dd.insert(0, "Dataframe (1)")
    axis_1_dataframe_dd.grid(row=0, column=2,padx=5, pady=3)
    
    # ========================== Graph Type 2===================================

    dd_box_graph_type_1 = ttk.Combobox(chart_opt_lf, textvariable=graph_type_1, values=graph_options)
    dd_box_graph_type_1.config(width=12, font= ("Calibri", 12))
    dd_box_graph_type_1.grid(row=0, column=3,padx=5, pady=3)

    # ----------------AXIS 2 Dropdown-----------------------------------------
    
    axis_2_dataframe_dd = ttk.Combobox(chart_opt_lf, textvariable=axis_2_dataframe, values=df_select_list)
    axis_2_dataframe_dd.configure(width=17, font= ("Calibri", 12))
    axis_2_dataframe_dd.delete(0, END)
    axis_2_dataframe_dd.insert(0, "Dataframe (1) Subset")
    axis_2_dataframe_dd.grid(row=0, column=4,padx=5, pady=3)

# -------------Graph legend labels----------------------

def axis_gui_gen(axis_num):
    
    global df_select_list
    global df
    df_sub = pcd.df_sub
    global df_2
    
    text_width = 20
    symbol_width = 4
    pad_x = 5
    pad_y = 7
    
    dd_y_width = int(root.winfo_width()/120)
    dd_set_pady = int(root.winfo_width()/1000)
    dd_set_padx = int(root.winfo_width()/300)
    df_axis = [df, df_sub, df_2, df_m]
    
    if axis_num == 'first':
        
        for x in range(0,3):
            if axis_1_dataframe.get()==df_select_list[x]:
                df_ax_1 = df_axis[x]

        field_loc = yaxis_lf
    
        # ======================Y VARIABLE 1==========================================

        dd_box_1 = ttk.Combobox(field_loc, textvariable=Var_Col_1, values=list(df_ax_1))
        dd_box_1.config(width=dd_y_width)
        dd_box_1.grid(row=0, column=0,padx=dd_set_padx, pady=dd_set_pady)
    
        y_title_1_e = Entry(field_loc, textvariable = y_title_1, width=text_width)
        y_title_1_e.grid(row=0, column=1,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_1_e.delete(0, END)
        y_title_1_e.insert(0, Var_Col_1.get())
    
        dd_box_plot_symbol_1 = ttk.Combobox(field_loc, textvariable=plot_symbol_1, values=plot_symbol_list)
        dd_box_plot_symbol_1.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_1.grid(row=0, column=2,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_1.delete(0, END)
        dd_box_plot_symbol_1.insert(0,"o")
        
        dd_box_plot_color_1 = ttk.Combobox(field_loc, textvariable=plot_color_1, values=plot_color_list)
        dd_box_plot_color_1.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_1.grid(row=0, column=3,padx=pad_x, pady=pad_y)
        dd_box_plot_color_1.delete(0, END)
        dd_box_plot_color_1.insert(0,"blue")

        # ======================Y VARIABLE 2==========================================

        dd_box_2 = ttk.Combobox(field_loc, textvariable=Var_Col_2, values=list(df_ax_1))
        dd_box_2.config(width=dd_y_width)
        dd_box_2.grid(row=0, column=4,padx=dd_set_padx, pady=dd_set_pady)
    
        y_title_2_e = Entry(field_loc, textvariable = y_title_2, width=text_width)
        y_title_2_e.grid(row=0, column=5,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_2_e.delete(0, END)
        y_title_2_e.insert(0, Var_Col_2.get())
    
        dd_box_plot_symbol_2 = ttk.Combobox(field_loc, textvariable=plot_symbol_2, values=plot_symbol_list)
        dd_box_plot_symbol_2.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_2.grid(row=0, column=6,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_2.delete(0, END)
        dd_box_plot_symbol_2.insert(0,"o")
        
        dd_box_plot_color_2 = ttk.Combobox(field_loc, textvariable=plot_color_2, values=plot_color_list)
        dd_box_plot_color_2.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_2.grid(row=0, column=7,padx=pad_x, pady=pad_y)
        dd_box_plot_color_2.delete(0, END)
        dd_box_plot_color_2.insert(0,"blue")
    
        # ======================Y VARIABLE 3==========================================

        dd_box_3 = ttk.Combobox(field_loc, textvariable=Var_Col_3, values=list(df_ax_1))
        dd_box_3.config(width=dd_y_width)
        dd_box_3.grid(row=1, column=0,padx=dd_set_padx, pady=dd_set_pady)
    
        y_title_3_e = Entry(field_loc, textvariable = y_title_3, width=text_width)
        y_title_3_e.grid(row=1, column=1,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_3_e.delete(0, END)
        y_title_3_e.insert(0, Var_Col_3.get())
    
        dd_box_plot_symbol_3 = ttk.Combobox(field_loc, textvariable=plot_symbol_3, values=plot_symbol_list)
        dd_box_plot_symbol_3.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_3.grid(row=1, column=2,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_3.delete(0, END)
        dd_box_plot_symbol_3.insert(0,"o")
        
        dd_box_plot_color_3 = ttk.Combobox(field_loc, textvariable=plot_color_3, values=plot_color_list)
        dd_box_plot_color_3.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_3.grid(row=1, column=3,padx=pad_x, pady=pad_y)
        dd_box_plot_color_3.delete(0, END)
        dd_box_plot_color_3.insert(0,"blue")
    
        # ======================Y VARIABLE 4==========================================

        dd_box_4 = ttk.Combobox(field_loc, textvariable=Var_Col_4, values=list(df_ax_1))
        dd_box_4.config(width=dd_y_width)
        dd_box_4.grid(row=1, column=4,padx=dd_set_padx, pady=dd_set_pady)
    
        y_title_4_e = Entry(field_loc, textvariable = y_title_4, width=text_width)
        y_title_4_e.grid(row=1, column=5,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_4_e.delete(0, END)
        y_title_4_e.insert(0, Var_Col_4.get())
    
        dd_box_plot_symbol_4 = ttk.Combobox(field_loc, textvariable=plot_symbol_4, values=plot_symbol_list)
        dd_box_plot_symbol_4.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_4.grid(row=1, column=6,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_4.delete(0, END)
        dd_box_plot_symbol_4.insert(0,"o")
        
        dd_box_plot_color_4 = ttk.Combobox(field_loc, textvariable=plot_color_4, values=plot_color_list)
        dd_box_plot_color_4.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_4.grid(row=1, column=7,padx=pad_x, pady=pad_y)
        dd_box_plot_color_4.delete(0, END)
        dd_box_plot_color_4.insert(0,"blue")
        
        # ======================Y VARIABLE 5==========================================
    
        dd_box_5 = ttk.Combobox(field_loc, textvariable=Var_Col_5, values=list(df_ax_1))
        dd_box_5.config(width=dd_y_width)
        dd_box_5.grid(row=2, column=0,padx=dd_set_padx, pady=dd_set_pady)
        
        y_title_5_e = Entry(field_loc, textvariable = y_title_5, width=text_width)
        y_title_5_e.grid(row=2, column=1,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_5_e.delete(0, END)
        y_title_5_e.insert(0, Var_Col_5.get())
        
        dd_box_plot_symbol_5 = ttk.Combobox(field_loc, textvariable=plot_symbol_5, values=plot_symbol_list)
        dd_box_plot_symbol_5.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_5.grid(row=2, column=2,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_5.delete(0, END)
        dd_box_plot_symbol_5.insert(0,"o")
        
        dd_box_plot_color_5 = ttk.Combobox(field_loc, textvariable=plot_color_5, values=plot_color_list)
        dd_box_plot_color_5.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_5.grid(row=2, column=3,padx=pad_x, pady=pad_y)
        dd_box_plot_color_5.delete(0, END)
        dd_box_plot_color_5.insert(0,"blue")
        
        # ======================Y VARIABLE 6======================================
    
        dd_box_6 = ttk.Combobox(field_loc, textvariable=Var_Col_6, values=list(df_ax_1))
        dd_box_6.config(width=dd_y_width)
        dd_box_6.grid(row=2, column=4,padx=dd_set_padx, pady=dd_set_pady)
        
        y_title_6_e = Entry(field_loc, textvariable = y_title_6, width=text_width)
        y_title_6_e.grid(row=2, column=5,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_6_e.delete(0, END)
        y_title_6_e.insert(0, Var_Col_6.get())
        
        dd_box_plot_symbol_6 = ttk.Combobox(field_loc, textvariable=plot_symbol_6, values=plot_symbol_list)
        dd_box_plot_symbol_6.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_6.grid(row=2, column=6,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_6.delete(0, END)
        dd_box_plot_symbol_6.insert(0,"o")
        
        dd_box_plot_color_6 = ttk.Combobox(field_loc, textvariable=plot_color_6, values=plot_color_list)
        dd_box_plot_color_6.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_6.grid(row=2, column=7,padx=pad_x, pady=pad_y)
        dd_box_plot_color_6.delete(0, END)
        dd_box_plot_color_6.insert(0,"blue")
    
        # ======================Y VARIABLE 7==========================================
    
        dd_box_7 = ttk.Combobox(field_loc, textvariable=Var_Col_7, values=list(df_ax_1))
        dd_box_7.config(width=dd_y_width)
        dd_box_7.grid(row=3, column=0,padx=dd_set_padx, pady=dd_set_pady)
        
        y_title_7_e = Entry(field_loc, textvariable = y_title_7, width=text_width)
        y_title_7_e.grid(row=3, column=1,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_7_e.delete(0, END)
        y_title_7_e.insert(0, Var_Col_7.get())
        
        dd_box_plot_symbol_7 = ttk.Combobox(field_loc, textvariable=plot_symbol_7, values=plot_symbol_list)
        dd_box_plot_symbol_7.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_7.grid(row=3, column=2,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_7.delete(0, END)
        dd_box_plot_symbol_7.insert(0,"o")
        
        dd_box_plot_color_7 = ttk.Combobox(field_loc, textvariable=plot_color_7, values=plot_color_list)
        dd_box_plot_color_7.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_7.grid(row=3, column=3,padx=pad_x, pady=pad_y)
        dd_box_plot_color_7.delete(0, END)
        dd_box_plot_color_7.insert(0,"blue")
        
        # ======================Y VARIABLE 8==========================================
    
        dd_box_8 = ttk.Combobox(field_loc, textvariable=Var_Col_8, values=list(df_ax_1))
        dd_box_8.config(width=dd_y_width)
        dd_box_8.grid(row=3, column=4,padx=dd_set_padx, pady=dd_set_pady)
        
        y_title_8_e = Entry(field_loc, textvariable = y_title_8, width=text_width)
        y_title_8_e.grid(row=3, column=5,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_8_e.delete(0, END)
        y_title_8_e.insert(0, Var_Col_8.get())
        
        dd_box_plot_symbol_8 = ttk.Combobox(field_loc, textvariable=plot_symbol_8, values=plot_symbol_list)
        dd_box_plot_symbol_8.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_8.grid(row=3, column=6,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_8.delete(0, END)
        dd_box_plot_symbol_8.insert(0,"o")
        
        dd_box_plot_color_8 = ttk.Combobox(field_loc, textvariable=plot_color_8, values=plot_color_list)
        dd_box_plot_color_8.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_8.grid(row=3, column=7,padx=pad_x, pady=pad_y)
        dd_box_plot_color_8.delete(0, END)
        dd_box_plot_color_8.insert(0,"blue")
        
        # ======================Y VARIABLE 9==========================================
    
        dd_box_9 = ttk.Combobox(field_loc, textvariable=Var_Col_9, values=list(df_ax_1))
        dd_box_9.config(width=dd_y_width)
        dd_box_9.grid(row=4, column=0,padx=dd_set_padx, pady=dd_set_pady)
        
        y_title_9_e = Entry(field_loc, textvariable = y_title_9, width=text_width)
        y_title_9_e.grid(row=4, column=1,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_9_e.delete(0, END)
        y_title_9_e.insert(0, Var_Col_9.get())
    
        dd_box_plot_symbol_9 = ttk.Combobox(field_loc, textvariable=plot_symbol_9, values=plot_symbol_list)
        dd_box_plot_symbol_9.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_9.grid(row=4, column=2,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_9.delete(0, END)
        dd_box_plot_symbol_9.insert(0,"o")
        
        dd_box_plot_color_9 = ttk.Combobox(field_loc, textvariable=plot_color_9, values=plot_color_list)
        dd_box_plot_color_9.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_9.grid(row=4, column=3,padx=pad_x, pady=pad_y)
        dd_box_plot_color_9.delete(0, END)
        dd_box_plot_color_9.insert(0,"blue")
        
        # ======================Y VARIABLE 10=========================================
        
        dd_box_10 = ttk.Combobox(field_loc, textvariable=Var_Col_10, values=list(df_ax_1))
        dd_box_10.config(width=dd_y_width)
        dd_box_10.grid(row=4, column=4,padx=dd_set_padx, pady=dd_set_pady)
    
        y_title_10_e = Entry(field_loc, textvariable = y_title_10, width=text_width)
        y_title_10_e.grid(row=4, column=5,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_10_e.delete(0, END)
        y_title_10_e.insert(0, Var_Col_10.get())

        dd_box_plot_symbol_10 = ttk.Combobox(field_loc, textvariable=plot_symbol_10, values=plot_symbol_list)
        dd_box_plot_symbol_10.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_10.grid(row=4, column=6,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_10.delete(0, END)
        dd_box_plot_symbol_10.insert(0,"o")
        
        dd_box_plot_color_10 = ttk.Combobox(field_loc, textvariable=plot_color_10, values=plot_color_list)
        dd_box_plot_color_10.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_10.grid(row=4, column=7,padx=pad_x, pady=pad_y)
        dd_box_plot_color_10.delete(0, END)
        dd_box_plot_color_10.insert(0,"blue")

    else:
        
        for x in range(0,3):
            if axis_2_dataframe.get()==df_select_list[x]:
                df_ax_2 = df_axis[x]
        
        field_loc = yaxis_lf_1
    
        # ======================Y VARIABLE 1_1================================

        dd_box_1_1 = ttk.Combobox(field_loc, textvariable=Var_Col_1_1, values=list(df_ax_2))
        dd_box_1_1.config(width=dd_y_width)
        dd_box_1_1.grid(row=0, column=0,padx=dd_set_padx, pady=dd_set_pady)
    
        y_title_1_1_e = Entry(field_loc, textvariable = y_title_1_1, width=text_width)
        y_title_1_1_e.grid(row=0, column=1,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_1_1_e.delete(0, END)
        y_title_1_1_e.insert(0, Var_Col_1_1.get())
    
        dd_box_plot_symbol_1_1 = ttk.Combobox(field_loc, textvariable=plot_symbol_1_1, values=plot_symbol_list)
        dd_box_plot_symbol_1_1.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_1_1.grid(row=0, column=2,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_1_1.delete(0, END)
        dd_box_plot_symbol_1_1.insert(0,"o")
        
        dd_box_plot_color_1_1 = ttk.Combobox(field_loc, textvariable=plot_color_1_1, values=plot_color_list)
        dd_box_plot_color_1_1.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_1_1.grid(row=0, column=3,padx=pad_x, pady=pad_y)
        dd_box_plot_color_1_1.delete(0, END)
        dd_box_plot_color_1_1.insert(0,"blue")

        # ======================Y VARIABLE 2_1================================

        dd_box_2_1_1 = ttk.Combobox(field_loc, textvariable=Var_Col_2_1, values=list(df_ax_2))
        dd_box_2_1_1.config(width=dd_y_width)
        dd_box_2_1_1.grid(row=0, column=4,padx=dd_set_padx, pady=dd_set_pady)
    
        y_title_2_1_e = Entry(field_loc, textvariable = y_title_2_1, width=text_width)
        y_title_2_1_e.grid(row=0, column=5,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_2_1_e.delete(0, END)
        y_title_2_1_e.insert(0, Var_Col_2_1.get())
    
        dd_box_plot_symbol_2 = ttk.Combobox(field_loc, textvariable=plot_symbol_2_1, values=plot_symbol_list)
        dd_box_plot_symbol_2.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_2.grid(row=0, column=6,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_2.delete(0, END)
        dd_box_plot_symbol_2.insert(0,"o")
        
        dd_box_plot_color_2_1 = ttk.Combobox(field_loc, textvariable=plot_color_2_1, values=plot_color_list)
        dd_box_plot_color_2_1.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_2_1.grid(row=0, column=7,padx=pad_x, pady=pad_y)
        dd_box_plot_color_2_1.delete(0, END)
        dd_box_plot_color_2_1.insert(0,"blue")
    
        # ======================Y VARIABLE 3_1====================================

        dd_box_3_1 = ttk.Combobox(field_loc, textvariable=Var_Col_3_1, values=list(df_ax_2))
        dd_box_3_1.config(width=dd_y_width)
        dd_box_3_1.grid(row=1, column=0,padx=dd_set_padx, pady=dd_set_pady)
    
        y_title_3_1_e = Entry(field_loc, textvariable = y_title_3_1, width=text_width)
        y_title_3_1_e.grid(row=1, column=1,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_3_1_e.delete(0, END)
        y_title_3_1_e.insert(0, Var_Col_3_1.get())
    
        dd_box_plot_symbol_3_1 = ttk.Combobox(field_loc, textvariable=plot_symbol_3_1, values=plot_symbol_list)
        dd_box_plot_symbol_3_1.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_3_1.grid(row=1, column=2,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_3_1.delete(0, END)
        dd_box_plot_symbol_3_1.insert(0,"o")
        
        dd_box_plot_color_3_1 = ttk.Combobox(field_loc, textvariable=plot_color_3_1, values=plot_color_list)
        dd_box_plot_color_3_1.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_3_1.grid(row=1, column=3,padx=pad_x, pady=pad_y)
        dd_box_plot_color_3_1.delete(0, END)
        dd_box_plot_color_3_1.insert(0,"blue")
    
        # ======================Y VARIABLE 4_1================================

        dd_box_4_1 = ttk.Combobox(field_loc, textvariable=Var_Col_4_1, values=list(df_ax_2))
        dd_box_4_1.config(width=dd_y_width)
        dd_box_4_1.grid(row=1, column=4,padx=dd_set_padx, pady=dd_set_pady)
    
        y_title_4_1_e = Entry(field_loc, textvariable = y_title_4_1, width=text_width)
        y_title_4_1_e.grid(row=1, column=5,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_4_1_e.delete(0, END)
        y_title_4_1_e.insert(0, Var_Col_4_1.get())
    
        dd_box_plot_symbol_4_1 = ttk.Combobox(field_loc, textvariable=plot_symbol_4_1, values=plot_symbol_list)
        dd_box_plot_symbol_4_1.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_4_1.grid(row=1, column=6,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_4_1.delete(0, END)
        dd_box_plot_symbol_4_1.insert(0,"o")
        
        dd_box_plot_color_4_1 = ttk.Combobox(field_loc, textvariable=plot_color_4_1, values=plot_color_list)
        dd_box_plot_color_4_1.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_4_1.grid(row=1, column=7,padx=pad_x, pady=pad_y)
        dd_box_plot_color_4_1.delete(0, END)
        dd_box_plot_color_4_1.insert(0,"blue")
        
        # ======================Y VARIABLE 5_1=================================
    
        dd_box_5_1 = ttk.Combobox(field_loc, textvariable=Var_Col_5_1, values=list(df_ax_2))
        dd_box_5_1.config(width=dd_y_width)
        dd_box_5_1.grid(row=2, column=0,padx=dd_set_padx, pady=dd_set_pady)
        
        y_title_5_1_e = Entry(field_loc, textvariable = y_title_5_1, width=text_width)
        y_title_5_1_e.grid(row=2, column=1,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_5_1_e.delete(0, END)
        y_title_5_1_e.insert(0, Var_Col_5_1.get())
        
        dd_box_plot_symbol_5_1 = ttk.Combobox(field_loc, textvariable=plot_symbol_5_1, values=plot_symbol_list)
        dd_box_plot_symbol_5_1.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_5_1.grid(row=2, column=2,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_5_1.delete(0, END)
        dd_box_plot_symbol_5_1.insert(0,"o")
        
        dd_box_plot_color_5_1 = ttk.Combobox(field_loc, textvariable=plot_color_5_1, values=plot_color_list)
        dd_box_plot_color_5_1.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_5_1.grid(row=2, column=3,padx=pad_x, pady=pad_y)
        dd_box_plot_color_5_1.delete(0, END)
        dd_box_plot_color_5_1.insert(0,"blue")
        
        # ======================Y VARIABLE 6_1==============================
    
        dd_box_6_1 = ttk.Combobox(field_loc, textvariable=Var_Col_6_1, values=list(df_ax_2))
        dd_box_6_1.config(width=dd_y_width)
        dd_box_6_1.grid(row=2, column=4,padx=dd_set_padx, pady=dd_set_pady)
        
        y_title_6_1_e = Entry(field_loc, textvariable = y_title_6_1, width=text_width)
        y_title_6_1_e.grid(row=2, column=5,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_6_1_e.delete(0, END)
        y_title_6_1_e.insert(0, Var_Col_6_1.get())
        
        dd_box_plot_symbol_6_1 = ttk.Combobox(field_loc, textvariable=plot_symbol_6_1, values=plot_symbol_list)
        dd_box_plot_symbol_6_1.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_6_1.grid(row=2, column=6,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_6_1.delete(0, END)
        dd_box_plot_symbol_6_1.insert(0,"o")
        
        dd_box_plot_color_6_1 = ttk.Combobox(field_loc, textvariable=plot_color_6_1, values=plot_color_list)
        dd_box_plot_color_6_1.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_6_1.grid(row=2, column=7,padx=pad_x, pady=pad_y)
        dd_box_plot_color_6_1.delete(0, END)
        dd_box_plot_color_6_1.insert(0,"blue")
    
        # ======================Y VARIABLE 7_1=================================
    
        dd_box_7_1 = ttk.Combobox(field_loc, textvariable=Var_Col_7_1, values=list(df_ax_2))
        dd_box_7_1.config(width=dd_y_width)
        dd_box_7_1.grid(row=3, column=0,padx=dd_set_padx, pady=dd_set_pady)
        
        y_title_7_1_e = Entry(field_loc, textvariable = y_title_7_1, width=text_width)
        y_title_7_1_e.grid(row=3, column=1,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_7_1_e.delete(0, END)
        y_title_7_1_e.insert(0, Var_Col_7_1.get())
        
        dd_box_plot_symbol_7_1 = ttk.Combobox(field_loc, textvariable=plot_symbol_7_1, values=plot_symbol_list)
        dd_box_plot_symbol_7_1.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_7_1.grid(row=3, column=2,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_7_1.delete(0, END)
        dd_box_plot_symbol_7_1.insert(0,"o")
        
        dd_box_plot_color_7_1 = ttk.Combobox(field_loc, textvariable=plot_color_7_1, values=plot_color_list)
        dd_box_plot_color_7_1.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_7_1.grid(row=3, column=3,padx=pad_x, pady=pad_y)
        dd_box_plot_color_7_1.delete(0, END)
        dd_box_plot_color_7_1.insert(0,"blue")
        
        # ======================Y VARIABLE 8_1================================
    
        dd_box_8_1 = ttk.Combobox(field_loc, textvariable=Var_Col_8_1, values=list(df_ax_2))
        dd_box_8_1.config(width=dd_y_width)
        dd_box_8_1.grid(row=3, column=4,padx=dd_set_padx, pady=dd_set_pady)
        
        y_title_8_1_e = Entry(field_loc, textvariable = y_title_8_1, width=text_width)
        y_title_8_1_e.grid(row=3, column=5,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_8_1_e.delete(0, END)
        y_title_8_1_e.insert(0, Var_Col_8_1.get())
        
        dd_box_plot_symbol_8_1 = ttk.Combobox(field_loc, textvariable=plot_symbol_8_1, values=plot_symbol_list)
        dd_box_plot_symbol_8_1.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_8_1.grid(row=3, column=6,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_8_1.delete(0, END)
        dd_box_plot_symbol_8_1.insert(0,"o")
        
        dd_box_plot_color_8_1 = ttk.Combobox(field_loc, textvariable=plot_color_8_1, values=plot_color_list)
        dd_box_plot_color_8_1.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_8_1.grid(row=3, column=7,padx=pad_x, pady=pad_y)
        dd_box_plot_color_8_1.delete(0, END)
        dd_box_plot_color_8_1.insert(0,"blue")
        
        # ======================Y VARIABLE 9_1================================
    
        dd_box_9_1 = ttk.Combobox(field_loc, textvariable=Var_Col_9_1, values=list(df_ax_2))
        dd_box_9_1.config(width=dd_y_width)
        dd_box_9_1.grid(row=4, column=0,padx=dd_set_padx, pady=dd_set_pady)
        
        y_title_9_1_e = Entry(field_loc, textvariable = y_title_9_1, width=text_width)
        y_title_9_1_e.grid(row=4, column=1,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_9_1_e.delete(0, END)
        y_title_9_1_e.insert(0, Var_Col_9_1.get())
    
        dd_box_plot_symbol_9_1 = ttk.Combobox(field_loc, textvariable=plot_symbol_9_1, values=plot_symbol_list)
        dd_box_plot_symbol_9_1.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_9_1.grid(row=4, column=2,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_9_1.delete(0, END)
        dd_box_plot_symbol_9_1.insert(0,"o")
        
        dd_box_plot_color_9_1 = ttk.Combobox(field_loc, textvariable=plot_color_9_1, values=plot_color_list)
        dd_box_plot_color_9_1.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_9_1.grid(row=4, column=3,padx=pad_x, pady=pad_y)
        dd_box_plot_color_9_1.delete(0, END)
        dd_box_plot_color_9_1.insert(0,"blue")
        
        # ======================Y VARIABLE 10_1===============================
        
        dd_box_10_1 = ttk.Combobox(field_loc, textvariable=Var_Col_10_1, values=list(df_ax_2))
        dd_box_10_1.config(width=dd_y_width)
        dd_box_10_1.grid(row=4, column=4,padx=dd_set_padx, pady=dd_set_pady)
    
        y_title_10_1_e = Entry(field_loc, textvariable = y_title_10_1, width=text_width)
        y_title_10_1_e.grid(row=4, column=5,padx=pad_x, pady=pad_y, sticky='nesw')
        y_title_10_1_e.delete(0, END)
        y_title_10_1_e.insert(0, Var_Col_10_1.get())

        dd_box_plot_symbol_10_1 = ttk.Combobox(field_loc, textvariable=plot_symbol_10_1, values=plot_symbol_list)
        dd_box_plot_symbol_10_1.config(width=symbol_width,justify='center')
        dd_box_plot_symbol_10_1.grid(row=4, column=6,padx=pad_x, pady=pad_y)
        dd_box_plot_symbol_10_1.delete(0, END)
        dd_box_plot_symbol_10_1.insert(0,"o")
        
        dd_box_plot_color_10_1 = ttk.Combobox(field_loc, textvariable=plot_color_10_1, values=plot_color_list)
        dd_box_plot_color_10_1.config(width=2*symbol_width,justify='center')
        dd_box_plot_color_10_1.grid(row=4, column=7,padx=pad_x, pady=pad_y)
        dd_box_plot_color_10_1.delete(0, END)
        dd_box_plot_color_10_1.insert(0,"blue")

# =========================================================================

# ============================================================================
# ====================Buttons=================================================
# ============================================================================
btns_padx = 5 #int(root.winfo_width())
btns_pady = 5

open_file_btn = Button(start_lf, text="Load File", command=lambda: open_file(0), width=12, bg=back_color, fg=forg_color,bd=4)
open_file_btn.grid(row=0, column=0, padx=btns_padx, pady=btns_pady)

create_folder_btn = Button(start_lf, text="New Folder", command=create_folder_window, width=12, bg=back_color, fg=forg_color,bd=4)
create_folder_btn.grid(row=0, column=1, padx=btns_padx, pady=btns_pady)

save_plot_btn = Button(start_lf, text="Save Plot", command =save_plot_window, width=12, bg=back_color, fg=forg_color,bd=4)
save_plot_btn.grid(row=0, column=2, padx=btns_padx, pady=btns_pady)

save_dataframe_csv_btn = Button(start_lf, text="Save Dataframe", command=save_dataframe_csv_window, width=12, bg=back_color, fg=forg_color,bd=4)
save_dataframe_csv_btn.grid(row=0, column=3, padx=btns_padx, pady=btns_pady)

save_subset_csv_btn = Button(start_lf, text="Save Subset", command=save_dataframe_csv_window, width=12, bg=back_color, fg=forg_color,bd=4)
save_subset_csv_btn.grid(row=0, column=4, padx=btns_padx, pady=btns_pady)


exit_btn = Button(start_lf, text="Exit", command=exit_program, width=12, bg=back_color, fg=forg_color,bd=4)
exit_btn.grid(row=0, column=5, padx=btns_padx, pady=btns_pady)

# ===========================END START BUTTONS================================



root.mainloop()