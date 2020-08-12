# coding=utf-8
def detection():
    import random
    from postures import *

    setPosture(im, getBasePose(), 1)
    im.robot.startSensorMonitor()              

    tm = 0.5
    i = 0
    childFound = False
    while not childFound and i != 40:
        vx = random.uniform(0,1)
        vy = 0
        vth = random.randint(-5, 5)
        im.robot.setSpeed(0, 0, vth, tm, False)
        im.robot.setSpeed(vx, 0, 0, tm, False)
        values = im.robot.sensorvalue() 
        childFound = values < 2.0
        i+= 1

    im.robot.stop()
    im.robot.stopSensorMonitor()
    pepper_cmd.robot.say("HEY!")

def welcome():
    # coding=utf-8
    from utils import *
    from postures import *
    from routines import *

    im.init()                                           # initialize interaction manager
    im.display.loadUrl('welcome_layout.html')           # display initial layout
    

    setPosture(im, getBasePose(), 1)
    quiet_behaviour(im)
    a = im.ask('welcome/welcome_1', timeout=15)        # execute action 'welcome_1' (language selection)
    if a == 'timeout':
        a = 'en'                                        # if timeout set default language
    
    im.profile = ['*', '*', a]                          # update user profile
    setPosture(im, getHelloPosture(), 0.8)

    im.display.loadUrl('main_layout.html')
    im.execute('welcome/welcome_2')                    # execute action 'welcome_2' (longer introduction)
    setPosture(im, getImPepperPosture(), 0.6)
    vocabulary = []    
    setPosture(im, getBasePose(), 1)                    # [ASSUMPTION] vocabulary
    name = im.robot.asr(vocabulary, timeout=15)         # get name of user
    im.executeModality('TEXT_title','')
    com = ''
    if(a == 'it'):
        com = 'Mmm {}, che bel nome!'.format(name)
    elif(a == 'en'):
        com = 'Mmm {}, such a beautiful name!'.format(name)
    elif(a == 'de'):
        com = 'Mmm {}, was für ein schöner Name!'.format(name)
    elif(a == 'es'):
        com = 'Mmm {}, que hermoso nombre!'.format(name)
    elif(a == 'fr'):
        com = 'Mmm {}, quel joli nom!'.format(name)
    setPosture(im, getGoodNamePose(), 0.8)
    happy_behaviour(im)
    im.executeModality('TEXT_default',com)
    pepper_cmd.robot.say(com)
    time.sleep(2)
    
    default_behaviour(im)
    
    categories = ['s', 'm', 'l']
    #[gender, age] = get_real_details(im)
    [gender, age] = get_fake_details()                  # simulate recognition gender and age made by Pepper APIs
    setPosture(im, getThinkingPose(), 0.8)
    im.execute('welcome/welcome_3')                    # start guessing age
    time.sleep(3)                                       # simulate thinking
    setPosture(im, getHandsOnFlanksPose(), 0.8)
    real_age = age
    while(True):                                        # age guessing game
        question_behaviour(im)
        im.executeModality('TEXT_default','Ok, in my opinion you are {} years old. Is it true?'.format(real_age))
        pepper_cmd.robot.say("Ok, in my opinion you are {} years old! Am I right?".format(real_age))
        vocabulary = ['yes', 'more', 'less']                                     
        ans = im.robot.asr(vocabulary, timeout=5)       # get answer age
        if 'yes' in ans.lower():
            setPosture(im, getCelebrationPose(), 0.8)
            happy_behaviour(im)
            pepper_cmd.robot.say("Amazing!")
            cat = categories[((real_age-1)//3)-1]       # get category
            im.profile = [cat, gender, a]             # update profile  
            break
        elif 'more' in ans.lower():
            real_age += 1
            sad_behaviour(im)
            im.executeModality('TEXT_default', 'Mmm.... I see, let me try again')       # [ASSUMPTION] people younger than minimum threshold or older than maximum are not considered here
            setPosture(im, getSadPose(), 0.8)
            pepper_cmd.robot.say("Mmm.... I see, let me try again.")
        elif 'less' in ans.lower():
            real_age -= 1
            sad_behaviour(im)
            im.executeModality('TEXT_default', 'Mmm.... I see, let me try again')
            setPosture(im, getCelebrationPose(), 0.8)
            pepper_cmd.robot.say("Mmm.... I see, let me try again.")

    time.sleep(1)
    setPosture(im, getBasePose(), 1) 
    default_behaviour(im)
    im.execute('welcome/welcome_4')                             # execute action 'welcome_4' (why there)
    vocabulary = []                                             # [ASSUMPTION] vocabulary
    reason = im.robot.asr(vocabulary, timeout=15)               # get reason hospitalization
    check = ['check', 'visit', 'exam', 'control']
    injury = ['injur', 'hurt', 'fall', 'bad']
    
    if checkAns(check, reason):
        happy_behaviour(im)
        im.execute('welcome/welcome_check')
        setPosture(im, getWelcomeCheckPose(), 0.8)
    elif checkAns(injury, reason):
        sad_behaviour(im)
        im.execute('welcome/welcome_injury')
        setPosture(im, getWelcomeInjuryPose(), 0.8)
    
def getemotion():
    from routines import *

    emotions = ["happy", "calm", "sad", "angry", "worried", "bored"]
    currentEmotion = estimateEmotion(emotions)

    currentEmotion = "happy"

    if(currentEmotion == "happy" or currentEmotion == "calm"):
        happyEmotionRoutine(im)
    elif(currentEmotion == "sad"):
        sadEmotionRoutine(im)
    elif(currentEmotion == "angry"):
        angryEmotionRoutine(im)
    elif(currentEmotion == "worried"):
        worriedEmotionRoutine(im)
    elif(currentEmotion == "bored"):
        boredEmotionRoutine(im)

def menu():
    from routines import *
    from postures import *

    setPosture(im, getWelcomeCheckPose(), 0.8)

    ris = 'timeout'
    while (ris != 'home'):         
        if(ris=='stories'):
            stories(im)

        elif(ris=='games'):
            while(ris != "none"):
                if(ris == "candy"):
                    candyGame(im)                   
                elif(ris == "patterns"):
                    colorsPatterns(im)
                elif(ris == "quiz"):
                    quiz(im)
                
                setPosture(im, getWelcomeCheckPose(), 0.8)
                ris = im.ask('menu/games', timeout=60)

        elif(ris=='videos'):
            not_implemented(im)
        
        setPosture(im, getWelcomeCheckPose(), 0.8)
        ris = im.ask('menu/menu', timeout=60)

    setPosture(im, getHelloPosture(), 0.8)
    im.execute("menu/end")
    setPosture(im, getBasePose(), 0.8)