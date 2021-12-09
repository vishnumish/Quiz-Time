import tkinter
import random
from tkinter import *
from tkinter import font
from PIL import Image
import tkinter.messagebox as tmsg


#Easy questions___________________________

questions1 = [
    "What is the cleanest city in india?",
    "Most polluted city in the world?",
    "What are constellations?",
    "What is the full form of RBI?",
    "Who invented aeroplane?",
    "Which bird is the universal symbol of peace?",
]

answers1_choice=[
    ["Gorakhpur","Jamshedpur","Indore","Muzaffarpur"],
    ["Pune","Delhi","Surat","Kanpur"],
    ["Group of stars","Group of rivers","Group of trees","Group of soil"],
    ["Reserve bank of india","Reserve bank of indore","Reserve bank of ireland","Reserve bank of ichalkaranji"],
    ["Ramdev Baba","Mahatama Gandhi","Abraham Lincon","Wright Brothers"],
    ["Dove","Broom","Pen","Hand"],
]

answers1=[2,1,0,0,3,0]#indexes of correct answers


user_easyanswer=[]

indexes=[]
def easygen():
    global indexes
    while(len(indexes)<5):
        x=random.randint(0,5)
        if x in indexes:
            continue
        else:
            indexes.append(x)
        
def easy_result(score):
    lbleasyquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    
    lbl_easy_text=Label(
        root,
        text="Great Your Score is ",
        font=("Lucida Handwriting Italic",30),
        width = 40,
        height=2,
        justify="center",
        background="#4f4f4a",
        foreground="#e0c40d",
    )
    lbl_easy_text.pack(pady=(70,10))
    
    lbl_easy_score=Label(
        root,
        text=("score",score),
        font=("Segoe Script",24),
        justify="center",
        background="#4f4f4a",
        foreground="#e0c40d",
    )
    lbl_easy_score.pack(pady=(70,10))
    
    global lblthank
    lblthank = Label(
        root,
        text = "Thank You For PLaying Quiz Time",
        font = ("Felix Titling",30),
        background="#e0c40d",
        foreground="black",
    )
    lblthank.place(x=32,y=430)
    
    lbl_easy_quit=Button(
        root,
        text="QUIT",
        font=("Segoe Print",15),
        background="red",
        foreground="black",
        command=root.destroy,
        
    )
    
    lbl_easy_quit.place(x=345,y=530)
    
    
    
def easy_calc():
    global indexes,user_easyanswer,answers1
    x=0
    score=0
    for i in indexes:
        if user_easyanswer[x]==answers1[i]:
            score=score + 5
        x +=1
    #print(score)
    #tmsg.showinfo("Your total score",f"Your final score is {score.get()}")
    easy_result(score)

        

ques1=1
def easyselected():
    global radiovar1,user_easyanswer,lbleasyquestion,r1,r2,r3,r4
    global ques1
    x=radiovar1.get()
    user_easyanswer.append(x)
    radiovar1.set(-1)
    if ques1<5:   #ques1 is a user defined variable
        lbleasyquestion.config(text=questions1[indexes[ques1]])
        r1['text']=answers1_choice[indexes[ques1]][0]
        r2['text']=answers1_choice[indexes[ques1]][1]
        r3['text']=answers1_choice[indexes[ques1]][2]
        r4['text']=answers1_choice[indexes[ques1]][3]
        
        ques1+=1
    else:
        easy_calc()
    
   

def easyquestions():
    global lbleasyquestion,r1,r2,r3,r4
    lbleasyquestion=Label(
        root,
        text= questions1[indexes[0]],
        font=("Arial Rounded MT Bold",22),
        width=500,
        justify="center",
        wraplength=400,
        background="#e0c40d",
        foreground="black",
    )
    lbleasyquestion.pack(pady=(50,0))
    
    global radiovar1
    radiovar1=IntVar()
    radiovar1.set(-1)
    
    r1=Radiobutton(
        root,
        text=answers1_choice[indexes[0]][0],
        font=("Gill Sans MT",16),
        value=0,
        variable=radiovar1,
        background="#4f4f4a",
        foreground="white",
        #activebackground="red",#highlightcolor="red",
        command=easyselected,
    )
    r1.place(x=250,y=200)
    
    r2=Radiobutton(
        root,
        text=answers1_choice[indexes[0]][1],
        font=("Gill Sans MT",16),
        value=1,
        variable=radiovar1,
        background="#4f4f4a",
        foreground="white",
        command=easyselected,
    )
    r2.place(x=300,y=250)
    
    r3=Radiobutton(
        root,
        text=answers1_choice[indexes[0]][2],
        font=("Gill Sans MT",16),
        value=2,
        variable=radiovar1,
        background="#4f4f4a",
        foreground="white",
        command=easyselected,
    )
    r3.place(x=350,y=300)
    
    r4=Radiobutton(
        root,
        text=answers1_choice[indexes[0]][3],
        font=("Gill Sans MT",16),
        value=3,
        variable=radiovar1,
        background="#4f4f4a",
        foreground="white",
        command=easyselected,
    )
    r4.place(x=400,y=350)
    
#End of easy questions_______________________


#start of normal questions********************8

questions2 = [
    "The Central Rice Research Station is situated in?",
    "Which one of the following river flows between Vindhyan and Satpura ranges?",
    "Who among the following wrote Sanskrit grammar?",
    "Patanjali is well known for the compilation of ?",
    "Tsunamis are not caused by",
    "The hottest planet in the solar system?",
]

answers2_choice=[
    ["Chennai","Cuttack","Bangalore","Quilon"],
    ["Narmada","Mahanadi","Son","Netravati"],
    ["Kalidasa","Charak","Panini","Aryabhatt"],
    ["Yoga Sutra","Panchatantra","Brahma Sutra","Ayurveda"],
    ["Hurricanes","Earthquakes","Undersea landslides","Volcanic eruptions"],
    ["Mercury","Venus"," Mars","Jupiter"],
]


answers2=[1,0,2,0,0,1]#indexes of correct answers



user_normalanswer=[]

indexes=[]
def normalgen():
    global indexes
    while(len(indexes)<5):
        x=random.randint(0,5)
        if x in indexes:
            continue
        else:
            indexes.append(x)
            

def normal_result(score):
    lblnormalquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    
    lbl_normal_text=Label(
        root,
        text="Great Your Score is ",
        font=("Lucida Handwriting Italic",30),
        width = 40,
        height=2,
        justify="center",
        background="#4f4f4a",
        foreground="#e0c40d",
    )
    lbl_normal_text.pack(pady=(70,10))
    
    lbl_normal_score=Label(
        root,
        text=("score",score),
        font=("Segoe Script",24),
        justify="center",
        background="#4f4f4a",
        foreground="#e0c40d",
    )
    lbl_normal_score.pack(pady=(70,10))
    
    global lblthank
    lblthank = Label(
        root,
        text = "Thank You For PLaying Quiz Time",
        font = ("Felix Titling",30),
        background="#e0c40d",
        foreground="black",
    )
    lblthank.place(x=32,y=430)
    
    lbl_normal_quit=Button(
        root,
        text="QUIT",
        font=("Segoe Print",15),
        background="red",
        foreground="black",
        command=root.destroy,
        
    )
    
    lbl_normal_quit.place(x=345,y=530)
    
    

    
    
def normal_calc():
    global indexes,user_normalanswer,answers2
    x=0
    score=0
    for i in indexes:
        if user_normalanswer[x]==answers2[i]:
            score=score + 5
        x +=1
    print(score)
    #tmsg.showinfo("Your total score",f"Your final score is {score.get()}")
    normal_result(score)
        
        

ques2=1
def normalselected():
    global radiovar1,user_normalanswer,lblnormalquestion,r1,r2,r3,r4
    global ques2
    x=radiovar1.get()
    user_normalanswer.append(x)
    radiovar1.set(-1)
    if ques2<5:   #ques1 is a user defined variable
        lblnormalquestion.config(text=questions2[indexes[ques2]])
        r1['text']=answers2_choice[indexes[ques2]][0]
        r2['text']=answers2_choice[indexes[ques2]][1]
        r3['text']=answers2_choice[indexes[ques2]][2]
        r4['text']=answers2_choice[indexes[ques2]][3]
        
        ques2+=1
    else:
        normal_calc()
    


def normalquestions():
    global lblnormalquestion,r1,r2,r3,r4
    lblnormalquestion=Label(
        root,
        text= questions2[indexes[0]],
        font=("Arial Rounded MT Bold",22),
        width=500,
        justify="center",
        wraplength=400,
        background="#e0c40d",
        foreground="black",
    )
    lblnormalquestion.pack(pady=(50,0))
    
    global radiovar1
    radiovar1=IntVar()
    radiovar1.set(-1)
    
    r1=Radiobutton(
        root,
        text=answers2_choice[indexes[0]][0],
        font=("Gill Sans MT",16),
        value=0,
        variable=radiovar1,
        background="#4f4f4a",
        foreground="white",
        command=normalselected,
    )
    r1.place(x=250,y=200)
    
    r2=Radiobutton(
        root,
        text=answers2_choice[indexes[0]][1],
        font=("Gill Sans MT",16),
        value=1,
        variable=radiovar1,
        background="#4f4f4a",
        foreground="white",
        command=normalselected,
    )
    r2.place(x=300,y=250)
    
    r3=Radiobutton(
        root,
        text=answers2_choice[indexes[0]][2],
        font=("Gill Sans MT",16),
        value=2,
        variable=radiovar1,
        background="#4f4f4a",
        foreground="white",
        command=normalselected,
    )
    r3.place(x=350,y=300)
    
    r4=Radiobutton(
        root,
        text=answers2_choice[indexes[0]][3],
        font=("Gill Sans MT",16),
        value=3,
        variable=radiovar1,
        background="#4f4f4a",
        foreground="white",
        command=normalselected,
    )
    r4.place(x=400,y=350)
    
#end of normal questions

#Start of hard questions*********************

questions3 = [
    "Which of the following is not a nuclear power center?",
    "FFC stands for?",
    "Each year World Red Cross and Red Crescent Day is celebrated on",
    "Where can Coral reefs be found in India?",
    "The biggest part of the brain is?",
    "Anthophobia is fear of which of the following?",
]

answers3_choice=[
    ["Narora","Kota","Chamera","Kakrapara"],
    ["Federation of Football Council","Film Finance Corporation","Foreign Finance Corporation","None of the above"],
    ["June 8","June 18","May 8","May 18"],
    ["The Malabar Coast","Rameshwaram","Trivandrum","Mahabalipuram"],
    ["Spinal cord","Cerebellum","Cerebrum","Brain Stem"],
    [" Boss","Fire","Flowers","Dogs"],
]


answers3=[2,1,2,1,2,2]#indexes of correct answers

user_hardanswer=[]

indexes=[]
def hardgen():
    global indexes
    while(len(indexes)<5):
        x=random.randint(0,5)
        if x in indexes:
            continue
        else:
            indexes.append(x)
            
def hard_result(score):
    lblhardquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    
    
    lbl_hard_text=Label(
        root,
        text="Great Your Score is ",
        font=("Lucida Handwriting Italic",30),
        width = 40,
        height=2,
        justify="center",
        background="#4f4f4a",
        foreground="#e0c40d",
    )
    lbl_hard_text.pack(pady=(70,10))
    
    lbl_hard_score=Label(
        root,
        text=("score",score),
        font=("Segoe Script",24),
        justify="center",
        background="#4f4f4a",
        foreground="#e0c40d",
    )
    lbl_hard_score.pack(pady=(70,10))
    
    global lblthank
    lblthank = Label(
        root,
        text = "Thank You For PLaying Quiz Time",
        font = ("Felix Titling",30),
        background="#e0c40d",
        foreground="black",
    )
    lblthank.place(x=32,y=430)
    
    lbl_hard_quit=Button(
        root,
        text="QUIT",
        font=("Segoe Print",15),
        background="red",
        foreground="black",
        command=root.destroy,
        
    )
    
    lbl_hard_quit.place(x=345,y=530)



def hard_calc():
    global indexes,user_hardanswer,answers3
    x=0
    score=0
    for i in indexes:
        if user_hardanswer[x]==answers3[i]:
            score=score + 5
        x +=1
    #print(score)
    #tmsg.showinfo("Your total score",f"Your final score is {score.get()}")
    hard_result(score)

        
        
        

ques3=1
def hardselected():
    global radiovar1,user_hardanswer,lblhardquestion,r1,r2,r3,r4
    global ques3
    x=radiovar1.get()
    user_hardanswer.append(x)
    radiovar1.set(-1)
    if ques3<5:   #ques1 is a user defined variable
        lblhardquestion.config(text=questions3[indexes[ques3]])
        r1['text']=answers3_choice[indexes[ques3]][0]
        r2['text']=answers3_choice[indexes[ques3]][1]
        r3['text']=answers3_choice[indexes[ques3]][2]
        r4['text']=answers3_choice[indexes[ques3]][3]
        
        ques3+=1
    else:
        hard_calc()
    


def hardquestions():
    global lblhardquestion,r1,r2,r3,r4
    lblhardquestion=Label(
        root,
        text= questions3[indexes[0]],
        font=("Arial Rounded MT Bold",22),
        width=500,
        justify="center",
        wraplength=400,
        background="#e0c40d",
        foreground="black",
    )
    lblhardquestion.pack(pady=(50,0))
    
    global radiovar1
    radiovar1=IntVar()
    radiovar1.set(-1)
    
    r1=Radiobutton(
        root,
        text=answers3_choice[indexes[0]][0],
        font=("Gill Sans MT",16),
        value=0,
        variable=radiovar1,
        background="#4f4f4a",
        foreground="white",
        command=hardselected,
    )
    r1.place(x=250,y=200)
    
    r2=Radiobutton(
        root,
        text=answers3_choice[indexes[0]][1],
        font=("Gill Sans MT",16),
        value=1,
        variable=radiovar1,
        background="#4f4f4a",
        foreground="white",
        command=hardselected,
    )
    r2.place(x=300,y=250)
    
    r3=Radiobutton(
        root,
        text=answers3_choice[indexes[0]][2],
        font=("Gill Sans MT",16),
        value=2,
        variable=radiovar1,
        background="#4f4f4a",
        foreground="white",
        command=hardselected,
    )
    r3.place(x=350,y=300)
    
    r4=Radiobutton(
        root,
        text=answers3_choice[indexes[0]][3],
        font=("Gill Sans MT",16),
        value=3,
        variable=radiovar1,
        background="#4f4f4a",
        foreground="white",
        command=hardselected,
    )
    r4.place(x=400,y=350)

#end of hard questions*******************

##2nd page
def startquiz():
    global lblLevel
    lblLevel = Label(
        root,
        text = "Choose Your level",
        font = ("Felix Titling",50),
        width=400,
        height=2,
        justify="center",
        #wraplength=400, 
        background="#e0c40d",
    )
    lblLevel.pack()
    
    global easy
    easy = PhotoImage(file = "easy.png")
    
    global easybtn
    easybtn = Button(
        root,
        image = easy,
        relief = FLAT,
        border=0,
        command = easyIspressed,
    )
    easybtn.pack(pady = (100,10))
    
    global normal
    normal = PhotoImage(file = "normal.png")
    
    global normalbtn
    normalbtn = Button(
        root,
        image = normal,
        relief = FLAT,
        border=0,
        command = normalIspressed,
        
    )
    normalbtn.pack(pady = (10,10))
    
    global hard
    hard = PhotoImage(file = "hard.png")
    
    global hardbtn
    hardbtn = Button(
        root,
        image = hard,
        relief = FLAT,
        border=0,
        command = hardIspressed,
        
    )
    hardbtn.pack(pady = (10,10))

    radiovar = IntVar()
    radiovar.set(-1)


   ##2nd page end 
   
def startIspressed():
    
    if (playerName.get()=="" or chckvalue.get()==0):
       tmsg.showerror("Missing information","Please enter your name and press the checkbox to start the quiz")
        
    
    else:
        labelimage.destroy()
        labeltext.destroy()
        btnstart.destroy()
        lblInstructions.destroy()
        lblRules.destroy()
        chck.destroy()
        labeltextentry.destroy()
    
    
        startquiz() 


#Destroying the EASY NORMAL HARD page 
def easyIspressed():
    easybtn.destroy()
    normalbtn.destroy()
    hardbtn.destroy()
    lblLevel.destroy()
    root.configure(background="#4f4f4a")#background colour
    easygen()
    easyquestions() #starting the quiz in easy mode
    
def normalIspressed():
    easybtn.destroy()
    normalbtn.destroy()
    hardbtn.destroy()
    lblLevel.destroy()
    root.configure(background="#4f4f4a")#background colour
    normalgen()
    normalquestions()
    
    
def hardIspressed():
    easybtn.destroy()
    normalbtn.destroy()
    hardbtn.destroy()
    lblLevel.destroy()
    root.configure(background="#4f4f4a")#background colour
    hardgen()
    hardquestions()


#Main program
    
root = tkinter.Tk()
root.title("Quiz Time")
root.geometry("800x600")
root.minsize(800,600)
root.maxsize(800,600)
root.config(background="white")
root.resizable(0,0)


img1 = PhotoImage(file = "logo.png")

labelimage  = Label(
    root,
    image = img1,
    background="white",
)
labelimage.pack()

labeltext = Label(
    root,
    text = "Enter Your Name",
    font = ("Poor Richard",15),
    background="white",

)
labeltext.place(x=240,y=230)

playerName=StringVar()

labeltextentry=Entry(
    root,
    textvariable=playerName
    )
labeltextentry.place(x=390,y=240)

img2 = PhotoImage(file="start.png")#start button

btnstart = Button(
    root,
    image = img2,
    relief= FLAT,
    border = 0,
    command= startIspressed,#redirecting to another page
)
btnstart.pack(pady=(30,10))

lblInstructions = Label(
    root,
    text = "Click start only after reading the rules!\nAll The Best",
    background="white",
    font = ("Consolas",16),
    
)
lblInstructions.pack(pady=(0,100))

lblRules = Label(
    root,
    text = "It contains a total of 5 questions in three sections \n Each Question contains Five Marks \n Once the radio button is clicked,you will got to next question \n Think before you click!",
    width = 50,
    font = ("Times",15)

)
lblRules.place(x=130,y=450)

chckvalue=IntVar()
chck=Checkbutton(text="I have read the rules",variable=chckvalue,font=("Comic Sans MS",15))
chck.place(x=300,y=550)


root.mainloop()