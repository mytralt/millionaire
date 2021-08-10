import tkinter as tk
from tkinter.constants import CENTER, COMMAND, DISABLED, LEFT, NORMAL, VERTICAL, W
from tkinter.ttk import Progressbar
from typing import Text
from pygame import mixer

import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voices', voices[1].id)

mixer.init()
#music playing
mixer.music.load('images/kbc.mp3')
mixer.music.play(-1)


#creating tkinter window
root = tk.Tk()
root.title("Millionaire")
# tkinter window with dimensions 1352x652
root.geometry('1270x652+0+0')
root.configure(background='black')
#--------------------------------------------------frames------------------------
leftFrame = tk.Frame(root, bg='black', padx = 90)
leftFrame.grid(row=0, column=0)

topFrame = tk.Frame(leftFrame, bg='black', pady = 15)
topFrame.grid()

centerFrame = tk.Frame(leftFrame, bg='black', pady = 15)
centerFrame.grid(row=1, column=0)

bottomFrame = tk.Frame(leftFrame)
bottomFrame.grid(row=2, column=0)

rightFrame = tk.Frame(root, padx = 50, pady = 25, bg='black')
rightFrame.grid(row=0, column=1)
#--------------------------------------------------Images------------------------
def live50():
    live50_50.config(image=image50_50used, state=DISABLED)
    if quesArea.get(1.0, 'end-1c') == questions[0]:
        btnOption1.config(text='')
        btnOption2.config(text='')
    if quesArea.get(1.0, 'end-1c') == questions[1]:
        btnOption1.config(text='')
        btnOption3.config(text='')
    if quesArea.get(1.0, 'end-1c') == questions[2]:
        btnOption3.config(text='')
        btnOption4.config(text='')
    if quesArea.get(1.0, 'end-1c') == questions[3]:
        btnOption1.config(text='')
        btnOption4.config(text='')
    if quesArea.get(1.0, 'end-1c') == questions[4]:
        btnOption2.config(text='')
        btnOption4.config(text='')
    if quesArea.get(1.0, 'end-1c') == questions[5]:
        btnOption4.config(text='')
        btnOption2.config(text='')
    if quesArea.get(1.0, 'end-1c') == questions[6]:
        btnOption1.config(text='')
        btnOption2.config(text='')
    if quesArea.get(1.0, 'end-1c') == questions[7]:
        btnOption3.config(text='')
        btnOption4.config(text='')

def livepeo():
    livePeople.config(image=imagePeopleused, state=DISABLED)
    progressbarA.place(x=580, y =190)
    progressbarB.place(x=620, y =190)
    progressbarC.place(x=660, y =190)
    progressbarD.place(x=700, y =190)

    lblprogressbarA.place(x=580,y=320)
    lblprogressbarB.place(x=620,y=320)
    lblprogressbarC.place(x=660,y=320)
    lblprogressbarD.place(x=700,y=320)

    if quesArea.get(1.0, 'end-1c')==questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=70)
        progressbarD.config(value=30)
    if quesArea.get(1.0, 'end-1c')==questions[1]:
        progressbarA.config(value=10)
        progressbarB.config(value=80)
        progressbarC.config(value=20)
        progressbarD.config(value=15)
    if quesArea.get(1.0, 'end-1c')==questions[2]:
        progressbarA.config(value=50)
        progressbarB.config(value=95)
        progressbarC.config(value=70)
        progressbarD.config(value=30)
    if quesArea.get(1.0, 'end-1c')==questions[3]:
        progressbarA.config(value=10)
        progressbarB.config(value=25)
        progressbarC.config(value=85)
        progressbarD.config(value=5)
    if quesArea.get(1.0, 'end-1c')==questions[4]:
        progressbarA.config(value=15)
        progressbarB.config(value=35)
        progressbarC.config(value=75)
        progressbarD.config(value=10)
    if quesArea.get(1.0, 'end-1c')==questions[5]:
        progressbarA.config(value=30)
        progressbarB.config(value=40)
        progressbarC.config(value=70)
        progressbarD.config(value=10)
    if quesArea.get(1.0, 'end-1c')==questions[6]:
        progressbarA.config(value=10)
        progressbarB.config(value=40)
        progressbarC.config(value=65)
        progressbarD.config(value=15)
    if quesArea.get(1.0, 'end-1c')==questions[7]:
        progressbarA.config(value=25)
        progressbarB.config(value=95)
        progressbarC.config(value=40)
        progressbarD.config(value=30)

def livelinephone():
    mixer.music.load('images/calling.mp3')
    mixer.music.play()
    btnCall.place(x=70, y=260)
    livePhone.config(image=imagePhoneused, state=DISABLED)

def phoneclick():
    for i in range(8):
        if quesArea.get(1.0, 'end-1c')==questions[i]:
            engine.say(f'Đáp án là {correct_answers[i]}')
            engine.runAndWait()
# engine.stop()

#--------------------------------------------------Images------------------------
centerImage = tk.PhotoImage(file='images/center.png')
logoCenter = tk.Button(centerFrame, image= centerImage, bg = 'black', width=300, height=200, bd =0)
logoCenter.grid(row=0, column=0)

image50_50 = tk.PhotoImage(file='images/5050.png')
image50_50used = tk.PhotoImage(file='images/5050used.png')
live50_50 = tk.Button(topFrame, image= image50_50, bg = 'black', width=180, height=80,bd =0, activebackground='black', command=live50)
live50_50.grid(row=0,column=0)

imagePeople = tk.PhotoImage(file='images/people.png')
imagePeopleused = tk.PhotoImage(file='images/peopleused.png')
livePeople = tk.Button(topFrame, image= imagePeople, bg = 'black', width=180, height=80,bd =0, activebackground='black', command=livepeo)
livePeople.grid(row=0,column=1)

imagePhone = tk.PhotoImage(file='images/phone.png')
imagePhoneused = tk.PhotoImage(file='images/phoneused.png')
livePhone = tk.Button(topFrame, image= imagePhone, bg = 'black', width=180, height=80,bd =0, activebackground='black', command=livelinephone)
livePhone.grid(row=0,column=2)

imgCall = tk.PhotoImage(file='images/calling.png')
btnCall = tk.Button(root, image=imgCall, bd=0, bg='black', activebackground='black',cursor='hand2', command=phoneclick)

# money table
imageList = tk.PhotoImage(file='images/Picture0.png')
imageList1 = tk.PhotoImage(file='images/Picture1.png')
imageList2 = tk.PhotoImage(file='images/Picture2.png')
imageList3 = tk.PhotoImage(file='images/Picture3.png')
imageList4 = tk.PhotoImage(file='images/Picture4.png')
imageList5 = tk.PhotoImage(file='images/Picture5.png')
imageList6 = tk.PhotoImage(file='images/Picture6.png')
imageList7 = tk.PhotoImage(file='images/Picture7.png')
imageList8 = tk.PhotoImage(file='images/Picture8.png')

amountImage = [imageList1,imageList2,imageList3,imageList4,imageList5,imageList6,imageList7,imageList8]

imgList = tk.Label(rightFrame, image= imageList, bg = 'black',bd =0)
imgList.grid(row=0,column=0)

imageLayout = tk.PhotoImage(file = 'images/lay.png')
imgLayout = tk.Label(bottomFrame, image=imageLayout, bg = 'black')
imgLayout.grid(row=0, column = 0)

#--------------------------------------------------Million questions--------------------
def select(event):
    btnCall.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    lblprogressbarA.place_forget()
    lblprogressbarB.place_forget()
    lblprogressbarC.place_forget()
    lblprogressbarD.place_forget()

    b=event.widget
    value=b['text']
    for i in range(8):
        if value==correct_answers[i]:
            if value == correct_answers[7]:
                def close():
                    root2.destroy()
                    root.destroy()

                def playagain():
                    live50_50.config(state=NORMAL, image = image50_50)
                    livePeople.config(state=NORMAL, image = imagePeople)
                    livePhone.config(state=NORMAL, image = imagePhone)
                    root2.destroy()
                    quesArea.delete(1.0, tk.END)
                    quesArea.insert(tk.END, questions[0])

                    btnOption1.config(text=first_option[0])
                    btnOption2.config(text=second_option[0])
                    btnOption3.config(text=third_option[0])
                    btnOption4.config(text=fourth_option[0])
                    imgList.config(image=imageList)

                mixer.music.load('images/kbcwon.mp3')
                mixer.music.play()
                root2 = tk.Toplevel()
                root2.overrideredirect(True)
                root2.config(bg="black")
                root2.geometry("500x400+140+30")
                root2.title("You won 0 VND")
                lblImage = tk.Label(root2, image= centerImage, bd = 0, bg='black')
                lblImage.pack(pady=30)

                lblWin = tk.Label(root2, text="You won", font=('arial',40,'bold'), bg="black", fg='white')
                lblWin.pack()

                btnPlayAgain = tk.Button(root2, text="Play again", font=('arial',20,"bold"),bg="black",fg="white",
                                        activebackground="black", activeforeground="white", bd =0, cursor="hand2", command=playagain)
                btnPlayAgain.pack()

                btnClose = tk.Button(root2, text="close", font=('arial',20,"bold"),bg="black",fg="white",
                                    activebackground="black", activeforeground="white", bd =0, cursor="hand2", command=close)
                btnClose.pack()
                

                root2.mainloop()
                break

            quesArea.delete("1.0", tk.END)
            quesArea.insert(tk.END, questions[i+1])

            btnOption1.config(text=first_option[i+1])
            btnOption2.config(text=second_option[i+1])
            btnOption3.config(text=third_option[i+1])
            btnOption4.config(text=fourth_option[i+1])
            imgList.config(image=amountImage[i])
        
        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()

            def tryagain():
                live50_50.config(state=NORMAL, image = image50_50)
                livePeople.config(state=NORMAL, image = imagePeople)
                livePhone.config(state=NORMAL, image = imagePhone)

                root1.destroy()
                quesArea.delete(1.0, tk.END)
                quesArea.insert(tk.END, questions[0])

                btnOption1.config(text=first_option[0])
                btnOption2.config(text=second_option[0])
                btnOption3.config(text=third_option[0])
                btnOption4.config(text=fourth_option[0])
                imgList.config(image=imageList)

            root1 = tk.Toplevel()
            root1.overrideredirect(True)
            root1.config(bg="black")
            root1.geometry("500x400+140+30")
            root1.title("You won 0 VND")
            lblImage = tk.Label(root1, image= centerImage, bd = 0, bg='black')
            lblImage.pack(pady=30)

            lblLose = tk.Label(root1, text="You lose", font=('arial',40,'bold'), bg="black", fg='white')
            lblLose.pack()

            btnTryAgain = tk.Button(root1, text="Try again", font=('arial',20,"bold"),bg="black",fg="white",
                                    activebackground="black", activeforeground="white", bd =0, cursor="hand2", command=tryagain)
            btnTryAgain.pack()

            btnClose = tk.Button(root1, text="close", font=('arial',20,"bold"),bg="black",fg="white",
                                activebackground="black", activeforeground="white", bd =0, cursor="hand2", command=close)
            btnClose.pack()
            

            root1.mainloop()
            break
    

correct_answers = ["Phụ nữ phải được đối xử như nam giới trừ khi áp dụng các trường hợp đặc biệt",
                   "Nhà giữ thức ăn chuẩn bị",
                   "bất bình đẳng",
                   "không quan trọng",
                   "về mặt xã hội",
                   "biểu quyết",
                   "trí tuệ",
                   "Bất bình đẳng giới"]

questions = ["Bình đẳng giới nghĩa là gì?",
            "Ở nhiều quốc gia, hoạt động nào chiếm nhiều thời gian của phụ nữ mà nam giới không phải giải quyết?",
            "Tìm từ trái nghĩa của từ được gạch chân Các quyền dân sự bao gồm tự do, bình đẳng về luật pháp và việc làm, và quyền bầu cử.",
            "Tìm từ trái nghĩa của từ được gạch chân. Đã có những thay đổi đáng kể trong cuộc sống của phụ nữ kể từ sau phong trào giải phóng phụ nữ.",
            "Nhờ sự giải phóng phụ nữ mà phụ nữ có thể tham gia các hoạt động____.",
            "Nếu bạn có ____ trong một cuộc bầu cử, bạn có quyền hợp pháp để chỉ ra sự lựa chọn của bạn.",
            "Ngày nay, sự đóng góp___ của phụ nữ cho xã hội của chúng ta ngày càng tốt hơn.",
            "Sự đối xử bất bình đẳng giữa nam và nữ là gì?"]

first_option = ["Tất cả phụ nữ đều được đối xử như nhau",
                "Đi học",
                "công bằng",
                "kiểm soát",
                "xã hội",
                "tình trạng",
                "khác biệt",
                "Bình đẳng giới"]
second_option = ["Tất cả nam giới đều được đối xử như nhau",
                "Nhà giữ thức ăn chuẩn bị",
                "bất bình đẳng",
                "đột nhiên",
                "xa hội",
                "cá nhân",
                "một cách tự nhiên",
                "Bất bình đẳng giới"]
third_option = ["Phụ nữ phải được đối xử như nam giới trừ khi áp dụng các trường hợp đặc biệt",
                "Kiếm thu nhập",
                "ngang nhau",
                "không quan trọng",
                "về mặt xã hội",
                "biểu quyết",
                "trí tuệ",
                "Sự khác biệt về giới tính"]
fourth_option = ["Phụ nữ nên được đối xử như nam giới.",
                "Làm vườn",
                "trạng thái cân bằng",
                "Thiên nhiên",
                "giao lưu",
                "bình đẳng",
                "đáng kể",
                "Bất bình đẳng"]

quesArea = tk.Text(bottomFrame, font=('arial',18,'bold'), width = 34, height=2, wrap='word', bg='black',
fg='white', bd=0)
quesArea.place(x =70, y = 10)

quesArea.insert(tk.END, questions[0])

lblA = tk.Label(bottomFrame, text='A: ', bg='black', fg ='white', font=('arial',16,'bold'))
lblA.place(x=60,y=110)

btnOption1 = tk.Button(bottomFrame, text=first_option[0], font=('arial',16,'bold'), bg = 'black', fg = 'white', bd = 0, activebackground='black',
activeforeground='white', cursor="hand2", wraplength=200, justify=LEFT)
btnOption1.place(x=100, y =100)

lblB = tk.Label(bottomFrame, text='B: ', bg='black', fg ='white', font=('arial',16,'bold'))
lblB.place(x=330,y=110)

btnOption2 = tk.Button(bottomFrame, text=second_option[0], font=('arial',16,'bold'), bg = 'black', fg = 'white', bd = 0, activebackground='black',
activeforeground='white', cursor="hand2", wraplength=200, justify=LEFT)
btnOption2.place(x=370, y =100)

lblC = tk.Label(bottomFrame, text='C: ', bg='black', fg ='white', font=('arial',16,'bold'))
lblC.place(x=60,y=190)

btnOption3 = tk.Button(bottomFrame, text=third_option[0], font=('arial',16,'bold'), bg = 'black', fg = 'white', bd = 0, activebackground='black',
activeforeground='white', cursor="hand2", wraplength=200, justify=LEFT)
btnOption3.place(x=100, y =180)

lblD = tk.Label(bottomFrame, text='D: ', bg='black', fg ='white', font=('arial',16,'bold'))
lblD.place(x=330,y=190)

btnOption4 = tk.Button(bottomFrame, text=fourth_option[0], font=('arial',16,'bold'), bg = 'black', fg = 'white', bd = 0, activebackground='black',
activeforeground='white', cursor="hand2", wraplength=200, justify=LEFT)
btnOption4.place(x=370, y =180)
#--------------------------------------------------text, labels, button--------------------
progressbarA = Progressbar(root, orient=VERTICAL, length=120)
progressbarB = Progressbar(root, orient=VERTICAL, length=120)
progressbarC = Progressbar(root, orient=VERTICAL, length=120)
progressbarD = Progressbar(root, orient=VERTICAL, length=120)

lblprogressbarA = tk.Label(root, text ='A', font=('arial', 20,'bold'), bg='black',fg='white')
lblprogressbarB = tk.Label(root, text ='B', font=('arial', 20,'bold'), bg='black',fg='white')
lblprogressbarC = tk.Label(root, text ='C', font=('arial', 20,'bold'), bg='black',fg='white')
lblprogressbarD = tk.Label(root, text ='D', font=('arial', 20,'bold'), bg='black',fg='white')

btnOption1.bind("<Button-1>", select)
btnOption2.bind("<Button-1>", select)
btnOption3.bind("<Button-1>", select)
btnOption4.bind("<Button-1>", select)

#excecute tkinter
root.mainloop()