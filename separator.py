from libqtile import widget
def left_arrow(bg_color, fg_color):
    return widget.TextBox(
        text = '\uE0B2',
        padding = 0,
        fontsize = 30,
        background = bg_color,
        foreground = fg_color)

def right_arrow(bg_color, fg_color):
    return widget.TextBox(
        text = '\uE0B0',
        padding = 0,
        fontsize = 22,
        background = bg_color,
        foreground = fg_color)

def left_half_circle(bg_color, fg_color):
    return widget.TextBox(
        text = '\uE0B6',
        padding = 0,
        fontsize = 30,
        background = bg_color,
        foreground = fg_color)

def right_half_circle(bg_color, fg_color):
    return widget.TextBox(
        text = '\uE0B4',
        padding = 0,
        fontsize = 30,
        background = bg_color,
        foreground = fg_color)

def upper_left_triangle(bg_color, fg_color):
    return widget.TextBox(
        text = '\uE0BC',
        padding = 0,
        fontsize = 30,
        background = bg_color,
        foreground = fg_color)

def upper_right_triangle(bg_color, fg_color):
    return widget.TextBox(
        text = '\uE0BE',
        padding = 0,
        fontsize = 30,
        background = bg_color,
        foreground = fg_color)

def lower_left_triangle(bg_color, fg_color):
    return widget.TextBox(
    	text = '\uE0B8',
    	padding = 0,
    	fontsize = 30,
    	background = bg_color,
    	foreground = fg_color)

def lower_right_triangle(bg_color, fg_color):
    return widget.TextBox(
    	text = '\uE0BA',
    	padding = 0,
    	fontsize = 30,
    	background = bg_color,
    	foreground = fg_color)

def lower_right_trianglev2(bg_color, fg_color):
    return widget.TextBox(
        text = '\u25e2',
        padding = 0,
        fontsize = 42,
        background = bg_color,
        foreground = fg_color)
