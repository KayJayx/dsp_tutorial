import controls as cc
import tkinter as tk
import numpy as np
import typing
import os
import threading

def StartButtonEventHandler(sender: typing.Any, app: typing.Any, user: typing.Any) -> None:

    generate_waveform: threading.Event = user
    generate_waveform.set()

def StopButtonEventHandler(sender: typing.Any, app: typing.Any, user: typing.Any) -> None:

    generate_waveform: threading.Event = user
    generate_waveform.clear()

def ClearPlotButtonEventHandler(sender: typing.Any, app: typing.Any, user: typing.Any) -> None:

    clear_plots: threading.Event = user
    clear_plots.set()

def main():

    # State variables
    generate_waveform = threading.Event()
    clear_plots       = threading.Event()
    length_of_plot    = 1

    # We need the tkinter library in order to get the window
    # screen width and height
    root          = tk.Tk()
    screen_width  = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() - 155 if os.name == "posix" else root.winfo_screenheight() - 50

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
    plot_window_width  = screen_width - 600
    plot_window_height = screen_height if os.name == "posix" else screen_height - 40
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
    time_plot.SetAxisLimits(time_plot.x_axis, 0, length_of_plot)
    time_plot.SetAxisLimits(time_plot.y_axis, -5, 5)
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
    control_window_width  = screen_width - plot_window_width if os.name == "posix" else screen_width - plot_window_width - 16
    control_window_height = plot_window_height
    control_window = cc.ChildWindow(width=control_window_width, height=control_window_height, parent=main_window, pos=[plot_window_width, 0], no_scrollbar=True)

    # Create a label to show the controls
    group1         = cc.Group(parent=control_window, pos=[0, 0])
    group1.ChangeGroupPadding(window_pad=[0, 0], frame_pad=[10, 10], item_spacing=[0, 0])
    group1.BindTheme()
    controls_label = cc.Label(label="   Controls", parent=group1)
    separator      = cc.LineSeparator(parent=group1)

    # Create buttons for generating, stoping and clearing the waveform
    group2 = cc.Group(parent=control_window, pos=[0, 35])
    generate_waveform_button = cc.Button(
        label="Generate Waveform",
        width=140, height=30,
        parent=group2,
        callback=StartButtonEventHandler,
        user_data=generate_waveform,
        pos=[20, 50]
    )
    stop_waveform_button = cc.Button(
        label="Stop Waveform Generation",
        width=180, height=30,
        parent=group2,
        callback=StopButtonEventHandler,
        user_data=generate_waveform,
        pos=[generate_waveform_button.GetPosition()[0] + generate_waveform_button.GetWidth() + 20, generate_waveform_button.GetPosition()[1]]
    )
    clear_plot_button = cc.Button(
        label="Clear Plots",
        width=140, height=30,
        parent=group2,
        callback=ClearPlotButtonEventHandler,
        user_data=clear_plots,
        pos=[stop_waveform_button.GetPosition()[0] + stop_waveform_button.GetWidth() + 20, stop_waveform_button.GetPosition()[1]]
    )

    # Create sliders to change the waveform
    group3 = cc.Group(parent=control_window, pos=[0, 90])
    resolution_slider = cc.Slider(type=int, label="Change Samples", width=140, height=100, parent=group3, pos=[20, 90], min_value=1, max_value=2500, default_value=101)
    amplitude_slider  = cc.Slider(type=float, label="Change Amplitude", width=140, height=100, parent=group3, pos=[20, 110], min_value=1.0, max_value=5.0, default_value=1.0)
    height_slider     = cc.Slider(type=float, label="Change Height", width=140, height=100, parent=group3, pos=[20, 130], min_value=-5.0, max_value=5.0, default_value=0.0)
    phase_slider      = cc.Slider(type=float, label="Change Phase", width=140, height=100, parent=group3, pos=[20, 150], min_value=-10.0, max_value=10.0, default_value=0.0)
    frequency_slider  = cc.Slider(type=float, label="Change Frequency", width=140, height=100, parent=group3, pos=[20, 170], min_value=1.0, max_value=200.0, default_value=1.0)
    angular_label     = cc.Label(label=f"Angular Freq: {'{:.3f}'.format(2 * np.pi * frequency_slider.GetSliderValue())}", parent=group3, pos=[20, 190])
    period_label      = cc.Label(label=f"Period: {'{:.3f}'.format(1 / frequency_slider.GetSliderValue())}", parent=group3, pos=[20, 210])
    frequency_slider.SetSliderCallback(
        callback=lambda sender, app, user : (
            angular_label.SetLabel(f"Angular Freq: {'{:.3f}'.format(2 * np.pi * frequency_slider.GetSliderValue())}"),
            period_label.SetLabel(f"Period: {'{:.3f}'.format(1 / frequency_slider.GetSliderValue())}")
        )
    )
    normalize_freq    = cc.CheckBox(label="Normalize Frequency", parent=group3, pos=[20, 230])
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
        max_height=screen_height + 155 if os.name == "posix" else screen_height,
        min_width=screen_width,
        min_height=screen_height
    )
    cc.dpg.setup_dearpygui()

    # Show the main window created by the operating system
    cc.dpg.show_viewport()

    # Main loop
    while cc.dpg.is_dearpygui_running():

        # Clear the plots here
        if clear_plots.is_set():
            clear_plots.clear()
            cc.dpg.configure_item(time_line_series, x=[0], y=[0])

        # If the generate waveform is set start populating the plots
        if generate_waveform.is_set():

            # Add the algorithm stuff here
            #*****************************************************************
            # DSP Notes
            # Sample Rate: Rate at which you sample a signal measured in second per samples (like the period)
            # Sampling Frequency: The inverse of the sampling rate measured in samples per second

            samples   = resolution_slider.GetSliderValue()
            x_data    = np.linspace(0, length_of_plot, samples, endpoint=True)
            amplitude = amplitude_slider.GetSliderValue()
            height    = height_slider.GetSliderValue()
            phase     = phase_slider.GetSliderValue()
            frequency = frequency_slider.GetSliderValue()
            if normalize_freq.IsChecked():
                y_data = [(amplitude * np.sin(((2 * np.pi * frequency * x) / samples) + phase)) + height for x in x_data]
            else:
                # Digital representation of what would be an analog signal, where samples represents the
                # total number of inputs into my function
                y_data = [(amplitude * np.sin(((2 * np.pi * frequency * x)) + phase)) + height for x in x_data]
            #*****************************************************************

            # Plot the data
            cc.dpg.configure_item(time_line_series, x=x_data, y=y_data)

        # Render the GUI frame
        cc.dpg.render_dearpygui_frame()

    # Destroy the Dear PyGUI context
    cc.dpg.destroy_context()

    return 0

if __name__ == "__main__": main()