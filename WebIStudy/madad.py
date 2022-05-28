from .models import *
def madad():
   
    forums = Forum.objects.all()
    messeges = ForumMessage.objects.all()
    user = User.objects.all()

    print()
    print("-----------------------------------------------------------------")
    print("Total Messeges:" + str(len(messeges)))
    print("-----------------------------------------------------------------")
    print("Number of users:" + str(len(user)))
    print("-----------------------------------------------------------------")
    print("Forum name                                |Number of Messege")
    print("-----------------------------------------------------------------")
    a = 30
    for i in forums:
        forum = ForumMessage.objects.filter(Forum_name = i.Forum_name)
        b = len(forum)
        print("Forum name: " + i.Forum_name , end="")
        for j in range(a -len(i.Forum_name)):
            print(" ", end="")
        print("|Messege: " + str(b))
        print("-----------------------------------------------------------------")
   
