#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pomow.py: Implementation a Pomodoro timer"""
__author__ = "linxuil"

import tkinter as tk

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.time_left = 25 * 60
        self.is_paused = True
        self.master.title("Pomodoro Timer")
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg='white')
        self.canvas.pack()
        self.draw_timer()
        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT)
        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_timer)
        self.pause_button.pack(side=tk.LEFT)
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT)

    def draw_timer(self):
        self.canvas.delete("all")
        x, y, r = 200, 200, 150  # center coordinates and radius
        self.canvas.create_oval(x-r, y-r, x+r, y+r)  # draw circle
        time_text = str(self.time_left // 60) + ":" + str(self.time_left % 60).zfill(2)
        self.canvas.create_text(x, y, text=time_text, font=("Arial", 24))

    def start_timer(self):
        if self.is_paused:
            self.is_paused = False
            self.update_timer()

    def pause_timer(self):
        if not self.is_paused:
            self.is_paused = True

    def reset_timer(self):
        self.time_left = 25 * 60
        self.draw_timer()

    def update_timer(self):
        if self.is_paused:
            return
        self.time_left -= 1
        if self.time_left < 0:
            self.time_left = 25 * 60
        self.draw_timer()
        self.master.after(1000, self.update_timer)

def main(): 
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
