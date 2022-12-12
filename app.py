''' Python file to connect HTML using Flask '''

import os
from flask import Flask,render_template,request
import numpy as np
import sklearn
import pickle
import pandas as pd

from werkzeug.utils import secure_filename
from autoviz.AutoViz_Class import AutoViz_Class 

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')

@app.route('/getVisualization', methods=['GET', 'POST'])
def getVisualization():
    if request.method == 'POST':
        fname = request.files['fname']
        rownum = request.form['rownum']

        # Saving the CSV file 
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, (fname.filename))
        fname.save(file_path)

        #Autoviz
        AV = AutoViz_Class() #instantiaze the AV  

        # %matplotlib inline - To run on Jupyter
        
        # Storing the name of the file in 'filename'               
        filename = fname.filename

        # Converting rownum from 'string' to 'int'
        rownum = int(rownum) 


        ''' Saving plots in HTML File : 
            KDE, cat_plots, distplot, heatmaps,
            pair_scatters,violin_plots 
        '''
        dft = AV.AutoViz(
            filename,
            sep=",",
            depVar="",
            dfte=None,
            header=rownum,
            verbose=2,
            lowess=False,
            chart_format="html",
            max_rows_analyzed=500000,
            max_cols_analyzed=100, 
            save_plot_dir='templates'
        ) 
        '''
        dft = AV.AutoViz(
            filename,
            sep=",",
            depVar="",
            dfte=None,
            header=rownum,
            verbose=2,
            lowess=False, 
            chart_format="svg",
            max_rows_analyzed=500000,
            max_cols_analyzed=100,
            save_plot_dir='templates'
        )
        '''
        f = 'File : '
        filename = f + filename
        heat = 'heatmaps'
        dist = 'distplots'
        cat = 'categorical var plots'
        pair = 'pair scatter plots'
        vio = 'violinplots'
        return render_template('visualization.html',a = filename,h = heat,d = dist,c = cat, p = pair, v = vio)

# Rendering the plots HTML page
@app.route('/heatmaps')
def heatmaps():
    return render_template('AutoViz/heatmaps.html')

@app.route('/catvarplots')
def catvarplots():
    return render_template('AutoViz/cat_var_plots.html')

@app.route('/distplots')
def distplots():
    return render_template('AutoViz/distplots_nums.html')

@app.route('/pairscatters')
def pairscatters():
    return render_template('AutoViz/pair_scatters.html')

@app.route('/violinplots')
def violinplots():
    return render_template('AutoViz/violinplots.html')


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
