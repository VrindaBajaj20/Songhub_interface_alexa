#importing libraries
import tkinter  
from tkinter import *  #Structure
from tkinter import ttk     #Styling
from tkinter.ttk import Notebook     #To switch  between tabs
from PIL import Image , ImageTk      #For image
import pyttsx3   #For text recognition
import speech_recognition as sr    #for speech recognition
import pygame #For mp3 player
from tkinter import filedialog  #For opening the dialog box



#root window

mw=Tk() #main window
mw.title('Songhub')
mw.geometry('900x700')
tabcontrol=Notebook(mw)


#------------

#TAB1

tab1=ttk.Frame(tabcontrol,width = 800 , height= 700)
tabcontrol.add(tab1,text='Home')
tabcontrol.grid(padx=20 , ipadx=18, ipady=18)


#space for entering user details

name=ttk.Label(tab1,text="Enter your Name" , font=(None,13))
name.pack()
name.place(x=350 , y=20)

#Area for user name
name2= StringVar()
enter=ttk.Entry(tab1,text=name2)
enter.pack()
enter.place(x=350 , y=50)


#function for button to display the welcome message

def Display():
    v = name2.get()
    name3= ttk.Label(tab1 , text = ('Welcome '+ v) , font = (None,15))
    name3.pack(padx = 10, pady = 20)
    name3.place(x=340 , y=120)

    user_name=ttk.Label(tab4,text="User's Name : "+v, font=(None,14))
    user_name.pack()
    user_name.place(x=20 , y=90)

#Button Structure

save = Button(tab1, text = "Save" , command = Display ,bd = 5, width = 5)
save.pack()
save.place(x=385 , y=80)
    


#Image
image1 = Image.open("E:/C data/Desktop/SONGHUB/user-icon.jpg")
image1 = image1.resize((450,400),Image.ANTIALIAS)  #Antialias - Antialiasing is a technique used in digital imaging to reduce visual defects in case high resolution images are presented with low resolution ones.
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(tab1, image=test)
label1.image = test
label1.pack()
label1.place(x= 185, y=160)


#TAB2

tab2 = ttk.Frame(tabcontrol , width = 600,height = 700)
tabcontrol.add (tab2, text = 'Menu')


wlcm=ttk.Label(tab2,text="Welcome to the Songhub" , font=(None,16))
wlcm.pack()
wlcm.place(x=300 , y=10)


#Image2
image2 = Image.open("E:/C data/Desktop/SONGHUB/Picture1.jpg")
image2 = image2.resize((400,250),Image.ANTIALIAS)  #Antialias - Antialiasing is a technique used in digital imaging to reduce visual defects in case high resolution images are presented with low resolution ones.
test2 = ImageTk.PhotoImage(image2)
label2 = tkinter.Label(tab2, image=test2)
label2.image = test2
label2.pack()
label2.place(x= 200, y=50)


wlcm2=ttk.Label(tab2,text="🎵" , font=(None,90))
wlcm2.pack()
wlcm2.place(x=20 , y=350)

wlcm2=ttk.Label(tab2,text="Today's Special" , font=(None,16))
wlcm2.pack()
wlcm2.place(x=340 , y=320)

#MOODS

moods=ttk.Label(tab2,text="MOODS:-                              CATEGORIES:-" , font=(None,14))
moods.pack()
moods.place(x=250 , y=360)

moods=ttk.Label(tab2,text="1.Happy                                1.Pop" , font=(None,14))
moods.pack()
moods.place(x=250 , y=390)

moods=ttk.Label(tab2,text="2.Sad                                    2.Kpop" , font=(None,14))
moods.pack()
moods.place(x=250 , y=419)

moods=ttk.Label(tab2,text="3.Motivation                          3.Popular" , font=(None,14))
moods.pack()
moods.place(x=250 , y=445)

moods=ttk.Label(tab2,text="4.Party                                  4.Bollywood" , font=(None,14))
moods.pack()
moods.place(x=250 , y=472)

moods=ttk.Label(tab2,text="5.Workout                             5.Rap" , font=(None,14))
moods.pack()
moods.place(x=250 , y=498)

def say():
    engine = pyttsx3.init()
    engine.say("Welcome to the Songhub! Play songs according to your mood? Say Moods. Wanna choose from the categories instead? Say categories.")
    engine.runAndWait()


#Button Structure

begin= Button(tab2, text = "Begin!" , command = say ,bd = 5, width = 8 ,font=(None,12))
begin.pack()
begin.place(x=345 , y=550)


def speak():
    
    r = sr.Recognizer()
    with sr.Microphone() as source2:
        # wait for a second to let the recognizer adjust to the surrounding noise
        r.adjust_for_ambient_noise(source2, duration=0.1)
              
        #listens for the user's input
        audio2 = r.listen(source2)
              
        # Uses google to recognize the audio
        ch = r.recognize_google(audio2)
        ch = ch.lower()
       
    def Display():
        ch3= ttk.Label(tab2 , text = ('Your choice is '+ ch) , font = (None,15))
        ch3.pack(padx = 10, pady = 20)
        ch3.place(x=348 , y=615)
    Display()

    def choice():
        if ch=='categories':
            tab3 = ttk.Frame(tabcontrol , width = 600,height = 700)
            tabcontrol.add (tab3, text = 'Categories')

            #Displaying categories again

            cat=ttk.Label(tab3,text="CATEGORIES:-" , font=(None,14))
            cat.pack()
            cat.place(x=20 , y=20)

            cat=ttk.Label(tab3,text="1.Pop" , font=(None,14))
            cat.pack()
            cat.place(x=20 , y=50)

            cat=ttk.Label(tab3,text="2.Kpop" , font=(None,14))
            cat.pack()
            cat.place(x=20 , y=80)

            cat=ttk.Label(tab3,text="3.Popular" , font=(None,14))
            cat.pack()
            cat.place(x=20 , y=110)

            cat=ttk.Label(tab3,text="4.Bollywood" , font=(None,14))
            cat.pack()
            cat.place(x=20 , y=140)

            cat=ttk.Label(tab3,text="5.Rap" , font=(None,14))
            cat.pack()
            cat.place(x=20 , y=170)

            #Function for category selection
            def category():
                engine = pyttsx3.init()
                engine.say("Enter the number against your category")
                engine.runAndWait()
                

            #Button for category selection

            begin2= Button(tab3, text = "Next" , command = category ,bd = 5, width = 6 ,font=(None,12))
            begin2.pack()
            begin2.place(x=20 , y=210)

            #Function for speaking the number against your category
            def speak_cat():
                w = sr.Recognizer()
                with sr.Microphone() as source3:
                    # wait for a second to let the recognizer adjust to the surrounding noise
                    w.adjust_for_ambient_noise(source3, duration=0.2)
              
                    #listens for the user's input
                    audio3 = w.listen(source3)
              
                    # Uses google to recognize the audio
                    sc = w.recognize_google(audio3)
                    sc = sc.lower()

                    



                    def Display2():
                        ch4= ttk.Label(tab3 , text = ('Your choice is '+ sc) , font = (None,14))
                        ch4.pack(padx = 10, pady = 20)
                        ch4.place(x=20, y=270)
                    Display2()

                    

                    def player():
                        
                        #from music2 import player_gui
                        import pygame
                        from PIL import ImageTk,Image
                        from tkinter import filedialog

                        music=Tk()
                        music.title("Song Player")
                        music.geometry("700x500")

                        #Initializing Pygame Mixer
                        pygame.mixer.init()



                        #Creating the Player Box

                        sb=Listbox(music , bg="black" , fg="white", width=90 , height=20, selectbackground="grey" , selectforeground="black")
                        sb.pack(pady=20)

                        #Play Function
                        def play():
                            
                            song=sb.get(ACTIVE)
                            pygame.mixer.music.load(song)
                            pygame.mixer.music.play(loops=0)
            

                        #Save Function
                        def save():
                           
                            song2 = sb.get(ACTIVE)
                            f=open("song3.txt" , 'a')
                            f.write("")
                            f.write(song2)
                            f.close()


                        #Stop Function
                        def stop():
                             pygame.mixer.music.stop()

                        #Global Variable

                        global paused
                        paused=False

                        #Pause Function
                        def pause(paused3):
                             global paused
                             paused=paused3

                             if paused:
                                  #Unpause
                                  pygame.mixer.music.unpause()
                                  paused=False
                             else:
                                  #Pause
                                  pygame.mixer.music.pause()
                                  paused=True





                        #BUTTONS

                        back2= Button(music, text = "⏮" ,bd = 5, width = 3 ,font=(None,18))
                        back2.pack()
                        back2.place(x=170 , y=375)

                        play2= Button(music, text = "▶" ,command = play , bd = 5, width = 3 ,font=(None,18))
                        play2.pack()
                        play2.place(x=240 , y=375)

                        pause2= Button(music, text = "⏸" ,command= lambda:pause(paused) ,bd = 5, width = 3 ,font=(None,18))
                        pause2.pack()
                        pause2.place(x=310 , y=375)


                        stop2= Button(music, text = "⏹" ,command = stop ,bd = 5, width =3,font=(None,18))
                        stop2.pack()
                        stop2.place(x=380 , y=375)


                        save2= Button(music, text = "⬇" ,bd = 5, command = save , width = 3 ,font=(None,18))
                        save2.pack()
                        save2.place(x=450 , y=375)

                       


        

                        #MENU

                        menu1=Menu(music)
                        music.config(menu=menu1)

                        #Functions

                        def add_song():
                             song=filedialog.askopenfilename(initialdir = 'Downloads/',title="Choose A Song", filetypes=(("mp3 Files" , "*.mp3"),))
                             #Adding to listbox
                             sb.insert(END,song)
                             

                        def addmany_songs():
                             songs=filedialog.askopenfilenames(initialdir = 'Downloads/',title="Choose Songs", filetypes=(("mp3 Files" , "*.mp3"),))
                             for song in songs:
                                  sb.insert(END,song)

                        #ADDING SONGS
                        add1=Menu(menu1)
                        menu1.add_cascade(label="Add Songs" , menu=add1)
                        add1.add_command(label="Add One Song To The List",command=add_song)

                        add1.add_command(label="Add Many Songs To The List",command=addmany_songs)

  
                        
                        if sc=='pop' or '1':
                                                  
                            def go2():
                                
                                    
                                song_location_list = ['E:/C data/Desktop/SONGHUB/I Like Me Better - Lauv.mp3' , 'E:/C data/Desktop/SONGHUB/10000 Hours - Dan and Shay Ft Justin Bieber.mp3' , 'E:/C data/Desktop/SONGHUB/Ed Sheeran - Beautiful People (feat. Khalid) [Official].mp3' , 'E:/C data/Desktop/SONGHUB/Friends - Marshmello, Anne Marie.mp3' , 'E:/C data/Desktop/SONGHUB/Jason_Derulo_-_Take_You_Dancing.mp3' , 'E:/C data/Desktop/SONGHUB/Halsey - Without Me.mp3' ]
                                f=open('insertsongs.txt' , 'r')
                                data = f.readlines()
                                song_select_dict = {data[0]:song_location_list[0] , data[1]:song_location_list[1] , data[2]:song_location_list[2] , data[3]:song_location_list[3] , data[4]:song_location_list[4] , data[5]:song_location_list[5]}
                                a=song_select_dict.values()
                                for i in a:
                                    sb.insert(END,i)
                            go2()

                        if sc=='kpop' or '2':
                            
                            def go3():
                                
                                song_location_list2 = ['C:/Users/Dell/Downloads/JENNIE - SOLO.mp3' , 'C:/Users/Dell/Downloads/Best of Me - BTS.mp3' , 'C:/Users/Dell/Downloads/Dope bts.mp3' ,'C:/Users/Dell/Downloads/You Never Know (BLACKPINK).mp3' , 'C:/Users/Dell/Downloads/Euphoria bts.mp3' , 'C:/Users/Dell/Downloads/BLACKPINK - Forever Young.mp3']
                                f=open('insertsongs.txt' , 'r')
                                data = f.readlines()
                                song_select_dict2 = {data[0]:song_location_list2[0] , data[1]:song_location_list2[1] , data[2]:song_location_list2[2] , data[3]:song_location_list2[3] , data[4]:song_location_list2[4] , data[5]:song_location_list2[5]}
                                a2=song_select_dict2.values()
                                for c in a2:
                                    sb.insert(END,c)
                            go3()
                            
                        if sc=='popular' or '3' or 'three' :

                            def go4():
                                
                                
                                song_location_list3 = ['C:/Users/Dell/Downloads/DJ Snake - Taki Taki.mp3' , 'C:/Users/Dell/Downloads/Despacito.mp3' , 'C:/Users/Dell/Downloads/Perfect - Ed Sheeran.mp3' ,'C:/Users/Dell/Downloads/Justin-Bieber - Stay.mp3' , 'C:/Users/Dell/Downloads/Counting Stars - OneRepublic.mp3' , 'C:/Users/Dell/Downloads/Sia_-_Cheap_Thrills.mp3' , "C:/Users/Dell/Downloads/We Don't Talk Anymore - Charlie Puth (feat. Selena Gomez).mp3" , 'C:/Users/Dell/Downloads/AnneMarie-2002.mp3']
                                f=open('insertsongs.txt' , 'r')
                                data = f.readlines()
                                song_select_dict3 = {data[0]:song_location_list3[0] , data[1]:song_location_list3[1] , data[2]:song_location_list3[2] , data[3]:song_location_list3[3] , data[4]:song_location_list3[4] , data[5]:song_location_list3[5] , data[6]:song_location_list3[6] , data[7]:song_location_list3[7]}
                                a3=song_select_dict3.values()
                                for n in a3:
                                    sb.insert(END,n)
                            go4()
                        if sc== '4' or 'four' or 'bollywood':
                            def go5():
                                
                                
                                song_location_list4 = ['C:/Users/Dell/Downloads/Raataan Lambiyan - Shershaah.mp3' , 'C:/Users/Dell/Downloads/Tujh Mein Rab Dikhta Hai.mp3' , 'C:/Users/Dell/Downloads/Dil Diyan Gallan - Tiger Zinda Hai.mp3' ,'C:/Users/Dell/Downloads/Tere Bin - Simmba.mp3' , 'C:/Users/Dell/Downloads/Qaafirana - Kedarnath.mp3' , 'C:/Users/Dell/Downloads/Mere Sohneya - Kabir Singh.mp3' , "C:/Users/Dell/Downloads/Tera Yaar Hoon Main - Sonu Ke Titu Ki Sweety.mp3"]
                                f=open('insertsongs.txt' , 'r')
                                data = f.readlines()
                                song_select_dict4 = {data[0]:song_location_list4[0] , data[1]:song_location_list4[1] , data[2]:song_location_list4[2] , data[3]:song_location_list4[3] , data[4]:song_location_list4[4] , data[5]:song_location_list4[5] , data[6]:song_location_list4[6]}
                                a4=song_select_dict4.values()
                                for n in a4:
                                    sb.insert(END,n)
                            go5()
                        
                        if sc=='5' or 'rap':
                            def go6():
                                
                                
                                song_location_list5 = ['C:/Users/Dell/Downloads/apna-time-aayega-gully-boy.mp3' , 'C:/Users/Dell/Downloads/MonteroCall-Me-by-Your-Name.mp3' , 'C:/Users/Dell/Downloads/Yalgaar - CarryMinati.mp3' ,'C:/Users/Dell/Downloads/Polo_G_-Rapstar.mp3' , 'C:/Users/Dell/Downloads/\Eminem-_Rap_God.mp3']
                                f=open('insertsongs.txt' , 'r')
                                data = f.readlines()
                                song_select_dict5 = {data[0]:song_location_list5[0] , data[1]:song_location_list5[1] , data[2]:song_location_list5[2] , data[3]:song_location_list5[3] , data[4]:song_location_list5[4]}
                                a5=song_select_dict5.values()
                                for n in a5:
                                    sb.insert(END,n)
                            go6()

                        def backend():
                            f=open('backend.txt' , 'a')
                            f.write(song)
                            f.close()
                        backend()
                            
                            

                        
                            
                    player()

                        
                                        



                        
                        
                    

                    
                        
                        
            #Button for displaying category selection

            begin2= Button(tab3, text = "➡" , command = speak_cat ,bd = 5, width = 2 ,font=(None,12))
            begin2.pack()
            begin2.place(x=100 , y=210)

            

            
                
        elif ch=='moods':
            tab3 = ttk.Frame(tabcontrol , width = 600,height = 700)
            tabcontrol.add (tab3, text = 'Moods')

            cat=ttk.Label(tab3,text="MOODS:-" , font=(None,14))
            cat.pack()
            cat.place(x=20 , y=20)

            cat=ttk.Label(tab3,text="1.Happy" , font=(None,14))
            cat.pack()
            cat.place(x=20 , y=50)

            cat=ttk.Label(tab3,text="2.Sad" , font=(None,14))
            cat.pack()
            cat.place(x=20 , y=80)

            cat=ttk.Label(tab3,text="3.Motivation" , font=(None,14))
            cat.pack()
            cat.place(x=20 , y=110)

            cat=ttk.Label(tab3,text="4.Party" , font=(None,14))
            cat.pack()
            cat.place(x=20 , y=140)

            cat=ttk.Label(tab3,text="5.Workout" , font=(None,14))
            cat.pack()
            cat.place(x=20 , y=170)

        #Function for mood selection
        def mood1():
            engine = pyttsx3.init()
            engine.say("Enter the number against your mood")
            engine.runAndWait()
                

        #Button for mood selection

        begin2= Button(tab3, text = "Next" , command = mood1 ,bd = 5, width = 6 ,font=(None,12))
        begin2.pack()
        begin2.place(x=20 , y=210)

        #Function for speaking the number against your category
        def speak_mood():
            w = sr.Recognizer()
            with sr.Microphone() as source3:
                # wait for a second to let the recognizer adjust to the surrounding noise
                w.adjust_for_ambient_noise(source3, duration=0.2)
          
                #listens for the user's input
                audio3 = w.listen(source3)
          
                # Uses google to recognize the audio
                sc = w.recognize_google(audio3)
                sc = sc.lower()

                



                def Display2():
                    ch4= ttk.Label(tab3 , text = ('Your choice is '+ sc) , font = (None,14))
                    ch4.pack(padx = 10, pady = 20)
                    ch4.place(x=20, y=270)
                Display2()

    

                def player():

                    #from music2 import player_gui
                    import pygame
                    from PIL import ImageTk,Image
                    from tkinter import filedialog

                    music=Tk()
                    music.title("Song Player")
                    music.geometry("700x500")

                    #Initializing Pygame Mixer
                    pygame.mixer.init()



                    #Creating the Player Box

                    sb=Listbox(music , bg="black" , fg="white", width=90 , height=20, selectbackground="grey" , selectforeground="black")
                    sb.pack(pady=20)
                        
                        

                    #Play Function
                    def play():
                        song=sb.get(ACTIVE)
                        count=0
                        #song = {song}
                        pygame.mixer.music.load(song)
                        pygame.mixer.music.play(loops=0)
                        
                         

                    #Stop Function
                    def stop():
                        pygame.mixer.music.stop()

                    #Save Function
                    def save():
                        song2 = sb.get(ACTIVE)
                        f=open("song3.txt" , 'a')
                        f.write("")
                        f.write(song2)
                        f.close()

                    #Global Variable

                    global paused
                    paused=False

                    #Pause Function
                    def pause(paused3):
                         global paused
                         paused=paused3

                         if paused:
                              #Unpause
                              pygame.mixer.music.unpause()
                              paused=False
                         else:
                              #Pause
                              pygame.mixer.music.pause()
                              paused=True





                    #BUTTONS

                    back2= Button(music, text = "⏮" ,bd = 5, width = 3 ,font=(None,18))
                    back2.pack()
                    back2.place(x=170 , y=375)

                    play2= Button(music, text = "▶" ,command = play , bd = 5, width = 3 ,font=(None,18))
                    play2.pack()
                    play2.place(x=240 , y=375)

                    pause2= Button(music, text = "⏸" ,command= lambda:pause(paused) ,bd = 5, width = 3 ,font=(None,18))
                    pause2.pack()
                    pause2.place(x=310 , y=375)


                    stop2= Button(music, text = "⏹" ,command = stop ,bd = 5, width =3,font=(None,18))
                    stop2.pack()
                    stop2.place(x=380 , y=375)


                    save2= Button(music, text = "⬇️" ,bd = 5, command = save , width = 3 ,font=(None,18))
                    save2.pack()
                    save2.place(x=450 , y=375)




                        




                    #MENU

                    menu1=Menu(music)
                    music.config(menu=menu1)

                    #Functions

                    def add_song():
                         song=filedialog.askopenfilename(initialdir = 'Downloads/',title="Choose A Song", filetypes=(("mp3 Files" , "*.mp3"),))
                         #Adding to listbox
                         sb.insert(END,song)
                         

                    def addmany_songs():
                         songs=filedialog.askopenfilenames(initialdir = 'Downloads/',title="Choose Songs", filetypes=(("mp3 Files" , "*.mp3"),))
                         for song in songs:
                              sb.insert(END,song)

                    #ADDING SONGS
                    add1=Menu(menu1)
                    menu1.add_cascade(label="Add Songs" , menu=add1)
                    add1.add_command(label="Add One Song To The List",command=add_song)

                    add1.add_command(label="Add Many Songs To The List",command=addmany_songs)

                            

                    
                    if sc=='happy' or '1':
                                              
                        def go2():
                            
                                
                            song_location_list = ['C:/Users/Dell/Downloads/Zara Larsson - Lush Life.mp3' , 'C:/Users/Dell/Downloads/Marshmello-ft.-Bastille-Happier.mp3' , 'C:/Users/Dell/Downloads/Ed Sheeran - Beautiful People (feat. Khalid) [Official].mp3' , 'C:/Users/Dell/Downloads/BTS-Permission-To-Dance.mp3' ,'C:/Users/Dell/Downloads/Katy_Perry-Firework.mp3' , 'C:/Users/Dell/Downloads/Jason_Derulo_-_Take_You_Dancing.mp3' , 'C:/Users/Dell/Downloads/Dance Monkey - Tones And I.mp3' , 'Deep-Chills-Run-Free-feat.-IVIE.mp3']
                            f=open('insertsongs.txt' , 'r')
                            data = f.readlines()
                            song_select_dict = {data[0]:song_location_list[0] , data[1]:song_location_list[1] , data[2]:song_location_list[2] , data[3]:song_location_list[3] , data[4]:song_location_list[4] , data[5]:song_location_list[5] , data[6]:song_location_list[6] , data[7]:song_location_list[7]}
                            a=song_select_dict.values()
                            for i in a:
                                sb.insert(END,i)
                        go2()

                    else:
                        if sc=='sad' or '2':
                            def go3():
                                song_location_list2 = ['C:/Users/Dell/Downloads/ROSE-Gone.mp3' , 'C:/Users/Dell/Downloads/Memories.mp3' , "C:/Users/Dell/Downloads/We Don't Talk Anymore - Charlie Puth (feat. Selena Gomez).mp3" ,'C:/Users/Dell/Downloads/Olivia_Rodrigo_-_drivers_license.mp3' , 'C:/Users/Dell/Downloads/Rihanna_ft_Mikky_Ekko-Stay.mp3']
                                f=open('insertsongs.txt' , 'r')
                                data = f.readlines()
                                song_select_dict2 = {data[0]:song_location_list2[0] , data[1]:song_location_list2[1] , data[2]:song_location_list2[2] , data[3]:song_location_list2[3] , data[4]:song_location_list2[4]}
                                a2=song_select_dict2.values()
                                for c in a2:
                                    sb.insert(END,c)
                            go3()

                        elif sc=='motivation' or '3' :

                            def go4():
                                
                                song_location_list2 = ['C:/Users/Dell/Downloads/Alan Walker - On My Way.mp3' , 'C:/Users/Dell/Downloads/Daya-Sit-Still-Look-Pretty.mp3' , "C:/Users/Dell/Downloads/LISA-MONEY.mp3" ,'C:/Users/Dell/Downloads/Sugar Crash - ElyOtto.mp3' , 'C:/Users/Dell/Downloads/Masked_Wolf-Astronaut_In_The_Ocean.mp3']
                                f=open('insertsongs.txt' , 'r')
                                data = f.readlines()
                                song_select_dict2 = {data[0]:song_location_list2[0] , data[1]:song_location_list2[1] , data[2]:song_location_list2[2] , data[3]:song_location_list2[3] , data[4]:song_location_list2[4]}
                                a2=song_select_dict2.values()
                                for c in a2:
                                    sb.insert(END,c)

                            go4()
                                    
                    
                        elif sc== 'party' or '3':

                            def go5():
                                
                                song_location_list2 = ['C:/Users/Dell/Downloads/Safari - Serena.mp3' , 'C:/Users/Dell/Downloads/Dance Monkey - Tones And I.mp3' , "C:/Users/Dell/Downloads/Take You Dancing.mp3" ,'C:/Users/Dell/Downloads/Bilionera.mp3' , 'C:/Users/Dell/Downloads/Maroon 5 Animals.mp3']
                                f=open('insertsongs.txt' , 'r')
                                data = f.readlines()
                                song_select_dict2 = {data[0]:song_location_list2[0] , data[1]:song_location_list2[1] , data[2]:song_location_list2[2] , data[3]:song_location_list2[3] , data[4]:song_location_list2[4]}
                                a2=song_select_dict2.values()
                                for c in a2:
                                    sb.insert(END,c)

                            go5()



                        elif sc=='workout' or '4':

                            def go6():
                                
                                song_location_list2 = ['C:/Users/Dell/Downloads/Get Ready To Fight - Baaghi.mp3' , 'C:/Users/Dell/Downloads/Dance Monkey - Tones And I.mp3' , "C:/Users/Dell/Downloads/Imagine Dragons - Thunder.mp3" ,'C:/Users/Dell/Downloads/Believer - Imagine Dragons.mp3' , 'C:/Users/Dell/Downloads/Kar Har Maidaan Fateh - Sanju.mp3']
                                f=open('insertsongs.txt' , 'r')
                                data = f.readlines()
                                song_select_dict2 = {data[0]:song_location_list2[0] , data[1]:song_location_list2[1] , data[2]:song_location_list2[2] , data[3]:song_location_list2[3] , data[4]:song_location_list2[4]}
                                a2=song_select_dict2.values()
                                for c in a2:
                                    sb.insert(END,c)

                            go6()
                            
                player()

            #Button for displaying mood selection

        begin2= Button(tab3, text = "➡" , command = speak_mood ,bd = 5, width = 2 ,font=(None,12))
        begin2.pack()
        begin2.place(x=100 , y=210)
                

    
                    

            

                    

                    
            
    choice()

#TAB4

tab4=ttk.Frame(tabcontrol,width = 800 , height= 700)
tabcontrol.add(tab4,text='Profile')
tabcontrol.grid(padx=20 , ipadx=18, ipady=18)

def profile():
    
    heading=ttk.Label(tab4,text="User Profile ", font=(None,15))
    heading.pack()
    heading.place(x=350 , y=15)

profile()


def last_5_songs():
    
    f=open('song3.txt')
    b=f.readlines()
    a=b[-1].replace("C:/Users/Dell/Downloads/", "")
    c=b[-2].replace("C:/Users/Dell/Downloads/", "")
    d=b[-3].replace("C:/Users/Dell/Downloads/", "")
    e=b[-4].replace("C:/Users/Dell/Downloads/", "")
    f=b[-5].replace("C:/Users/Dell/Downloads/", "")
    
    user_song1=ttk.Label(tab4,text=a, font=(None,14))
    user_song1.pack()
    user_song1.place(x=200 , y=160)

    user_song2=ttk.Label(tab4,text=c, font=(None,14))
    user_song2.pack()
    user_song2.place(x=200 , y=200)

    user_song3=ttk.Label(tab4,text=d, font=(None,14))
    user_song3.pack()
    user_song3.place(x=200 , y=240)

    user_song4=ttk.Label(tab4,text=e, font=(None,14))
    user_song4.pack()
    user_song4.place(x=200 , y=280)

    user_song5=ttk.Label(tab4,text=f, font=(None,14))
    user_song5.pack()
    user_song5.place(x=200 , y=320)
   

def count():
    list2=[]
    f=open('song3.txt' , 'r')
    a=f.read()
    count=0
    numlines=a.split('\n')
    for i in numlines:
        count+=1
        user_song=ttk.Label(tab4,text=count, font=(None,14))
        user_song.pack()
        user_song.place(x=335 , y=400)
    f.close()



    
begin4= Button(tab4, text = "Last 5 Songs:" , command = last_5_songs ,bd = 5, width = 15 ,font=(None,12))
begin4.pack()
begin4.place(x=20 , y=160)
    

begin3= Button(tab4, text = "Number of songs heard till now are :" , command = count ,bd = 5, width = 30 ,font=(None,12))
begin3.pack()
begin3.place(x=20 , y=400)


            
    
        


# MAIN BUTTON FOR SPEAK FUNCTION

begin2= Button(tab2, text = "➡" , command = speak ,bd = 5, width = 2 ,font=(None,12))
begin2.pack()
begin2.place(x=450 , y=550)



mw.mainloop()
