#!/bin/python

# Copyright (c) 2024 Michael Tennant
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
----------------------------------------------------------------
Custom qtile configuration for the X11 window manager
----------------------------------------------------------------
This file defines keyboard shortcuts and mouse gestures
~/.config/qtile/keymap.py

Requires:
 - flameshot [1]
 - rofi [2]
 - xscreensaver [3]

Small modifications to the script allows for requirements to be 
removed or replaced with alternatives.

At the time of writing this script qtile does not play nicely 
with wayland (see [4]) so it is recommened to switch to an 
alternative such as sway. Modifications to the script may be 
required to get it running on wayland.

[1] https://flameshot.org/
[2] https://github.com/davatorium/rofi
[3] https://www.jwz.org/xscreensaver/
[4] https://github.com/qtile/qtile/discussions/2409
----------------------------------------------------------------
"""

from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

__all__ = [
    "gen_keyboard_shortcuts", 
    "gen_mouse_motions", 
]

# Note: These constants may need to be changed depending on your keyboard layout
# Note: Use xmodmap to get key modifiers or xev to get keycodes
CONTROL = "control"
SHIFT = "shift"
SUPER = "mod4"
ALT = "mod1"
ALT_GR = "mod5"


def gen_keyboard_shortcuts(groups):
    keys = [
        # Qtile/X11/Systemd Manipulation
        Key(
            [CONTROL, SUPER], 
            "q", 
            lazy.shutdown(), 
            desc = "Shutdown Qtile", 
        ), 

        Key(
            [CONTROL, SUPER], 
            "r", 
            lazy.reload_config(), 
            desc = "Refresh Qtile", 
        ), 

        Key(
            [CONTROL, SUPER], 
            "l", 
            lazy.spawn("xscreensaver-command -lock"), 
            desc = "Lock computer", 
        ), 

        Key(
            [CONTROL, SUPER], 
            "s", 
            lazy.spawn("systemctl poweroff"), 
            desc = "Shutdown computer", 
        ), 

        # Window Manipulation
        Key(
            [ALT], 
            "Tab", 
            lazy.next_layout(), 
            desc = "Toggle between window layouts", 
        ), 

        Key(
            [ALT], 
            "w", 
            lazy.window.kill(), 
            desc = "Kill focused window", 
        ), 

        # Rofi Menus
        Key(
            [SUPER], 
            "Return", 
            lazy.spawn("rofi -show drun"), 
            desc = "Run application menu", 
        ), 

        Key(
            [SUPER], 
            "Tab", 
            lazy.spawn("rofi -show window"), 
            desc = "Show window list", 
        ), 

        # Misc
        Key(
            [], 
            "Print", 
            lazy.spawn("flameshot gui"), 
            desc = "Take a screenshot", 
        ), 
    ]

    # Navigating qtile groups
    if len(groups) > 10:
        raise Exception("Too many groups to assign a shortcut to.")

    for i, group in enumerate(groups):
        keys.extend(
            [
                Key(
                    [SUPER], 
                    str((i + 1) % 10), 
                    lazy.group[group.name].toscreen(), 
                    desc = f"Switch to group {group.name}", 
                ), 

                Key(
                    [SUPER, SHIFT], 
                    str((i + 1) % 10), 
                    lazy.window.togroup(
                        group.name, 
                        switch_group = False, 
                    ), 
                    desc = f"Moved focused window to group {group.name}", 
                ), 
            ]
        )

    return keys


# Note: Why don't the Drag and Click classes have a desc argument 
#       while the Key class does? Is this a discrepancy?
def gen_mouse_motions():
    mouse = [
        Drag(
            [SUPER], 
            "Button1", 
            lazy.window.set_position(), 
            start = lazy.window.get_position(), 
            # desc = "Move floating window", 
        ), 
    
        Drag(
            [SUPER], 
            "Button2", 
            lazy.window.set_size_floating(), 
            start = lazy.window.get_size(), 
            # desc = "Resize window", 
        ), 
    
        Click(
            [SUPER], 
            "Button3", 
            lazy.window.toggle_floating(), 
            # desc = "Toggle between floating and docked window"
        ), 
    ]
    
    return mouse
