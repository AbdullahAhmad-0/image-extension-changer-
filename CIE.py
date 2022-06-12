from PIL import Image as PIL_Image
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from Autocomplete_Combo import AutocompleteCombobox
import os


class cls_ChangeImageExtension:
    # Main Variables
    title = "Change Image Extension"
    iconPath = "ico.ico"
    wSize, hSize = 500, 200
    mainLbg = '#3C3F41'
    mainFg = '#A2A2A2'
    mainDbg = '#2B2B2B'
    mainWbg = '#45494A'
    mainWbd = '#646464'
    mainWhBg = '#3D6185'
    mainWfg = '#BBBBBB'

    def __init__(self, wind) -> None:
        self.root = wind
        self.root.title(self.title)
        self.root.iconbitmap(self.iconPath)
        self.root.config(bg=self.mainLbg)

        screen_width = self.root.winfo_screenwidth()
        screen_width = (screen_width / 2) - (self.wSize / 2)
        screen_height = self.root.winfo_screenheight()
        screen_height = (screen_height / 2) - (self.hSize / 2)
        self.root.geometry(f'200x200+{int(float(screen_width))}+{int(float(screen_height))}')
        self.root.minsize(self.wSize, self.hSize)
        self.root.maxsize(self.wSize, self.hSize)
        # self.root.overrideredirect(True)
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.focus_force()

        # Variables
        self.var_imageName = StringVar()
        self.var_imageExt = StringVar()
        self.var_saveImage = StringVar()
        self.list_Extension = []
        self.isFolder_Image_Images = 0  # 0 for not selected 1 for folder 2 for image 3 for images
        self.isError = True

        # TTk Style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground=self.mainWbg, background=self.mainWbg)

        y_space = 40
        y_ = y_space
        lbl_iPath = Label(self.root, text='Path:', font="calibri", bg=self.mainLbg, fg=self.mainWfg,
                          highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_iPath.place(x=20, y=y_)
        ent_iPath = Entry(self.root, textvariable=self.var_imageName, border=0, font="calibri", bg=self.mainWbg,
                          fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2,
                          highlightcolor=self.mainWhBg)
        ent_iPath.place(x=130, y=y_, width=270)
        self.root.update()
        btn_openImage = Button(self.root, command=self.open_image, justify=LEFT, text='+', font=('wingdings', 15), bd=0,
                               cursor='hand2', bg=self.mainLbg, activeforeground=self.mainDbg,
                               activebackground=self.mainLbg, fg=self.mainWfg)
        btn_openImage.place(x=400, y=y_, width=30, height=25)
        btn_openImages = Button(self.root, command=self.open_images, justify=LEFT, text='4', font=('wingdings', 15),
                                bd=0, cursor='hand2', bg=self.mainLbg, activeforeground=self.mainDbg,
                                activebackground=self.mainLbg, fg=self.mainWfg)
        btn_openImages.place(x=430, y=y_, width=30, height=25)
        btn_openFolder = Button(self.root, command=self.open_folder, justify=LEFT, text='1', font=('wingdings', 15),
                                bd=0, cursor='hand2', bg=self.mainLbg, activeforeground=self.mainDbg,
                                activebackground=self.mainLbg, fg=self.mainWfg)
        btn_openFolder.place(x=460, y=y_, width=30, height=25)

        def extensionList():
            abcd = PIL_Image.registered_extensions()
            for i in abcd.items():
                aaa = i[0].split('.')
                self.list_Extension.append(f'{aaa[1]} | {i[1]}')

        extensionList()
        y_ += y_space
        lbl_iExtension = Label(self.root, text='Extension:', font="calibri", bg=self.mainLbg, fg=self.mainWfg,
                               highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_iExtension.place(x=20, y=y_)
        ent_iExtension = AutocompleteCombobox(self.root, values=self.list_Extension, textvariable=self.var_imageExt, font="calibri", background=self.mainWbg, foreground=self.mainWfg)
        ent_iExtension.set_completion_list(self.list_Extension)
        ent_iExtension.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.mainWbg}' % ent_iExtension)
        ent_iExtension.place(x=130, y=y_, width=360)
        ent_iExtension.current(0)

        y_ += y_space
        lbl_iSaveLoc = Label(self.root, text='Save Location:', font="calibri", bg=self.mainLbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_iSaveLoc.place(x=20, y=y_)
        ent_iSaveLoc = Entry(self.root, textvariable=self.var_saveImage, border=0, font="calibri", bg=self.mainWbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        ent_iSaveLoc.place(x=130, y=y_, width=330)
        btn_openSave = Button(self.root, command=self.open_save, justify=LEFT, text='=', font=('wingdings', 15), bd=0, cursor='hand2', bg=self.mainLbg, activeforeground=self.mainDbg, activebackground=self.mainLbg, fg=self.mainWfg)
        btn_openSave.place(x=460, y=y_, width=30, height=25)

        y_ += y_space
        btn_border_saveImage = Entry(self.root, border=0, font="calibri", disabledbackground=self.mainWbg, state=DISABLED, disabledforeground=self.mainWfg)
        btn_border_saveImage.place(x=395, y=y_-5, width=100, height=35)
        btn_saveImage = Button(self.root, command=self.save_image, justify=LEFT, text='Convert', font=('calibri', 15), bd=0, cursor='hand2', bg=self.mainLbg, activeforeground=self.mainDbg, activebackground=self.mainLbg, fg=self.mainWfg)
        btn_saveImage.place(x=400, y=y_, width=90, height=25)

        # self.checkSupportedFormat("E:\Python Projects\Ahmad Soft\Image Processing\Converter\img.jpg")

    def open_folder(self):
        folderName = filedialog.askdirectory(title='Select Folder Of Images')
        if folderName != '':
            print(folderName)
            self.isFolder_Image_Images = 1
            self.var_imageName.set(folderName)
            self.checkSupportedFormat(folderName)

    def open_image(self):
        imageName = filedialog.askopenfilename(title='Select Image')
        if imageName != '':
            print(imageName)
            self.isFolder_Image_Images = 2
            self.var_imageName.set(imageName)
            self.checkSupportedFormat(imageName)

    def open_images(self):
        imagesName = filedialog.askopenfilenames(title='Select Images')
        if imagesName != '':
            print(imagesName)
            self.isFolder_Image_Images = 3
            self.var_imageName.set(imagesName)
            self.checkSupportedFormat(imagesName)

    def open_save(self):
        folderName = filedialog.askdirectory(title='Select Folder Of Images')
        self.var_saveImage.set(folderName)

    def save_image(self):
        if not self.isError:
            if self.isFolder_Image_Images == 0:
                messagebox.showerror('Error', 'First Select The Image Path Or Any Folder')
            elif self.var_saveImage == '':
                messagebox.showerror('Error', 'First Select The Save Location')
            elif self.var_imageName == '':
                messagebox.showerror('Error', 'First Select The Image Path Or Any Folder')
            elif self.var_imageExt == '':
                messagebox.showerror('Error', 'First Select The Image Extension')

            elif self.isFolder_Image_Images == 1 or self.isFolder_Image_Images ==3:
                fn = self.var_imageName.get()
                fn = fn.replace('(', '')
                fn = fn.replace(')', '')
                fn = fn.replace('\'', '')
                fn = fn.split(',')
                fn = [i.lstrip() for i in fn]
                print(fn)
                fe = self.var_imageExt.get()
                sl = self.var_saveImage.get()

                er = 0
                ne = 0
                el = []
                for i in fn:
                    name = os.path.basename(i)
                    try:
                        name, _ext = name.split('.')
                        img = PIL_Image.open(i)
                        ext, _ext = fe.split(' | ')

                        saveLoc = f'{sl}/{name}-Edited.{ext}'
                        print(saveLoc)
                        img.save(saveLoc)
                        ne += 1
                    except Exception as e:
                        er += 1
                        el.append(f"{i} | {e}")

                if er == 0:
                    messagebox.showinfo('Conversion Successfully Completed', f'Total Images Found: {ne}\nAll Your image Successfully Converted')
                else:
                    messagebox.showerror(f'Conversion Successfully Completed With {er} Error', f'Total Images found: {ne+er}\nSuccessfully Converted: {ne}\nError In Conversion: {er}\nError In These Files: {el}')

            elif self.isFolder_Image_Images == 2:
                try:
                    fn = self.var_imageName.get()
                    fe = self.var_imageExt.get()
                    sl = self.var_saveImage.get()

                    name = os.path.basename(fn)
                    name, _ext = name.split('.')
                    img = PIL_Image.open(fn)
                    ext, _ext = fe.split(' | ')

                    saveLoc = f'{sl}/{name}-Edited.{ext}'
                    print(saveLoc)
                    img.save(saveLoc)
                except Exception as e:
                    messagebox.showerror('Error', e)

            else:
                messagebox.showerror('Error', 'First Select The Image Path Or Any Folder\nAnd also Save Location')
        else:
            messagebox.showerror('Error', 'First Select The Image Path Or Any Folder\nAnd also Save Location')


    def checkSupportedFormat(self, path):
        if self.isFolder_Image_Images == 1:
            filenames = next(os.walk(path), (None, None, []))[2]
            filenames_ = []
            for i in filenames:
                filenames_.append(path+'/'+i)
            print(filenames)
            countError = 0
            countSuccess = 0
            fetched = []
            ext_l = []
            for path_ in filenames_:
                name = os.path.basename(path_)
                path = os.path.splitext(path_)
                fullname, ext = path[0], path[1]
                print(fullname, name, ext)

                abcd = PIL_Image.registered_extensions()
                er = 0
                for i in abcd.items():
                    if i[0] == ext:
                        er = 1
                        self.isError = False
                        fetched.append(path_)
                        countSuccess += 1
                if er == 0:
                    ext_l.append(f'{ext}')
                    countError += 1
            ext_l = set(ext_l)
            ext_l = list(ext_l)
            if len(ext_l) != 0:
                messagebox.showinfo(title="Error", message=f"Total Founded = {countError+countSuccess}\nTotal Image Found = {countSuccess}\nExtensions Not Supported = {countError}\nSorry We Can't Support These Formats: {ext_l}")
            else:
                messagebox.showinfo(title="Error", message=f"Total Images Found = {countSuccess}")
            self.var_imageName.set(fetched)

        elif self.isFolder_Image_Images == 2:
            name = os.path.basename(path)
            path = os.path.splitext(path)
            fullname, ext = path[0], path[1]
            print(fullname, name, ext)

            abcd = PIL_Image.registered_extensions()
            er = 0
            for i in abcd.items():
                if i[0] == ext:
                    er = 1
                    self.isError = False
                    break
            if er == 0:
                messagebox.showerror(title="Error", message=f"Sorry At This Time We Can't Support {ext} Format")
                self.isError = True

        elif self.isFolder_Image_Images == 3:
            countError = 0
            countSuccess = 0
            fetched = []
            ext_l = []
            for path_ in path:
                name = os.path.basename(path_)
                path = os.path.splitext(path_)
                fullname, ext = path[0], path[1]
                print(fullname, name, ext)

                abcd = PIL_Image.registered_extensions()
                er = 0
                for i in abcd.items():
                    if i[0] == ext:
                        er = 1
                        self.isError = False
                        fetched.append(path_)
                        countSuccess += 1
                if er == 0:
                    ext_l.append(f'{ext}')
                    countError += 1
            ext_l = set(ext_l)
            ext_l = list(ext_l)
            if len(ext_l) != 0:
                messagebox.showinfo(title="Error", message=f"Total Founded = {countError+countSuccess}\nTotal Image Found = {countSuccess}\nExtensions Not Supported = {countError}\nSorry We Can't Support These Formats: {ext_l}")
            else:
                messagebox.showinfo(title="Error", message=f"Total Images Found = {countSuccess}")
            self.var_imageName.set(fetched)


if __name__ == '__main__':
    root = Tk()
    obj = cls_ChangeImageExtension(root)
    root.mainloop()
