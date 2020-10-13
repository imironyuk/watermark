import PySimpleGUI as sg

ISO_HEX_FILE = "_ihf_"
PROBE_HEX_FILE = "_phf_"
PROG_BTN = "_pib_"

progflash_layout = [[sg.T(" "* 5),sg.T("Flash Programmig for Microocntroller"),sg.T(" "* 5)],
                            [sg.T(" "* 6),sg.Frame(layout= [[sg.T("Select file A"),sg.T(" "* 5),
                                                sg.FileBrowse (key=ISO_HEX_FILE,target="-hexfilein-",
                                                                file_types=(('PNG pictures', '*.png'), ('JPEG pictures', '*.jpg'),)),sg.T(" "* 5)]], title= "A",
                                                                title_location="n")],
                            [(sg.T(" "* 7))],
                            [sg.T(" "* 6),sg.Frame ( layout=[[sg.T ( "Select file for B" ),sg.T(" "* 20),
                                                 sg.FileBrowse ( key=PROBE_HEX_FILE,target="-hexfilein-",
                                                                 initial_folder=r"P:\CTM 100101-100200\100197 TankUS 1.25in ATEX probe\Firmware\Released",
                                                                 file_types=(('PNG pictures', '*.png'), ('JPEG pictures', '*.jpg'),)),
                                                 sg.T ( " " * 5 )]], title="B",title_location="n" )],
                            [sg.Text('File'), sg.Input(key="-hexfilein-",size=(100,1))],
                            [sg.T(" "*4), sg.Button("Начать",button_color=('white', '#28a745') , size=(20,3),key = PROG_BTN,disabled=False)],
                            [sg.Frame ( layout=[[sg.Text ( 'Loading Data' ),
                                                 sg.ProgressBar ( 100, size=(65, 20), orientation='h', key='-PROG-',
                                                                  bar_color=('#548EE1', '#234588') )],
                                                [sg.Output ( size=(100, 10), background_color="#234588",text_color='white' )]],
                                        title="Messages",
                                        title_location='n' )]]

progFlashWin = sg.Window ( "Program Flash", size=(800,550)).Layout ( progflash_layout )
flashEvent, flashValue = progFlashWin.Read ( timeout=1 )
print("^C")

while True:
    flashEvent, flashValue = progFlashWin.Read ( timeout=1 )
