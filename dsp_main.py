import controls as cc
import tkinter as tk
import numpy as np
import typing

def StartButtonEventHandler(sender: typing.Any, app: typing.Any, user: typing.Any) -> None:

    # 
    pass

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

    # Create a window just for the plots
    plot_window_width  = screen_width - 800
    plot_window_height = screen_height - 40
    plot_window = cc.ChildWindow(width=plot_window_width, height=plot_window_height, parent=main_window, pos=[0, 0], no_scrollbar=True)

    # Create a time-domain plot and add it to the window
    x_label = "Time"
    y_label = "Amplitude"
    time_plot = cc.Plot(
        label=f"{y_label} vs. {x_label}",
        width=plot_window_width,
        height=int(plot_window_height / 2),
        parent=plot_window,
        pos=[0, 0]
    )
    time_plot.AddPlot(x_label=x_label, y_label=y_label)
    time_plot.SetPlotLineColor(color=[36, 183, 199], theme_component=time_plot.line_theme_component)
    time_plot.BindTheme()
    time_plot.SetAxisLimits(time_plot.x_axis, 0, 100)
    time_line_series = cc.dpg.add_line_series(x=[0], y=[0], parent=time_plot.x_axis)

    # Create a frequency-domain plot and add it to the window
    x_label = "Frequency"
    y_label = "Intensity"
    freq_plot = cc.Plot(
        label=f"{y_label} vs. {x_label}",
        width=plot_window_width,
        height=int(plot_window_height / 2),
        parent=plot_window,
        pos=[0, time_plot.GetPosition()[1] + time_plot.GetHeight()]
    )
    freq_plot.AddPlot(x_label=x_label, y_label=y_label)
    freq_plot.SetPlotLineColor(color=[36, 183, 199], theme_component=freq_plot.line_theme_component)
    freq_plot.BindTheme()
    freq_line_series = cc.dpg.add_line_series(x=[0], y=[0], parent=freq_plot.x_axis)

    # Create a window for the controls
    control_window_width  = screen_width - plot_window_width - 16
    control_window_height = plot_window_height
    control_window = cc.ChildWindow(width=control_window_width, height=control_window_height, parent=main_window, pos=[plot_window_width, 0], no_scrollbar=True)
    control_group  = cc.Group(width=control_window_width, height=control_window_height, parent=control_window, pos=[0, 0])
    control_group.ChangeGroupPadding(window_pad=[0, 0], frame_pad=[10, 10], item_spacing=[0, 0])
    control_group.BindTheme()

    # Create a label to show the controls
    controls_label = cc.Label(label="   Controls", parent=control_group)
    separator      = cc.LineSeparator(parent=control_group)

    # Create a button to generate a waveform
    generate_waveform_button = cc.Button(
        label="Generate Waveform",
        width=140, height=30,
        parent=control_group,
        pos=[30, 30]
    )
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

    curr_count = 0
    prev_count = 0

    # Main loop
    while cc.dpg.is_dearpygui_running():

        """
        curr_count = len(incoming_data)
        if curr_count != prev_count:

            x = incoming_data
            y = [np.sin(t) for t in x]

            cc.dpg.configure_item(line_series, x=x, y=y)
            cc.dpg.fit_axis_data(time_plot.y_axis)

            prev_count = curr_count
        """

        # Render the GUI frame
        cc.dpg.render_dearpygui_frame()

    # Destroy the Dear PyGUI context
    cc.dpg.destroy_context()

    return 0

if __name__ == "__main__": main()