import pyttsx3
import tkinter as tk
import tkinter.font as font
from tkinter.constants import CENTER, COMMAND, DISABLED, LEFT, NORMAL, VERTICAL, W
from tkinter.ttk import Progressbar
from typing import Text
from pygame import mixer

#set male voice for calling
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voices', voices[1].id)

mixer.init()
#music playing
mixer.music.load('kbc.mp3')
mixer.music.play(-1)



#creating tkinter window
root = tk.Tk()
root.title("Millionaire")
# tkinter window with dimensions 1270x652 at x =0, y=0
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
        btnOption2.config(text='')
        btnOption4.config(text='')
    if quesArea.get(1.0, 'end-1c') == questions[3]:
        btnOption3.config(text='')
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
        progressbarB.config(value=70)
        progressbarC.config(value=95)
        progressbarD.config(value=30)
    if quesArea.get(1.0, 'end-1c')==questions[3]:
        progressbarA.config(value=85)
        progressbarB.config(value=25)
        progressbarC.config(value=10)
        progressbarD.config(value=5)
    if quesArea.get(1.0, 'end-1c')==questions[4]:
        progressbarA.config(value=75)
        progressbarB.config(value=35)
        progressbarC.config(value=15)
        progressbarD.config(value=10)
    if quesArea.get(1.0, 'end-1c')==questions[5]:
        progressbarA.config(value=70)
        progressbarB.config(value=40)
        progressbarC.config(value=30)
        progressbarD.config(value=10)
    if quesArea.get(1.0, 'end-1c')==questions[6]:
        progressbarA.config(value=10)
        progressbarB.config(value=40)
        progressbarC.config(value=15)
        progressbarD.config(value=65)
    if quesArea.get(1.0, 'end-1c')==questions[7]:
        progressbarA.config(value=95)
        progressbarB.config(value=25)
        progressbarC.config(value=40)
        progressbarD.config(value=30)

def livelinephone():
    mixer.music.load('calling.mp3')
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
centerImage = tk.PhotoImage(file='center.png')
logoCenter = tk.Button(centerFrame, image= centerImage, bg = 'black', width=300, height=200, bd =0)
logoCenter.grid(row=0, column=0)

# 50-50
image50_50 = tk.PhotoImage(file='5050.png')
image50_50used = tk.PhotoImage(file='5050used.png')
live50_50 = tk.Button(topFrame, image= image50_50, bg = 'black', width=180, height=80,bd =0, activebackground='black', command=live50)
live50_50.grid(row=0,column=0)

# ask people
imagePeople = tk.PhotoImage(file='people.png')
imagePeopleused = tk.PhotoImage(file='peopleused.png')
livePeople = tk.Button(topFrame, image= imagePeople, bg = 'black', width=180, height=80,bd =0, activebackground='black', command=livepeo)
livePeople.grid(row=0,column=1)

# phone
imagePhone = tk.PhotoImage(file='phone.png')
imagePhoneused = tk.PhotoImage(file='phoneused.png')
livePhone = tk.Button(topFrame, image= imagePhone, bg = 'black', width=180, height=80,bd =0, activebackground='black', command=livelinephone)
livePhone.grid(row=0,column=2)

imgCall = tk.PhotoImage(file='calling.png')
btnCall = tk.Button(root, image=imgCall, bd=0, bg='black', activebackground='black',cursor='hand2', command=phoneclick)

# money table
imageList = tk.PhotoImage(file='Picture0.png')
imageList1 = tk.PhotoImage(file='Picture1.png')
imageList2 = tk.PhotoImage(file='Picture2.png')
imageList3 = tk.PhotoImage(file='Picture3.png')
imageList4 = tk.PhotoImage(file='Picture4.png')
imageList5 = tk.PhotoImage(file='Picture5.png')
imageList6 = tk.PhotoImage(file='Picture6.png')
imageList7 = tk.PhotoImage(file='Picture7.png')
imageList8 = tk.PhotoImage(file='Picture8.png')

amountImage = [imageList1,imageList2,imageList3,imageList4,imageList5,imageList6,imageList7,imageList8]

imgList = tk.Label(rightFrame, image= imageList, bg = 'black',bd =0)
imgList.grid(row=0,column=0)

# questions
imageLayout = tk.PhotoImage(file = 'lay.png')
imgLayout = tk.Label(bottomFrame, image=imageLayout, bg = 'black')
imgLayout.grid(row=0, column = 0)

#--------------------------------------------------Million questions--------------------
# function to be called when the selection changes
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

                mixer.music.load('kbcwon.mp3')
                mixer.music.play()
                root2 = tk.Toplevel()
                root2.overrideredirect(True)
                root2.config(bg="black")
                root2.geometry("1270x652+10+30")
                root2.title("You won 0 VND")
                lblImage = tk.Label(root2, image= centerImage, bd = 0, bg='black')
                lblImage.pack(pady=30)

                lblWin = tk.Label(root2, text="You won", font=('arial',50,'bold'), bg="black", fg='white')
                lblWin.pack()

                btnPlayAgain = tk.Button(root2, text="Play again", font=('arial',30,"bold"),bg="black",fg="white",
                                        activebackground="black", activeforeground="white", bd =0, cursor="hand2", command=playagain)
                btnPlayAgain.pack(side = 'top', fill = 'both', expand = 'yes')

                btnClose = tk.Button(root2, text="close", font=('arial',30,"bold"),bg="black",fg="white",
                                    activebackground="black", activeforeground="white", bd =0, cursor="hand2", command=close)
                btnClose.pack(side = 'bottom', fill = 'both', expand = 'yes')
                

                root2.mainloop()
                break
            # next question, answers
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
            root1.geometry("1270x652+10+30")
            root1.title("You won 0 VND")
            lblImage = tk.Label(root1, image= centerImage, bd = 0, bg='black')
            lblImage.pack(pady=30)

            lblLose = tk.Label(root1, text="You lose", font=('arial',50,'bold'), bg="black", fg='white')
            lblLose.pack()

            btnTryAgain = tk.Button(root1, text="Try again", font=('arial',30,"bold"),bg="black",fg="white",
                                    activebackground="black", activeforeground="white", bd =0, cursor="hand2", command=tryagain)
            btnTryAgain.pack(side = 'top', fill = 'both', expand = 'yes')

            btnClose = tk.Button(root1, text="close", font=('arial',30,"bold"),bg="black",fg="white",
                                activebackground="black", activeforeground="white", bd =0, cursor="hand2", command=close)
            btnClose.pack(side = 'bottom', fill = 'both', expand = 'yes')
            

            root1.mainloop()
            break
    

correct_answers = ["Phụ nữ phải được đối xử như nam giới trừ khi áp dụng các trường hợp đặc biệt",
                   "Nội trợ",
                   "Xử lý kỷ luật, xử lý hành chính hoặc bị truy cứu trách nhiệm hình sự",
                   "Thứ 2",
                   "Lựa chọn giới tính thai nhi",
                   "Tổng đài quốc gia bảo vệ trẻ em",
                   "Khi đến nhà cô giáo, cả nam và nữ cùng giúp cô phần nội trợ",
                   "40/53"]

questions = ["Bình đẳng giới nghĩa là gì?",
            "Ở nhiều quốc gia, hoạt động nào chiếm nhiều thời gian của phụ nữ mà nam giới không phải giải quyết?",
            "Luật Bình đẳng giới quy định hình thức xử lý vi phạm pháp luật về bình đẳng giới như thế nào?",
            "Năm 2020, Việt Nam xếp thứ bao nhiêu trong khu vực ASEAN về chỉ số cam kết giảm bất bình đẳng?",
            "Hành vi nào vi phạm pháp luật về bình đẳng giới trong lĩnh vực y tế?",
            "111 là hotline của tổng đài nào",
            "Câu nào sau đây thể hiện bình đẳng giới?",
            "Bao nhiêu dân tộc thiểu số ở nước ta có tỷ lệ tảo hôn từ 20% trở lên?"]
                          
first_option = ["Tất cả phụ nữ đều được đối xử như nhau",
                "Đi học",
                "Góp ý, phê bình",
                "Thứ 2",
                "Lựa chọn giới tính thai nhi",
                "Tổng đài quốc gia bảo vệ trẻ em",
                "Cô chủ nhiệm nói 'Chỉ con gái được để tóc dài', yêu cầu bạn nam để tóc dài trong lớp phải cắt tóc ngắn",
                "40/53"]
second_option = ["Tất cả nam giới đều được đối xử như nhau",
                "Nội trợ",
                "Cảnh cáo, khiển trách",
                "Thứ 7",
                "Thực hiện phong tục tập quán lạc hậu mang tính phân biệt đối xử về giới dưới mọi hình thức",
                "Tổng đài  yêu cầu trợ giúp và tìm kiếm cứu nạn trên phạm vi toàn quốc",
                "Những bạn nam cười đùa, dùng từ ngữ 'đầy đủ điện nước'khi bắt gặp bạn nữ có thân hình đầy đặn",
                "37/53"]
third_option = ["Phụ nữ phải được đối xử như nam giới trừ khi áp dụng các trường hợp đặc biệt",
                "Kiếm thu nhập",
                "Xử lý kỷ luật, xử lý hành chính hoặc bị truy cứu trách nhiệm hình sự",
                "Thứ 4",
                "Từ chối tuyển dụng những người phù hợp vì lý do giới tính hoặc do việc mang thai/sinh con/có con nhỏ",
                "Tổng đài cứu hóa",
                "Hình ảnh minh họa sách giáo khoa luôn lựa chọn nam giới cho các nghề bác sĩ/công an còn nữ làm nội trợ",
                "16/53"]
fourth_option = ["Phụ nữ nên được đối xử như nam giới.",
                "Làm vườn",
                "Chưa có hình thức xử lý",
                "Thứ 5",
                "Cho thôi việc người lao động vì lý do mang thai",
                "Tổng đài cấp cứu",
                "Khi đến nhà cô giáo, cả nam và nữ cùng giúp cô phần nội trợ",
                "28/53"]

# question area
quesArea = tk.Text(bottomFrame, font=('arial',10,'bold'), width = 50, height=3, wrap='word', bg='black',
fg='white', bd=0)
quesArea.place(x =70, y = 10)

quesArea.insert(tk.END, questions[0])

# answer A B C D
lblA = tk.Label(bottomFrame, text='A: ', bg='black', fg ='white', font=('arial',10,'bold'))
lblA.place(x=60,y=110)

btnOption1 = tk.Button(bottomFrame, text=first_option[0], font=('arial',8,'bold'), bg = 'black', fg = 'white', bd = 0, activebackground='black',
activeforeground='white', cursor="hand2", wraplength=150, justify=LEFT)
btnOption1.place(x=100, y =100)

lblB = tk.Label(bottomFrame, text='B: ', bg='black', fg ='white', font=('arial',10,'bold'))
lblB.place(x=330,y=110)

btnOption2 = tk.Button(bottomFrame, text=second_option[0], font=('arial',8,'bold'), bg = 'black', fg = 'white', bd = 0, activebackground='black',
activeforeground='white', cursor="hand2", wraplength=150, justify=LEFT)
btnOption2.place(x=370, y =100)

lblC = tk.Label(bottomFrame, text='C: ', bg='black', fg ='white', font=('arial',10,'bold'))
lblC.place(x=60,y=190)

btnOption3 = tk.Button(bottomFrame, text=third_option[0], font=('arial',8,'bold'), bg = 'black', fg = 'white', bd = 0, activebackground='black',
activeforeground='white', cursor="hand2", wraplength=150, justify=LEFT)
btnOption3.place(x=100, y =180)

lblD = tk.Label(bottomFrame, text='D: ', bg='black', fg ='white', font=('arial',10,'bold'))
lblD.place(x=330,y=190)

btnOption4 = tk.Button(bottomFrame, text=fourth_option[0], font=('arial',8,'bold'), bg = 'black', fg = 'white', bd = 0, activebackground='black',
activeforeground='white', cursor="hand2", wraplength=150, justify=LEFT)
btnOption4.place(x=370, y =180)
#--------------------------------------------------progressbar--------------------
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