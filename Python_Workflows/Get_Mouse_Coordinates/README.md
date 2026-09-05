# Get Mouse Coordinates On Screen

A practical Python utility I built to quickly capture exact mouse cursor coordinates for automation scripting.

## The Problem It Solves

When building automation scripts, I frequently need precise X and Y coordinates. Especially when dealing with stubborn desktop applications and/or windows that freeze or refuse to close properly. 

This tool gives me a clean countdown so I can position my mouse exactly where needed and instantly get the coordinates.

## Files in this Project

- `get_mouse_coordinates_on_screen.py` - Main tool to capture coordinates
- `example_usage.py` - Shows how to use the captured coordinates in a real automation script

## Quick Start

```bash
pip install pyautogui
python get_mouse_coordinates_on_screen.py
```

## How I Use It in Real Automation Work

Run get_mouse_coordinates_on_screen.py to capture the coordinates I need.
Copy the x and y values into my main automation scripts.
Use them for reliable clicks. Especially for force-closing frozen applications.

This approach has helped me make automation workflows much more robust when working with legacy business systems and internal tools.

## Summary

Simple and reliable coordinate capture.
Useful for error handling and cleanup sections in automation scripts.
Helps turn fragile scripts into more resilient ones.
