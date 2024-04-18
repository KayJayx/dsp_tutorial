import controls as cc
import tkinter as tk
import numpy as np
import typing
import math

def KeyPressEventHandler(sender: typing.Any, app: typing.Any, user: typing.Any) -> None:

    # Extract stuff from user data
    plot: cc.Plot = user[0]
    line_series   = user[1]

    # Add a sine wave
    x = [t for t in range(0, 101)]
    y = [10 * np.sin(2 * np.pi * 1 * t) for t in x]

    print(x)
    print(y)

    cc.dpg.configure_item(line_series, x=x, y=y)

def main():

    # We need the tkinter library in order to get the window
    # screen width and height
    root          = tk.Tk()
    screen_width  = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() - 155

    # In order to make successful calls to the Dear PyGUI framework we must 
    # establish a context where we can make calls to that code
    cc.dpg.create_context()

    # Set the theme of the application
    cc.SetGlobalTheme()

    # Add the window and controls here
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Create the main window
    main_window = cc.Window()
    main_window.ChangeWindowPadding(window_pad=[0, 0], frame_pad=[0, 0], item_spacing=[0, 0])
    main_window.BindTheme()

    # Create a plot and add it to the window
    time_plot = cc.Plot(label="Amplitude vs. Time", height=500, width=-1, parent=main_window)
    time_plot.AddPlot(x_label="Time", y_label="Amplitude")
    time_plot.SetPlotLineColor(color=[36, 183, 199], theme_component=time_plot.line_theme_component)
    time_plot.BindTheme()
    time_plot.SetAxisLimits(time_plot.x_axis, 0, 100)

    # Add the line series plot here
    line_series = cc.dpg.add_line_series(x=[0], y=[0], parent=time_plot.x_axis)

    # Setup the key board for key presses
    keyboard = cc.Keyboard()
    keyboard.RegisterKeyPressEventHandler(user_data=[time_plot, line_series], callback=KeyPressEventHandler)
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    # Set a primary window which will always be drawn in the background
    cc.dpg.set_primary_window(main_window.tag, True)

    # This is technically the main window of the application
    # Call the viewport function which actually creates the window through the 
    # operating system followed by some other setup functions
    cc.dpg.create_viewport(
        title="DSP Tutorial",
        x_pos=0, y_pos=0,
        width=screen_width,
        height=screen_height,
        max_width=screen_width,
        max_height=screen_height + 155,
        min_width=screen_width,
        min_height=screen_height
    )
    cc.dpg.setup_dearpygui()

    # Show the main window created by the operating system
    cc.dpg.show_viewport()

    # Main loop
    while cc.dpg.is_dearpygui_running():

        # Render the GUI frame
        cc.dpg.render_dearpygui_frame()

    # Destroy the Dear PyGUI context
    cc.dpg.destroy_context()

    return 0

if __name__ == "__main__": main()