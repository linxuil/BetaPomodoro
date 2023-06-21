#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pomow.py: Implementation a Pomodoro timer"""
__author__ = "linxuil"

import tkinter as tk
import simpleaudio as sa
import os

pkg_path = os.path.dirname(os.path.abspath(__file__))
tick_file_path = pkg_path + '/src/tick.wav'
bang_file_path = pkg_path + '/src/bang.wav'

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.time_left = 25 * 60
        self.is_paused = True
        self.sound2_counter = 0
        self.master.title("Pomodoro Timer")
        self.create_widgets()
        self.bind_hotkeys()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg='white')
        self.canvas.pack()
        self.draw_timer()

        self.start_button = tk.Button(self.master, text="Start",
                                      command=self.start_timer)
        self.start_button.pack(side=tk.LEFT)
        self.pause_button = tk.Button(self.master, text="Pause",
                                      command=self.pause_timer)
        self.pause_button.pack(side=tk.LEFT)
        self.reset_button = tk.Button(self.master, text="Reset",
                                      command=self.reset_and_stop_timer)
        self.reset_button.pack(side=tk.LEFT)

    def bind_hotkeys(self):
        self.master.bind("<space>", self.space_key)
        self.master.bind("<Return>", self.reset_and_stop_timer)
        self.master.bind("<Escape>", self.minimize_window)

    def space_key(self, event):
        if self.is_paused:
            self.start_timer()
        else:
            self.pause_timer()

    def minimize_window(self, event):
        self.master.iconify()

    def draw_timer(self):
        self.canvas.delete("all")
        x, y, r = 200, 200, 150  # center coordinates and radius
        self.canvas.create_oval(x-r, y-r, x+r, y+r)  # draw circle
        time_text = f"{self.time_left // 60}:{str(self.time_left % 60).zfill(2)}"
        self.canvas.create_text(x, y, text=time_text, font=("Arial", 24))

    def start_timer(self):
        if self.is_paused:
            self.is_paused = False
            self.update_timer()
            self.play_sound1()
            self.play_sound2()

    def pause_timer(self):
        if not self.is_paused:
            self.is_paused = True

    def reset_and_stop_timer(self, event=None):
        self.is_paused = True
        self.time_left = 25 * 60
        self.sound2_counter = 0
        self.draw_timer()

    def update_timer(self):
        if self.is_paused:
            return
        self.time_left -= 1
        self.sound2_counter += 1
        if self.time_left < 0:
            self.time_left = 25 * 60
        self.draw_timer()
        self.master.after(1000, self.update_timer)

    def play_sound(self, filename):
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()

    def play_sound1(self):
        self.play_sound(tick_file_path)
        if not self.is_paused:
            self.master.after(1000, self.play_sound1)

    def play_sound2(self):
        if self.sound2_counter >= 5:
            self.play_sound(bang_file_path)
            self.sound2_counter = 0
        if not self.is_paused:
            self.master.after(1000, self.play_sound2)

def main(): 
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

