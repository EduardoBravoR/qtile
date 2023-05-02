import os
import theme

# import separator
import subprocess
from typing import List
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# from libqtile.dgroups import simple_key_binder


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/scripts/autostart.sh")
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

terminal = "kitty"  # "kitty --listen-on unix:/tmp/mykitty"  # guess_terminal()
dmenu = "dmenu_run -i -fn 'Source Code Pro:size=10' -nb '#282C34' -nf '#F3F4F5' -sb '#E5C07B' -sf '#000'"  # -p '➜ '
drofi = "rofi -show drun -show-icons"
rofi = "rofi -show run"
lock = "slock"

time = "zsh /home/kb/.config/scripts/time_date.sh"

vol_cur = "amixer -D pulse get Master"
vol_up = "zsh /home/kb/.config/scripts/volume.sh up"
vol_down = "zsh /home/kb/.config/scripts/volume.sh down"
mute = "zsh /home/kb/.config/scripts/volume.sh mute"

# vol_up = "amixer set Master 5%+"
# vol_down = "amixer set Master 5%-"
# mute = "amixer set Master toggle"

# vol_up = "amixer -q -D pulse sset Master 5%+"
# vol_down = "amixer -q -D pulse sset Master 5%-"
# mute = "amixer -q -D pulse set Master toggle"

# bright_up = "xbacklight -inc 10"
# bright_down = "xbacklight -dec 10"
bright_up = "zsh /home/kb/.config/scripts/brightness.sh up"
bright_down = "zsh /home/kb/.config/scripts/brightness.sh down"

ss = "scrot '%F_%T_$wx$h.png' -e 'mv $f ~/Pictures/Screenshots/'"
ss_cb = "scrot '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'"
ss_w = "scrot -u '%F_%T_$wx$h.png' -e 'mv $f ~/Pictures/Screenshots/'"
ss_w_cb = "scrot -u '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'"
ss_a = "scrot -s -l mode=edge '%F_%T_$wx$h.png' -e 'mv $f ~/Pictures/Screenshots/'"
ss_a_cb = "scrot -s -l mode=edge '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'"

password = "passmenu"

keys = [
    # Change focus window
    Key([mod], "u", lazy.layout.up()),
    Key([mod], "e", lazy.layout.down()),
    # Key([mod], "n", lazy.layout.left()),
    # Key([mod], "i", lazy.layout.right()),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Resize window
    Key(
        [mod, "control"],
        "i",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "n",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "u",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "e",
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
    # Screenshot
    Key([], "Print", lazy.spawn(ss)),
    Key(["control"], "Print", lazy.spawn(ss_cb)),
    Key([alt], "Print", lazy.spawn(ss_w)),
    Key(["control", alt], "Print", lazy.spawn(ss_w_cb)),
    Key(["shift"], "Print", lazy.spawn(ss_a)),
    Key(["control", "shift"], "Print", lazy.spawn(ss_a_cb)),
    # App launcher
    Key([mod], "r", lazy.spawn(time), desc="Launch date time information"),
    Key([mod], "d", lazy.spawn(dmenu), desc="Launch dmenu drun"),
    Key([mod], "space", lazy.spawn(drofi), desc="Launch rofi run"),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch Alacritty"),
    Key([mod], "l", lazy.spawn(lock), desc="Lock the screen with slock"),
    # Password
    Key([mod], "semicolon", lazy.spawn(password), desc="Dmenu for passwords"),
    # Qtile system
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "space", lazy.window.toggle_floating()),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key(
        [mod],
        "f",
        lazy.layout.maximize(),
        desc="toggle window between minimum and maximum sizes",
    ),
    # Toggle bar
    Key(
        [mod],
        "h",
        lazy.hide_show_bar(),
    ),
]

icons = (
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    "  ",
    "  ",
    " ",
    " ",
    " ",
    " ",
    " ",
    "",
    " ",
    "ﭮ ",
    " ",
    " ",
    "﨣",
)

workspaces = [
    {"name": "1", "label": icons[0], "layout": "stack"},
    {"name": "2", "label": icons[1], "layout": "stack"},
    {"name": "3", "label": icons[2], "layout": "stack"},
    {"name": "4", "label": icons[3], "layout": "stack"},
    {"name": "5", "label": icons[4], "layout": "stack"},
    {"name": "6", "label": icons[5], "layout": "stack"},
    {"name": "7", "label": icons[6], "layout": "stack"},
    {"name": "8", "label": icons[7], "layout": "stack"},
    {"name": "9", "label": icons[8], "layout": "stack"},
]

groups = []
for workspace in workspaces:
    groups.append(
        Group(
            name=workspace["name"],
            label=workspace["label"],
            layout=workspace["layout"].lower(),
        )
    )

for i in groups:
    keys.extend(
        [
            # Change to i-workspace
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # Move the focused window to the i-workspace
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Change to next or prev workspace
            Key([mod], "i", lazy.screen.next_group()),  # Right
            Key([mod], "n", lazy.screen.prev_group()),  # Left
        ]
    )

colors = theme.onedark()
bgColor = "#2E3440"  #'#4C566A'
fgColor = "#F3F4F5"


def init_layout_theme():
    return {
        "margin": 10,
        "border_width": 0,
        "border_focus": colors["purple"],
        "border_normal": colors["gray"],
    }


layout_theme = init_layout_theme()

layouts = [
    # layout.Max(**layout_theme),
    layout.Stack(num_stacks=1, **layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Floating(**layout_theme),
]

widget_defaults = dict(
    font="Source Code Pro",
    fontsize=14,
    padding=2,
    foreground=fgColor,
    background=bgColor,
)

extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Sep(linewidth=0, padding=6),
        widget.GroupBox(
            # padding_y = 5,
            # padding_x = 5,
            borderwidth=2,
            disable_drag=True,
            active=colors["yellow"],
            inactive=colors["gray"],
            hide_unused=False,
            rounded=True,
            highlight_method="line",
            highlight_color=bgColor,  # [bgColor, colors['green']],#Active group highlight color when using 'line' highlight method.
            this_current_screen_border=colors["green"],
            # this_screen_border = colors['purple'],
            # other_screen_border = colors['turquoise'],
            # other_current_screen_border = colors['turquoise'],
            # urgent_alert_method = "line",
            urgent_border=colors["red"],
            urgent_text=colors["red"],
            block_highlight_text_color=colors["green"],
            use_mouse_wheel=False,
        ),
        # widget.GroupBox(
        #     padding_y = 5,
        #     padding_x = 5,
        #     borderwidth = 0,
        #     disable_drag = True,
        #     active = colors['red'],
        #     inactive = colors['gray'],
        #     hide_unused = False,
        #     rounded = True,
        #     highlight_method = "block",
        #     this_current_screen_border = colors['red'],
        #     # this_screen_border = colors['purple'],
        #     # other_screen_border = colors['turquoise'],
        #     # other_current_screen_border = colors['turquoise'],
        #     # urgent_alert_method = "line",
        #     # urgent_border = colors['yellow'],
        #     # urgent_text = colors['blue'],
        #     block_highlight_text_color = colors['dark_gray'],
        #     use_mouse_wheel = False,
        # ),
        widget.CurrentLayoutIcon(
            scale=0.4,
        ),
        # widget.WindowName(),
        widget.TaskList(
            icon_size=0,
            borderwidth=2,
            border=colors["yellow"],
            margin=2,
            padding=5,
            highlight_method="block",
            # title_width_method = "uniform",
            urgent_alert_method="border",
            urgent_border=colors["red"],
            rounded=True,
            txt_floating="🗗 ",
            txt_maximized="🗖 ",
            txt_minimized="🗕 ",
        ),
        # widget.WindowTabs(),
        # separator.lower_right_trianglev2(bgColor, '#4C566A'),
        widget.TextBox(
            text="  ", foreground="#bb97f5", background=bgColor  # colors['brown']
        ),
        widget.CPU(
            format="{load_percent}%",
            update_interval=3,
            foreground="#bb97f5",  # colors['brown']
            background=bgColor,
        ),
        widget.TextBox(
            text="  ", foreground="#a0cd6a", background=bgColor  # colors['red']
        ),
        widget.Backlight(
            backlight_name="intel_backlight",
            format="{percent:1.0%}",
            update_interval=0.2,
            foreground="#a0cd6a",  # colors['red']
            background=bgColor,
        ),
        widget.TextBox(
            text="  ", foreground="#e3b16f", background=bgColor  # colors['purple']
        ),
        widget.Volume(
            fontsize=14,
            update_interval=0.2,
            foreground="#e3b16f",  # colors['purple']
            background=bgColor,
        ),
        widget.TextBox(
            text="   ", foreground="#f27692", background=bgColor  # colors['yellow']
        ),
        widget.Battery(
            battery=0,
            format="{percent:0.1%} ",  # format="{char} {percent:0.1%}"
            energy_now_file="charge_now",
            energy_full_file="charge_full",
            power_now_file="current_now",
            update_delay=5,
            charge_char="  ",
            discharge_char="  ",
            full_char=" ",
            foreground="#f27692",  # colors['yellow']
            background=bgColor,
        ),
        # widget.Wlan(),
        widget.Clock(
            format=" %a %b %-d - %-I:%M %p ",
            foreground="#73d9ca",  # colors['lime']
            background=bgColor,
        ),
        # separator.lower_right_trianglev2('#4C566A', bgColor),
    ]
    return widgets_list


widgets_list = init_widgets_list()

screens = [
    Screen(
        top=bar.Bar(
            widgets=widgets_list,
            size=30,  # size=30,
            margin=[10, 10, 0, 10],
            opacity=0.8,
        ),
        # bottom = bar.Gap(10),#Comment if i want a margin but in the application
        # left = bar.Gap(10),#
        # right = bar.Gap(10),#
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# dgroups_key_binder = simple_key_binder(mod)
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    **layout_theme
)  # for floating layout the theme is defined here

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wmname = "qtile"
