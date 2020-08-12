# coding=utf-8
import random


# |=======================|
# |   Generic Utilities   |
# |=======================|
def get_fake_details():
    genders = ['m', 'f']
    gender = genders[random.randint(0,1)]
    age = random.randint(4, 12)
    info = [gender, age]
    return info

def checkAns(l, sent):
    for i in l:
        if i in sent:
            return True
    return False

def get_real_details(im):
    global id
    
    subPeopleList = im.robot.memory_service.subscriber("PeoplePerception/VisiblePeopleList")
    idSubPeopleList = subPeopleList.signal.connect(on_visible_people_change)

    subPeopleList.signal.disconnect(idSubPeopleList)
    
    age = im.robot.memory_service.getData("PeoplePerception/Person/"+str(id)+"/AgeProperties")[0]
    gender_temp = im.robot.memory_service.getData("PeoplePerception/Person/"+str(id)+"/GenderProperties")[0]
    gender = "f" if gender_temp == 0 else "m"
    
    return [gender, age]

def on_visible_people_change(peopleList):
    global id
    if(len(peopleList)!=0):
        id = peopleList[0]





