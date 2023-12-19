#!/usr/bin/env python3

import datetime
import sys
import time

class Logger:
    def __init__(self, log_file_path, script_name):
        self.log_file_path = log_file_path
        self.script_name = script_name


    def _get_timestamp(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def _write_log_entry(self, status, message):
        timestamp = self._get_timestamp()
        log_entry = f"{timestamp} | {self.script_name} | {status} | {message}\n"
        with open(self.log_file_path, 'a') as log_file:
            log_file.write(log_entry)


    def start(self):
        self.start_time = time.time()
        self._write_log_entry("start", "The script has started")

    def finish(self):
        self._write_log_entry("end", "The script is finished")

    def info(self, message):
        self._write_log_entry("info", message)

    def warning(self, message):
        self._write_log_entry("warning", message)

    def error(self, message):
        self._write_log_entry("error", message)

    def critical(self, message):
        self._write_log_entry("critical", message)
        sys.exit(1)  # Exit on critical error

    def long_run_error(self, seconds):
        elapsed_time = time.time() - self.start_time
        if elapsed_time > seconds:
            self.warning(f"Long run error! Run time is {elapsed_time} second(s)")
