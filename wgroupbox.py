import theme
from libqtile import widget
colors = theme.onedark()
def block():
    return widget.GroupBox(
        padding_y = 5,
        padding_x = 5,
        borderwidth = 0,
        disable_drag = True,
        active = colors['red'],
        inactive = colors['gray'],
        hide_unused = False,
        rounded = True,
        highlight_method = "block",
        this_current_screen_border = colors['red'],
        # this_screen_border = colors['purple'],
        # other_screen_border = colors['turquoise'],
        # other_current_screen_border = colors['turquoise'],
        # urgent_alert_method = "line",
        # urgent_border = colors['yellow'],
        # urgent_text = colors['blue'],
        block_highlight_text_color = colors['dark_gray'],
        use_mouse_wheel = False,
    ),

def line():
    return widget.GroupBox(
        padding_y = 5,
        padding_x = 5,
        borderwidth = 2,
        disable_drag = True,
        active = colors['turquoise'],
        inactive = colors['gray'],
        hide_unused = True,
        rounded = True,
        highlight_method = "line",
        highlight_color = '#2E3440',#['#2E3440', colors['green']],#Active group highlight color when using 'line' highlight method.
        this_current_screen_border = colors['green'],
        # this_screen_border = colors['purple'],
        # other_screen_border = colors['turquoise'],
        # other_current_screen_border = colors['turquoise'],
        # urgent_alert_method = "line",
        # urgent_border = colors['yellow'],
        # urgent_text = colors['blue'],
        block_highlight_text_color = colors['purple'],
        use_mouse_wheel = False,
    ),
