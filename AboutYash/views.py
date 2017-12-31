from django.http import HttpResponse

def index(request):
    return HttpResponse( "<h1><marquee>Hello from Yash's Blog Homepage,</marquee></h1>"
                         "<br><h2>In This Blog:</h2>"
                         "<h3><br>1)Myself<br>"
                         "2)My Hobbies<br>"
                         "3)Address<br>"
                         "4)Contact</h3>"
                         "<h2>-Myself</h2><h3><body bgcolor='green'text='white' background='night.png'><p> Hi I am Yash Vermani From India. I am 13 years old. I live in Navi Mummbai"
               "<h2>-My Hobbies</h2><h3>I like to play table tennis, badminton and football.<br>I also like to read books especially the Goosebump series by R.L. Stine<h3>" 
                         "<h2>-Address</h2><h3>I live in India.B-701,Neelsidhi Atlantis,Nerul,Navi Mumbai-400706,Maharashtra"
                         "<h2>-Contact</h2>"
                         "<h3>you can contact me in<br>1)Gmail-yash25vermani@gmail.com<br>2)Twitter-twitter.com/VermaniYash")


