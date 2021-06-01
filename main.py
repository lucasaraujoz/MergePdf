import glob, PyPDF2, os.path
from natsort import natsorted
from tkinter import filedialog, messagebox
from tkinter import *

root = Tk()

class App():
    def __init__(self):
        self.root = root
        self.screen()
        self.buttons()

        self.root.mainloop()
    def screen(self):
        self.root.title("Merge Pdfs")
        self.root.geometry("300x150")
        self.root.iconbitmap(r'favicon.ico')
        self.root.resizable(False, False)
        self.root.configure(background = "#76D7C4")
    def buttons(self):
        self.lb_qntval = Label(self.root, text = "Void", fg = "black", bg = "white", font = ("Calibri", 11)  )
        self.lb_qntval.pack()

        self.bt_input = Button(self.root, text = 'Input', command = self.input_dir)
        self.bt_input.pack()

        self.lb_output = Label(self.root, text = "Void", fg = "black", bg = "white", font = ("Calibri", 11)  )
        self.lb_output.pack()

        self.bt_output = Button(self.root, text = 'Output', command = self.output)
        self.bt_output.pack()

        self.bt_merge = Button(self.root, text = 'Merge', command = self.merge)
        self.bt_merge.pack()
    def input_dir(self):
        self.open_dir = filedialog.askdirectory()
        self.lb_qntval['text'] = str(self.open_dir)
    def output(self):
        self.output_dir = filedialog.askdirectory()
        self.lb_output['text'] = str(self.output_dir)

    def merge(self):
        self.pdfs = glob.glob(self.open_dir + '\*.pdf') #return all pdfs in a list, with directory
        self.output_dir.replace('/', '\\')
        self.new_merged_pdf = self.output_dir + '\\new_merge_pdf.pdf'
        if os.path.isfile(self.new_merged_pdf):
            result = messagebox.askquestion("Overwrite", "This file already exists, do you want to overwrite it?", icon='warning')
            print(result)
            if result == "yes":
                self.fusion()
                messagebox.showinfo(title=None, message='Done!')
            else:
                messagebox.showwarning(title=None, message= 'Did not merge the pdfs')
        else:
            self.fusion()
            messagebox.showinfo(title=None, message='Done!')

    def fusion(self):
        merge_pdfs = PyPDF2.PdfFileMerger()

        for pdf in natsorted(self.pdfs):
            merge_pdfs.append(pdf, 'rb')

        merge_pdfs.write(open(self.new_merged_pdf, 'wb'))

App()
