import tkinter as tk
from tkinter import ttk, font, colorchooser, filedialog, messagebox
import os

application = tk.Tk()
application.geometry("1200x600")
application.title("Text Editor")
################### main menu ################

main_menu = tk.Menu()

# file

# file icons
new_icon = tk.PhotoImage(file=r".\icons\new.png")
open_icon = tk.PhotoImage(file=r'.\icons\open.png')
save_icon = tk.PhotoImage(file=r'.\icons\save.png')
save_as_icon = tk.PhotoImage(file=r'.\icons\save_as.png')
exit_icon = tk.PhotoImage(file=r'.\icons\exit.png')


# edit
# edit icons
copy_icon = tk.PhotoImage(file=r'.\icons\copy.png')
paste_icon = tk.PhotoImage(file=r'.\icons\paste.png')
cut_icon = tk.PhotoImage(file=r'.\icons\cut.png')
clear_all_icon = tk.PhotoImage(file=r'.\icons\clear_all.png')
undo_icon = tk.PhotoImage(file=r'.\icons\undo.png')
redo_icon = tk.PhotoImage(file=r".\icons\redo.png")
find_icon = tk.PhotoImage(file=r'.\icons\find.png')


# view

# view icons
tool_bar_icon = tk.PhotoImage(file=r'.\icons\tool_bar.png')
status_bar_icon = tk.PhotoImage(file=r'.\icons\status_bar.png')


# color_theme

# color_theme_icons
light_default_icon = tk.PhotoImage(file=r'.\icons\light_default.png')
light_plus_icon = tk.PhotoImage(file=r'.\icons\light_plus.png')
dark_icon = tk.PhotoImage(file=r'.\icons\dark.png')
red_icon = tk.PhotoImage(file=r'.\icons\red.png')
monokai_icon = tk.PhotoImage(file=r'.\icons\monokai.png')
night_blue_icon = tk.PhotoImage(file=r'.\icons\night_blue.png')

file = tk.Menu(main_menu, tearoff=False)
edit = tk.Menu(main_menu, tearoff=False)
view = tk.Menu(main_menu, tearoff=False)
color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon,
               red_icon, monokai_icon, night_blue_icon)

color_dict = {
    "Light Default": ("#000000", "#ffffff"),
    "Light Plus": ("#474747", "#e0e0e0"),
    "Dark": ("#c4c4c4", "#2d2d2d"),
    "Monokai": ("#d3b774", "#474747"),
    "Night Blue": ("#ededed", "#6b9dc2")
}


# cascade (show menus)
main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Color Theme", menu=color_theme)



#------------------End main menu--------------#


###################toolbar ################
toolbar = ttk.Label(application)
toolbar.pack(side=tk.TOP, fill=tk.X)


# font_box
font_tuples = tk.font.families()
user_font_store = tk.StringVar()
font_box = ttk.Combobox(
    toolbar, width=30, textvariable=user_font_store, state="readonly")
font_box["values"] = font_tuples
font_box.current(font_tuples.index("Arial"))
font_box.grid(row=0, column=0, padx=5)


# size box
user_fontsize_select = tk.IntVar()
font_size = ttk.Combobox(
    toolbar, width=14, textvariable=user_fontsize_select, state="readonly")
font_size["values"] = tuple(range(6, 82, 2))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)


# buttons

# bold button
bold_icon = tk.PhotoImage(file=r'.\icons\bold.png')
bold_btn = ttk.Button(toolbar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# italic button
italic_icon = tk.PhotoImage(file=r'.\icons\italic.png')
italic_btn = ttk.Button(toolbar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

# underline button
underline_icon = tk.PhotoImage(file=r'.\icons\underline.png')
underline_btn = ttk.Button(toolbar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)


# font color button

font_color_icon = tk.PhotoImage(file=r".\icons\font_color.png")
font_color_btn = ttk.Button(toolbar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

# custom bg color button
bg_color_icon = tk.PhotoImage(file=r".\icons\bg_color.png")
bg_color_btn = ttk.Button(toolbar, image=bg_color_icon)
bg_color_btn.grid(row=0, column=6, padx=5)

# left_align btn
align_left_icon = tk.PhotoImage(file=r".\icons\left.png")
align_left_btn = ttk.Button(toolbar, image=align_left_icon)
align_left_btn.grid(row=0, column=7, padx=5)

# center_align btn
align_center_icon = tk.PhotoImage(file=r".\icons\center.png")
align_center_btn = ttk.Button(toolbar, image=align_center_icon)
align_center_btn.grid(row=0, column=8, padx=5)

# right_align btn
align_right_icon = tk.PhotoImage(file=r".\icons\right.png")
align_right_btn = ttk.Button(toolbar, image=align_right_icon)
align_right_btn.grid(row=0, column=9, padx=5)

#------------------End toolbar--------------#


################### text editor ################
text_editor = tk.Text(application, undo=True)
text_editor.config(wrap="word", relief=tk.FLAT)

scroll_bar = tk.Scrollbar(application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


# font family and font size functionality
current_font = "Arial"
current_font_size = 14


def change_font(application):
    global current_font
    current_font = user_font_store.get()
    text_editor.config(font=(current_font, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)


def change_font_size(application):
    global current_font_size
    current_font_size = user_fontsize_select.get()
    text_editor.config(font=(current_font, current_font_size))


font_size.bind("<<ComboboxSelected>>", change_font_size)

# buttons functionality

# bold button functionality


def bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()["weight"] == "normal":
        text_editor.config(font=(current_font, current_font_size, "bold"))
    elif text_property.actual()["weight"] == "bold":
        text_editor.config(font=(current_font, current_font_size, "normal"))


bold_btn.config(command=bold)

# italic button functionality


def italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()["slant"] == "roman":
        text_editor.config(font=(current_font, current_font_size, "italic"))
    elif text_property.actual()["slant"] == "italic":
        text_editor.config(font=(current_font, current_font_size, "roman"))


italic_btn.config(command=italic)

# underline button functionality


def underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()["underline"] == 0:
        text_editor.config(font=(current_font, current_font_size, "underline"))
    elif text_property.actual()["underline"] == 1:
        text_editor.config(font=(current_font, current_font_size, "normal"))


underline_btn.config(command=underline)


# font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.config(fg=color_var[1])


font_color_btn.config(command=change_font_color)


# background custom color functionality
def change_bg_color():
    color_var_bg = tk.colorchooser.askcolor()
    text_editor.config(bg=color_var_bg[1])


bg_color_btn.config(command=change_bg_color)


# align left functionality
def align_left():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "left")


align_left_btn.config(command=align_left)

# align center functionality


def align_center():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "center")


align_center_btn.config(command=align_center)

# align right functionality


def align_right():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("right", justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "right")


align_right_btn.config(command=align_right)


text_editor.configure(font=("Arial", 14))


#------------------End text editor--------------#


################### mini status bar################
status_bar = ttk.Label(application, text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

text_changed = False


def counts(application):
    if text_editor.edit_modified():
        global text_changed
        text_changed = True
        words = len(text_editor.get(1.0, "end-1c").split())
        characters = len(text_editor.get(1.0, "end-1c"))
        status_bar.config(text=f"Characters: {characters}  Words: {words}")
    # to count again and again
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>", counts)
#------------------End mini status bar--------------#


################### main menu functionality ################
# file sub_menus


# golbal variable
url = ""

# new functionality


def new_file(event=None):
    global url
    url = ""
    text_editor.delete(1.0, tk.END)


file.add_command(label="New", image=new_icon, compound=tk.LEFT,
                 accelerator="Ctrl+N", command=new_file)


# open functionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(
    ), title="Select File", filetypes=(("Text File", "*.txt"), ("All files", "*.*")))
    try:
        with open(url, "r") as rf:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, rf.read())

    except FileNotFoundError:
        return
    except:
        return
    application.title(os.path.basename(url))


file.add_command(label="Open", image=open_icon, compound=tk.LEFT,
                 accelerator="Ctrl+O", command=open_file)

# save file


def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, "w", encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(
                ("Text File", "*.txt"), ("All files", "*.*")))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return


file.add_command(label="Save", image=save_icon,
                 compound=tk.LEFT, accelerator="Ctrl+S", command=save_file)

# save as file


def save_as(event=None):
    global url
    try:
        url = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(
            ("Text File", "*.txt"), ("All files", "*.*")))
        content2 = text_editor.get(1.0, tk.END)
        url.write(content2)
        url.close()

    except:
        return


file.add_command(label="Save_as", image=save_as_icon,
                 compound=tk.LEFT, accelerator="Ctrl+Alt+S", command=save_as)

# exit functionality


def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel(
                "Warning", "Do you want to save the file?")
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, "w", encoding="utf-8") as fw:
                        fw.write(content)
                        application.destroy()
                else:
                    content2 = text_editor.get(1.0, tk.END)
                    url = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(
                        ("Text File", "*.txt"), ("All Files", "*.*")))
                    url.write(content2)
                    url.close()
                    application.destroy()
            elif mbox is False:
                application.destroy()
        else:
            application.destroy()
    except:
        return


file.add_command(label="Exit", image=exit_icon,
                 compound=tk.LEFT, accelerator="Ctrl+Q", command=exit_func)


# edit sub_menus
edit.add_command(label="Copy", image=copy_icon,
                 compound=tk.LEFT, accelerator="Ctrl+C", command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste", image=paste_icon,
                 compound=tk.LEFT, accelerator="Ctrl+V", command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut", image=cut_icon,
                 compound=tk.LEFT, accelerator="Ctrl+X", command=lambda: text_editor.event_generate("<Control x>"))
edit.add_command(label="Undo", image=undo_icon,
                 compound=tk.LEFT, accelerator="Ctrl+Z", command=text_editor.edit_undo)
edit.add_command(label="Redo", image=redo_icon,
                 compound=tk.LEFT, accelerator="Ctrl+Y", command=text_editor.edit_redo)
edit.add_command(label="Clear All", image=clear_all_icon,
                 compound=tk.LEFT, command=lambda: text_editor.delete(1.0, tk.END))


#   find functionality
def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove("match", "1.0", tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text_editor.search(
                    word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config(
                    "match", foreground="white", background="blue")

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialog = tk.Toplevel()
    find_dialog.geometry("350x100+500+200")
    find_dialog.title("Find")
    find_dialog.resizable(0, 0)

    # labels
    text_find_label = ttk.Label(find_dialog, text="Find: ")
    text_find_label.grid(row=0, column=0, padx=5, pady=5)

    text_replace_label = ttk.Label(find_dialog, text="Replace: ")
    text_replace_label.grid(row=1, column=0, padx=5, pady=5)


#  entry
    find_input = ttk.Entry(find_dialog, width=30)

    replace_input = ttk.Entry(find_dialog, width=30)

#  button
    find_button = ttk.Button(find_dialog, text="Find", command=find)
    replace_button = ttk.Button(find_dialog, text="Replace", command=replace)


# grid all

    find_input.grid(row=0, column=1, padx=5, pady=5)
    replace_input.grid(row=1, column=1, padx=5, pady=5)

    find_button.grid(row=2, column=0, padx=8, pady=5)
    replace_button.grid(row=2, column=1, padx=8, pady=5)

    find_dialog.mainloop()


edit.add_command(label="Find", image=find_icon,
                 compound=tk.LEFT, accelerator="Ctrl+F", command=find_func)


#
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        toolbar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_tooolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


# view sub_menus
view.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=False,
                     image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label="Status Bar", image=status_bar_icon, onvalue=True,
                     offvalue=False, compound=tk.LEFT, command=hide_statusbar)
# color_theme sub_menus
# color_theme.add_radiobutton(label="Light Default", image=light_default_icon, compound=tk.LEFTT, variable=theme_choice)
# color_theme.add_radiobutton(label="Light Plus", image=light_plus_icon, compound=tk.LEFT, variable=theme_choice)
# color_theme.add_radiobutton(label="Dark", image=dark_icon, compound=tk.LEFT, variable=theme_choice)
# color_theme.add_radiobutton(label="Red", image=red_icon, compound=tk.LEFT, variable=theme_choice)
# color_theme.add_radiobutton(label="Monokai", image=monokai_icon, compound=tk.LEFT, variable=theme_choice)
# color_theme.add_radiobutton(label="Night Blue", image=night_blue_icon, compound=tk.LEFT, variable=theme_choice)

# Alternative color theme sub menus using loop
# color theme


def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(bg=bg_color, fg=fg_color)


count = 0
for i in color_dict:
    color_theme.add_radiobutton(
        label=i, image=color_icons[count], compound=tk.LEFT, variable=theme_choice, command=change_theme)
    count += 1
#------------------End main menu functionality --------------#

application.config(menu=main_menu)

# bind shortcut keys
application.bind("<Control-n>", new_file)
application.bind("<Control-o>", open_file)
application.bind("<Control-s>", save_file)
application.bind("<Control-Alt-s>", save_as)
application.bind("<Control-q>", exit_func)
application.bind("<Control-f>", find_func)

application.mainloop()
