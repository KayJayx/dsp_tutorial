#************************************************************************************
#   This code acts as a wrapper for the DearPyGUI framework, to more easily make
#   calls to the API in a module way.
#************************************************************************************
from __future__ import annotations
import dearpygui.dearpygui as dpg
import typing

def SetGlobalFont(font_file_path: str, font_size: int) -> None:
    """
    Sets the font for the entire application
    """

    # Set the font for the entire application here using one of Google's font libraries
    # Create a font registry
    with dpg.font_registry():

        # Load the font file
        dpg.add_font(font_file_path, font_size)

    # Update the font for the whole application
    dpg.bind_font(dpg.last_item())

def SetGlobalTheme() -> None:
    """
    Sets the theme for the entire application
    Hardcoded for now!!
    """

    # Modify the theme and control layout to desired values
    global_theme = dpg.add_theme()

    # This sets the theme for all controls
    with dpg.theme_component(dpg.mvAll, parent=global_theme):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding,     4,      category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_GrabRounding,      4,      category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_ScrollbarRounding, 9,      category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize,  0,      category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize,   0,      category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding,     0,   0, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding,      0,   0, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing,       0,   0, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize,     16,     category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_GrabMinSize,       14,     category=dpg.mvThemeCat_Core)

    # I believe this sets the theme for all input controls
    with dpg.theme_component(dpg.mvInputInt, parent=global_theme):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding,     4,      category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_GrabRounding,      4,      category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_ScrollbarRounding, 9,      category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize,  0,      category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize,   0,      category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding,     0,   0, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding,      0,   0, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing,       0,   0, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize,     16,     category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_GrabMinSize,       14,     category=dpg.mvThemeCat_Core)

    # Bind the modifications for all controls/windows
    dpg.bind_theme(global_theme)

class Mouse():

    """
    Gets information tied to the mouse
    """

    @staticmethod
    def GetMousePosition(local_to_window: bool = False) -> 'list[int]':
        """
        Gets the current mouse position on the screen
        """
        return dpg.get_mouse_pos(local=local_to_window)
    
    @staticmethod
    def GetMouseDragDelta() -> 'list[float]':
        """
        Get the mouse drag delta
        """
        return dpg.get_mouse_drag_delta()
    
class Keyboard():

    """
    Register Callbacks for Key presses.
    """

    @staticmethod
    def RegisterKeyPressEventHandler(key: int = -1, user_data: typing.Any = None, callback: typing.Any = None) -> None:
        with dpg.handler_registry():
            dpg.add_key_press_handler(key=key, user_data=user_data, callback=callback)

    @staticmethod
    def RegisterKeyDownEventHandler(key: int = -1, user_data: typing.Any = None, callback: typing.Any = None) -> None:
        with dpg.handler_registry():
            dpg.add_key_down_handler(key=key, user_data=user_data, callback=callback)

    @staticmethod
    def RegisterKeyReleaseEventHandler(key: int = -1, user_data: typing.Any = None, callback: typing.Any = None) -> None:
        with dpg.handler_registry():
            dpg.add_key_release_handler(key=key, user_data=user_data, callback=callback)

class Control():

    """
    Base class for all other control classes
    """

    def __init__(self, parent: Control) -> None:
        self.tag             = None
        self.theme           = dpg.add_theme()
        self.theme_component = None
        self.parent          = parent
        self.children        = []

        # Add self as a child to the parent
        if self.parent is not None and isinstance(self.parent, Control):
            self.parent.children.append(self)

    def Destroy(self) -> Control:
        """
        Destroy the control
        """
        dpg.delete_item(self.tag)

        return self

    def Enable(self) -> Control:
        """
        Enable the control
        """
        dpg.enable_item(self.tag)

        return self

    def Disable(self) -> Control:
        """
        Disable Control
        """
        dpg.disable_item(self.tag)

        return self

    def IsEnabled(self) -> bool:
        """
        Is control enabled
        """
        return dpg.is_item_enabled(self.tag)

    def Show(self) -> Control:
        """
        Show the window
        """
        dpg.show_item(self.tag)

        return self
        
    def Hide(self) -> Control:
        """
        Hide the window
        """
        dpg.hide_item(self.tag)

        return self

    def IsShown(self) -> bool:
        """
        Is control shown
        """
        return dpg.is_item_shown(self.tag)

    def GetPosition(self) -> 'list[int]':
        """
        Get the position of the control on the screen
        """
        return dpg.get_item_pos(self.tag)
    
    def SetPosition(self, pos: 'list[int]') -> Control:
        """
        Set the position of the control on the screen
        """
        dpg.set_item_pos(self.tag, pos)

        return self
    
    def GetWidth(self) -> int:
        """
        Gets the controls width
        """
        return dpg.get_item_width(self.tag)
    
    def GetHeight(self) -> int:
        """
        Gets the controls width
        """
        return dpg.get_item_height(self.tag)
    
    def GetValue(self) -> typing.Any:
        """
        Get the value of the control
        """
        return dpg.get_value(self.tag)
    
    def SetValue(self, value: typing.Any) -> Control:
        """
        Set the value of the control
        """
        dpg.set_value(self.tag, value=value)

        return self
    
    def SetDragCallback(self, callback: typing.Any) -> Control:
        """
        Set the drag callback for the item
        """
        dpg.set_item_drag_callback(self.tag, callback=callback)

        return self
    
    def SetDropCallback(self, callback: typing.Any) -> Control:
        """
        Set the drop callback for the item
        """
        dpg.set_item_drop_callback(self.tag, callback=callback)

        return self
    
    def SetCallback(self, callback: typing.Any) -> Control:
        """
        Set the callback for the item
        """
        dpg.set_item_callback(self.tag, callback=callback)

        return self
    
    def SetUserData(self, user_data: typing.Any) -> Control:
        """
        Set the user data for the item
        """
        dpg.set_item_user_data(self.tag, user_data=user_data)

        return self
    
    def ChangePadding(self, window_pad: 'list[int]', frame_pad: 'list[int]', item_spacing: 'list[int]') -> Control:
        """
        Change padding for the item
        """
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, window_pad[0],   window_pad[1],   category=dpg.mvThemeCat_Core, parent=self.theme_component)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding,  frame_pad[0],    frame_pad[1],    category=dpg.mvThemeCat_Core, parent=self.theme_component)
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing,   item_spacing[0], item_spacing[1], category=dpg.mvThemeCat_Core, parent=self.theme_component)

        return self
    
    def ChangeRounding(self, frame_rounding: int = 0) -> Control:
        """
        Change the rounding of the item
        """
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, frame_rounding, category=dpg.mvThemeCat_Core, parent=self.theme_component)

        return self
    
    def BindTheme(self) -> Control:
        """
        Binds the theme to the item
        """
        dpg.bind_item_theme(self.tag, self.theme)

        return self
    
class DragAndDropPayloadExtension(Control):

    """
    A class that encapsulates the drag and drop functionality
    """

    def __init__(self, label: str = None, drag_data: typing.Any = None, 
                 drop_data: typing.Any = None, user_data: typing.Any = None, 
                 payload_type: str = '$$DPG_PAYLOAD', parent: Control = None) -> None:
        super().__init__(parent=parent)
        self.tag = dpg.add_drag_payload(
            label=label,
            drag_data=drag_data,
            drop_data=drop_data,
            user_data=user_data,
            payload_type=payload_type,
            parent=self.parent.tag
        )

class Menu(Control):

    """
    Menu Control, creates a menu
    """

    def __init__(self, label: str = None, indent: int = -1, parent: Control = None) -> None:
        super().__init__(parent=parent)
        self.theme_component = dpg.add_theme_component(dpg.mvMenu, parent=self.theme)
        self.tag             = dpg.add_menu(
            label=label,
            indent=indent,
            parent=self.parent.tag
        )

    def AddMenuItem(self, label: str = None, callback: typing.Any = None, user_data: typing.Any = None) -> Menu:
        """
        Add menu item to the menu option
        """
        menu_item_tag = dpg.add_menu_item(
            label=label,
            parent=self.tag,
            callback=callback,
            user_data=user_data
        )

        # Create a menu item control on the fly and add it as child to this control
        self.children.append(Control(tag=menu_item_tag, label=label))

        return self
    
    def AddBorder(self, border_size: float = 0.6) -> Menu:
        """
        Add a border to the menu selection list
        """
        dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize, border_size, category=dpg.mvThemeCat_Core, parent=self.theme_component)

        return self

class MenuBar(Control):

    """
    Menu Bar Control, creates a menu bar control
    """

    def __init__(self, label: str = None, parent: Control = None) -> None:
        super().__init__(parent=parent)
        self.tag = dpg.add_menu_bar(
            label=label,
            parent=self.parent.tag
        )

    def AddMenu(self, label: str = None, indent: int = -1) -> Menu:
        """
        Add a menu to the menu bar
        """
        return Menu(label=label, indent=indent, parent=self)

class Tab(Control):

    """
    Tab Control, create a tab control
    """

    def __init__(self, label: str = None, indent: int = -1, parent: Control = None) -> None:
        super().__init__(parent=parent)
        self.tag = dpg.add_tab(
            label=label,
            indent=indent,
            parent=self.parent.tag
        )

class TabBar(Control):

    """
    Tab Bar Control, creates the tab bar control
    """

    def __init__(self, label: str = None, parent: Control = None) -> None:
        super().__init__(parent=parent)
        self.tag = dpg.add_tab_bar(
            label=label,
            parent=self.parent.tag
        )

    def AddTab(self, label: str = None, indent: int = -1) -> Tab:
        """
        Add a tab to the tab bar
        """
        return Tab(label=label, indent=indent, parent=self)

class CollapseHeader(Control):

    """
    Collapse Header Control, creates a collapse header control
    """

    def __init__(self, label: str = None, indent: int = -1, pos: 'list[int]' = [], parent: Control = None,
                 closable: bool = False, default_open: bool = False, open_on_double_click: bool = False,
                 open_on_arrow: bool = False, leaf: bool = False, bullet: bool = False) -> None:
        super().__init__(parent=parent)
        self.theme_component = dpg.add_theme_component(dpg.mvCollapsingHeader, parent=self.theme)
        self.tag             = dpg.add_collapsing_header(
            label=label,
            indent=indent,
            pos=pos,
            parent=self.parent.tag,
            closable=closable,
            default_open=default_open,
            open_on_double_click=open_on_double_click,
            open_on_arrow=open_on_arrow,
            leaf=leaf,
            bullet=bullet
        )

class Window(Control):

    """
    Window control, creates window
    """

    def __init__(self, label: str = None, width: int = 0, height: int = 0, 
                 pos: 'list[int]' = [], add_menubar: bool = False, min_size: 'list[int]' = [100, 100], 
                 max_size: 'list[int]' = [30000, 30000], collapsed: bool = False, autosize: bool = False,
                 no_resize: bool = False, no_title_bar: bool = False, no_move: bool = False,
                 no_scrollbar: bool = False, no_collapse: bool = False, horizontal_scrollbar: bool = False,
                 no_focus_on_appearing: bool = False, no_bring_to_front_on_focus: bool = False, 
                 no_close: bool = False, no_background: bool = False, modal: bool = False,
                 popup: bool = False, no_saved_settings: bool = False, 
                 no_open_over_existing_popup: bool = True, on_close: typing.Any = None) -> None:
        super().__init__(parent=None)
        self.theme_component = dpg.add_theme_component(dpg.mvWindowAppItem, parent=self.theme)
        self.tag             = dpg.add_window(
            label=label,
            width=width,
            height=height,
            pos=pos,
            menubar=add_menubar,
            min_size=min_size,
            max_size=max_size,
            collapsed=collapsed,
            autosize=autosize,
            no_resize=no_resize,
            no_title_bar=no_title_bar,
            no_move=no_move,
            no_scrollbar=no_scrollbar,
            no_collapse=no_collapse,
            horizontal_scrollbar=horizontal_scrollbar,
            no_focus_on_appearing=no_focus_on_appearing,
            no_bring_to_front_on_focus=no_bring_to_front_on_focus,
            no_close=no_close,
            no_background=no_background,
            modal=modal,
            popup=popup,
            no_saved_settings=no_saved_settings,
            no_open_over_existing_popup=no_open_over_existing_popup,
            on_close=on_close
        )

        if add_menubar:

            # Create the menu bar control
            self.menu_bar = MenuBar(label=f"{label}_menu_bar", parent=self)

    def AddBorder(self, border_size: float = 0.6) -> Window:
        """
        Add a border to the window
        """
        dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, border_size, category=dpg.mvThemeCat_Core, parent=self.theme_component)

        return self

    def ChangeBackgroundColor(self, color: 'list[int]') -> Window:
        """
        Changes the color of the window
        """
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, color, category=dpg.mvThemeCat_Core, parent=self.theme_component)

        return self

class ChildWindow(Control):

    """
    Sub-Window Control, creates sub-window
    """

    def __init__(self, label: str = None, width: int = 0, height: int = 0, 
                 pos: 'list[int]' = [], add_menubar: bool = False, parent: Control = None, 
                 drop_callback: typing.Any = None, user_data: typing.Any = None,
                 payload_type: str = '$$DPG_PAYLOAD', border: bool = True, autosize_x: bool = False,
                 autosize_y: bool = False, no_scrollbar: bool = False, horizontal_scrollbar: bool = False) -> None:
        super().__init__(parent=parent)
        self.misc_data       = []
        self.theme_component = dpg.add_theme_component(dpg.mvChildWindow, parent=self.theme)
        self.tag             = dpg.add_child_window(
            label=label,
            width=width,
            height=height,
            pos=pos,
            menubar=add_menubar,
            parent=self.parent.tag,
            drop_callback=drop_callback,
            user_data=user_data,
            payload_type=payload_type,
            border=border,
            autosize_x=autosize_x,
            autosize_y=autosize_y,
            no_scrollbar=no_scrollbar,
            horizontal_scrollbar=horizontal_scrollbar
        )

        if add_menubar:

            # Create the menu bar control
            self.menu_bar = MenuBar(label=f"{label}_menu_bar", parent=self)
    
    def ChangeBackgroundColor(self, color: 'list[int]') -> ChildWindow:
        """
        Change the background color of the window
        """
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, color, category=dpg.mvThemeCat_Core, parent=self.theme_component)

        return self
    
    def ChangeBorderColor(self, color: 'list[int]') -> ChildWindow:
        """
        Changes the color of the windows border
        """
        dpg.add_theme_color(dpg.mvThemeCol_Border, color, category=dpg.mvThemeCat_Core, parent=self.theme_component)

        return self
    
    def AddToMiscData(self, data: typing.Any) -> ChildWindow:
        """
        Add any type of data to the instance of this class
        """
        self.misc_data.append(data)

        return self

class Button(Control):

    """
    Button control, creates button
    """

    def __init__(self, label: str = None, width: int = 0, height: int = 0, 
                 pos: 'list[int]' = [], parent: Control = None, callback: typing.Any = None,
                 drag_callback: typing.Any = None, drop_callback: typing.Any = None,
                 user_data: typing.Any = None, payload_type: str = '$$DPG_PAYLOAD', small: bool = False,
                 arrow: bool = False, direction: int = 0) -> None:
        super().__init__(parent=parent)
        self.payload_type    = payload_type
        self.theme_component = dpg.add_theme_component(dpg.mvButton, parent=self.theme)
        self.tag             = dpg.add_button(
            label=label,
            width=width,
            height=height,
            pos=pos,
            parent=self.parent.tag,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            payload_type=self.payload_type,
            small=small,
            arrow=arrow,
            direction=direction
        )

    def AddBorder(self, border_size: float = 0.6) -> Button:
        """
        Add a border to the button
        """
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, border_size, category=dpg.mvThemeCat_Core, parent=self.theme_component)

        return self
    
    def ChangeBackgroundColor(self, color: 'list[int]') -> Button:
        """
        Change the color of the background of the button
        """
        dpg.add_theme_color(dpg.mvThemeCol_Button, color, category=dpg.mvThemeCat_Core, parent=self.theme_component)

        return self
    
    def MakeDragSource(self, drag_data: typing.Any = None) -> DragAndDropPayloadExtension:
        """
        Add drag and drop capability to the button
        """

        drag_and_drop = DragAndDropPayloadExtension(
            label=self.payload_type,
            parent=self,
            drag_data=drag_data,
            payload_type=self.payload_type
        )

        return drag_and_drop

class Group(Control):

    """
    Group Control, creates group control
    """

    def __init__(self, label: str = None, width: int = 0, height: int = 0,
                 pos: 'list[int]' = [], horizontal: bool = False, parent: Control = None, 
                 drag_callback: typing.Any = None, drop_callback: typing.Any = None, 
                 user_data: typing.Any = None, payload_type: str = '$$DPG_PAYLOAD') -> None:
        super().__init__(parent=parent)
        self.theme_component = dpg.add_theme_component(dpg.mvGroup, parent=self.theme)
        self.tag             = dpg.add_group(
            label=label,
            width=width,
            height=height,
            pos=pos,
            horizontal=horizontal,
            parent=self.parent.tag,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            payload_type=payload_type
        )

class Label(Control):

    """
    Label Control, creates a label
    """

    def __init__(self, label: str = None, pos: 'list[int]' = [], wrap: int = -1, 
                 bullet: bool = False, color: 'list[int]' = (-255, 0, 0, 255), indent: int = -1,
                 parent: Control = None, drag_callback: typing.Any = None,
                 drop_callback: typing.Any = None, user_data: typing.Any = None) -> None:
        super().__init__(parent=parent)
        self.theme_component = dpg.add_theme_component(dpg.mvText, parent=self.theme)
        self.tag             = dpg.add_text(
            default_value=label,
            label=label,
            pos=pos,
            wrap=wrap,
            bullet=bullet,
            color=color,
            indent=indent,
            parent=self.parent.tag,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data
        )
    
    def ChangeColor(self, color: 'list[float]') -> Label:
        """
        Change the color of the label text
        """
        dpg.configure_item(self.tag, color=color)

        return self

class LineSeparator(Control):

    """
    Line Separator Control, creates a line separator within a window
    """

    def __init__(self, pos: 'list[int]' = [], parent: Control = None) -> None:
        super().__init__(parent=parent)
        self.tag = dpg.add_separator(
            pos=pos,
            parent=self.parent.tag
        )

class Plot(Control):

    """
    Plot Control, creates a plot control
    """

    def __init__(self, label: str = None, width: int = 0, height: int = 0, pos: 'list[int]' = [],
                 one_plot_at_a_time: bool = False, override_plot_on_entry: bool = False,
                 parent: Control = None, callback: typing.Any = None, 
                 drag_callback: typing.Any = None, drop_callback: typing.Any = None, 
                 user_data: typing.Any = None, payload_type: str = '$$DPG_PAYLOAD', no_title: bool = False,
                 no_menus: bool = False, no_box_select: bool = False, no_mouse_pos: bool = False, 
                 no_highlight: bool = False, no_child: bool = False, query: bool = False,
                 crosshairs: bool = False, anti_aliased: bool = False, equal_aspects: bool = False,
                 use_local_time: bool = False, use_ISO8601: bool = False, use_24hour_clock: bool = False,
                 pan_button: int = dpg.internal_dpg.mvMouseButton_Left, pan_mod: int = -1,
                 fit_button: int = dpg.internal_dpg.mvMouseButton_Left, 
                 context_menu_button: int = dpg.internal_dpg.mvMouseButton_Right,
                 box_select_button: int = dpg.internal_dpg.mvMouseButton_Right, box_select_mod: int = -1,
                 box_select_cancel_button: int = dpg.internal_dpg.mvMouseButton_Left,
                 query_button: int = dpg.internal_dpg.mvMouseButton_Middle, query_mod: int = -1,
                 query_toggle_mod: int = dpg.internal_dpg.mvKey_Control,
                 horizontal_mod: int = dpg.internal_dpg.mvKey_Alt,
                 vertical_mod: int = dpg.internal_dpg.mvKey_Shift) -> None:
        super().__init__(parent=parent)
        self.one_plot_at_a_time     = one_plot_at_a_time
        self.override_plot_on_entry = override_plot_on_entry
        self.candle_theme_component = dpg.add_theme_component(dpg.mvCandleSeries, parent=self.theme)
        self.line_theme_component   = dpg.add_theme_component(dpg.mvLineSeries, parent=self.theme)
        self.tag                    = dpg.add_plot(
            label=label,
            width=width,
            height=height,
            pos=pos,
            parent=parent.tag,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            payload_type=payload_type,
            no_title=no_title,
            no_menus=no_menus,
            no_box_select=no_box_select,
            no_mouse_pos=no_mouse_pos,
            no_highlight=no_highlight,
            no_child=no_child,
            query=query,                  # NOTE: May raise an exception for some reason
            crosshairs=crosshairs,
            anti_aliased=anti_aliased,
            equal_aspects=equal_aspects,
            use_local_time=use_local_time,
            use_ISO8601=use_ISO8601,
            use_24hour_clock=use_24hour_clock,
            pan_button=pan_button,
            pan_mod=pan_mod,
            fit_button=fit_button,
            context_menu_button=context_menu_button,
            box_select_button=box_select_button,
            box_select_mod=box_select_mod,
            box_select_cancel_button=box_select_cancel_button,
            query_button=query_button,
            query_mod=query_mod,
            query_toggle_mod=query_toggle_mod,
            horizontal_mod=horizontal_mod,
            vertical_mod=vertical_mod
        )
        self.granularity   = {
            "1m"  : dpg.mvTimeUnit_Min,
            "2m"  : dpg.mvTimeUnit_Min,
            "5m"  : dpg.mvTimeUnit_Min,
            "15m" : dpg.mvTimeUnit_Min,
            "30m" : dpg.mvTimeUnit_Min,
            "60m" : dpg.mvTimeUnit_Hr,
            "90m" : dpg.mvTimeUnit_Hr,
            "1h"  : dpg.mvTimeUnit_Hr,
            "1d"  : dpg.mvTimeUnit_Day,
            "5d"  : dpg.mvTimeUnit_Day,
            "1wk" : dpg.mvTimeUnit_Day,
            "1mo" : dpg.mvTimeUnit_Mo,
            "3mo" : dpg.mvTimeUnit_Mo
        }
        self.no_children_onetime_only = True

    def AddPlot(self, x_label: str, y_label: str, add_legend: bool = False, x_time: bool = False, y_time: bool = False, 
                x_lock_min: bool = False, x_lock_max: bool = False, y_lock_min: bool = False, y_lock_max: bool = False,
                x_no_gridlines: bool = False, y_no_gridlines: bool = False) -> Plot:
        """
        Creates the proper resources/references for plotting callbacks
        """

        if add_legend:
            self.legend = dpg.add_plot_legend(parent=self.tag)

        self.x_axis = dpg.add_plot_axis(dpg.mvXAxis, label=x_label, time=x_time, parent=self.tag, lock_max=x_lock_max, lock_min=x_lock_min, no_gridlines=x_no_gridlines)
        self.y_axis = dpg.add_plot_axis(dpg.mvYAxis, label=y_label, time=y_time, parent=self.tag, lock_max=y_lock_max, lock_min=y_lock_min, no_gridlines=y_no_gridlines)

        return self
    
    def FitAxis(self, axis: int) -> Plot:
        """
        Auto fits the axis to the plot
        """
        dpg.fit_axis_data(axis)

        return self
    
    def SetAxisLimits(self, axis: int, min: float, max: float) -> Plot:
        """
        Sets axis limits.
        """
        dpg.set_axis_limits(axis=axis, ymin=min, ymax=max)

        return self
    
    def CandleStickPlotDrop(self, sender: typing.Any, app_data: typing.Any, user_data: typing.Any) -> None:
        """
        Adds a candle stick plot to the plotting area, must be passed in as a drop callback
        """

        # Lets define the app_data[8] as the source of the drag and drop
        source_control: Control = app_data[8]

        # If the override plot flag is set, we want to disable the one plot at a time flag
        if self.override_plot_on_entry:
            self.one_plot_at_a_time = False

            # Also destroy the previous plot such as to override it with a new one
            plot_children = dpg.get_item_children(self.y_axis)[1]

            for previous_plot in plot_children:
                dpg.delete_item(previous_plot)

            # Also destroy the previous plot such as to override it with a new one
            plot_children = dpg.get_item_children(self.x_axis)[1]

            for previous_plot in plot_children:
                dpg.delete_item(previous_plot)

        # If we have the one plot at a time flag enabled, then check to see if the drag source is
        # still active and if it is just return as we dont want to plot again
        if self.one_plot_at_a_time:
            if not source_control.IsEnabled():
                return

        # Lets define the 3 inputs from the app_data
        timestamps   = app_data[0]
        opens        = app_data[1]
        closes       = app_data[2]
        lows         = app_data[3]
        highs        = app_data[4]
        legend_label = app_data[5]    # Legend label
        autofit      = app_data[6]
        granularity  = app_data[7]
        candle_stick = dpg.add_candle_series(
            dates=timestamps,
            opens=opens,
            closes=closes,
            lows=lows,
            highs=highs,
            label=legend_label,
            parent=self.y_axis,
            time_unit=self.granularity[granularity]
        )

        # Autofit the plot
        if autofit or self.no_children_onetime_only:
            dpg.fit_axis_data(self.x_axis)
            dpg.fit_axis_data(self.y_axis)
            self.no_children_onetime_only = False

        # Add a button when you right click on the legend item to delete the entry
        if self.one_plot_at_a_time:
            callback = lambda sender, app, user: (dpg.delete_item(user), source_control.Enable())
        else:
            callback = lambda sender, app, user: dpg.delete_item(user)

        candle_stick_control = Control(tag=candle_stick, label="Candle Stick Series")

        delete_button: Button = Button(
            label="Delete Plot",
            width=70,
            height=25,
            parent=candle_stick_control,
            callback=callback,
            user_data=candle_stick_control.tag
        )
        delete_button.BindTheme()

        if self.one_plot_at_a_time:
            source_control.Disable()

    def LineSeriesPlotDrop(self, sender: typing.Any, app_data: typing.Any, user_data: typing.Any) -> None:
        """
        Adds a line series plot to the plotting area, must be passed in as the drop callback
        """

        # Lets define the app_data[4] as the source of the drag and drop
        source_control: Control = app_data[4]

        # If the override plot flag is set, we want to disable the one plot at a time flag
        if self.override_plot_on_entry:
            self.one_plot_at_a_time = False

            # Also destroy the previous plot such as to override it with a new one
            plot_children = dpg.get_item_children(self.y_axis)[1]

            for previous_plot in plot_children:
                dpg.delete_item(previous_plot)

            # Also destroy the previous plot such as to override it with a new one
            plot_children = dpg.get_item_children(self.x_axis)[1]

            for previous_plot in plot_children:
                dpg.delete_item(previous_plot)

        # If we have the one plot at a time flag enabled, then check to see if the drag source is
        # still active and if it is just return as we dont want to plot again
        if self.one_plot_at_a_time:
            if not source_control.IsEnabled():
                return

        # Lets define the 3 inputs from the app_data
        x_data       = app_data[0]
        y_data       = app_data[1]
        legend_label = app_data[2]    # Legend label
        autofit      = app_data[3]
        line_series  = dpg.add_line_series(x_data, y_data, label=legend_label, parent=self.x_axis)

        # Autofit the plot
        if autofit or self.no_children_onetime_only:
            dpg.fit_axis_data(self.x_axis)
            dpg.fit_axis_data(self.y_axis)
            self.no_children_onetime_only = False

        # Add a button when you right click on the legend item to delete the entry
        if self.one_plot_at_a_time:
            callback = lambda sender, app, user: (dpg.delete_item(user), source_control.Enable())
        else:
            callback = lambda sender, app, user: dpg.delete_item(user)

        line_series_control = Control(tag=line_series, label="Plot Line Series")

        delete_button: Button = Button(
            label="Delete Plot",
            width=70,
            height=25,
            parent=line_series_control,
            callback=callback,
            user_data=line_series_control.tag
        )
        delete_button.BindTheme()

        if self.one_plot_at_a_time:
            source_control.Disable()

    def SetPlotTitle(self, label: str) -> Plot:
        """
        Sets the label of the plot i.e. title
        """
        dpg.set_item_label(self.tag, label)

        return self
    
    def SetPlotLineColor(self, color: 'list[int]', theme_component: int) -> Plot:
        """
        Set the color of the line on plot
        """
        dpg.add_theme_color(dpg.mvPlotCol_Line, color, category=dpg.mvThemeCat_Plots, parent=theme_component)

        return self
    
    def AddBorderToLegend(self, theme_component: int, border_size: float = 0.6) -> Plot:
        """
        Adds a border to the legend
        """
        dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize, border_size, category=dpg.mvThemeCat_Core, parent=theme_component)

        return self

class ListBox(Control):

    """
    ListBox Control, creates a listbox control
    """

    def __init__(self, items: 'list[str]' = [], num_items: int = 3, default_value: str = '', 
                 label: str = None, width: int = 0, pos: 'list[int]' = [], parent: Control = None, 
                 callback: typing.Any = None, drag_callback: typing.Any = None, 
                 user_data: typing.Any = None, payload_type: str = '$$DPG_PAYLOAD') -> None:
        super().__init__(parent=parent)
        self.payload_type    = payload_type
        self.theme_component = dpg.add_theme_component(dpg.mvListbox, parent=self.theme)
        self.tag             = dpg.add_listbox(
            items=items,
            num_items=num_items,
            default_value=default_value,
            label=label,
            width=width,
            pos=pos,
            parent=self.parent.tag,
            callback=callback,
            drag_callback=drag_callback,
            user_data=user_data,
            payload_type=self.payload_type
        )

    def AddToListBox(self, item: str) -> ListBox:
        """
        Add an item to the listbox
        """

        config      = dpg.get_item_configuration(self.tag)
        items: list = config["items"]
        if len(item) > 0 and item not in items:
            items.append(item)
            dpg.configure_item(self.tag, items=items)

        return self
    
    def DeleteFromListBox(self, item: str) -> ListBox:
        """
        Delete an item from the listbox
        """

        config      = dpg.get_item_configuration(self.tag)
        items: list = config["items"]
        if len(items) > 0 and item in items:
            items.remove(item)
            dpg.configure_item(self.tag, items=items)

        return self
    
    def GetSelectedItem(self) -> str:
        """
        Gets the selected item from the listbox
        """
        return self.GetValue()
    
    def MakeDragSource(self, drag_data: typing.Any = None) -> DragAndDropPayloadExtension:
        """
        Add drag and drop capability to the button
        """

        drag_and_drop = DragAndDropPayloadExtension(
            label=self.payload_type,
            parent=self,
            drag_data=drag_data,
            payload_type=self.payload_type
        )

        return drag_and_drop

class InputTextBox(Control):

    """
    Input TextBox Control, creates an input textbox control
    """

    def __init__(self, label: str = None, width: int = 0, height: int = 0, pos: 'list[int]' = [],
                 parent: Control = None, callback: typing.Any = None, drag_callback: typing.Any = None,
                 drop_callback: typing.Any = None, user_data: typing.Any = None, payload_type: str = '$$DPG_PAYLOAD', 
                 default_value: str = '', hint: str = '', multiline: bool = False, no_spaces: bool = False, 
                 uppercase: bool = False, tab_input: bool = False, decimal: bool = False, 
                 hexadecimal: bool = False, readonly: bool = False, password: bool = False, 
                 scientific: bool = False, on_enter: bool = False) -> None:
        super().__init__(parent=parent)
        self.payload_type    = payload_type
        self.theme_component = dpg.add_theme_component(dpg.mvInputText, parent=self.theme)
        self.disabled_theme  = dpg.add_theme_component(dpg.mvInputText, parent=self.theme, enabled_state=False)
        self.tag             = dpg.add_input_text(
            label=label,
            width=width,
            height=height,
            pos=pos,
            parent=self.parent.tag,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            payload_type=self.payload_type,
            default_value=default_value,
            hint=hint,
            multiline=multiline,
            no_spaces=no_spaces,
            uppercase=uppercase,
            tab_input=tab_input,
            decimal=decimal,
            hexadecimal=hexadecimal,
            readonly=readonly,
            password=password,
            scientific=scientific,
            on_enter=on_enter
        )

    def AddBorder(self, border_size: float = 0.6, theme_component: int = None) -> InputTextBox:
        """
        Add a border to the button
        """

        theme_component = self.theme_component if theme_component is None else theme_component

        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, border_size, category=dpg.mvThemeCat_Core, parent=theme_component)

        return self
    
    def ChangeInputTextBoxRounding(self, frame_rounding: int, grab_rounding: int, theme_component: int = None) -> InputTextBox:
        """
        Change the rounding of the control
        """

        theme_component = self.theme_component if theme_component is None else theme_component

        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, frame_rounding, category=dpg.mvThemeCat_Core, parent=theme_component)
        dpg.add_theme_style(dpg.mvStyleVar_GrabRounding,  grab_rounding,  category=dpg.mvThemeCat_Core, parent=theme_component)

        return self
    
    def ChangeInputTextBoxPadding(self, window_pad: 'list[int]', frame_pad: 'list[int]', item_spacing: 'list[int]', theme_component: int = None) -> InputTextBox:
        """
        Change padding for the control
        """

        theme_component = self.theme_component if theme_component is None else theme_component

        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, window_pad[0],   window_pad[1],   category=dpg.mvThemeCat_Core, parent=theme_component)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding,  frame_pad[0],    frame_pad[1],    category=dpg.mvThemeCat_Core, parent=theme_component)
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing,   item_spacing[0], item_spacing[1], category=dpg.mvThemeCat_Core, parent=theme_component)

        return self
    
    def GetText(self) -> str:
        """
        Get the text that is currently in the textbox
        """
        return str(self.GetValue())
    
    def SetText(self, text: str) -> InputTextBox:
        """
        Set the text that is currently in the textbox
        """
        self.SetValue(text)

        return self

    def MakeDragSource(self, drag_data: typing.Any = None) -> DragAndDropPayloadExtension:
        """
        Add drag and drop capability to the button
        """

        drag_and_drop = DragAndDropPayloadExtension(
            label=self.payload_type,
            parent=self,
            drag_data=drag_data,
            payload_type=self.payload_type
        )

        return drag_and_drop
    
class DateSelect(Control):

    """
    Date Select Control, creates a date selection control
    """

    def __init__(self, label: str = None, default_value: dict = { 'month_day': 14,'year': 20,'month': 5 },
                 level: int = 0, pos: 'list[int]' = [], parent: Control = None, callback: typing.Any = None, 
                 user_data: typing.Any = None) -> None:
        super().__init__(parent=parent)
        self.theme_component = dpg.add_theme_component(dpg.mvDatePicker, parent=self.theme)
        self.tag             = dpg.add_date_picker(
            label=label,
            default_value=default_value,
            level=level,
            pos=pos,
            parent=self.parent.tag,
            callback=callback,
            user_data=user_data
        )
    
    def GetSelectedDateString(self) -> str:
        """
        Get the selected date from the date select control
        """
        time_data: dict = self.GetValue()

        month = int(time_data.get("month")) + 1
        day   = int(time_data.get("month_day"))
        year  = int(time_data.get("year"))

        if year < 100:
            year += 1900
        elif year >= 100:
            year -= 100
            year += 2000

        return f"{month:>02}-{day:>02}-{year}"
    
    def SetSelectedDate(self, month: int, day: int, year: int) -> DateSelect:
        """
        Sets the selected date for the control
        """

        if year < 2000:
            year -= 1900
        elif year >= 2000:
            year += 100
            year -= 2000

        data_structure = self.GetValue()

        data_structure['month']     = month - 1
        data_structure['month_day'] = day
        data_structure['year']      = year

        self.SetValue(data_structure)

        return self

class TimeSelect(Control):

    """
    Time Select Control, creates a time selection control
    """

    def __init__(self, label: str = None, default_value: dict = { 'hour': 14,'min': 32,'sec': 23 },
                 pos: 'list[int]' = [], hour24: bool = False, parent: Control = None, callback: typing.Any = None, 
                 user_data: typing.Any = None) -> None:
        super().__init__(parent=parent)
        self.hour24          = hour24
        self.theme_component = dpg.add_theme_component(dpg.mvTimePicker, parent=self.theme)
        self.tag             = dpg.add_time_picker(
            label=label,
            default_value=default_value,
            pos=pos,
            hour24=self.hour24,
            parent=self.parent.tag,
            callback=callback,
            user_data=user_data
        )
    
    def GetSelectedTimeString(self, get_24hr: bool = False) -> str:
        """
        Gets the selected time
        """
        value = self.GetValue()
        
        if self.hour24 or get_24hr:

            selected_time = f"{value['hour']:>02}:{value['min']:>02}:{value['sec']:>02}"

        else:

            # Convert the hour to 12Hr time
            hour  = int(value['hour'])
            am_pm = "AM"

            if hour > 11:
                am_pm = "PM"

            if hour > 12:
                hour -= 12

            selected_time = f"{hour:>02}:{value['min']:>02}:{value['sec']:>02} {am_pm}"
        
        return selected_time
    
    def SetSelectedTime(self, hour: int, minute: int, second: int) -> TimeSelect:
        """
        Set the selected time for the control
        """

        data_structure = self.GetValue()

        data_structure['hour'] = hour
        data_structure['min']  = minute
        data_structure['sec']  = second

        self.SetValue(data_structure)

        return self
    
class ComboBox(Control):

    """
    ComboBox Control, creates a ComboBox control
    """

    def __init__(self, items: 'list[str]' = [], default_value: str = '', width: int = 0, label: str = None, 
                 pos: 'list[int]' = [], parent: Control = None, callback: typing.Any = None, 
                 drag_callback: typing.Any = None, user_data: typing.Any = None, 
                 payload_type: str = '$$DPG_PAYLOAD') -> None:
        super().__init__(parent=parent)
        self.theme_component = dpg.add_theme_component(dpg.mvCombo, parent=self.theme)
        self.tag             = dpg.add_combo(
            items=items,
            default_value=default_value,
            label=label,
            width=width,
            pos=pos,
            parent=self.parent.tag,
            callback=callback,
            drag_callback=drag_callback,
            user_data=user_data,
            payload_type=payload_type
        )

    def AddToComboBox(self, item: str) -> ComboBox:
        """
        Add an item to the combobox
        """

        config      = dpg.get_item_configuration(self.tag)
        items: list = config["items"]
        if len(item) > 0 and item not in items:
            items.append(item)
            dpg.configure_item(self.tag, items=items)

        return self
    
    def DeleteFromComboBox(self, item: str) -> ComboBox:
        """
        Delete an item from the combobox
        """

        config      = dpg.get_item_configuration(self.tag)
        items: list = config["items"]
        if len(items) > 0 and item in items:
            items.remove(item)
            dpg.configure_item(self.tag, items=items)

        return self
    
    def SetSelectedItem(self, selected_item: str) -> ComboBox:
        """
        Sets the selected item in the combobox
        """
        self.SetValue(selected_item)

        return self
    
    def GetSelectedItem(self) -> str:
        """
        Gets the selected item from the combobox
        """
        return self.GetValue()
    
    def AddBorder(self, border_size: float = 0.6) -> ComboBox:
        """
        Add a border to the combobox
        """
        dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize, border_size, category=dpg.mvThemeCat_Core, parent=self.theme_component)

        return self
    
class CheckBox(Control):

    """
    CheckBox Control, creates a checkbox control
    """

    def __init__(self, default_value: bool = False, label: str = None, pos: 'list[int]' = [], 
                 parent: Control = None, callback: typing.Any = None, user_data: typing.Any = None) -> None:
        super().__init__(parent=parent)
        self.theme_component = dpg.add_theme_component(dpg.mvCheckbox, parent=self.theme)
        self.tag             = dpg.add_checkbox(
            default_value=default_value,
            label=label,
            pos=pos,
            parent=self.parent.tag,
            callback=callback,
            user_data=user_data
        )
    
    def IsChecked(self) -> bool:
        """
        Checks if the checkbox control has been checked
        """
        return self.GetValue()
    
    def CheckUncheck(self, uncheck: bool = False) -> CheckBox:
        """
        Either checks or unchecks the checkbox
        """
        self.SetValue(not uncheck)

        return self
    
class TableRow(Control):

    """
    Table Row Control, creates a table row control
    """

    def __init__(self, label: str = None, height: int = 0, parent: Control = None) -> None:
        super().__init__(parent=parent)
        self.tag = dpg.add_table_row(
            label=label,
            height=height,
            parent=self.parent.tag
        )

    def AddEmptyColumnEntry(self, label: str = None, height: int = 0) -> TableRow:
        """
        Add an empty entry into the column for the row
        """

        table_cell_tag = dpg.add_table_cell(label=label, height=height, parent=self.tag)

        # Create a table cell control on the fly and add it as child to this control
        self.children.append(Control(tag=table_cell_tag, label=label))

        return self

class TableColumn(Control):

    """
    Table Column Control, creates a table column control
    """

    def __init__(self, label: str = None, width: int = 0, parent: Control = None, enabled: bool = True,
                 init_width_or_weight: float = 0, default_hide: bool = False, default_sort: bool = False,
                 width_stretch: bool = False, width_fixed: bool = False, no_resize: bool = False,
                 no_reorder: bool = False, no_hide: bool = False, no_clip: bool = False,
                 no_sort: bool = False, no_sort_ascending: bool = False, no_sort_descending: bool = False,
                 no_header_width: bool = False, prefer_sort_ascending: bool = True,
                 prefer_sort_descending: bool = False, indent_enable: bool = False, 
                 indent_disable: bool = False) -> None:
        super().__init__(parent=parent)
        self.tag = dpg.add_table_column(
            label=label,
            width=width,
            parent=self.parent.tag,
            enabled=enabled,
            init_width_or_weight=init_width_or_weight,
            default_hide=default_hide,
            default_sort=default_sort,
            width_stretch=width_stretch,
            width_fixed=width_fixed,
            no_resize=no_resize,
            no_reorder=no_reorder,
            no_hide=no_hide,
            no_clip=no_clip,
            no_sort=no_sort,
            no_sort_ascending=no_sort_ascending,
            no_sort_descending=no_sort_descending,
            no_header_width=no_header_width,
            prefer_sort_ascending=prefer_sort_ascending,
            prefer_sort_descending=prefer_sort_descending,
            indent_enable=indent_enable,
            indent_disable=indent_disable
        )

class Table(Control):

    """
    Table Control, creates a table control
    """

    def __init__(self, label: str = None, width: int = 0, height: int = 0, indent: int = -1,
                 pos: 'list[int]' = [], parent: Control = None, callback: typing.Any = None,
                 header_row: bool = True, clipper: bool = False, inner_width: int = 0, policy: int = 0,
                 freeze_rows: int = 0, freeze_columns: int = 0, sort_multi: bool = False,
                 sort_tristate: bool = False, resizable: bool = False, reorderable: bool = False,
                 hideable: bool = False, sortable: bool = False, context_menu_in_body: bool = False,
                 row_background: bool = False, borders_innerH: bool = False, borders_outerH: bool = False,
                 borders_innerV: bool = False, borders_outerV: bool = False, no_host_extendX: bool = False,
                 no_host_extendY: bool = False, no_keep_columns_visible: bool = False,
                 precise_widths: bool = False, no_clip: bool = False, pad_outerX: bool = False,
                 no_pad_outerX: bool = False, no_pad_innerX: bool = False, scrollX: bool = False,
                 scrollY: bool = False, no_saved_settings: bool = False) -> None:
        super().__init__(parent=parent)
        self.theme_component = dpg.add_theme_component(dpg.mvTable, parent=self.theme)
        self.tag             = dpg.add_table(
            label=label,
            width=width,
            height=height,
            indent=indent,
            pos=pos,
            parent=self.parent.tag,
            callback=callback,
            header_row=header_row,
            clipper=clipper,
            inner_width=inner_width,
            policy=policy,
            freeze_rows=freeze_rows,
            freeze_columns=freeze_columns,
            sort_multi=sort_multi,
            sort_tristate=sort_tristate,
            resizable=resizable,
            reorderable=reorderable,
            hideable=hideable,
            sortable=sortable,
            context_menu_in_body=context_menu_in_body,
            row_background=row_background,
            borders_innerH=borders_innerH,
            borders_outerH=borders_outerH,
            borders_innerV=borders_innerV,
            borders_outerV=borders_outerV,
            no_host_extendX=no_host_extendX,
            no_host_extendY=no_host_extendY,
            no_keep_columns_visible=no_keep_columns_visible,
            precise_widths=precise_widths,
            no_clip=no_clip,
            pad_outerX=pad_outerX,
            no_pad_outerX=no_pad_outerX,
            no_pad_innerX=no_pad_innerX,
            scrollX=scrollX,
            scrollY=scrollY,
            no_saved_settings=no_saved_settings
        )

    def AddColumn(self, label: str = None, width: int = 0, enabled: bool = True,
                  init_width_or_weight: float = 0, default_hide: bool = False, default_sort: bool = False,
                  width_stretch: bool = False, width_fixed: bool = False, no_resize: bool = False,
                  no_reorder: bool = False, no_hide: bool = False, no_clip: bool = False,
                  no_sort: bool = False, no_sort_ascending: bool = False, no_sort_descending: bool = False,
                  no_header_width: bool = False, prefer_sort_ascending: bool = True,
                  prefer_sort_descending: bool = False, indent_enable: bool = False, 
                  indent_disable: bool = False) -> TableColumn:
        """
        Adds a column to the table
        """

        table_column = TableColumn(
            label=label,
            width=width,
            enabled=enabled,
            parent=self,
            init_width_or_weight=init_width_or_weight,
            default_hide=default_hide,
            default_sort=default_sort,
            width_stretch=width_stretch,
            width_fixed=width_fixed,
            no_resize=no_resize,
            no_reorder=no_reorder,
            no_hide=no_hide,
            no_clip=no_clip,
            no_sort=no_sort,
            no_sort_ascending=no_sort_ascending,
            no_sort_descending=no_sort_descending,
            no_header_width=no_header_width,
            prefer_sort_ascending=prefer_sort_ascending,
            prefer_sort_descending=prefer_sort_descending,
            indent_enable=indent_enable,
            indent_disable=indent_disable
        )

        return table_column
    
    def AddRow(self, label: str = None, height: int = 0) -> TableRow:
        """
        Adds a row to the table
        """
        return TableRow(label=label, height=height, parent=self)
    
class LoadingIndicator(Control):

    """
    Loading Indicator Control, creates the loading indicator control
    """

    def __init__(self, label: str = None, width: int = 0, height: int = 0, indent: int = -1,
                 pos: 'list[int]' = [], parent: Control = None, style: int = 0, circle_count: int = 8,
                 speed: float = 1, radius: float = 3, thickness: float = 1, color: 'list[int]' = [51, 51, 55, 255],
                 secondary_color: 'list[int]' = [29, 151, 236, 103]) -> None:
        super().__init__(parent=parent)
        self.tag = dpg.add_loading_indicator(
            label=label,
            width=width,
            height=height,
            indent=indent,
            pos=pos,
            parent=self.parent.tag,
            style=style,
            circle_count=circle_count,
            speed=speed,
            radius=radius,
            thickness=thickness,
            color=color,
            secondary_color=secondary_color
        )

class Slider(Control):

    """
    Adds a floating point slider control
    """

    def __init__(self, type: typing.Any, label: str = None, width: int = 0, height: int = 0, indent: int = -1,
                 parent: Control = None, callback: typing.Any = None, show: bool = True, enabled: bool = True,
                 pos: 'list[int]' = [], default_value: typing.Union[float, int] = 0, vertical: bool = False, no_input: bool = False,
                 clamped: bool = False, min_value: typing.Union[float, int] = 0, max_value: typing.Union[float, int] = 100,
                 format: str = None) -> None:
        super().__init__(parent=parent)
        if type == float:
            self.tag = dpg.add_slider_float(
                label=label,
                width=width,
                height=height,
                indent=indent,
                parent=self.parent.tag,
                callback=callback,
                show=show,
                enabled=enabled,
                pos=pos,
                default_value=default_value,
                vertical=vertical,
                no_input=no_input,
                clamped=clamped,
                min_value=min_value,
                max_value=max_value,
                format=format if format is not None else '%.3f'
            )
        elif type == int:
            self.tag = dpg.add_slider_int(
                label=label,
                width=width,
                height=height,
                indent=indent,
                parent=self.parent.tag,
                callback=callback,
                show=show,
                enabled=enabled,
                pos=pos,
                default_value=default_value,
                vertical=vertical,
                no_input=no_input,
                clamped=clamped,
                min_value=min_value,
                max_value=max_value,
                format=format if format is not None else '%d'
            )

    def GetSliderValue(self) -> float:
        """
        Get the slider value.
        """
        return self.GetValue()