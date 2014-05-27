# Copyright (c) 2013 Alessandro Fragnani de Morais 
#
# The code in licensed under the MIT license

import sublime, sublime_plugin
import os

# valid_extensions = [".pas", ".dfm", ".fmx"]

# .pas -> .dfm / .fmx
# .dfm -> .pas
# .fmx -> .pas
# .dpr -> .dof / .cfg (circular)
# .dpk -> .dof / .cfg (circular)
mapping = {'.pas': '.dfm,.fmx', 
            '.dfm': '.pas',
            '.dpr': '.dof,.cfg'}

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
            s = sublime.load_settings("toggle_delphi_file.sublime-settings")
            use_buffer = s.get("use_buffer", "false")
            if use_buffer:
                self.view.window().open_file(file_name_toggled, sublime.TRANSIENT)
            else:
                self.view.window().open_file(file_name_toggled)
        else:
            sublime.error_message("Toggle file \"" + file_name_toggled + "\" does not exists.")

    def is_visible(self):
        file_extension = os.path.splitext(self.view.file_name())[1]
        file_extension_lowercase = file_extension.lower()
        #print len(valid_extensions)
        print len(mapping)
        print mapping[".pas"]
        print mapping.keys()
        print "splitting" + str(mapping[".pas"].split(",")[0])
        return file_extension_lowercase == ".pas"
