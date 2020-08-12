# |=======================|
# |   Postures Methods    |
# |=======================|
from math import radians

def setPosture(im, jointValues, time):
    jointNames = ["HeadYaw", "HeadPitch",
                  "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw",
                  "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw",
                  "LHand", "RHand", "HipRoll", "HipPitch", "KneePitch"]
    im.robot.motion_service.angleInterpolation(jointNames, jointValues, time, True)

def getBasePose():
    HeadYaw = radians(0.2)
    HeadPitch = radians(0.6)
    LShoulderPitch = radians(88.3)
    LShoulderRoll = radians(7.4)
    LElbowYaw = radians(-71.6)
    LElbowRoll = radians(-29.5)
    LWristYaw = radians(0.1)
    RShoulderPitch = radians(89)
    RShoulderRoll = radians(-8.2)
    RElbowYaw = radians(69.8)
    RElbowRoll = radians(29.6)
    RWristYaw = radians(-0.2)
    LHand = 0.02
    RHand = 0.03
    HipRoll = radians(-0.3)
    HipPitch = radians(-0.2)
    KneePitch = radians(0.1)

    jointValues = [HeadYaw, HeadPitch,
               LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw,
               RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw,
               LHand, RHand, HipRoll, HipPitch, KneePitch]

    return jointValues

def getCandyPose():
    HeadYaw = radians(0)
    HeadPitch = radians(5.1)
    LShoulderPitch = radians(19.7)
    LShoulderRoll = radians(1)
    LElbowYaw = radians(14.8)
    LElbowRoll = radians(-11.1)
    LWristYaw = radians(-21.2)
    RShoulderPitch = radians(19.8)
    RShoulderRoll = radians(-1)
    RElbowYaw = radians(-14)
    RElbowRoll = radians(11)
    RWristYaw = radians(21.2)
    LHand = 0
    RHand = 0
    HipRoll = radians(-0.3)
    HipPitch = radians(-6.3)
    KneePitch = radians(2)


    jointValues = [HeadYaw, HeadPitch,
               LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw,
               RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw,
               LHand, RHand, HipRoll, HipPitch, KneePitch]

    return jointValues

def getLeftRevealed():
    HeadYaw = radians(0)
    HeadPitch = radians(5.1)
    LShoulderPitch = radians(19.7)
    LShoulderRoll = radians(1)
    LElbowYaw = radians(-119)
    LElbowRoll = radians(-11.1)
    LWristYaw = radians(-55.4)
    RShoulderPitch = radians(19.8)
    RShoulderRoll = radians(-1)
    RElbowYaw = radians(-14)
    RElbowRoll = radians(11)
    RWristYaw = radians(21.2)
    LHand = 0.98
    RHand = 0
    HipRoll = radians(-0.3)
    HipPitch = radians(-6.3)
    KneePitch = radians(2)


    jointValues = [HeadYaw, HeadPitch,
               LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw,
               RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw,
               LHand, RHand, HipRoll, HipPitch, KneePitch]

    return jointValues

def getRightRevealed():
    HeadYaw = radians(0)
    HeadPitch = radians(5.1)
    LShoulderPitch = radians(19.7)
    LShoulderRoll = radians(1)
    LElbowYaw = radians(14.8)
    LElbowRoll = radians(-11.1)
    LWristYaw = radians(-21.2)
    RShoulderPitch = radians(19.8)
    RShoulderRoll = radians(-1)
    RElbowYaw = radians(119)
    RElbowRoll = radians(11)
    RWristYaw = radians(55.4)
    LHand = 0
    RHand = 0.98
    HipRoll = radians(-0.3)
    HipPitch = radians(-6.3)
    KneePitch = radians(2)


    jointValues = [HeadYaw, HeadPitch,
               LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw,
               RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw,
               LHand, RHand, HipRoll, HipPitch, KneePitch]

    return jointValues

def getGoodNamePose():
    HeadYaw = radians(0)
    HeadPitch = radians(-11.3)
    LShoulderPitch = radians(91.4)
    LShoulderRoll = radians(9.1)
    LElbowYaw = radians(-119.2)
    LElbowRoll = radians(-89.4)
    LWristYaw = radians(-85.6)
    RShoulderPitch = radians(91.3)
    RShoulderRoll = radians(-2.3)
    RElbowYaw = radians(119.3)
    RElbowRoll = radians(89.1)
    RWristYaw = radians(90.2)
    LHand = 0.98
    RHand = 0.98
    HipRoll = radians(9.6)
    HipPitch = radians(-22.5)
    KneePitch = radians(4.6)

    jointValues = [HeadYaw, HeadPitch,
               LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw,
               RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw,
               LHand, RHand, HipRoll, HipPitch, KneePitch]

    return jointValues

def getThinkingPose():
    HeadYaw = radians(0)
    HeadPitch = radians(-11.4)
    LShoulderPitch = radians(-3.7)
    LShoulderRoll = radians(2.7)
    LElbowYaw = radians(-39.1)
    LElbowRoll = radians(-88.6)
    LWristYaw = radians(-100.1)
    RShoulderPitch = radians(81.3)
    RShoulderRoll = radians(-33.1)
    RElbowYaw = radians(32.4)
    RElbowRoll = radians(70.4)
    RWristYaw = radians(21.4)
    LHand = 0.5
    RHand = 0.98
    HipRoll = radians(0)
    HipPitch = radians(-6.8)
    KneePitch = radians(-0.1)

    jointValues = [HeadYaw, HeadPitch,
               LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw,
               RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw,
               LHand, RHand, HipRoll, HipPitch, KneePitch]

    return jointValues  

def getHandsOnFlanksPose():
    HeadYaw = radians(0)
    HeadPitch = radians(-11.4)
    LShoulderPitch = radians(89.8)
    LShoulderRoll = radians(38.4)
    LElbowYaw = radians(-17.2)
    LElbowRoll = radians(-62.6)
    LWristYaw = radians(-78)
    RShoulderPitch = radians(85.9)
    RShoulderRoll = radians(-37.7)
    RElbowYaw = radians(17.2)
    RElbowRoll = radians(63.3)
    RWristYaw = radians(78.8)
    LHand = 0.98
    RHand = 0.98
    HipRoll = radians(0)
    HipPitch = radians(-6.8)
    KneePitch = radians(0.5)

    jointValues = [HeadYaw, HeadPitch,
               LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw,
               RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw,
               LHand, RHand, HipRoll, HipPitch, KneePitch]

    return jointValues  

def getCelebrationPose():
    HeadYaw = radians(0)
    HeadPitch = radians(-11.4)
    LShoulderPitch = radians(36)
    LShoulderRoll = radians(7.8)
    LElbowYaw = radians(-90.3)
    LElbowRoll = radians(-89.1)
    LWristYaw = radians(-101.4)
    RShoulderPitch = radians(37.1)
    RShoulderRoll = radians(-8.6)
    RElbowYaw = radians(92.2)
    RElbowRoll = radians(89.4)
    RWristYaw = radians(96.1)
    LHand = 0.04
    RHand = 0.03
    HipRoll = radians(0.1)
    HipPitch = radians(-0.5)
    KneePitch = radians(-0.4)

    jointValues = [HeadYaw, HeadPitch,
               LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw,
               RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw,
               LHand, RHand, HipRoll, HipPitch, KneePitch]

    return jointValues   

def getSadPose():
    HeadYaw = radians(0)
    HeadPitch = radians(25.5)
    LShoulderPitch = radians(74)
    LShoulderRoll = radians(2)
    LElbowYaw = radians(-71.8)
    LElbowRoll = radians(-0.7)
    LWristYaw = radians(-0.1)
    RShoulderPitch = radians(71.8)
    RShoulderRoll = radians(-8.7)
    RElbowYaw = radians(70.5)
    RElbowRoll = radians(0.7)
    RWristYaw = radians(-0.1)
    LHand = 0.087
    RHand = 0.03
    HipRoll = radians(-4.5)
    HipPitch = radians(-31.2)
    KneePitch = radians(9.5)

    jointValues = [HeadYaw, HeadPitch,
               LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw,
               RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw,
               LHand, RHand, HipRoll, HipPitch, KneePitch]

    return jointValues 

def getWelcomeCheckPose():
    HeadYaw = radians(0)
    HeadPitch = radians(-21.4)
    LShoulderPitch = radians(119.2)
    LShoulderRoll = radians(19.9)
    LElbowYaw = radians(-2.3)
    LElbowRoll = radians(-79.9)
    LWristYaw = radians(-0.7)
    RShoulderPitch = radians(107)
    RShoulderRoll = radians(-30)
    RElbowYaw = radians(-7)
    RElbowRoll = radians(83.2)
    RWristYaw = radians(-1.2)
    LHand = 0.02
    RHand = 0.03
    HipRoll = radians(-0.5)
    HipPitch = radians(-25.7)
    KneePitch = radians(3.7)

    jointValues = [HeadYaw, HeadPitch,
               LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw,
               RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw,
               LHand, RHand, HipRoll, HipPitch, KneePitch]

    return jointValues 

def getWelcomeInjuryPose():
    HeadYaw = radians(0)
    HeadPitch = radians(-21.4)
    LShoulderPitch = radians(47.6)
    LShoulderRoll = radians(0.6)
    LElbowYaw = radians(-94.1)
    LElbowRoll = radians(-89)
    LWristYaw = radians(-0.4)
    RShoulderPitch = radians(104.5)
    RShoulderRoll = radians(-24.9)
    RElbowYaw = radians(-3.6)
    RElbowRoll = radians(74.2)
    RWristYaw = radians(-1.2)
    LHand = 0.02
    RHand = 0.03
    HipRoll = radians(-0.5)
    HipPitch = radians(-9.1)
    KneePitch = radians(-0.4)

    jointValues = [HeadYaw, HeadPitch,
               LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw,
               RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw,
               LHand, RHand, HipRoll, HipPitch, KneePitch]

    return jointValues

def getHelloPosture():

    HeadYaw = radians(1.4)
    HeadPitch = radians(-9.7)
    LShoulderPitch = radians(91.0)
    LShoulderRoll = radians(5.2)
    LElbowYaw = radians(-81.4)
    LElbowRoll = radians(-11.2)
    LWristYaw = radians(-22)
    RShoulderPitch = radians(-7.0)
    RShoulderRoll = radians(-58.9)
    RElbowYaw = radians(65.3)
    RElbowRoll = radians(71.9)
    RWristYaw = radians(13.0)
    LHand = 0.51
    RHand = 0.98
    HipRoll = radians(0.1)
    HipPitch = radians(-7.0)
    KneePitch = radians(0.5)


    jointValues = [HeadYaw, HeadPitch,
               LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw,
               RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw,
               LHand, RHand, HipRoll, HipPitch, KneePitch]
    return jointValues

def getImPepperPosture():

    HeadYaw = radians(1.3)
    HeadPitch = radians(-9.5)
    LShoulderPitch = radians(70.2)
    LShoulderRoll = radians(4.9)
    LElbowYaw = radians(-84.1)
    LElbowRoll = radians(-88.1)
    LWristYaw = radians(-21.5)
    RShoulderPitch = radians(86.5)
    RShoulderRoll = radians(-12.5)
    RElbowYaw = radians(52.5)
    RElbowRoll = radians(70.3)
    RWristYaw = radians(13.2)
    LHand = 0.56
    RHand = 0.98
    HipRoll = radians(-0.2)
    HipPitch = radians(-6.8)
    KneePitch = radians(0.3)


    jointValues = [HeadYaw, HeadPitch,
               LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw,
               RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw,
               LHand, RHand, HipRoll, HipPitch, KneePitch]
    return jointValues
