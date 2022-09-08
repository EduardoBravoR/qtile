from typing import List
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/scripts/autostart.sh')
    subprocess.call([home])

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

alt = "mod1"
mod = "mod4"

terminal = guess_terminal()
dmenu = "dmenu_run -i -fn 'Source Code Pro:size=10' -nb '#2E3440' -nf '#F3F4F5' -sb '#73d9ca' -sf '#000'"# -p '➜ '
drofi = "rofi -show drun -show-icons"
rofi = "rofi -show run"
lock = "slock"

vol_cur = "amixer -D pulse get Master"
vol_up = "amixer -q -D pulse sset Master 5%+"
vol_down = "amixer -q -D pulse sset Master 5%-"
mute = "amixer -q -D pulse set Master toggle"

bright_up = "xbacklight -inc 10"
bright_down = "xbacklight -dec 10"

scrot = "scrot '%F_%T_$wx$h.png' -e 'mv $f ~/Pictures/Screenshots/'"
scrot_clipboard = "scrot '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'"
scrot_window = "scrot -u '%F_%T_$wx$h.png' -e 'mv $f ~/Pictures/Screenshots/'"
scrot_window_clipboard = "scrot -u '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'"
scrot_region = "scrot -s '%F_%T_$wx$h.png' -e 'mv $f ~/Pictures/Screenshots/'"
scrot_region_clipboard = "scrot -s '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'"

keys = [
    # Change focus window
    Key([mod], "u", lazy.layout.up()),
    Key([mod], "e", lazy.layout.down()),
    #Key([mod], "n", lazy.layout.left()),
    #Key([mod], "i", lazy.layout.right()),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Resize window
    Key([mod, "control"], "i",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key([mod, "control"], "n",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key([mod, "control"], "u",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key([mod, "control"], "e",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    Key([mod], "a", lazy.layout.reset(), desc="Reset all window sizes"),

    # Move windows in current stack
    Key([mod, "shift"], "e", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "u", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "n", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "i", lazy.layout.shuffle_right()),

    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn(vol_up)),
    Key([], "XF86AudioLowerVolume", lazy.spawn(vol_down)),
    Key([], "XF86AudioMute", lazy.spawn(mute)),

    # Multimedia
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn(bright_up)),
    Key([], "XF86MonBrightnessDown", lazy.spawn(bright_down)),

    # Print
    Key([], "Print", lazy.spawn(scrot)),
    Key(["control"], "Print", lazy.spawn(scrot_clipboard)),
    Key([alt], "Print", lazy.spawn(scrot_window)),
    Key(["control", alt], "Print", lazy.spawn(scrot_window_clipboard)),
    Key(["shift"], "Print", lazy.spawn(scrot_region)),
    Key(["control", "shift"], "Print", lazy.spawn(scrot_region_clipboard)),

    # Applications
    Key([mod], "space", lazy.spawn(dmenu), desc="Launch rofi drun"),
    Key([mod], "r", lazy.spawn(rofi), desc="Launch rofi run"),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch Alacritty"),
    Key([mod], "l", lazy.spawn(lock), desc="Lock the screen with slock"),

    # Qtile system
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "space", lazy.window.toggle_floating()),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "f", lazy.layout.maximize(), desc='toggle window between minimum and maximum sizes'),

    #Toggle bar
	Key([mod], "h", lazy.hide_show_bar(),),
]
icon = " " #""
workspaces = [

    {"name": "1", "label": icon, "layout": "stack"},
    {"name": "2", "label": icon, "layout": "stack"},
    {"name": "3", "label": icon, "layout": "stack"},
    {"name": "4", "label": icon, "layout": "stack"},
    {"name": "5", "label": icon, "layout": "stack"},
    {"name": "6", "label": icon, "layout": "stack"},
    {"name": "7", "label": icon, "layout": "stack"},
	{"name": "8", "label": icon, "layout": "stack"},
    {"name": "9", "label": icon, "layout": "stack"},

#    {"name": "1", "label": " ", "layout": "stack"},
#    {"name": "2", "label": " ", "layout": "stack"},
#    {"name": "3", "label": " ", "layout": "stack"},
#    {"name": "4", "label": " ", "layout": "stack"},
#    {"name": "5", "label": " ", "layout": "stack"},
#    {"name": "6", "label": " ", "layout": "stack"},
#    {"name": "7", "label": " ", "layout": "stack"},
#    {"name": "8", "label": " ", "layout": "stack"},
#    {"name": "9", "label": " ", "layout": "stack"},
    #                            
    #[" "," "," "," "," "," "," "," ",]
    # "  ", "  ", "  ", "  ", "   ", "  "
]

groups = []
for workspace in workspaces:
    groups.append(Group(
        name=workspace["name"], label=workspace["label"], layout=workspace["layout"].lower()))

for i in groups:
    keys.extend([
        # Change to i-workspace
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
        # Move the focused window to the i-workspace
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Change to next or prev workspace
        Key([mod], "i", lazy.screen.next_group()),#Right
        Key([mod], "n", lazy.screen.prev_group()),#Left
    ])

dgroups_key_binder = simple_key_binder(mod)

def init_onedark_colors():
    return {
        'dark_blue':	'#282C34',
        'red':			'#E06C75',
        'green':		'#98C379',
        'yellow':		'#E5C07B',
        'blue':			'#61AFEF',
        'purple':		'#C678DD',
        'turquoise':	'#56B6C2',
        'gray':			'#ABB2BF'
    }

onedark = init_onedark_colors()

def init_colors():
    return {
        'orange':			'#FCAE1E',
		'dark_blue':		'#2E3440',
		'white':			'#F3F4F5',
		'pink':				'#CD1F3F',
		'blue': 			'#6790EB',
		'blue2':			'#5498C7',
		'gray':				'#A9A9A9',
        'dark_blue2':   	'#4C566A',
        'brown':        	'#C3A492',
		'red':				'#EC7063',
		'purple':			'#A569BD',
		'yellow':			'#F5B041',
		'lime':				'#48C9B0',
        'gb_yellow':    	'#FABD2F',
		'gb_dark_yellow':	'#D79921'
    }

colors = init_colors()

def init_layout_theme():
    return {
        "margin": 10,
        "border_width": 2,
        "border_focus": onedark['yellow'],
        "border_normal": onedark['gray']
    }

layout_theme = init_layout_theme()

layouts = [
    #layout.Max(**layout_theme),
    layout.Stack(num_stacks = 1, **layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Floating(**layout_theme)
]

widget_defaults = dict(
    font = 'Source Code Pro',
    fontsize = 14,
    padding = 2,
    foreground = colors['white'],
    background = colors['dark_blue']
)

extension_defaults = widget_defaults.copy()

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

def left_circle(bg_color, fg_color):
        return widget.TextBox(
            text = '\uE0B6',
            padding = 0,
            fontsize = 30,
            background = bg_color,
            foreground = fg_color)

def right_circle(bg_color, fg_color):
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

def lower_left_triangle(bg_color, fg_color):
    return widget.TextBox(
        text = '\u25e2',
        padding = 0,
        fontsize = 42,
        background = bg_color,
        foreground = fg_color
    )

def lower_right_triangle(bg_color, fg_color):
    return widget.TextBox(
    	text = '\uE0BA',
    	padding = 0,
    	fontsize = 30,
    	background = bg_color,
    	foreground = fg_color)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth = 0,
                    padding = 6
                ),
                widget.GroupBox(
                    fontsize = 14,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 6,
                    padding_x = 5,
                    borderwidth = 0,
                    disable_drag = True,
                    active = '#73d9ca',#onedark['red'],
                    inactive = onedark['gray'],
                    rounded = True,
                    highlight_method = "block",
                    #highlight_color = colors['dark_blue'],#Active group highlight color when using 'line' highlight method.
                    block_highlight_text_color = onedark['dark_blue'],
                    this_current_screen_border = '#73d9ca',#onedark['red'],
                    #hide_unused = True,
                ),
                #right_arrow(colors['yellow'], colors['dark_blue']),
                widget.CurrentLayoutIcon(
				#	background = colors['yellow'],
				#	foreground = colors['white'],
					scale = 0.5
				),
				#widget.CurrentLayout(
				#	background = colors['yellow'],
				#	foreground = colors['white']
				#),
                #right_arrow(colors['dark_blue'], colors['yellow']),
                widget.WindowName(),
                #lower_right_triangle(colors['dark_blue'], colors['brown']),
                lower_left_triangle(colors['dark_blue'], colors['dark_blue2']),
                widget.TextBox(
                    text = "  ",
                    foreground = '#bb97f5',#colors['brown']
                    background = colors['dark_blue2']
                ),
                widget.CPU(
                    format = '{load_percent}%',
                    update_interval = 3,
                    foreground = '#bb97f5',#colors['brown']
                    background = colors['dark_blue2']
                ),
                #left_arrow(colors['brown'], colors['blue2']),
                #widget.Memory(
                #    format = '  {MemUsed:.0f}/{MemTotal:.0f} MB',
                #    padding = 5,
                #    mouse_callbacks = {'Button1': lazy.spawn('alacritty -e htop')},
                #    background = '#2bc3df'#colors['blue2']
                #),
                #left_arrow(colors['blue2'], colors['red']),
                #lower_left_triangle('#bb97f5', '#a0cd6a'),
                widget.TextBox(
                    text = "  ",
                    foreground = '#a0cd6a',#colors['red']
                    background = colors['dark_blue2']
                ),
                widget.Backlight(
                    backlight_name = 'intel_backlight',
                    format = '{percent:1.0%}',
                    update_interval = 0.2,
                    foreground = '#a0cd6a',#colors['red']
                    background = colors['dark_blue2']
                ),
                #left_arrow(colors['red'], colors['purple']),
                #lower_left_triangle('#a0cd6a', '#e3b16f'),
                widget.TextBox(
                    text = "  ",
                    foreground = '#e3b16f',#colors['purple']
                    background = colors['dark_blue2']
                ),
                widget.Volume(
                    fontsize = 14,
                    update_interval = 0.2,
                    foreground = '#e3b16f',#colors['purple']
                    background = colors['dark_blue2']
                ),
                #left_arrow(colors['purple'], colors['yellow']),
                #lower_left_triangle('#e3b16f', '#f27692'),
                widget.TextBox(
                    text = "   ",
                    foreground = '#f27692',#colors['yellow']
                    background = colors['dark_blue2']
                ),
                widget.Battery(
                    battery = 0,
                    format = "{percent:0.1%} ",  # format="{char} {percent:0.1%}"
                    energy_now_file = "charge_now",
                    energy_full_file = "charge_full",
                    power_now_file = "current_now",
                    update_delay = 5,
                    charge_char = '  ',
                    discharge_char = '  ',
                    full_char = ' ',
                    foreground = '#f27692',#colors['yellow']
                    background = colors['dark_blue2']
                ),
                #lower_left_triangle('#f27692', '#73d9ca'),
                #left_arrow(colors['yellow'], colors['lime']),
                widget.Clock(
                    #fontsize = 14,
                    format = " %a %b %-d - %-I:%M %p",
                    foreground = '#73d9ca',#colors['lime']
                    background = colors['dark_blue2']
                ),
                lower_left_triangle(colors['dark_blue2'], colors['dark_blue']),
                #left_arrow(colors['lime'], colors['dark_blue']),
            ],
            24,
            #24,
            #30,
            #margin = [10, 10, 0, 10],
            #opacity = 0.75,
        ),
        #bottom = bar.Gap(10),#Comment if i want a margin but in the application
        #left = bar.Gap(10),#
        #right = bar.Gap(10),#
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], **layout_theme)#for floating layout the theme is defined here
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wmname = "LG3D"
