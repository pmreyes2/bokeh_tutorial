"""
usage:
$ bokeh serve bokeh_app_01.py --port XXXX
"""
import bokeh
import bokeh.plotting
import numpy as np

p = bokeh.plotting.figure(plot_width=200, plot_height=200,x_range=(0,4),y_range=(0,4))

data_source = bokeh.models.ColumnDataSource(dict(image=[[[1,3.],[2,4]],
                                                        [[1,3.,2],[1,2,4],[3,3,2]],
                                                       ],
                                                 x=[0,2],
                                                 dw=[2,2],
                                                 y=[0,2],
                                                 dh=[2,2]))

p.image(image="image", x="x", dw="dw", y="y", dh="dh",source = data_source)

def button_pressed():
    print("Button Pressed")
    data_source.data.update(dict(image=[np.random.random((2,2)),
                                        np.random.random((3,3))]))

button = bokeh.models.Button(label="Modify Data")
button.on_click(button_pressed)

layout = bokeh.layouts.row(p,button)
doc = bokeh.plotting.curdoc()
doc.add_root(layout)