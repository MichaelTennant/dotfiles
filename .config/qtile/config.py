# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
# Copytight (c) 2024 Michael Tennant
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
requires
python iwlib
"""

from libqtile import bar, layout, widget
from libqtile.config import Group, Match, Screen

from colour_palette import MACCHIATO as COLOURS
from keymap import *
from screens import *


groups = [Group(i) for i in "123456789"]

keys = gen_keyboard_shortcuts(groups)
mouse = gen_mouse_motions()

layouts = [
    layout.Columns(

        border_focus = COLOURS[4], 
        border_normal = COLOURS[22], 

        border_width = 4, 
        border_on_single = 0, 

        margin = 4, 
        margin_on_single = 0, 
    ),

    layout.Max(), 
]

floating_layout = layout.Floating(
    float_rules = [

        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,

        Match(wm_class="confirmreset"),     # gitk
        Match(wm_class="makebranch"),       # gitk
        Match(wm_class="maketag"),          # gitk
        Match(wm_class="ssh-askpass"),      # ssh-askpass
        Match(title="branchdialog"),        # gitk
        Match(title="pinentry"),            # GPG key password entry
    ],

    border_focus = COLOURS[4],
    border_normal = COLOURS[22],

    border_width = 4,
    border_on_single = 0,

    margin = 4,
    margin_on_single = 0
)

screens = [
    gen_primary_screen(
        # Note: Change wallpaper to your desired wallpaper
        wallpaper = "~/Pictures/porkchop_background.png", 
        wallpaper_mode = "fill", 

        # Note: Change wlan_interface to your internet interface
        #       This can be found by using the command 'ip address'
        #       This can also be removed entirely
        wlan_interface = "wlo1", 
    ), 

    # Note: Remove (or add more) for different monitor counts
    gen_secondry_screen(
        wallpaper = "~/Pictures/ASCII-Mandlebrot.png", 
        wallpaper_mode = "fill", 
    ), 
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = False
