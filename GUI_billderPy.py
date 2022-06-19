print('meke by Andre Augusto 3f')

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font

# from fontTopLevel import *

class pyPROApp:
    def __init__(self, master):
        global dictDesignWindowPropCollect
        dictDesignWindowPropCollect = {}  #### Dictionary to collect properties of the design window
        self.implementFont_determine = 0    ### Variable that works in conjunction with implementFont command
        self.dictCountFont = {}     ### Dicitonary to store font instances for design window widgets
        self.implementImage_determine = 0   ### Variable that works in conjunction with implementImage command
        self.dictCountImage = {}         ### Dictionary to store PhotoImage instances for design window
        self.count_image_instances = 1
        self.commands_all = {}      ### Dictionary to store commands for all widgets

        self.styleWidgetConfigLabel = ttk.Style()       ###ttk.Style for Main and WidgetToplevel widgets
        self.clickWidgetConfig = 0  # Variable that determines if WidgetConfig Window has been opened earlier

        self.numberFont_2 = 1  ###### Variable for New Font Name
        self.isFontToplevel = 0  #### Variable to determine whether FontToplevel is opened

        self.iswinConfigToplevel = 0    ### Variable to determine wheter winConfigToplevel is opned earlier


        global screen_width, screen_height
        self.master = master
        screen_width = windowPRO.winfo_screenwidth()
        screen_height = windowPRO.winfo_screenheight()

    ### Parameters for Title of Design Window
        dictDesignWindowPropCollect["title"] = f"windowDesign.title('Design Window')"
        
    ### Parameters for Geometry of Design Window
        global new_value_width
        new_value_width = int(screen_width / 2)
        global new_value_height
        new_value_height = int(screen_height / 1.57)
        global new_value_position_x
        new_value_position_x = int(screen_width / 4.5)
        global new_value_position_y
        new_value_position_y = int(screen_height / 3.36)
        dictDesignWindowPropCollect["geometry"] = f"windowDesign.geometry('{new_value_width}x{new_value_height}+" \
                                                  f"{new_value_position_x}+{new_value_position_y}')"

        ######## Main Window
        windowPRO.title("BuildIt")
        windowPRO.geometry(
            "%dx%d+%d+%d" % (screen_width / 2, screen_height / 8, screen_width / 4.5, (screen_height / 20) - 20))

        ####### Main Menu Widget
        Menu_main = Menu(master)

        ### comms for Code Gen
        def comm4compile_text():
            codeGen = CodeGenerate()
            codeGen.compile2Text()

        def comm4compile_python():
            codeGen2 = CodeGenerate()
            codeGen2.compile2PythonFile()

        command4Code_Gen = Menu()
        command4Code_Gen.add_command(label = "To Python File", command = comm4compile_python)
        command4Code_Gen.add_command(label="To pyPRO's NotePad", command = comm4compile_text)


        ### comms for Beautify
        cascade_change_theme = Menu()
        cascade_change_theme.add_command(label="alt", command=lambda: self.styleWidgetConfigLabel.theme_use("alt"))
        cascade_change_theme.add_command(label="clam", command=lambda: self.styleWidgetConfigLabel.theme_use("clam"))
        cascade_change_theme.add_command(label = "classic", command = lambda: self.styleWidgetConfigLabel.theme_use("classic"))
        cascade_change_theme.add_command(label = "default", command = lambda: self.styleWidgetConfigLabel.theme_use("default"))
        cascade_change_theme.add_command(label="vista", command=lambda: self.styleWidgetConfigLabel.theme_use("vista"))
        cascade_change_theme.add_command(label="winnative", command=lambda: self.styleWidgetConfigLabel.theme_use("winnative"))
        cascade_change_theme.add_command(label="xpnative", command=lambda: self.styleWidgetConfigLabel.theme_use("xpnative"))

        command4Beautify = Menu()
        command4Beautify.add_separator()
        command4Beautify.add_command(label = "Default Theme", command=lambda: self.styleWidgetConfigLabel.theme_use("vista"))
        command4Beautify.add_cascade(label = "Change Theme", menu = cascade_change_theme)
        command4Beautify.add_separator()

        ### comms for Window Setup
        def command4winConfig():
            global winsetupObject
            winsetupObject = DesignWindowSetup()
        command4Window = Menu()
        command4Window.add_command(label = "Window Setup", command = command4winConfig)


        Menu_main.add_cascade(label="Code Gen", menu=command4Code_Gen)  ### CodeGen cass
        Menu_main.add_cascade(label="Beautify", menu = command4Beautify) ### Beautify cass
        Menu_main.add_cascade(label="Edit")
        Menu_main.add_cascade(label="Window", menu = command4Window)
        master.config(menu=Menu_main)  ##### Configure main menu widget to window

        self.toplevel4WidgetToolkit()  #####Run Widget Toolkit Toplevel

    def toplevel4WidgetToolkit(self):  ####### Creates Wigets Toolkit Window and All Inside It
        ####### Top level for Widget Toolkit
        toplevelWidgetToolkit = Toplevel(self.master)
        toplevelWidgetToolkit.transient(self.master)
        toplevelWidgetToolkit.geometry("%dx%d+%d+%d" % (207, screen_height/1.105, screen_width/168, screen_height/35))
        toplevelWidgetToolkit.title("Widgets Toolkit")
        toplevelWidgetToolkit.resizable(False, True)
        print(toplevelWidgetToolkit.winfo_screenwidth())
        ####### Scrollbar for Main Widgets
        scrollbarWidgetToolkit = ttk.Scrollbar(toplevelWidgetToolkit, )
        scrollbarWidgetToolkit.pack(side=RIGHT, fill=Y)

        ####### Canvas for Widget Toolkit
        canvasWidgetToolkit = Canvas(toplevelWidgetToolkit, highlightthickness=0,
                                     yscrollcommand=scrollbarWidgetToolkit.set, width=207,
                                     height=screen_height/1.105)
        canvasWidgetToolkit.pack(side=LEFT, )

        ####### Frame to contain all Main Widgets
        frameWidgetToolkit = ttk.Frame(canvasWidgetToolkit)
        frameWidgetToolkit.pack()
        # n, ne, e, se, s, sw, w, nw, or center
        canvasWidgetToolkit.create_window((0, 0), window=frameWidgetToolkit, anchor=NW)

        scrollbarWidgetToolkit.config(
            command=canvasWidgetToolkit.yview)  #### Set scrollbarWidgetToolkit for canvasWidgetToolkit

        toplevelWidgetToolkit.bind("<Configure>", lambda event: canvasWidgetToolkit.config(
            scrollregion=canvasWidgetToolkit.bbox(ALL)))  #### Bind Scroll region to Configure Event

        ######### Widgets Placement for the Widget Toolkit

        ### All Main Widgets Here

        # Label  for Tk Widgets
        label_tk_widgets = ttk.Label(frameWidgetToolkit, text="tk Widgets", font=("Onyx", 15, "bold"))
        label_tk_widgets.pack(anchor=N, pady=5)

        # Main Button Widget
        self.widget_button = ttk.Button(frameWidgetToolkit, text="Button", style="main.TButton",
                                        command=lambda: self.determineButton("button"))
        self.widget_button.pack(anchor=W, )

        # Main Checkbutton Widget
        widget_checkbutton = ttk.Button(frameWidgetToolkit, text="Checkbutton", style="main.TButton",
                                        command=lambda: self.determineCheckbutton("checkbutton"))
        widget_checkbutton.pack(anchor=W, )

        # Main Entry Widget
        widget_entry = ttk.Button(frameWidgetToolkit, text="Entry", style="main.TButton",
                                  command=lambda: self.determineEntry("entry"))
        widget_entry.pack(anchor=W, )

        # Main Label Widget
        widget_label = ttk.Button(frameWidgetToolkit, text="Label", style="main.TButton",
                                  command=lambda: self.determineLabel("label"))
        widget_label.pack(anchor=W, )

        # Main Listbox Widget
        widget_listbox = ttk.Button(frameWidgetToolkit, text="Listbox", style="main.TButton",
                                    command=lambda: self.determineListbox("listbox"))
        widget_listbox.pack(anchor=W)

        # Main Menu Widget
        widget_menu = ttk.Button(frameWidgetToolkit, text="Menu", style="main.TButton", command=self.mainMenu)
        widget_menu.pack(anchor=W)

        # Main Menubutton Widget
        widget_menubutton = ttk.Button(frameWidgetToolkit, text="Menubutton", style="main.TButton",
                                       command=lambda: self.determineMenubutton("menubutton"))
        widget_menubutton.pack(anchor=W)

        # Main Message Widget
        widget_message = ttk.Button(frameWidgetToolkit, text="Message", style="main.TButton",
                                    command=lambda: self.determineMessage("message"))
        widget_message.pack(anchor=W)

        # Main OptionMenu Widget
        widget_optionmenu = ttk.Button(frameWidgetToolkit, text="OptionMenu", style="main.TButton",
                                       command=lambda: self.mainOptionMenu("optionmenu"))
        widget_optionmenu.pack(anchor=W)

        # Main Radiobutton Widget
        widget_radiobutton = ttk.Button(frameWidgetToolkit, text="Radiobutton", style="main.TButton",
                                        command=lambda: self.determineRadiobutton("radiobutton"))
        widget_radiobutton.pack(anchor=W, )

        # Main Scale - Horizontal
        widget_scalehorizontal = ttk.Button(frameWidgetToolkit, text="Scale - Horizontal", style="main.TButton",
                                            command=lambda: self.determineScale("scale_horizontal"))
        widget_scalehorizontal.pack(anchor=W, )

        # Main Scale - Vertical
        widget_scalevertical = ttk.Button(frameWidgetToolkit, text="Scale - Vertical", style="main.TButton",
                                          command=lambda: self.determineScale("scale_vertical"))
        widget_scalevertical.pack(anchor=W, )

        # Main Scrollbar - Horizontal
        widget_scrollbar = ttk.Button(frameWidgetToolkit, text="Scrollbar - Horizontal", style="main.TButton",
                                      command=lambda: self.determineScrollbar("scrollbar"))
        widget_scrollbar.pack(anchor=W)

        # Main Scrollbar - Vertical
        widget_scrollbar = ttk.Button(frameWidgetToolkit, text="Scrollbar - Vertical", style="main.TButton",
                                      command=lambda: self.determineScrollbar("scrollbar"))
        widget_scrollbar.pack(anchor=W)

        # Main Spinbox Widget
        widget_spinbox = ttk.Button(frameWidgetToolkit, text="Spinbox", style="main.TButton",
                                    command=lambda: self.determineSpinbox("spinbox"))
        widget_spinbox.pack(anchor=W, )

        # Main Text Widget
        widget_text = ttk.Button(frameWidgetToolkit, text="Text", style="main.TButton",
                                 command=lambda: self.determineText("text"))
        widget_text.pack(anchor=W, )

        # Label for Tk Containers
        label_tk_containers = ttk.Label(frameWidgetToolkit, text="tk Containers", font=("Onyx", 15, "bold"))
        label_tk_containers.pack(anchor=N, pady=5)

        # Main Frame Contain
        widget_frame = ttk.Button(frameWidgetToolkit, text="Frame", style="main.TButton",
                                  command=lambda: self.determineFrame("frame"))
        widget_frame.pack(anchor=W, )

        # Main LabelFrame Contain
        widget_labelframe = ttk.Button(frameWidgetToolkit, text="LabelFrame", style="main.TButton",
                                       command=lambda: self.determineLabelFrame("labelframe"))
        widget_labelframe.pack(anchor=W, )

        # Main PanedWindow Contain
        widget_panedwindow = ttk.Button(frameWidgetToolkit, text="PanedWindow", style="main.TButton",
                                        command=lambda: self.determinePanedWindow("panedwindow"))
        widget_panedwindow.pack(anchor=W, )

        # Main Toplevel Contain
        widget_toplevel = ttk.Button(frameWidgetToolkit, text="Toplevel", style="main.TButton",
                                     command=lambda: self.determineToplevel("toplevel"))
        widget_toplevel.pack(anchor=W, )

        # Styling for Main Buttons
        style_main_buttons = ttk.Style()
        style_main_buttons.configure("main.TButton", width=30, anchor=W, )


    ########## Command for Main tk Widgets
    def determineButton(self, widget_value):
        global iswidget
        iswidget = widget_value

    def mainButton(self):
        self.validateWidgetConfigTopLevelState()
        ### Removal of Unavailable Attributes for this Widget
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineCheckbutton(self, widget_value):
        global iswidget
        iswidget = widget_value

    def mainCheckbutton(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineEntry(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainEntry(self):
        self.validateWidgetConfigTopLevelState()

        self.combo4state.config(values = ("active", "disabled", "normal", "readonly"))  ### Add 'readonly' to state
        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4height.destroy()
        self.spinbox4height.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    ### Addition of Attributes

    def determineLabel(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainLabel(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineListbox(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainListbox(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()


    def mainMenu(self):
        self.validateWidgetConfigTopLevelState()

    ### Removal of Unavailable Attributes for this Widget

    def determineMenubutton(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainMenubutton(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()


    def determineMessage(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainMessage(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def mainOptionMenu(self, widget_value):
        self.validateWidgetConfigTopLevelState()

        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

        ### Removal of Unavailable Attributes for this Widget
        self.validateWidgetConfigTopLevelState()
        self.label4activebackground.destroy()
        self.label4highlightthickness.destroy()
        self.frame4activebackground.destroy()
        self.spinbox4highlightthickness.destroy()
        self.label4activeforeground.destroy()
        self.label4highlightcolor.destroy()
        self.frame4activeforeground.destroy()
        self.frame4highlightcolor.destroy()
        self.label4anchor.destroy()
        self.label4highlightbackground.destroy()
        self.combo4anchor.destroy()
        self.frame4highlightbackground.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4foreground.destroy()
        self.frame4foreground.destroy()
        self.label4font.destroy()
        self.frame4font.destroy()
        self.label4justify.destroy()
        self.combo4justify.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4relief.destroy()
        self.combo4relief.destroy()
        self.label4takefocus.destroy()
        self.frame4takefocus.destroy()
        self.label4height.destroy()
        self.spinbox4height.destroy()
        self.label4cursor.destroy()
        self.combo4cursor.destroy()
        self.label4borderwidth.destroy()
        self.spinbox4borderwidth.destroy()
        self.label4width.destroy()
        self.spinbox4width.destroy()
        self.label4background.destroy()
        self.frame4background.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineRadiobutton(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainRadiobutton(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavialable Attributes for this widget
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineScale(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainScale(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4justify.destroy()  # Remove Justify Attribute
        self.combo4justify.destroy()
        self.label4height.destroy()  # Remove Height Attribute
        self.spinbox4height.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineScrollbar(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainScrollbar(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4font.destroy()
        self.frame4font.destroy()
        self.label4foreground.destroy()  # Remove Foreground Label Attribute
        self.frame4foreground.destroy()
        self.label4height.destroy()
        self.spinbox4height.destroy()
        self.label4justify.destroy()
        self.combo4justify.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineSpinbox(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainSpinbox(self):
        self.validateWidgetConfigTopLevelState()

        self.combo4state.config(values=("active", "disabled", "normal", "readonly"))    ### Add 'readonly' to state
        ### Removal of Unavailable Attributes for this Widget
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4height.destroy()
        self.spinbox4height.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineText(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainText(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4justify.destroy()  # Remove Justify Attribute
        self.combo4justify.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    ###### Command for Main tk Containers
    def determineFrame(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainFrame(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4font.destroy()  # Remove Font  Attribute
        self.frame4font.destroy()
        self.label4foreground.destroy()  # Remove Foreground Label Attribute
        self.frame4foreground.destroy()
        self.label4justify.destroy()  # Remove Justify Attribute
        self.combo4justify.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineLabelFrame(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainLabelFrame(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4justify.destroy()  # Remove Justify Attribute
        self.combo4justify.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determinePanedWindow(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainPanedWindow(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4font.destroy()
        self.frame4font.destroy()
        self.label4foreground.destroy()
        self.frame4foreground.destroy()
        self.label4highlightbackground.destroy()
        self.frame4highlightbackground.destroy()
        self.label4highlightcolor.destroy()
        self.frame4highlightcolor.destroy()
        self.label4highlightthickness.destroy()
        self.spinbox4highlightthickness.destroy()
        self.label4justify.destroy()
        self.combo4justify.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4takefocus.destroy()
        self.frame4takefocus.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()

    def determineToplevel(self, widget_value):
        global iswidget
        iswidget = widget_value     ### Widget Deteminant

    def mainToplevel(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4foreground.destroy()
        self.frame4foreground.destroy()
        self.label4font.destroy()
        self.frame4font.destroy()
        self.label4justify.destroy()
        self.combo4justify.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()


    ###### Commands for >> Font Buttons
    def executeFontToplevel(self):
        self.numberFont_2
        self.isFontToplevel

        global fontObject

        if self.isFontToplevel == 0:
            fontObject = ChooseFont(self.numberFont_2,
                                    self.toplevelWidgetConfig,)  #### Creates font Object and passes in the CHANGED new font name
        elif self.isFontToplevel == 1:
            fontObject.toplevel4Font.destroy()
            fontObject = ChooseFont(self.numberFont_2,
                                    self.toplevelWidgetConfig,)  #### Creates font Object and passes in the CHANGED new font name
        if self.entry4font.get() == "":
            self.entry4font.insert(0, fontObject.fontNameVariable)
        elif self.entry4font.get() != "":
            self.entry4font.delete(0, END)
            self.entry4font.insert(0, fontObject.fontNameVariable)

        self.numberFont_2 += 1
        self.isFontToplevel = 1


class ChooseFont:
    def __init__(self, numberFont_1, master):

        self.toplevel4Font = Toplevel(master)

        self.toplevel4Font.resizable(False, False)
        self.fontScreenWidth = self.toplevel4Font.winfo_screenwidth()
        fontScreenHeight = self.toplevel4Font.winfo_screenheight()
        self.toplevel4Font.transient()
        self.toplevel4Font.geometry("%dx%d+%d+%d" % (self.fontScreenWidth/2.973, 445, self.fontScreenWidth/3, fontScreenHeight/2.5))
        # global selectedFont

        self.numberFont_1 = numberFont_1     #### Variable that determines new Font Name
        self.fontNameVariable = "font_{}".format(self.numberFont_1)     ###### Variable for Font Names
        self.dictFontSettings = {"name": self.fontNameVariable, "family": "Segoe UI", "size": 9}

        self.sampleFont = font.Font(family = "Arial", size= 8)
        windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"] = font.Font(root = windowDesign, **self.dictFontSettings) #### Font object for selected font in Font Window

        self.fontWidgets()    ######## Display Font Toplevel Widgets


    def applyFont(self,):
        # global selectedFont

        getFontFamily = self.comboFontFamily.get()
        self.dictFontSettings["family"] = getFontFamily
        self.sampleFont.config(family = getFontFamily)
        
        getFontSize = int(self.spinboxSize.get())
        self.dictFontSettings["size"] = getFontSize
        self.sampleFont.config(size = getFontSize)

        self.text4Preview.tag_config("tagPreviewText", font = self.sampleFont)
        self.groupStyle = (self.checkVariable1.get(), self.checkVariable2.get(), self.checkVariable3.get(), self.checkVariable4.get())  ##### Tuple that commulates responses from check boxes

        def iterateStyle():
            if fontObject.groupStyle[0] == 1:
                self.sampleFont.config(weight = font.BOLD)
            if fontObject.groupStyle[0] == 0:
                self.sampleFont.config(weight = font.NORMAL)
            if fontObject.groupStyle[1] == 1:
                self.sampleFont.config(slant = font.ITALIC)
            if fontObject.groupStyle[1] == 0:
                self.sampleFont.config(slant = font.ROMAN)
            if fontObject.groupStyle[2] == 1:
                self.sampleFont.config(overstrike = 1)
            if fontObject.groupStyle[2] == 0:
                self.sampleFont.config(overstrike = 0)
            if fontObject.groupStyle[3] == 1:
                self.sampleFont.config(underline = 1)
            if fontObject.groupStyle[3] == 0:
                self.sampleFont.config(underline = 0)
        self.toplevel4Font.after(1, iterateStyle)


    def applyFont_WidgetEvent(self, event):
        self.applyFont()

    def fontWidgets(self):
        ###### Font Family Sec
            ### Label for font family
        labelFontFamily = ttk.Label(self.toplevel4Font, text = "font family:",)
        labelFontFamily.grid(row = 1, column = 1, sticky = N, padx = 20, pady = 10)
            ### Combobox for font family
        get_families = font.families()   ##### Get all Available Font Families
        self.comboFontFamily = ttk.Combobox(self.toplevel4Font, values = get_families, )
        self.comboFontFamily.grid(row = 2, column = 1, sticky = W, padx = 20, pady = 10)
        self.comboFontFamily.set("Segoe UI")

        ###### Font Size Sec
            ### Label font size
        labelFontSize = ttk.Label(self.toplevel4Font, text = "font size:")
        labelFontSize.grid(row = 3, column = 1, sticky = N, padx = 20, pady = 10)
            ### Spinbox
        ##size_var = IntVar()
        ##size_var.initialize (8)
        self.spinboxSize = ttk.Spinbox(self.toplevel4Font, from_ = 8, to = 98, increment = 3, wrap = True, command = self.applyFont)
        self.spinboxSize.grid(row = 4, column = 1, sticky = W, padx = 20, pady = 10)
        self.spinboxSize.set(9)

        Label(self.toplevel4Font, ).grid(row = 5, column = 1)   ####### Spacing Label
        Label(self.toplevel4Font, ).grid(row = 6, column = 1)

        ###### Separator - Horizontal Sec
        seperatorFontHorizontal = ttk.Separator(self.toplevel4Font, orient = HORIZONTAL,  )
        seperatorFontHorizontal.grid(row = 7, column = 1, columnspan = 4, sticky = EW, )

        ###### Separator - Vertical Sec
        separatorFontVertical = ttk.Separator(self.toplevel4Font, orient = VERTICAL)
        separatorFontVertical.grid(row = 1, column = 2, rowspan = 6, sticky = NS, )

        ###### Preview Section
            ### Label for Preview
        labelPreview = ttk.Label(self.toplevel4Font, text = "Preview: ")
        labelPreview.grid(sticky = N, row = 8, column = 0, columnspan = 5, pady = 10)
            ### Text for Preview
        self.text4Preview = Text(self.toplevel4Font, width = int(self.fontScreenWidth/24)+1, height = 10, relief = FLAT, wrap = WORD)
        self.text4Preview.grid(sticky = W, row = 9, column = 0, columnspan = 5, pady = 5)
        self.text4Preview.insert(END, "abcABC")
        self.text4Preview.tag_add("tagPreviewText", 1.0, END)
        self.text4Preview.tag_config("tagPreviewText", font = self.sampleFont,
                                     justify = CENTER, spacing1 = 10)
        self.text4Preview["state"] = "disabled"

        ###### Font Styling Section
            ### Label for font styling
        labelFontStyle = ttk.Label(self.toplevel4Font, text = "font styling:")
        labelFontStyle.grid(row = 1, column = 3, sticky = N, padx = 40, pady = 10)
            ### Check button to select styling
        self.checkVariable1 = IntVar()
        checkFontStyle1 = ttk.Checkbutton(self.toplevel4Font, text = "Bold", variable = self.checkVariable1, command = self.applyFont)
        checkFontStyle1.grid(row = 2, column = 3, sticky = W, padx = 30)
        self.checkVariable2 = IntVar()
        checkFontStyle2 = ttk.Checkbutton(self.toplevel4Font, text = "Italic", variable = self.checkVariable2, command = self.applyFont)
        checkFontStyle2.grid(row = 3, column = 3, sticky = W, padx = 30)
        self.checkVariable3 = IntVar()
        checkFontStyle3 = ttk.Checkbutton(self.toplevel4Font, text = "Overstrike", variable = self.checkVariable3, command = self.applyFont)
        checkFontStyle3.grid(row = 4, column = 3, sticky = W, padx = 30)
        self.checkVariable4 = IntVar()
        checkFontStyle4 = ttk.Checkbutton(self.toplevel4Font, text = "Underline", variable = self.checkVariable4, command = self.applyFont)
        checkFontStyle4.grid(row = 5, column = 3, sticky = W, padx = 30)

        ####### apply Font Button
        def implementFont():
            try:
                self.sampleFont.config(family = fontObject.comboFontFamily.get())
                self.sampleFont.config(size = fontObject.spinboxSize.get())
                windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(family=fontObject.comboFontFamily.get())
                windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(size=fontObject.spinboxSize.get())
                if fontObject.groupStyle[0] == 1:
                    self.dictFontSettings["weight"] = "bold"
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(weight = font.BOLD)
                if fontObject.groupStyle[0] == 0:
                    self.dictFontSettings["weight"] = "normal"
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(weight = font.NORMAL)
                if fontObject.groupStyle[1] == 1:
                    self.dictFontSettings["slant"] = "italic"
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(slant = font.ITALIC)
                if fontObject.groupStyle[1] == 0:
                    self.dictFontSettings["slant"] = "roman"
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(slant = font.ROMAN)
                if fontObject.groupStyle[2] == 1:
                    self.dictFontSettings["overstrike"] = 1
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(overstrike = 1)
                if fontObject.groupStyle[2] == 0:
                    self.dictFontSettings["overstrike"] = 0
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(overstrike = 0)
                if fontObject.groupStyle[3] == 1:
                    self.dictFontSettings["underline"] = 1
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(underline = 1)
                if fontObject.groupStyle[3] == 0:
                    self.dictFontSettings["underline"] = 0
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(underline = 0)

                windowObject.implementFont_determine = 22
                arrangeObject.refreshAttributes()
                windowObject.implementFont_determine = 0
            except AttributeError:
                pass
        
        def resetFont():
            fontObject.sampleFont.config(family = "Segoe UI", size = 9, weight = font.NORMAL, slant = font.ROMAN,
                                         overstrike = 0, underline = 0)
            windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(family = "Segoe UI", size = 9,
                                                weight = font.NORMAL, slant = font.ROMAN, overstrike = 0, underline = 0)
            fontObject.comboFontFamily.set("Segoe UI")
            fontObject.spinboxSize.set(9)
            self.checkVariable1.set(0)
            self.checkVariable2.set(0)
            self.checkVariable3.set(0)
            self.checkVariable4.set(0)

        def closeFont():
            fontObject.toplevel4Font.destroy()

        buttonResetFont = ttk.Button(self.toplevel4Font, text="Reset Font", command=resetFont)
        buttonResetFont.grid(row=11, column=1, sticky = W)

        buttonApplyFont = ttk.Button(self.toplevel4Font, text = "Apply Font", command = implementFont)
        buttonApplyFont.grid(row = 11, columnspan = 5)

        buttonCloseFont = ttk.Button(self.toplevel4Font, text = "Close", command = closeFont)
        buttonCloseFont.grid(row = 11, column = 4, sticky = W)

        ###### Styling for All Font Labels
        style4LabelFontStyling = ttk.Style()
        style4LabelFontStyling.configure("TLabel", font = ("Segoe UI", 9, "bold", "italic"))

        ###### Event Handlers
        self.comboFontFamily.bind("<<ComboboxSelected>>", self.applyFont_WidgetEvent)    ####### Combobox Event
        self.spinboxSize.bind("<Return>", self.applyFont_WidgetEvent)              ####### Spinbox Event for Enter Key
        self.comboFontFamily.bind("<Return>", self.applyFont_WidgetEvent)                ####### Combobox Event for Enter Key

global winConfigStart
winConfigStart = [0]
class DesignWindowSetup:
    global winConfigStart
    def __init__(self):
        if windowObject.iswinConfigToplevel == 0:
            winConfigStart[0] = (Toplevel(master = windowPRO))
            self.winConfig(winConfigStart[0])
        elif windowObject.iswinConfigToplevel == 1:
            winConfigStart[0].destroy()
            winConfigStart[0] = Toplevel(master = windowPRO)
            self.winConfig(winConfigStart[0])
        self.exitDesignWindowSetup()

    def winConfig(self,  get_toplevel_winconfig):
        self.toplevel4winConfig = get_toplevel_winconfig
        self.toplevel4winConfig.geometry("%dx%d+%d+%d" % (620, 535,
                                                          windowPRO.winfo_screenwidth()/4, windowPRO.winfo_screenheight()/5))
        global iswinConfigToplevel
        windowObject.iswinConfigToplevel = 1
        self.placeWidgetsDesign()

    def placeWidgetsDesign(self):
        ### Parameter Assignment for windowDesign geometry meth
        global new_value_width
        new_value_width = int(screen_width / 2)
        global new_value_height
        new_value_height = int(screen_height / 1.57)
        global new_value_position_x
        new_value_position_x = int(screen_width / 4.5)
        global new_value_position_y
        new_value_position_y = int(screen_height / 3.36)
        dictDesignWindowPropCollect["geometry"] = f"windowDesign.geometry({new_value_width}x{new_value_height}+" \
                                                  f"{new_value_position_x}+{new_value_position_y})"

        ### Parameter Assignment for windowDesign resizable meth
        global new_resizable_width
        new_resizable_width = True
        global new_resizable_height
        new_resizable_height = True
        dictDesignWindowPropCollect["resizable"] = f"windowDesign.resizable(width = {new_resizable_width}, " \
                                                   f"height = {new_resizable_height})"

        ### Parameter Assignment for windowDesign overrideredirect
        global new_overrideredirect
        new_overrideredirect = False

        ### Parameter Assignment for maxsize
        global new_maxsize_width
        new_maxsize_width = int(windowPRO.winfo_screenwidth() / 2)
        global new_maxsize_height
        new_maxsize_height = int(windowPRO.winfo_screenheight() / 1.57)

        ### Parameter Assignment for minsize
        global new_minsize_width
        new_minsize_width = int(windowPRO.winfo_screenwidth() / 2)
        global new_minsize_height
        new_minsize_height = int(windowPRO.winfo_screenheight() / 1.57)

        ### main toplevel title
        label4designconfig = ttk.Label(self.toplevel4winConfig, text = "Configure Your GUI Window To Your Taste",
                                       font = ("Courier", 15, "bold"), background = "grey", anchor = CENTER)
        label4designconfig.grid(row = 10, column = 0, columnspan = 9, ipadx = 75)

        Label(self.toplevel4winConfig, text = "").grid(row = 12)

        ### title
        dictDesignWindowPropCollect["title"] = f"windowDesign.title('Design Window')"
        def command4title():
            variable4title = entry4title.get()
            windowDesign.title(variable4title)
            dictDesignWindowPropCollect["title"] = f"windowDesign.title('{variable4title}')"
            
        frame4title_iconphoto = ttk.Frame(self.toplevel4winConfig)
        frame4title_iconphoto.grid(row = 20, column = 0, columnspan = 8)
        label4title = ttk.Label(frame4title_iconphoto, text = "title")
        label4title.grid(row = 20, column = 1, padx = 20)
        entry4title = ttk.Entry(master = frame4title_iconphoto)
        entry4title.grid(row = 20, column = 2,)
        button4title = ttk.Button(frame4title_iconphoto, text=">>", width=3, command = command4title)
        button4title.grid(row=20, column=3, padx=2)

        Label(frame4title_iconphoto, text = "").grid(row = 20, column = 4, padx = 40)

        ### photo
        def command4photo():
            file = filedialog.askopenfile("r", filetypes = [("Portable Network Graphics (PNG)", "*png")])
            value_image = PhotoImage(master = windowDesign, file = file.name)
            windowDesign.iconphoto(False, value_image)
            entry4photo.delete(0,END)
            entry4photo.insert(0, file.name)
            entry4photo["state"] = "readonly"
            dictDesignWindowPropCollect["iconphoto"] = f"PhotoImage(master = windowDesign, file = '{file.name}')"
            dictDesignWindowPropCollect["iconphoto2"] = f"windowDesign.iconphoto(False, IconPhoto)"
            
        label4photo = ttk.Label(frame4title_iconphoto, text = "icon photo")
        label4photo.grid(row = 20, column = 5, padx = 20)
        entry4photo = ttk.Entry(frame4title_iconphoto)
        entry4photo.grid(row = 20, column = 6)
        scroll4photo = ttk.Scrollbar(frame4title_iconphoto, orient = "horizontal", command = entry4photo.xview)
        scroll4photo.grid(row = 21, column = 6, ipadx = 40)
        entry4photo.config(xscrollcommand = scroll4photo.set)
        button4photo = ttk.Button(frame4title_iconphoto, text = ">>", width = 3, command = command4photo)
        button4photo.grid(row = 20, column = 7, padx = 2)

        Label(self.toplevel4winConfig, text = "").grid(row = 27)
        label4geometry = ttk.Label(self.toplevel4winConfig, text = "Geometry (Window Dimensions)",
                                   font = ("Calisto MT", 12, "bold"))
        label4geometry.grid(row = 30, column = 0, columnspan = 2)

        ### geometry width
        def command4width(new_value):
            global new_value_width
            new_value_width = int(float(new_value))
            windowDesign.geometry(
                "%dx%d+%d+%d" % (new_value_width, new_value_height, new_value_position_x,  new_value_position_y))
            label24width.config(text = new_value_width)
            dictDesignWindowPropCollect["geometry"] = f"windowDesign.geometry({new_value_width}, {new_value_height}, " \
                                                      f"{new_value_position_x}, {new_value_position_y})"
        label4width = ttk.Label(self.toplevel4winConfig, text = "width")
        label4width.grid(row = 40, column = 1)
        int_width = IntVar(value = windowPRO.winfo_screenwidth()/2)
        frame4width = ttk.Frame(self.toplevel4winConfig)
        frame4width.grid(row = 40, column = 2)
        label24width = ttk.Label(frame4width, text = int_width.get())
        label24width.pack()
        scale4width = ttk.Scale(frame4width, variable = int_width, from_ = 50,
                                to = windowPRO.winfo_screenwidth(), command = command4width)
        scale4width.pack()

        ### geometry height
        def command4height(new_value):
            global new_value_height
            new_value_height = int(float(new_value))
            windowDesign.geometry(
                "%dx%d+%d+%d" % (new_value_width, new_value_height, new_value_position_x,  new_value_position_y))
            label24height.config(text = new_value_height)
            dictDesignWindowPropCollect["geometry"] = f"windowDesign.geometry({new_value_width}, {new_value_height}, " \
                                                      f"{new_value_position_x}, {new_value_position_y})"
        label4height = ttk.Label(self.toplevel4winConfig, text = "height")
        label4height.grid(row = 50, column = 1)
        int_height = IntVar(value = windowPRO.winfo_screenheight()/1.57)
        frame4height = ttk.Frame(self.toplevel4winConfig)
        frame4height.grid(row = 50, column = 2)
        label24height = ttk.Label(frame4height, text = int_height.get())
        label24height.pack()
        scale4height = ttk.Scale(frame4height, variable = int_height, from_ = 50,
                                 to = windowPRO.winfo_screenheight(), command = command4height)
        scale4height.pack()

        ### position_x relative to screen
        def command4position_x(new_value):
            global new_value_position_x
            new_value_position_x = int(float(new_value))
            windowDesign.geometry(
                "%dx%d+%d+%d" % (new_value_width, new_value_height, new_value_position_x, new_value_position_y))
            label24position_x.config(text = new_value_position_x)
            dictDesignWindowPropCollect["geometry"] = f"windowDesign.geometry({new_value_width}, {new_value_height}, " \
                                                      f"{new_value_position_x}, {new_value_position_y})"
        label4position_x = ttk.Label(self.toplevel4winConfig, text = "x position of Design Window")
        label4position_x.grid(row = 60, column = 1)
        int_position_x = IntVar(value = windowPRO.winfo_screenwidth()/4.5)
        frame4position_x = ttk.Frame(self.toplevel4winConfig)
        frame4position_x.grid(row = 60, column = 2)
        label24position_x = ttk.Label(frame4position_x, text = int_position_x.get())
        label24position_x.pack()
        scale4position_x = ttk.Scale(frame4position_x, variable = int_position_x, from_ = 0,
                                     to = windowPRO.winfo_screenwidth()-50, command = command4position_x)
        scale4position_x.pack()

        ### position_y relative to screen
        def command4position_y(new_value):
            global new_value_position_y
            new_value_position_y = int(float(new_value))
            windowDesign.geometry(
                "%dx%d+%d+%d" % (new_value_width, new_value_height, new_value_position_x, new_value_position_y))
            label24position_y.config(text = new_value_position_y)
            dictDesignWindowPropCollect["geometry"] = f"windowDesign.geometry('{new_value_width}, {new_value_height}, " \
                                                      f"{new_value_position_x}, {new_value_position_y}')"
        label4position_y = ttk.Label(self.toplevel4winConfig, text = "y position of Design Window")
        label4position_y.grid(row = 70, column = 1)
        int_position_y = IntVar(value = windowPRO.winfo_screenheight() / 3.36)
        frame4position_y = ttk.Frame(self.toplevel4winConfig)
        frame4position_y.grid(row = 70, column = 2)
        label24position_y = ttk.Label(frame4position_y, text = int_position_y.get())
        label24position_y.pack()
        scale4position_y = ttk.Scale(frame4position_y, variable = int_position_y, from_ = 0,
                                     to = windowPRO.winfo_screenheight()-50, command = command4position_y)
        scale4position_y.pack()

        ### Window Properties Section Label
        Label(self.toplevel4winConfig, text="").grid(row=71)
        label4geometry = ttk.Label(self.toplevel4winConfig, text="Window Properties",
                                   font=("Calisto MT", 12, "bold"))
        label4geometry.grid(row=72, column=0, columnspan=2, sticky = W)

        ### is resizable_width
        def command4resizable_width():
            global new_resizable_width
            new_resizable_width = bool_resizable_width.get()
            windowDesign.resizable(width = new_resizable_width, height = new_resizable_height)
            dictDesignWindowPropCollect["resizable"] = f"windowDesign.resizable(width = {new_resizable_width}, " \
                                                             f"height = {new_resizable_height})"
        label4resizable_width = ttk.Label(self.toplevel4winConfig, text = "Is width resizable?")
        label4resizable_width.grid(row = 80, column = 1)
        bool_resizable_width = BooleanVar(value = True)
        frame4resizable_width = ttk.Frame(self.toplevel4winConfig)
        frame4resizable_width.grid(row = 80, column = 2)
        radioTrue4resizable_width = ttk.Radiobutton(frame4resizable_width, variable = bool_resizable_width, text = "Yes",
                                                    value = True, command = command4resizable_width)
        radioTrue4resizable_width.pack(side = LEFT, padx = 20)
        radioFalse4resizable_width = ttk.Radiobutton(frame4resizable_width, variable = bool_resizable_width, text = "No",
                                                     value = False, command = command4resizable_width)
        radioFalse4resizable_width.pack(side = RIGHT)

        ### is resizable height
        def command4resizable_height():
            global new_resizable_height
            new_resizable_height = bool_resizable_height.get()
            windowDesign.resizable(width = new_resizable_width, height = new_resizable_height)
            dictDesignWindowPropCollect["resizable"] = f"windowDesign.resizable(width = {new_resizable_width}, " \
                                                             f"height = {new_resizable_height})"
        label4resizable_height = ttk.Label(self.toplevel4winConfig, text="Is height resizable?")
        label4resizable_height.grid(row=90, column=1)
        bool_resizable_height = BooleanVar(value=True)
        frame4resizable_height = ttk.Frame(self.toplevel4winConfig)
        frame4resizable_height.grid(row=90, column=2)
        radioTrue4resizable_height = ttk.Radiobutton(frame4resizable_height, variable=bool_resizable_height, text="Yes",
                                                    value=True, command = command4resizable_height)
        radioTrue4resizable_height.pack(side=LEFT, padx=20)
        radioFalse4resizable_height = ttk.Radiobutton(frame4resizable_height, variable=bool_resizable_height, text="No",
                                                     value=False, command = command4resizable_height)
        radioFalse4resizable_height.pack(side=RIGHT)

        ### override redirect flag
        def command4overrideredirect():
            global new_overrideredirect
            new_overrideredirect = bool_overrideredirect.get()
            windowDesign.overrideredirect(new_overrideredirect)
            dictDesignWindowPropCollect["overrideredirect"] = f"windowDesign.overrideredirect({new_overrideredirect})"
        label4overrideredirect = ttk.Label(self.toplevel4winConfig, text = "Set the override redirect flag?")
        label4overrideredirect.grid(row = 100, column = 1)
        bool_overrideredirect = BooleanVar(value = False)
        frame4overrideredirect = ttk.Frame(self.toplevel4winConfig)
        frame4overrideredirect.grid(row = 100, column =2)
        radioTrue4overrideredirect = ttk.Radiobutton(frame4overrideredirect, variable = bool_overrideredirect,
                                                     text="Yes", value = True, command = command4overrideredirect)
        radioTrue4overrideredirect.pack(side = LEFT, padx = 20)
        radioFalse4overrideredirect = ttk.Radiobutton(frame4overrideredirect, variable = bool_overrideredirect,
                                                      text = "No", value = False, command = command4overrideredirect)
        radioFalse4overrideredirect.pack(side = RIGHT)

        ### maxsize
        def command4maxsize():
            new_maxsize_width = entry4maxsize_width.get()
            new_maxsize_height = entry4maxsize_height.get()
            windowDesign.maxsize(width = new_maxsize_width, height = new_maxsize_height)
            dictDesignWindowPropCollect["maxsize"] = f"windowDesign.maxsize(width = {new_maxsize_width}, " \
                                                     f"height = {new_maxsize_height})"
        label4maxsize = ttk.Label(self.toplevel4winConfig, text = "Maximum size for the window")
        label4maxsize.grid(row = 110, column = 1)
        frame4maxsize = ttk.Frame(self.toplevel4winConfig)
        frame4maxsize.grid(row = 110, column = 2)
        label4maxsize_width = ttk.Label(frame4maxsize, text = "width:", font = ("TkDefaultFont", 9, "bold"))
        label4maxsize_width.grid(row = 1, column = 1)
        entry4maxsize_width = ttk.Entry(frame4maxsize, width = 7)
        entry4maxsize_width.grid(row = 2, column = 1, padx = 5)
        label4maxsize_height = ttk.Label(frame4maxsize, text = "height:", font = ("TkDefaultFont", 9, "bold"))
        label4maxsize_height.grid(row=1, column=2)
        entry4maxsize_height = ttk.Entry(frame4maxsize, width = 7)
        entry4maxsize_height.grid(row=2, column=2)
        button4maxsize = ttk.Button(frame4maxsize, width = 3, text = ">>", command = command4maxsize)
        button4maxsize.grid(row = 1, rowspan = 2, column = 3, padx = 10)

        ### minsize
        def command4minsize():
            new_minsize_width = entry4minsize_width.get()
            new_minsize_height = entry4minsize_height.get()
            windowDesign.minsize(width = new_minsize_width, height = new_minsize_height)
            dictDesignWindowPropCollect["minsize"] = f"windowDesign.minsize(width = {new_minsize_width}, " \
                                                     f"height = {new_minsize_height})"
        label4minsize = ttk.Label(self.toplevel4winConfig, text="Minimum size for the window")
        label4minsize.grid(row=120, column=1)
        frame4minsize = ttk.Frame(self.toplevel4winConfig)
        frame4minsize.grid(row=120, column=2)
        label4minsize_width = ttk.Label(frame4minsize, text="width:", font = ("TkDefaultFont", 9, "bold"))
        label4minsize_width.grid(row=1, column=1)
        entry4minsize_width = ttk.Entry(frame4minsize, width=7)
        entry4minsize_width.grid(row=2, column=1, padx=5)
        label4minsize_height = ttk.Label(frame4minsize, text="height:", font = ("TkDefaultFont", 9, "bold"))
        label4minsize_height.grid(row=1, column=2)
        entry4minsize_height = ttk.Entry(frame4minsize, width=7)
        entry4minsize_height.grid(row=2, column=2)
        button4minsize = ttk.Button(frame4minsize, width=3, text=">>", command = command4minsize)
        button4minsize.grid(row=1, rowspan=2, column=3, padx = 10)
        
        def command4okay_button():
            print(dictDesignWindowPropCollect)
            self.toplevel4winConfig.destroy()
        button4okay = ttk.Button(self.toplevel4winConfig, text = "Okay", command = command4okay_button)
        button4okay.grid(row = 130, column = 7)

    def exitDesignWindowSetup(self):
        pass

        

    # def destroy(self):
    #     self.toplevel4winConfig.destroy()

    
class WidgetArrange:
    def __init__(self):
        global iswidget
        iswidget = 0  ### Variable to determine type of Widget to place on Design Window

        ###  Variables to count type of Widget placed on Design Window
        self.widget_button = 1
        self.widget_checkbutton = 1
        self.widget_entry = 1
        self.widget_label = 1
        self.widget_listbox = 1
        self.widget_menu = 1
        self.widget_menubutton = 1
        self.widget_message = 1
        self.widget_optionmenu = 1
        self.widget_scale = 1
        self.widget_scrollbar = 1
        self.widget_spinbox = 1
        self.widget_text = 1
        self.widget_radiobutton = 1
        self.widget_frame = 1
        self.widget_labelframe = 1
        self.widget_panedwindow = 1
        self.widget_toplevel = 1

        ### Variable List to hold handle Widgets that have been added to the Listbox
        self.list_widget_lists = []  ###

        ### Variable List to hold handle Widgets that have been paned to the PanedWindow
        self.dict_widget_panes = {} ###

        ### Dictionary that contains ATTRIBUTES and VALUES of a widget to be displayed
        self.dictCountWidget = {}

        ### Dictionary that contains place layout configurations of all the widgets
        self.dictLayoutConfig = {}

    def focusWidgetTree(self, event):

        self.focus_get = windowObject.tree4Widget.focus()
        
    def createList(self):

        for gg in windowObject.list_entry_list:
            try:
                gg.get()
                self.dictCountWidget[arrangeObject.focus_get].insert(END, gg.get())

            except:
                pass

            else:
                if gg.get() in self.list_widget_lists:
                    pass
                else:
                    self.list_widget_lists.append(gg.get())

    def createPane(self):

        for gg in windowObject.pane_entry_list:
            try:
                gg.get()
                self.dictCountWidget[gg.get()].lift(self.dictCountWidget[arrangeObject.focus_get])
                self.dictCountWidget[arrangeObject.focus_get].add(self.dictCountWidget[gg.get()])

            except:
                pass

            else:
                list_panes = list(self.dict_widget_panes.values())
                print(list_panes)
                if gg.get() in list_panes:
                    pass
                else:
                    self.dict_widget_panes[gg.get()] = arrangeObject.focus_get


    def motionRelease(self,event):
        global iswidget
        iswidget = None
        try:
            self.focus_get = event.widget.widgetName
            try:
                windowObject.tree4Widget.selection_set(self.focus_get)
            except:
                if self.focus_get.startswith("FramePW"):
                    self.focus_get = event.widget.children["!panedwindow"].widgetName
                    windowObject.tree4Widget.selection_set(self.focus_get)

            event.widget.focus()
            windowObject.tree4Widget.focus(self.focus_get)

            if self.focus_get.startswith("Button"):
                windowObject.determineButton(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                     "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainButton()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    for k,v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:

                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0,v[1])
                        except:
                            eval(f"windowObject.bool_{k}.set(v[1])")


            elif self.focus_get.startswith("Checkbutton"):
                windowObject.determineCheckbutton(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                     "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainCheckbutton()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))

                    for k,v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0,str(v[1]))
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")


            elif self.focus_get.startswith("Entry"):
                windowObject.determineEntry(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                     "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainEntry()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))

                    for k,v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0,v[1])
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("LabelFrame"):
                windowObject.determineLabelFrame(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainLabelFrame()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    print(dictAttributeCollect)
                    for k,v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0)
                            dictAttributeCollect[k][0].insert(0,v[1])
                        except:
                            eval(f"windowObject.bool_{k}.set(v[1])")
                            
                            
            elif self.focus_get.startswith("Label"):
                windowObject.determineLabel(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                     "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainLabel()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))

                    for k,v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0,v[1])
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("Listbox"):
                windowObject.determineListbox(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                     "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainListbox()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))

                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0, v[1])
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("Menubutton"):
                windowObject.determineMenubutton(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainMenubutton()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))

                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0, v[1])
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("Message"):
                windowObject.determineMessage(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainMessage()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    print(dictAttributeCollect)
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            try:
                                dictAttributeCollect[k][0].delete(0, END)
                                dictAttributeCollect[k][0].insert(0, v[1])
                            except AttributeError:
                                eval(f"windowObject.bool_{k}.set(v[1])")
                        except:
                            eval(f"windowObject.int_{k}.set(v[1])")

            elif self.focus_get.startswith("Radiobutton"):
                windowObject.determineRadiobutton(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainRadiobutton()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0, str(v[1]))
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("Scale"):
                windowObject.determineScale(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}

                if event.widget.winfo_name() == "!scale_h":
                    windowObject.spinbox4width.insert(END, int(res["height"])-70)
                elif event.widget.winfo_name() == "!scale_v":
                    windowObject.spinbox4width.insert(END, int(res["width"])-70)
                windowObject.mainScale()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    print(dictAttributeCollect)
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            try:
                                dictAttributeCollect[k][0].delete(0, END)
                                dictAttributeCollect[k][0].insert(0, v[1])
                            except AttributeError:
                                eval(f"windowObject.bool_{k}.set(v[1])")
                        except:
                            eval(f"windowObject.int_{k}.set(v[1])")

            elif self.focus_get.startswith("Spinbox"):
                windowObject.determineSpinbox(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0, str(v[1]))
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("Text"):
                windowObject.determineText(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainText()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0, str(v[1]))
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("Frame"):
                windowObject.determineFrame(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainFrame()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0, str(v[1]))
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("PanedWindow"):

                self.dictCountWidget[event.widget.master.widgetName].config(borderwidth = 2, relief = "solid")

                windowObject.determinePanedWindow(None)
                res = self.dictCountWidget[event.widget.master.widgetName].place_info()
                res_sub = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[event.widget.master.widgetName] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                self.dictLayoutConfig[self.focus_get] = {"relwidth": res_sub["relwidth"], "relheight": res_sub["relheight"],
                                                        "anchor": res_sub["anchor"]}
                windowObject.mainPanedWindow()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            try:
                                dictAttributeCollect[k][0].delete(0, END)
                                dictAttributeCollect[k][0].insert(0, v[1])
                            except AttributeError:
                                eval(f"windowObject.bool_{k}.set(v[1])")
                        except:
                            eval(f"windowObject.int_{k}.set(v[1])")



        except AttributeError:
            pass


    # def release(self, event):
    #     try:
    #         res = self.dictCountWidget[self.identifier].place_info()
    #         print(self.identifier, res)
    #     except AttributeError:
    #         pass

    def refreshAttributes(self):

        try:
            if arrangeObject.focus_get.startswith("Button") == True:
                # self.dictCountWidget[arrangeObject.focus_get].focus()
                # print(arrangeObject.focus_get)
                DragDropResizeWidget.__bases__ = (Button,)

                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]

                listAttr.remove("bd"); listAttr.remove("bg"); listAttr.remove("default"); listAttr.remove("fg");
                listAttr.remove("height"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground, windowObject.entry4activeforeground,
                           windowObject.combo4anchor,
                           windowObject.entry4background, windowObject.combo4bitmap, windowObject.spinbox4borderwidth,
                           windowObject.entry4command, windowObject.combo4compound,
                           windowObject.combo4cursor, windowObject.entry4disabledforeground,
                           windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4image, windowObject.combo4justify,
                           windowObject.combo4overrelief, windowObject.spinbox4padx, windowObject.spinbox4pady,
                           windowObject.combo4relief, windowObject.spinbox4repeatdelay, windowObject.spinbox4repeatinterval,
                           windowObject.combo4state, windowObject.bool_takefocus, windowObject.entry4text,
                           windowObject.entrytextvariable,
                           windowObject.entry4underline, windowObject.entry4wraplength]
                for i,j in zip(listAttr, listVal):

                    if i == "command":
                        if (i == "command") & (j.get() == ""):
                            windowObject.commands_all[arrangeObject.focus_get] = None
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]
                        else:
                            windowObject.commands_all[arrangeObject.focus_get] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j,j.get()]

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "image") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]
                    
                    if (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                                
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                                windowObject.implementFont_determine = 0

                            if windowObject.implementImage_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                                arrangeObject.dictCountWidget[arrangeObject.focus_get].image = j.get()

                                windowObject.implementImage_determine = 0
                                windowObject.count_image_instances += 1
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                try:
                    del dict_[arrangeObject.focus_get]["command"]
                except KeyError:
                    pass

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)
                # print(dict_)
                # print(dictAttributeCollect)
                # print(dictAttributeEditorUpdate)

            elif arrangeObject.focus_get.startswith("Checkbutton") == True:
                DragDropResizeWidget.__bases__ = (Checkbutton,)

                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("fg"); listAttr.remove("height");
                listAttr.remove("offvalue"); listAttr.remove("onvalue");
                listAttr.remove("tristateimage"); listAttr.remove("tristatevalue"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground, windowObject.entry4activeforeground,
                           windowObject.combo4anchor,
                           windowObject.entry4background, windowObject.combo4bitmap, windowObject.spinbox4borderwidth,
                           windowObject.entry4command, windowObject.combo4compound,
                           windowObject.combo4cursor, windowObject.entry4disabledforeground,
                           windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4image, windowObject.bool_indicatoron,
                           windowObject.combo4justify, windowObject.combo4offrelief,
                           windowObject.combo4overrelief, windowObject.spinbox4padx, windowObject.spinbox4pady,
                           windowObject.combo4relief, windowObject.entry4selectcolor, windowObject.entry4selectimage,
                           windowObject.combo4state, windowObject.bool_takefocus, windowObject.entry4text,
                           windowObject.entrytextvariable, windowObject.entry4underline, windowObject.entry4variable,
                           windowObject.entry4wraplength]

                for i, j in zip(listAttr, listVal):
                    if i == "command":
                        if (i == "command") & (j.get() == ""):
                            windowObject.commands_all[arrangeObject.focus_get] = None
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]
                        else:
                            windowObject.commands_all[arrangeObject.focus_get] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "image") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            if windowObject.implementImage_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                arrangeObject.dictCountWidget[arrangeObject.focus_get].image = j.get()

                                windowObject.implementImage_determine = 0
                                windowObject.count_image_instances += 1
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                try:
                    del dict_[arrangeObject.focus_get]["command"]
                except KeyError:
                    pass
                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Entry") == True:
                DragDropResizeWidget.__bases__ = (Entry,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("fg");  listAttr.remove("invcmd");
                listAttr.remove("vcmd"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4background, windowObject.spinbox4borderwidth, windowObject.combo4cursor,
                           windowObject.entry4disabledbackground, windowObject.entry4disabledforeground,
                           windowObject.bool_exportselection, windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4insertbackground,
                           windowObject.spinbox4insertborderwidth, windowObject.spinbox4insertofftime,
                           windowObject.spinbox4insertontime, windowObject.spinbox4insertwidth,
                           windowObject.entry4invalidcommand, windowObject.combo4justify,
                           windowObject.entry4readonlybackground, windowObject.combo4relief,
                           windowObject.entry4selectbackground, windowObject.spinbox4selectborderwidth,
                           windowObject.entry4selectforeground, windowObject.entry4show, windowObject.combo4state,
                           windowObject.bool_takefocus, windowObject.entrytextvariable, windowObject.combo4validate,
                           windowObject.entry4validatecommand, windowObject.entry4xscrollcommand]
                for i,j in zip(listAttr,listVal):

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("LabelFrame") == True:
                DragDropResizeWidget.__bases__ = (LabelFrame,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("class");  listAttr.remove("colormap");
                listAttr.remove("container"); listAttr.remove("fg"); listAttr.remove("height");
                listAttr.remove("visual"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4background, windowObject.spinbox4borderwidth, windowObject.combo4cursor,
                           windowObject.entry4font, windowObject.entry4foreground, windowObject.entry4highlightbackground,
                           windowObject.entry4highlightcolor, windowObject.spinbox4highlightthickness,
                           windowObject.combo4labelanchor, windowObject.entry4labelwidget,
                           windowObject.spinbox4padx, windowObject.spinbox4pady, windowObject.combo4relief,
                           windowObject.bool_takefocus, windowObject.entry4text]

                for i,j in zip(listAttr, listVal):
                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                
                windowPRO.after(40, self.refreshAttributes)


            elif arrangeObject.focus_get.startswith("Label") == True:
                DragDropResizeWidget.__bases__ = (Label,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg"); listAttr.remove("fg"); listAttr.remove("height");
                listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground, windowObject.entry4activeforeground,
                           windowObject.combo4anchor,
                           windowObject.entry4background, windowObject.combo4bitmap, windowObject.spinbox4borderwidth,
                           windowObject.combo4compound,
                           windowObject.combo4cursor, windowObject.entry4disabledforeground,
                           windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4image, windowObject.combo4justify,
                           windowObject.spinbox4padx, windowObject.spinbox4pady,
                           windowObject.combo4relief,
                           windowObject.combo4state, windowObject.bool_takefocus, windowObject.entry4text,
                           windowObject.entrytextvariable,
                           windowObject.entry4underline, windowObject.entry4wraplength]

                for i, j in zip(listAttr, listVal):

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "image") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0

                            if windowObject.implementImage_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                arrangeObject.dictCountWidget[arrangeObject.focus_get].image = j.get()
                                windowObject.implementImage_determine = 0
                                windowObject.count_image_instances += 1
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Listbox") == True:
                DragDropResizeWidget.__bases__ = (Listbox,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("fg"); listAttr.remove("height");
                listAttr.remove("setgrid"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.combo4activestyle, windowObject.entry4background,
                           windowObject.spinbox4borderwidth, windowObject.combo4cursor,
                           windowObject.entry4disabledforeground,
                           windowObject.bool_exportselection, windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness,
                           windowObject.combo4justify, windowObject.entry4listvariable, windowObject.combo4relief,
                           windowObject.entry4selectbackground, windowObject.spinbox4selectborderwidth,
                           windowObject.entry4selectforeground, windowObject.combo4selectmode, windowObject.combo4state,
                           windowObject.bool_takefocus, windowObject.entry4xscrollcommand,
                           windowObject.entry4yscrollcommand]

                for i,j in zip(listAttr,listVal):

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Menubutton") == True:
                DragDropResizeWidget.__bases__ = (Menubutton,)
                self.dictCountWidget[arrangeObject.focus_get].focus()
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg"); listAttr.remove("fg"); listAttr.remove("height");
                listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground, windowObject.entry4activeforeground,
                           windowObject.combo4anchor,
                           windowObject.entry4background, windowObject.combo4bitmap, windowObject.spinbox4borderwidth,
                           windowObject.combo4compound, windowObject.combo4cursor,
                           windowObject.combo4direction, windowObject.entry4disabledforeground,
                           windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4image,
                           windowObject.bool_indicatoron, windowObject.combo4justify, windowObject.entry4menu,
                           windowObject.spinbox4padx, windowObject.spinbox4pady,
                           windowObject.combo4relief, windowObject.combo4state, windowObject.bool_takefocus,
                           windowObject.entry4text, windowObject.entrytextvariable,
                           windowObject.entry4underline, windowObject.entry4wraplength]

                for i,j in zip(listAttr, listVal):

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "image") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0

                            if windowObject.implementImage_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                arrangeObject.dictCountWidget[arrangeObject.focus_get].image = j.get()
                                windowObject.implementImage_determine = 0
                                windowObject.count_image_instances += 1
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Message") == True:
                DragDropResizeWidget.__bases__ = (Message,)
                self.dictCountWidget[arrangeObject.focus_get].focus()

                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg"); listAttr.remove("fg"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.combo4anchor, windowObject.int_aspect,
                           windowObject.entry4background, windowObject.spinbox4borderwidth,
                           windowObject.combo4cursor,
                           windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.combo4justify,
                           windowObject.spinbox4padx, windowObject.spinbox4pady,
                           windowObject.combo4relief,  windowObject.bool_takefocus,
                           windowObject.entry4text, windowObject.entrytextvariable, ]

                for i,j in zip(listAttr, listVal):
                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Radiobutton") == True:
                DragDropResizeWidget.__bases__ = (Radiobutton,)
                self.dictCountWidget[arrangeObject.focus_get].focus()
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg"); listAttr.remove("fg"); listAttr.remove("height");
                listAttr.remove("tristateimage"); listAttr.remove("tristatevalue"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground, windowObject.entry4activeforeground,
                           windowObject.combo4anchor,
                           windowObject.entry4background, windowObject.combo4bitmap, windowObject.spinbox4borderwidth,
                           windowObject.entry4command, windowObject.combo4compound,
                           windowObject.combo4cursor, windowObject.entry4disabledforeground,
                           windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4image,
                           windowObject.bool_indicatoron,
                           windowObject.combo4justify, windowObject.combo4offrelief,
                           windowObject.combo4overrelief, windowObject.spinbox4padx, windowObject.spinbox4pady,
                           windowObject.combo4relief, windowObject.entry4selectcolor, windowObject.entry4selectimage,
                           windowObject.combo4state, windowObject.bool_takefocus, windowObject.entry4text,
                           windowObject.entrytextvariable, windowObject.entry4underline, windowObject.entry4value,
                           windowObject.entry4variable, windowObject.entry4wraplength]

                for i,j in zip(listAttr, listVal):
                    if i == "command":
                        if (i == "command") & (j.get() == ""):
                            windowObject.commands_all[arrangeObject.focus_get] = None
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]
                        else:
                            windowObject.commands_all[arrangeObject.focus_get] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "image") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0

                            if windowObject.implementImage_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                arrangeObject.dictCountWidget[arrangeObject.focus_get].image = j.get()
                                windowObject.implementImage_determine = 0
                                windowObject.count_image_instances += 1
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                try:
                    del dict_[arrangeObject.focus_get]["command"]
                except KeyError:
                    pass
                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Scale") == True:
            # self.dictCountWidget[arrangeObject.focus_get].focus()
            # print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bigincrement"), listAttr.remove("bd"); listAttr.remove("bg"); listAttr.remove("fg");
                listAttr.remove("length"); listAttr.remove("orient"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground,
                           windowObject.entry4background, windowObject.spinbox4borderwidth,
                           windowObject.entry4command,
                           windowObject.combo4cursor, windowObject.spinbox4digits,
                           windowObject.entry4font, windowObject.entry4foreground, windowObject.entry4from_,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4label,
                           windowObject.combo4relief, windowObject.spinbox4repeatdelay, windowObject.spinbox4repeatinterval,
                           windowObject.entry4resolution, windowObject.bool_showvalue, windowObject.int_sliderlength,
                           windowObject.combo4sliderrelief,
                           windowObject.combo4state, windowObject.bool_takefocus, windowObject.entry4tickinterval,
                           windowObject.entry4to, windowObject.entry4troughcolor, windowObject.entry4variable]
                for i,j in zip(listAttr, listVal):
                    if i == "command":
                        if (i == "command") & (j.get() == ""):
                            windowObject.commands_all[arrangeObject.focus_get] = None
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]
                        else:
                            windowObject.commands_all[arrangeObject.focus_get] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "label") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                try:
                    del dict_[arrangeObject.focus_get]["command"]
                except KeyError:
                    pass
                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Spinbox") == True:
                DragDropResizeWidget.__bases__ = (Spinbox,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("fg");  listAttr.remove("invcmd");
                listAttr.remove("vcmd"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground,windowObject.entry4background,
                           windowObject.spinbox4borderwidth, windowObject.entry4buttonbackground,
                           windowObject.combo4buttoncursor, windowObject.combo4buttondownrelief,
                           windowObject.combo4buttonuprelief, windowObject.entry4command,windowObject.combo4cursor,
                           windowObject.entry4disabledbackground, windowObject.entry4disabledforeground,
                           windowObject.bool_exportselection, windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4format, windowObject.entry4from_,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4increment,
                           windowObject.entry4insertbackground,
                           windowObject.spinbox4insertborderwidth, windowObject.spinbox4insertofftime,
                           windowObject.spinbox4insertontime, windowObject.spinbox4insertwidth,
                           windowObject.entry4invalidcommand, windowObject.combo4justify,
                           windowObject.entry4readonlybackground, windowObject.combo4relief,
                           windowObject.spinbox4repeatdelay, windowObject.spinbox4repeatinterval,
                           windowObject.entry4selectbackground, windowObject.spinbox4selectborderwidth,
                           windowObject.entry4selectforeground, windowObject.combo4state,
                           windowObject.bool_takefocus, windowObject.entrytextvariable, windowObject.entry4to,
                           windowObject.combo4validate, windowObject.entry4validatecommand,
                           windowObject.entry4values, windowObject.bool_wrap, windowObject.entry4xscrollcommand]
                for i,j in zip(listAttr,listVal):
                    if i == "command":
                        if (i == "command") & (j.get() == ""):
                            windowObject.commands_all[arrangeObject.focus_get] = None
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]
                        else:
                            windowObject.commands_all[arrangeObject.focus_get] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                try:
                    del dict_[arrangeObject.focus_get]["command"]
                except KeyError:
                    pass
                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Text") == True:
                DragDropResizeWidget.__bases__ = (Text,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("endline"); listAttr.remove("fg");
                listAttr.remove("height"); listAttr.remove("setgrid"); listAttr.remove("startline");
                listAttr.remove("tabstyle"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.bool_autoseparators, windowObject.entry4background, windowObject.bool_blockcursor,
                           windowObject.spinbox4borderwidth, windowObject.combo4cursor,
                           windowObject.bool_exportselection, windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4inactiveselectbackground,
                           windowObject.entry4insertbackground,
                           windowObject.spinbox4insertborderwidth, windowObject.spinbox4insertofftime,
                           windowObject.spinbox4insertontime, windowObject.combo4insertunfoccussed,
                           windowObject.spinbox4insertwidth, windowObject.entry4maxundo, windowObject.spinbox4padx,
                           windowObject.spinbox4pady, windowObject.combo4relief,
                           windowObject.entry4selectbackground, windowObject.spinbox4selectborderwidth,
                           windowObject.entry4selectforeground, windowObject.spinbox4spacing1, windowObject.spinbox4spacing2,
                           windowObject.spinbox4spacing3, windowObject.combo4state, windowObject.entry4tabs,
                           windowObject.bool_takefocus, windowObject.bool_undo, windowObject.combo4wrap_Text,
                           windowObject.entry4xscrollcommand, windowObject.entry4yscrollcommand]
                for i,j in zip(listAttr,listVal):

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(1000, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Frame") == True:
                DragDropResizeWidget.__bases__ = (Frame,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("class");  listAttr.remove("colormap");
                listAttr.remove("container"); listAttr.remove("height"); listAttr.remove("visual");
                listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4background, windowObject.spinbox4borderwidth,
                           windowObject.combo4cursor, windowObject.entry4highlightbackground,
                           windowObject.entry4highlightcolor, windowObject.spinbox4highlightthickness,
                           windowObject.spinbox4padx, windowObject.spinbox4pady, windowObject.combo4relief,
                           windowObject.bool_takefocus]

                for i,j in zip(listAttr, listVal):

                    if j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("PanedWindow") == True:
                DragDropResizeWidget.__bases__ = (Frame,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("height");
                listAttr.remove("proxybackground"); listAttr.remove("proxyborderwidth"); listAttr.remove("proxyrelief");
                listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4background, windowObject.spinbox4borderwidth, windowObject.combo4cursor,
                           windowObject.spinbox4handlepad, windowObject.spinbox4handlesize,
                           windowObject.bool_opaqueresize, windowObject.combo4orient,
                           windowObject.combo4relief, windowObject.combo4sashcursor, windowObject.int_sashpad,
                           windowObject.combo4sashrelief, windowObject.int_sashwidth, windowObject.bool_showhandle]

                for i,j in zip(listAttr, listVal):

                    if j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                                
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)



        except (AttributeError, TclError,):
            # print("okay")
            windowPRO.after(10, self.refreshAttributes)


    def executeWidgetsOnDesignWindow(self, event):
        global iswidget

        try:
            if event.widget.widgetName.startswith("PanedWindow"):
                self.dictCountWidget[event.widget.master.widgetName].config(borderwidth = 2, relief = SOLID)
            elif event.widget.widgetName.startswith("FramePW"):
                self.dictCountWidget[event.widget.widgetName].config(borderwidth=2, relief=SOLID)

        except:
             for ii in self.dictCountWidget:
                 if ii.startswith("FramePW"):
                     self.dictCountWidget[ii].config(borderwidth = 0, relief = SOLID)

        if iswidget == "button":

            dict_[list_button[self.widget_button]] = {"text": f"Button{self.widget_button}"}
            dictAttributeEditorUpdate[list_button[self.widget_button]] = {}     ### Initiate storage of Attributes for every widget

            if str(event.widget) == ".":
                self.dictLayoutConfig[list_button[self.widget_button]] = {"x": event.x, "y": event.y, "width": 70,
                                                                          "height": 30, "anchor": "nw"}
            elif str(event.widget).startswith(".!scale") == True:
                self.dictLayoutConfig[list_button[self.widget_button]] = {"x": event.widget.winfo_x() + event.x,
                                                    "y": event.widget.winfo_y() + event.y, "width": 70, "height": 30,
                                                                          "anchor": "nw"}
            elif str(event.widget).startswith(".!dragdropresizewidget") == True:
                self.dictLayoutConfig[list_button[self.widget_button]] = {"x": event.widget.winfo_x() + event.x,
                                                                          "y": event.widget.winfo_y() + event.y,
                                                                          "width": 70, "height": 30, "anchor": "nw"}

            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"Button{self.widget_button}",
                                            text=f"Button{self.widget_button}")
            windowObject.tree4Widget.selection_set(f"Button{self.widget_button}")
            windowObject.tree4Widget.focus(f"Button{self.widget_button}")
            DragDropResizeWidget.__bases__ = (Button,)
            self.dictCountWidget[f"Button{self.widget_button}"] = DragDropResizeWidget(windowDesign,
                                                                         **dict_[list_button[self.widget_button]])
            self.dictCountWidget[f"Button{self.widget_button}"].place(**self.dictLayoutConfig[list_button[self.widget_button]])
            self.dictCountWidget[f"Button{self.widget_button}"].focus()

            self.dictCountWidget[f"Button{self.widget_button}"].widgetName = f"Button{self.widget_button}"
            windowObject.mainButton()
            windowObject.entry4text.delete(0, END)
            windowObject.entry4text.insert(0, f"Button{self.widget_button}")
            windowObject.entry4widget_variable.insert(END, f"Button{self.widget_button}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_button += 1


class CodeGenerate:
    def __init__(self):
        self.compile2Shell()
        


    def compile2Text(self):
        toplevel4Text = Toplevel(master = windowPRO, name = "toplevel_textbox")
        toplevel4Text.geometry = ("400x400+500+500")
        toplevel4Text.resizable(False, False)

        def copy_gen_codes():
            windowPRO.clipboard_clear()
            windowPRO.clipboard_append(self.string_final_codes)
            label_copy = Label(toplevel4Text, text = "Copied Successfully", font = ("Segoe UI", 10, "bold"))
            label_copy.pack(fill = X, )

        menu4copy = Menu(tearoff = False)
        menu4copy.add_command(label = "Copy", command = copy_gen_codes)
        toplevel4Text.config(menu = menu4copy)

        scroll4CompileText = Scrollbar(master=toplevel4Text, orient="vertical", )
        scroll4CompileText.pack(side=RIGHT, fill=Y)

        text4CompileText = Text(master = toplevel4Text, yscrollcommand = scroll4CompileText.set)
        text4CompileText.insert(END, self.string_final_codes)
        text4CompileText.config(state = "disabled")
        text4CompileText.pack()
        scroll4CompileText.config(command = text4CompileText.yview)




    def compile2PythonFile(self):
        file_gen_code = filedialog.asksaveasfile("w", filetypes = [("Python file","*.py")], defaultextension = ".py")
        print(file_gen_code)
        file_open = open(file_gen_code.name, "w")
        file_open.write(self.string_final_codes)
        file_open.close()


    def compile2Shell(self):
        string_command_all = ""
        string_font_all = ""
        string_image_all = ""
        string_button_all = ""
        string_checkbutton_all = ""
        string_entry_all = ""
        string_frame_all = ""
        string_labelframe_all = ""
        string_label_all = ""
        string_listbox_all = ""
        string_menubutton_all = ""
        string_message_all = ""
        string_radiobutton_all = ""
        string_scale_all = ""
        string_spinbox_all = ""
        string_text_all = ""
        string_framepw_all = ""
        string_panedwindow_all = ""
        string_panes = ""
        ### Run main window and its properties
        string_window_prop = ""
        string_iconphoto = ""
        string_header = "from tkinter import *\nfrom tkinter import font \n\nwindowDesign = Tk()"
        string_commands = ''
        string_mainloop = "windowDesign.mainloop()"
        for k,v in zip(dictDesignWindowPropCollect.keys(), dictDesignWindowPropCollect.values()):
            if k == "iconphoto":
                string_iconphoto = f"IconPhoto = {v})"
                continue
            string_window_prop = string_window_prop + v + "\n"
        string_all_header = string_header+"\n"+string_iconphoto+"\n"+string_window_prop

        ##### Commands Output section for Design window widgets
        for com in windowObject.commands_all:
            string_commands = ""
            if windowObject.commands_all[com] == None:
                continue
            else:
                com_value = windowObject.commands_all[com]
                string_commands = string_commands + f"def {com_value}():      # Command for {com}" + "\n"
                string_commands = string_commands + "    pass"
            string_command_all = string_command_all + string_commands

        for i,j,k in zip(arrangeObject.dictCountWidget.keys(), dict_.items(), arrangeObject.dictLayoutConfig.items()):
            new_dict_main = {}
            new_dict_layout = {}
            if i.startswith("FramePW")|i.startswith("PanedWindow"):
                continue;

            else:
                string_font_button = ""
                string_image_button = ""
                if i.startswith("Button"):

                    j = dict(sorted(j[1].items()))
                    widget_font = j["font"]
                    for n in windowObject.dictCountFont:
                        if widget_font == windowObject.dictCountFont[n].name:
                            font_name = windowObject.dictCountFont[n].name
                            actual = windowObject.dictCountFont[n].actual()
                            string_font_button = string_font_button + f"{n} = font.Font(name = '{font_name}', " \
                                                            f"family = '{actual['family']}', " \
                                  f"size = {actual['size']}, weight = '{actual['weight']}', " \
                                  f"slant = '{actual['slant']}', underline = {actual['underline']}, " \
                                  f"overstrike = {actual['overstrike']})\n"
                        else:
                            pass
                    string_font_all = string_font_all + string_font_button

                    widget_image = j["image"]
                    for im in windowObject.dictCountImage:
                        if widget_image == windowObject.dictCountImage[im].name:
                            image_name = windowObject.dictCountImage[im].name
                            image_file = windowObject.dictCountImage[im].cget("file")
                            string_image_button = f"{im} = PhotoImage(name = '{image_name}', file = '{image_file}')\n"
                        else:
                            pass
                    string_image_all = string_image_all + string_image_button

                    k = arrangeObject.dictLayoutConfig[i]
                    widgetStr = f"Button("
                    for jj in j:
                        dd = jj.replace("'", "")
                        dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                        widgetStr = widgetStr + dd
                    if windowObject.commands_all[i] == None:
                        widgetStr = widgetStr + f")"
                    else:
                        widgetStr = widgetStr + f"command = {windowObject.commands_all[i]})"

                    widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, " \
                      f"anchor = '{k['anchor']}')"
                    widgetStr = f"{i} = {widgetStr}\n"
                    string_button_all = string_button_all + widgetStr


                

        for i, j, k in zip(arrangeObject.dictCountWidget.keys(), dict_.items(), arrangeObject.dictLayoutConfig.items()):
            if i.startswith("FramePW"):
                j = dict(sorted(j[1].items()))
                k = arrangeObject.dictLayoutConfig[i]
                widgetStr = f"Frame("
                for jj in j:
                    dd = jj.replace("'", "")
                    dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                    widgetStr = widgetStr + dd
                widgetStr = widgetStr + ")"
                widgetStr = f"{i} = {widgetStr}"
                widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, " \
                      f"anchor = '{k['anchor']}')\n"
                masterPW = i
                string_framepw_all = string_framepw_all + widgetStr

            elif i.startswith("PanedWindow"):
                j = dict(sorted(j[1].items()))
                widgetStr = f"PanedWindow({masterPW}, "
                for jj in j:
                    dd = jj.replace("'", "")
                    dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                    widgetStr = widgetStr + dd
                widgetStr = widgetStr + ")"

                widgetStr = f"{i} = {widgetStr}"
                widgetStr = widgetStr + f"\n{i}.place(relheight = 1, relwidth = 0.8)\n"
                for ke,val in zip(arrangeObject.dict_widget_panes.keys(), arrangeObject.dict_widget_panes.values()):
                    print(arrangeObject.dict_widget_panes)
                    string_panes = string_panes + f"{ke}.lift()\n"
                    string_panes = string_panes + f"{val}.add({ke})\n"
                string_panedwindow_all = string_panedwindow_all + widgetStr


        self.string_final_codes = string_all_header + "\n" + string_command_all + "\n" + string_font_all + string_image_all + \
        string_button_all + string_checkbutton_all + string_entry_all + string_frame_all + string_labelframe_all + \
        string_label_all + string_listbox_all + string_menubutton_all + string_message_all + string_radiobutton_all + \
        string_scale_all + string_spinbox_all + string_text_all + string_framepw_all + string_panedwindow_all + \
        string_panes + "\n" + string_mainloop



class DragDropResizeWidget(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Motion>", self.motion1Both)

    def cursorChange(self, event):
        self["cursor"] = windowObject.combo4cursor.get()

    def startDrag(self, event):
        self.start_drag_x = event.x
        self.start_drag_y = event.y

    def motionDrag(self, event):
        self["cursor"] = "bogosity"
        self.place_configure(anchor="nw")
        new_x = (self.winfo_x() + event.x) - self.start_drag_x
        new_y = (self.winfo_y() + event.y) - self.start_drag_y
        self.place(x=new_x, y=new_y)

    def motion1Both(self, event):
        self.xx = self.winfo_x() + int(self.place_info()["width"])
        self.yy = self.winfo_y() + int(self.place_info()["height"])
        self.ttx = event.x + self.winfo_x()
        self.tty = event.y + self.winfo_y()

        if ((self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)) & (
                (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
            self["cursor"] = "bottom_right_corner"
            self.bind("<Button1-Motion>", self.motionBottomRight)

        elif ((self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (
                self.winfo_x() == self.ttx - 3)) & (
                (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
            self["cursor"] = "bottom_left_corner"
            self.bind("<Button1-Motion>", self.motionBottomLeft)

        elif ((self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (
                self.winfo_y() == self.tty - 3)) & (
                (self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (
                self.winfo_x() == self.ttx - 3)):
            self["cursor"] = "top_left_corner"
            self.bind("<Button1-Motion>", self.motionTopLeft)

        elif ((self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (
                self.winfo_y() == self.tty - 3)) & (
                (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)):
            self["cursor"] = "top_right_corner"
            self.bind("<Button1-Motion>", self.motionTopRight)

        elif (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3):
            self["cursor"] = "right_side"
            self.bind("<Button1-Motion>", self.motionRight)

        elif (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3):
            self["cursor"] = "bottom_side"
            self.bind("<Button1-Motion>", self.motionBottom)

        elif (self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (self.winfo_x() == self.ttx - 3):
            self["cursor"] = "left_side"
            self.bind("<Button1-Motion>", self.motionLeft)

        elif (self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (self.winfo_y() == self.tty - 3):
            self["cursor"] = "top_side"
            self.bind("<Button1-Motion>", self.motionTop)


        else:
            self["cursor"] = windowObject.combo4cursor.get()
            self.bind("<Button-1>", self.startDrag)
            self.bind("<Button1-Motion>", self.motionDrag)
            self.bind("<ButtonRelease-1>", self.cursorChange)

    def motionTop(self, event):
        self.place_configure(x=self.winfo_x(), y=(self.winfo_y() + int(self.place_info()["height"])), anchor="sw")
        new_height = (0 - event.y) + int(self.place_info()["height"])
        self.place_configure(height=new_height)

    def motionBottom(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self.place_configure(height=new_height)

    def motionLeft(self, event):
        self.place_configure(x=(self.winfo_x() + int(self.place_info()["width"])), y=self.winfo_y(), anchor="ne")
        new_width = (0 - event.x) + int(self.place_info()["width"])
        self.place_configure(width=new_width)

    def motionRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        self.place_configure(width=new_width)

    def motionTopLeft(self, event):
        self.place_configure(x=self.winfo_x() + int(self.place_info()["width"]),
                             y=self.winfo_y() + int(self.place_info()["height"]), anchor="se")
        new_width = 0 - event.x + int(self.place_info()["width"])
        new_height = 0 - event.y + int(self.place_info()["height"])
        self.place_configure(width=new_width, height=new_height)

    def motionTopRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y() + int(self.place_info()["height"]), anchor="sw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        new_height = (0 - event.y) + int(self.place_info()["height"])
        self.place_configure(width=new_width, height=new_height)

    def motionBottomLeft(self, event):
        self.place_configure(x=(self.winfo_x() + int(self.place_info()["width"])), y=self.winfo_y(), anchor="ne")
        new_width = 0 - event.x + int(self.place_info()["width"])
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self.place_configure(width=new_width, height=new_height)

    def motionBottomRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self.place_configure(width=new_width, height=new_height)


class Scale_H(Scale):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Motion>", self.motion1Both)

    def cursorChange(self, event):
        self["cursor"] = windowObject.combo4cursor.get()


    def startDrag(self, event):

        self.start_drag_x = event.x
        self.start_drag_y = event.y

    def motionDrag(self, event):
        self["cursor"] = "bogosity"
        self.place_configure(anchor="nw")
        new_x = (self.winfo_x() + event.x) - self.start_drag_x
        new_y = (self.winfo_y() + event.y) - self.start_drag_y
        self.place(x=new_x, y=new_y)

    def motion1Both(self, event):

        if self.identify(event.x, event.y) == "":
            self.xx = self.winfo_x() + int(self.place_info()["width"])
            self.yy = self.winfo_y() + int(self.place_info()["height"])
            self.ttx = event.x + self.winfo_x()
            self.tty = event.y + self.winfo_y()

            if ((self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)) & (
                    (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
                self["cursor"] = "bottom_right_corner"
                self.bind("<Button1-Motion>", self.motionBottomRight)

            elif ((self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (
                    self.winfo_x() == self.ttx - 3)) & (
                    (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
                self["cursor"] = "bottom_left_corner"
                self.bind("<Button1-Motion>", self.motionBottomLeft)

            elif ((self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (
                    self.winfo_y() == self.tty - 3)) & (
                    (self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (
                    self.winfo_x() == self.ttx - 3)):
                self["cursor"] = "top_left_corner"
                self.bind("<Button1-Motion>", self.motionTopLeft)

            elif ((self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (
                    self.winfo_y() == self.tty - 3)) & (
                    (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)):
                self["cursor"] = "top_right_corner"
                self.bind("<Button1-Motion>", self.motionTopRight)

            elif (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3):
                self["cursor"] = "right_side"
                self.bind("<Button1-Motion>", self.motionRight)

            elif (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3):
                self["cursor"] = "bottom_side"
                self.bind("<Button1-Motion>", self.motionBottom)

            elif (self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (self.winfo_x() == self.ttx - 3):
                self["cursor"] = "left_side"
                self.bind("<Button1-Motion>", self.motionLeft)

            elif (self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (self.winfo_y() == self.tty - 3):
                self["cursor"] = "top_side"
                self.bind("<Button1-Motion>", self.motionTop)


            else:
                self["cursor"] = windowObject.combo4cursor.get()
                self.bind("<Button-1>", self.startDrag)
                self.bind("<Button1-Motion>", self.motionDrag)
                self.bind("<ButtonRelease-1>", self.cursorChange)

        else:
            self.bind("<Button1-Motion>", lambda x: None)

    def motionTop(self, event):
        self.place_configure(x=self.winfo_x(), y=(self.winfo_y() + int(self.place_info()["height"])), anchor="sw")
        new_height = (0 - event.y) + int(self.place_info()["height"])
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(height=new_height)

    def motionBottom(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(height=new_height)

    def motionLeft(self, event):
        self.place_configure(x=(self.winfo_x() + int(self.place_info()["width"])), y=self.winfo_y(), anchor="ne")
        new_width = (0 - event.x) + int(self.place_info()["width"])
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(width=new_width)

    def motionRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(width=new_width)

    def motionTopLeft(self, event):
        self.place_configure(x=self.winfo_x() + int(self.place_info()["width"]),
                             y=self.winfo_y() + int(self.place_info()["height"]), anchor="se")
        new_width = 0 - event.x + int(self.place_info()["width"])
        new_height = 0 - event.y + int(self.place_info()["height"])
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(width=new_width, height=new_height)

    def motionTopRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y() + int(self.place_info()["height"]), anchor="sw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        new_height = (0 - event.y) + int(self.place_info()["height"])
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(width=new_width, height=new_height)

    def motionBottomLeft(self, event):
        self.place_configure(x=(self.winfo_x() + int(self.place_info()["width"])), y=self.winfo_y(), anchor="ne")
        new_width = 0 - event.x + int(self.place_info()["width"])
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(width=new_width, height=new_height)

    def motionBottomRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(width=new_width, height=new_height)


class Scale_V(Scale):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Motion>", self.motion1Both)

    def cursorChange(self, event):
        self["cursor"] = windowObject.combo4cursor.get()

    def startDrag(self, event):

        self.start_drag_x = event.x
        self.start_drag_y = event.y

    def motionDrag(self, event):
        self["cursor"] = "bogosity"
        self.place_configure(anchor="nw")
        new_x = (self.winfo_x() + event.x) - self.start_drag_x
        new_y = (self.winfo_y() + event.y) - self.start_drag_y
        self.place(x=new_x, y=new_y)

    def motion1Both(self, event):

        if self.identify(event.x, event.y) == "":
            self.xx = self.winfo_x() + int(self.place_info()["width"])
            self.yy = self.winfo_y() + int(self.place_info()["height"])
            self.ttx = event.x + self.winfo_x()
            self.tty = event.y + self.winfo_y()

            if ((self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)) & (
                    (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
                self["cursor"] = "bottom_right_corner"
                self.bind("<Button1-Motion>", self.motionBottomRight)

            elif ((self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (
                    self.winfo_x() == self.ttx - 3)) & (
                    (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
                self["cursor"] = "bottom_left_corner"
                self.bind("<Button1-Motion>", self.motionBottomLeft)

            elif ((self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (
                    self.winfo_y() == self.tty - 3)) & (
                    (self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (
                    self.winfo_x() == self.ttx - 3)):
                self["cursor"] = "top_left_corner"
                self.bind("<Button1-Motion>", self.motionTopLeft)

            elif ((self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (
                    self.winfo_y() == self.tty - 3)) & (
                    (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)):
                self["cursor"] = "top_right_corner"
                self.bind("<Button1-Motion>", self.motionTopRight)

            elif (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3):
                self["cursor"] = "right_side"
                self.bind("<Button1-Motion>", self.motionRight)

            elif (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3):
                self["cursor"] = "bottom_side"
                self.bind("<Button1-Motion>", self.motionBottom)

            elif (self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (self.winfo_x() == self.ttx - 3):
                self["cursor"] = "left_side"
                self.bind("<Button1-Motion>", self.motionLeft)

            elif (self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (self.winfo_y() == self.tty - 3):
                self["cursor"] = "top_side"
                self.bind("<Button1-Motion>", self.motionTop)


            else:
                self["cursor"] = windowObject.combo4cursor.get()
                self.bind("<Button-1>", self.startDrag)
                self.bind("<Button1-Motion>", self.motionDrag)
                self.bind("<ButtonRelease-1>", self.cursorChange)

        else:
            self.bind("<Button1-Motion>", lambda x: None)

    def motionTop(self, event):
        self.place_configure(x=self.winfo_x(), y=(self.winfo_y() + int(self.place_info()["height"])), anchor="sw")
        new_height = (0 - event.y) + int(self.place_info()["height"])
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(height=new_height)

    def motionBottom(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(height=new_height)

    def motionLeft(self, event):
        self.place_configure(x=(self.winfo_x() + int(self.place_info()["width"])), y=self.winfo_y(), anchor="ne")
        new_width = (0 - event.x) + int(self.place_info()["width"])
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(width=new_width)

    def motionRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(width=new_width)

    def motionTopLeft(self, event):
        self.place_configure(x=self.winfo_x() + int(self.place_info()["width"]),
                             y=self.winfo_y() + int(self.place_info()["height"]), anchor="se")
        new_width = 0 - event.x + int(self.place_info()["width"])
        new_height = 0 - event.y + int(self.place_info()["height"])
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(width=new_width, height=new_height)

    def motionTopRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y() + int(self.place_info()["height"]), anchor="sw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        new_height = (0 - event.y) + int(self.place_info()["height"])
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(width=new_width, height=new_height)

    def motionBottomLeft(self, event):
        self.place_configure(x=(self.winfo_x() + int(self.place_info()["width"])), y=self.winfo_y(), anchor="ne")
        new_width = 0 - event.x + int(self.place_info()["width"])
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(width=new_width, height=new_height)

    def motionBottomRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(width=new_width, height=new_height)

windowPRO = Tk()  ######## Creates Main Window



windowObject = pyPROApp(windowPRO)  ####### Instance Object for pyPROApp class

##### Lists of widget control variables names
list_button = [f"Button{x}" for x in range(0,1000)]    #### list to contain widget control variables names for Button

dict_ = {}                                      #### Dictionary to hold attributes for control variables
dictAttributeEditorUpdate = {}                  #### Dictionary to update Attribute Editor for any selected widget
# dictAttributeCollect = {}                       #### Dictionary to collect attributes to display in Attribute Editor


arrangeObject = WidgetArrange()  ####### Instance Object for WidgetArrange class
arrangeObject.refreshAttributes()


####### Design Window - To Work On
windowDesign = Tk()
windowDesign.title("Design Window")
windowDesign.geometry("%dx%d+%d+%d" % (screen_width / 2, screen_height / 1.57, screen_width / 4.5, screen_height / 3.36))


### Events For Design Window
windowDesign.bind("<Button-1>", arrangeObject.executeWidgetsOnDesignWindow)
windowDesign.bind_all("<ButtonRelease-1>", arrangeObject.motionRelease)

implementFont_determine = None    ### Variable that determines whether to run implementFont command
windowPRO.mainloop()