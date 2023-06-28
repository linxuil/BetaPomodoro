#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pomow.py: Implementation a Pomodoro timer"""
__author__ = "linxuil"

import tkinter as tk
import simpleaudio as sa
import os

# Path to sound files
pkg_path = os.path.dirname(os.path.abspath(__file__))
tick_file_path = pkg_path + '/src/tick.wav'
bang_file_path = pkg_path + '/src/bang.wav'

class TimerApp:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.time_left = 25 * 60
        self.is_paused = True
        self.sound1_interval = 1  # seconds
        self.sound2_interval = 5 * 60  # seconds
        self.master.title("Pomodoro Timer")
        self.create_widgets()
        self.bind_hotkeys()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg='white')
        self.canvas.pack()
        
        button_frame = tk.Frame(self.master)
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="Start",
                                      command=self.start_timer)
        self.start_button.pack(side=tk.LEFT)
        self.pause_button = tk.Button(button_frame, text="Pause",
                                      command=self.pause_timer)
        self.pause_button.pack(side=tk.LEFT)
        self.reset_button = tk.Button(button_frame, text="Reset",
                                      command=self.reset_and_stop_timer)
        self.reset_button.pack(side=tk.LEFT)

        sound_frame = tk.Frame(self.master)
        sound_frame.pack()

        # Add widgets for configuring sound intervals
        self.sound1_entry = tk.Entry(sound_frame, width=5)
        self.sound1_entry.insert(0, self.sound1_interval)
        self.sound1_entry.pack(side=tk.LEFT)
        self.sound2_entry = tk.Entry(sound_frame, width=5)
        self.sound2_entry.insert(0, self.sound2_interval)
        self.sound2_entry.pack(side=tk.LEFT)
        self.apply_button = tk.Button(sound_frame, text="Apply sound intervals",
                                      command=self.apply_intervals)
        self.apply_button.pack(side=tk.LEFT)

        self.draw_timer()

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
        x, y, r = 200, 200, 150
        self.canvas.create_oval(x-r, y-r, x+r, y+r)
        text = "{}:{:02}".format(self.time_left // 60, self.time_left % 60)
        self.canvas.create_text(x, y, text=text, font=("Helvetica", 36))

    def start_timer(self):
        if self.is_paused:
            self.is_paused = False
            self.master.after(0, self.update_timer)
            self.master.after(0, self.play_sound2)
            self.master.after(self.sound1_interval * 1000, self.play_sound1)

    def pause_timer(self):
        if not self.is_paused:
            self.is_paused = True

    def reset_and_stop_timer(self, event=None):
        self.pause_timer()
        self.time_left = 25 * 60
        self.draw_timer()

    def update_timer(self):
        if not self.is_paused and self.time_left > 0:
            self.time_left -= 1
            self.draw_timer()
            self.master.after(1000, self.update_timer)

    def play_sound(self, filename: str):
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()

    def play_sound1(self):
        if not self.is_paused:
            self.play_sound(tick_file_path)
            self.master.after(self.sound1_interval * 1000, self.play_sound1)

    def play_sound2(self):
        if self.time_left % self.sound2_interval == 0:
            self.play_sound(bang_file_path)
        if not self.is_paused:
            self.master.after(1000, self.play_sound2)

    def apply_intervals(self):
        try:
            new_sound1_interval = int(self.sound1_entry.get())
            new_sound2_interval = int(self.sound2_entry.get())
            if new_sound1_interval > 0 and new_sound2_interval > 0:
                self.sound1_interval = new_sound1_interval
                self.sound2_interval = new_sound2_interval
        except ValueError:
            pass  # ignore invalid input


def main(): 
    root = tk.Tk()
    TimerApp(root)
    root.mainloop()
