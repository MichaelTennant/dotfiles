#!/bin/python

# MIT License
# 
# Copyright (c) 2021 Catppuccin
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
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
This file defines the configution colour palettes
~/.config/qtile/colour_palette.py

The colour palettes used can be found at
https://github.com/catppuccin/catppuccin
----------------------------------------------------------------
"""

FRAPPE = [
    "#f2d5cf",  #  [0] Rosewater
    "#eebebe",  #  [1] Flamingo
    "#f4b8e4",  #  [2] Pink
    "#ca9ee6",  #  [3] Mauve
    "#e78284",  #  [4] Red
    "#ea999c",  #  [5] Maroon
    "#ef9f76",  #  [6] Peach
    "#e5c890",  #  [7] Yellow
    "#a6d189",  #  [8] Green
    "#81c8be",  #  [9] Teal
    "#99d1db",  # [10] Sky
    "#85c1dc",  # [11] Sapphire
    "#8caaee",  # [12] Blue
    "#babbf1",  # [13] Lavender
    "#c6d0f5",  # [14] Text
    "#b5bfe2",  # [15] Subtext 1
    "#a5adce",  # [16] Subtext 0
    "#949cbb",  # [17] Overlay 2
    "#838ba7",  # [18] Overlay 1
    "#737994",  # [19] Overlay 0
    "#626880",  # [20] Surface 2
    "#51576d",  # [21] Surface 1
    "#414559",  # [22] Surface 0
    "#303446",  # [23] Base
    "#292c3c",  # [24] Mantle
    "#232634",  # [25] Crust
]

LATTE = [
    "#dc8a78",  #  [0] Rosewater
    "#dd7878",  #  [1] Flamingo  
    "#ea76cb",  #  [2] Pink      
    "#8839ef",  #  [3] Mauve     
    "#d20f39",  #  [4] Red       
    "#e64553",  #  [5] Maroon    
    "#fe640b",  #  [6] Peach     
    "#df8e1d",  #  [7] Yellow    
    "#40a02b",  #  [8] Green     
    "#179299",  #  [9] Teal      
    "#04a5e5",  # [10] Sky       
    "#209fb5",  # [11] Sapphire  
    "#1e66f5",  # [12] Blue      
    "#7287fd",  # [13] Lavender  
    "#4c4f69",  # [14] Text      
    "#5c5f77",  # [15] Subtext 1 
    "#6c6f85",  # [16] Subtext 0 
    "#7c7f93",  # [17] Overlay 2 
    "#8c8fa1",  # [18] Overlay 1 
    "#9ca0b0",  # [19] Overlay 0 
    "#acb0be",  # [20] Surface 2 
    "#bcc0cc",  # [21] Surface 1 
    "#ccd0da",  # [22] Surface 0 
    "#eff1f5",  # [23] Base      
    "#e6e9ef",  # [24] Mantle    
    "#dce0e8",  # [25] Crust
]

MACCHIATO = [
    "#f4dbd6",  #  [0] Rosewater
    "#f0c6c6",  #  [1] Flamingo
    "#f5bde6",  #  [2] Pink
    "#c6a0f6",  #  [3] Mauve
    "#ed8796",  #  [4] Red
    "#ee99a0",  #  [5] Maroon
    "#f5a97f",  #  [6] Peach
    "#eed49f",  #  [7] Yellow
    "#a6da95",  #  [8] Green
    "#8bd5ca",  #  [9] Teal
    "#91d7e3",  # [10] Sky
    "#7dc4e4",  # [11] Sapphire
    "#8aadf4",  # [12] Blue
    "#b7bdf8",  # [13] Lavender
    "#cad3f5",  # [14] Text
    "#b8c0e0",  # [15] Subtext 1
    "#a5adcb",  # [16] Subtext 0
    "#939ab7",  # [17] Overlay 2
    "#8087a2",  # [18] Overlay 1
    "#6e738d",  # [19] Overlay 0
    "#5b6078",  # [20] Surface 2
    "#494d64",  # [21] Surface 1
    "#363a4f",  # [22] Surface 0
    "#24273a",  # [23] Base
    "#1e2030",  # [24] Mantle
    "#181926",  # [25] Crust
]

MOCHA = [
    "#f5e0dc",  #  [0] Rosewater
    "#f2cdcd",  #  [1] Flamingo
    "#f5c2e7",  #  [2] Pink
    "#cba6f7",  #  [3] Mauve
    "#f38ba8",  #  [4] Red
    "#eba0ac",  #  [5] Maroon
    "#fab387",  #  [6] Peach
    "#f9e2af",  #  [7] Yellow
    "#a6e3a1",  #  [8] Green
    "#94e2d5",  #  [9] Teal
    "#89dceb",  # [10] Sky
    "#74c7ec",  # [11] Sapphire
    "#89b4fa",  # [12] Blue
    "#b4befe",  # [13] Lavender
    "#cdd6f4",  # [14] Text
    "#bac2de",  # [15] Subtext 1
    "#a6adc8",  # [16] Subtext 0
    "#9399b2",  # [17] Overlay 2
    "#7f849c",  # [18] Overlay 1
    "#6c7086",  # [19] Overlay 0
    "#585b70",  # [20] Surface 2
    "#45475a",  # [21] Surface 1
    "#313244",  # [22] Surface 0
    "#1e1e2e",  # [23] Base
    "#181825",  # [24] Mantle
    "#11111b",  # [25] Crust
]
