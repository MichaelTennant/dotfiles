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
This file defines the primary and secondry screen layouts
~/.config/qtile/screens.py

Requires:
 - Noto Sans Font Family
----------------------------------------------------------------
"""

from libqtile import bar, widget
from libqtile.config import Screen

from colour_palette import MACCHIATO as COLOURS

__all__ = [
    "widget_defaults", 
    "extension_defaults", 
    "gen_primary_screen", 
    "gen_secondry_screen", 
]


widget_defaults = {
    "font": "Noto Sans Medium", 
    "fontsize": 12, 
    "padding": 3, 
}

extension_defaults = {
    "font": "Noto Sans Medium", 
    "fontsize": 12, 
    "padding": 3, 
}


def gen_primary_screen(wallpaper=None, wallpaper_mode=None, wlan_interface=None):
    if wlan_interface:
        wlan_widget = [
            widget.Spacer(
                length = 8, 
            ), 

            widget.Wlan(
                interface = wlan_interface, 
                format = "{essid} {percent:2.0%}", 
            ), 

            widget.Spacer(
                length = 8, 
            ), 
        ]

    else:
        wlan_widget = [
            widget.Spacer(
                length = 8
            ), 
        ]


    screen = Screen(
        bottom = bar.Bar(
            [
                widget.CurrentLayoutIcon(), 

                widget.Spacer(
                    length = 8, 
                ), 

                widget.GroupBox(), 

                widget.Spacer (
                    length = 8, 
                ), 

                widget.WindowName(), 
                widget.Systray(), 

                *wlan_widget, 

                widget.Clock(
                    format = "%A, %d %B %H:%M", 
                ), 

                widget.Spacer(
                    length = 4, 
                )
            ], 

            24, 
            background = COLOURS[22], 
            border_color = COLOURS[22], 
            border_width = 4, 
        ), 

        wallpaper = wallpaper, 
        wallpaper_mode = wallpaper_mode, 

        x11_drag_polling_rate = 60
    )

    return screen

def gen_secondry_screen(wallpaper=None, wallpaper_mode=None):
    screen = Screen(
        bottom = bar.Bar(
            [
                widget.CurrentLayoutIcon(), 

                widget.Spacer(
                    length = 8, 
                ), 

                widget.GroupBox(), 

                widget.Spacer (
                    length = 8, 
                ), 

                widget.WindowName(), 

                widget.Clock(
                    format = "%A, %d %B %H:%M", 
                ), 

                widget.Spacer(
                    length = 4, 
                )

            ], 

            24, 
            background = COLOURS[22], 
            border_color = COLOURS[22], 
            border_width = 4, 

        ), 

        wallpaper = wallpaper, 
        wallpaper_mode = wallpaper_mode, 

        x11_drag_polling_rate = 60, 
    )

    return screen
