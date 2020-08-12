# coding=utf-8
from math import radians
from postures import *
import random, time


# |=======================|
# |     TTS Behaviours    |
# |=======================|
def yellow_eyes(robot):
        if robot.leds_service!=None:
            # yellow face leds
            robot.leds_service.on('LeftFaceLedsGreen')
            robot.leds_service.on('LeftFaceLedsRed')
            robot.leds_service.off('LeftFaceLedsBlue')
            robot.leds_service.on('RightFaceLedsGreen')
            robot.leds_service.on('RightFaceLedsRed')
            robot.leds_service.off('RightFaceLedsBlue')

def tts_parameters(robot, speed=100, volume=1):
    robot.tts_service.setParameter("speed", speed)
    robot.tts_service.setParameter("volume", volume)

def happy_behaviour(im):
    tts_parameters(im.robot, 140, 1.5)
    yellow_eyes(im.robot)

def sad_behaviour(im):
    tts_parameters(im.robot, 60, 0.5)
    im.robot.red_eyes()

def default_behaviour(im):
    tts_parameters(im.robot, 100, 1.0)
    im.robot.white_eyes()

def quiet_behaviour(im):
    tts_parameters(im.robot, 100, 1.0)
    im.robot.green_eyes()

def question_behaviour(im):
    tts_parameters(im.robot, 80, 0.9)
    im.robot.blue_eyes()


# |=======================|
# |    Emotion Routines   |
# |=======================|
def isAffermative(sentence):
    return 'yes' in sentence or 'si' in sentence

def checkPresence(keywords, sentence):
    print(sentence)
    print(keywords)
    for word in keywords:
        if(word in sentence):
            return True
    return False

def estimateEmotion(emotions):
    return emotions[random.randint(0,len(emotions)-1)]

def happyEmotionRoutine(im):
    happy_behaviour(im)
    setPosture(im, getThinkingPose(), 0.8)
    im.execute("emotions/happy")
    setPosture(im, getBasePose(), 0.8)

def boredEmotionRoutine(im):
    question_behaviour(im)
    setPosture(im, getThinkingPose(), 0.8)
    im.execute("emotions/bored")
    setPosture(im, getBasePose(), 0.8)

def sadEmotionRoutine(im):
    question_behaviour(im)
    setPosture(im, getThinkingPose(), 0.8)
    ris = im.ask('emotions/sad_q1', timeout=60)
    if(ris == 'yes'):
        sad_behaviour(im)
        setPosture(im, getSadPose(), 0.8)
        im.execute("emotions/sad_q2")
        vocab = ["paura", "noia", "afraid", "bored"]
        ris = im.robot.asr(vocab, 60)
        if(checkPresence(["paura", "afraid", "fear"], ris)):
            happy_behaviour(im)
            setPosture(im, getWelcomeCheckPose(), 0.8)

            if(checkPresence(["dottore", "doctor"], ris)):
                im.execute("emotions/doctor_fear")

            elif(checkPresence(["dolore", "male", "pain", "hurt"], ris)):
                im.execute("emotions/pain_fear")
            
            im.execute("emotions/doing_something")

        elif(checkPresence(["noia", "bored"], ris)):
            quiet_behaviour(im)
            boredEmotionRoutine(im)

    elif(ris == 'no'):
        default_behaviour(im)
        setPosture(im, getWelcomeCheckPose(), 0.8)
        im.execute("emotions/no_problem")
    else:
        default_behaviour(im)
        setPosture(im, getWelcomeCheckPose(), 0.8)
        im.execute("emotions/no_answer") 

def worriedEmotionRoutine(im):
    question_behaviour(im)
    setPosture(im, getThinkingPose(), 0.8)
    im.execute("emotions/worried_question")
    vocab = ["dolore", "pain", "doctor", "dottore", "fratello", "brother", "sorella", "sister"]
    ris = im.robot.asr(vocab, 60)
    if(checkPresence(["dolore", "pain"], ris)):
        #Preoccupato dal dolore.
        quiet_behaviour(im)
        setPosture(im, getWelcomeCheckPose(), 0.8)
        im.execute("emotions/pain_fear")
        im.execute("emotions/doing_something")

    elif(checkPresence(["doctor", "dottore"], ris)):
        #Paura del dottore
        quiet_behaviour(im)
        setPosture(im, getWelcomeCheckPose(), 0.8)
        im.execute("emotions/doctor_fear")
        im.execute("emotions/doing_something")

    elif(checkPresence["fratello", "brother", "sorella", "sister"], ris):
        #paura per fratello o sorella
        quiet_behaviour(im)
        setPosture(im, getSadPose(), 0.8)
        im.execute("emotions/worried_question")
        vocab = ["influenza", "flu", "braccio", "gamba", "arm","leg"]
        ris = im.robot.asr(vocab, 60)
        if(checkPresence(["influenza", "flu"], ris)):
            #influenza
            setPosture(im, getWelcomeCheckPose(), 0.8)
            im.execute("emotions/relative_flu")
        elif(checkPresence(["braccio", "gamba", "arm","leg"], ris)):
            #infortunio arti
            setPosture(im, getWelcomeCheckPose(), 0.8)
            im.execute("emotions/relative_limbs")
        else:
            #infortunio generico
            setPosture(im, getWelcomeCheckPose(), 0.8)
            im.execute("emotions/relative_general")
        
        im.execute("emotions/doing_something")  

    elif(checkPresence["non ho paura", "niente", "no worried", "nothing", "none"], ris):
        #no problem
        happy_behaviour(im)
        setPosture(im, getWelcomeCheckPose(), 0.8)
        im.execute("emotions/no_problem")
    else:
        #nessuna risposta
        sad_behaviour(im)
        setPosture(im, getWelcomeCheckPose(), 0.8)
        im.execute("emotions/no_answer") 

def angryEmotionRoutine(im):
    question_behaviour(im)
    setPosture(im, getThinkingPose(), 0.8)
    im.execute("emotions/angry_question")
    vocab = ["noia", "bored", "amic", "friend"]
    quiet_behaviour(im)
    ris = im.robot.asr(vocab, 60)
    if(checkPresence(["noia", "bored"], ris)):
        boredEmotionRoutine(im)
    elif(checkPresence(["amic", "friend"], ris)):
        setPosture(im, getWelcomeCheckPose(), 0.8)
        im.execute("emotions/angry_friend")
    else:
        setPosture(im, getWelcomeCheckPose(), 0.8)
        im.execute("emotions/angry_general")


# |=======================|
# |       Activities      |
# |=======================|
def not_implemented(im):
    im.execute("not_implemented")

def stories(im):
    templatePar = '/stories/par-'
    for i in range(1,19):
        ris = im.ask(templatePar+str(i),timeout=5)
        if(ris == 'stop'):
            break


# |=======================|
# |         Games         |
# |=======================|
def randomWin(threshold):
    sample = random.random()
    return sample < threshold    

def candyGame(im):
    setPosture(im, getCandyPose(), 1)
    age = im.profile[0]
    threshold = 0.75 if(age=='s') else (0.65 if(age=='m') else 0.55)
    im.execute("games/candy/candy_question")

    im.robot.startSensorMonitor()              

    values = im.robot.sensorvalue() 
    candy_ris = "none"
    while(values[4] == 0 and values[5] == 0 and candy_ris == "none"):
        values = im.robot.sensorvalue()
        vocab = ["sinistra", "destra","left","right"] 
        candy_ris = im.robot.asr(vocab, 5)
        candy_ris = candy_ris if (candy_ris in vocab) else "none" 

    im.robot.stopSensorMonitor()

    if(values[4] == 1 or candy_ris == "left" or candy_ris == "sinistra"):
        setPosture(im, getLeftRevealed(), 0.5)  
    elif(values[5] == 1 or candy_ris == "right" or candy_ris == "destra"):
        setPosture(im, getRightRevealed(), 0.5)

    if(randomWin(threshold)):
        im.execute("games/candy/candy_win")
    else:
        im.execute("games/candy/candy_lose")

    setPosture(im, getCandyPose(), 1)
    setPosture(im, getBasePose(), 1)

def colorsPatterns(im):
    #introduction
    im.execute('games/colorsPattern/color_explaination')

    #inizializzazione di n in base alla fascia d'età
    age = im.profile[0]
    n = 3 if (age == 's') else (4 if(age=='m') else 5)
    duration =  5 if (age == 's') else (4 if(age=='m') else 3)
    #geneazione sequenza di colori lunga n
    seq=[]
    colors = ['red','blue','green','yellow']
    for aux in range(n):
        i = random.randint(0,3)
        color = colors[i]
        seq.append(color)
        if(color=='red'):
            im.robot.white_eyes()
        elif(color=='blue'):
            im.robot.blue_eyes()
        elif(color=='green'):
            im.robot.green_eyes()
        elif(color=='yellow'):
            yellow_eyes(im.robot)      
        time.sleep(duration)

    im.robot.white_eyes()
    print("===================")
    print(seq)
    print("===================")
    i=0
    #sequenza di risposta
    while (i < n):
        #aquisizione riposta i-esima
        ris = im.ask('games/colorsPattern/color_answer', timeout=60)

        #no risposta
        if(ris == "timeout"):
            continue

        #stop
        elif(ris == "stop"):
            return

        #risposta i-esima corretta
        elif(ris == seq[i]):
            i += 1

        #risposta i-esima sbagliata
        else:
            setPosture(im, getSadPose(), 0.8)
            im.execute('games/colorsPattern/color_lose')
            return
    
    #Vittoria.
    setPosture(im, getCelebrationPose(), 0.8)
    im.execute('games/colorsPattern/color_win')
    return

def quiz(im):
    setPosture(im, getWelcomeCheckPose(), 1)
    age = im.profile[0]
    completedQuestion = []
    
    im.execute("games/quiz/explaination")

    n = 1 if (age == 's') else (2 if(age=='m') else 3)

    for x in range(n):
        i = random.randint(1,7)
        if(i not in completedQuestion):
            ris = im.ask('games/quiz/quiz'+str(i), timeout=60)
            if(ris == "wrong"):
                setPosture(im, getSadPose(), 0.8)
                im.execute("games/quiz/quiz_lose")
                return
            elif(ris == "stop"):
                return
            im.execute("games/quiz/correct_answer")
            completedQuestion.append(i)
    
    setPosture(im, getCelebrationPose(), 0.8)
    im.execute("games/quiz/quiz_win")
    return