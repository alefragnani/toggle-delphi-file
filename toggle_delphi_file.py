# Copyright (c) 2013 Alessandro Fragnani de Morais 
#
# The code in licensed under the MIT license

import sublime, sublime_plugin
import os

class ToggleDelphiFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name = os.path.splitext(self.view.file_name())[0]
        file_extension = os.path.splitext(self.view.file_name())[1]

        file_extension_toggle = ""    
        file_extension_lowercase = file_extension.lower()

        if file_extension_lowercase == ".pas":
            file_extension_toggle = ".dfm"
        elif file_extension_lowercase == ".dfm":
            file_extension_toggle = ".pas"
        else:
            sublime.status_message("Unsupported extension (" + file_extension_lowercase + ")")
            return

        file_name_toggled = file_name + file_extension_toggle
        
        if os.path.exists(file_name_toggled):
            self.view.window().open_file(file_name_toggled)
        else:
            sublime.error_message("Toggle file \"" + file_name_toggled + "\" does not exists.")

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0