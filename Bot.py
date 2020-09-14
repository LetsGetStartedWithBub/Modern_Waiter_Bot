'''
step 1 -------> Greet User
step 2 -------> take users name
step 3 -------> Ask what user would prefer (About , Booking , Menu)
step 4 -------> According to the preference if they want to book a table than take details
step 5 ------->If user wants to choose about option then tell him/her about restaurant, menu , speciality, location , opening and closing time.
step 6 ------->If user choodes menu then tell them about the dishes that you provide and share some reviews


'''
import random
import smtplib
import wolframalpha
import wikipedia
import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def send_mail(name,contact,email,people_count,timing,code):
    # Send email to visitor as well as owner
    #tutorial Link "https://www.youtube.com/watch?v=MKv1RzBo1-Q"
    #s.login("mitchellanthony1999august@gmail.com", "lgcdbkwtbmqajuhl")
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("mitchellanthony1999august@gmail.com", "lgcdbkwtbmqajuhl")

    msg = MIMEMultipart()
    message_template = read_template('message.txt')
    message = message_template.substitute(PERSON_NAME=name.title(),COUPON_CODE=code,NUMBER_OF_PEOPLE=people_count,TIMING=timing,MOBILE_NUMBER=contact)
    msg['From'] = 'mitchellanthony1999august@gmail.com'
    msg['To'] = email
    msg['Subject'] = "Confirmation Mail"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # message to be sent
    #message = ("%s your booking at Restaurant Zaffran for %d number people around %s timing is confirmed. Your registered mobile number is %d and the coupon code that you have received is %s" %(name,people_count,timing,contact,code))

    # sending the mail
    s.send_message(msg)

    # terminating the session
    s.quit()


def take_user_data(name):        #OPTION 3 FUNCTIONALITY
    owner_mail_id='mitrya20@gmail.com'
    list_of_code = random.sample(range(1, 500), 2)
    data_dictionary={}
    print("So it will our pleasure to have you as our guest ......\n please provide me with you contact number and your email address so that we can send you a confirmation message after booking a table for you .... and don't forget to tell us the number of beautiful peoples that are going to join you at our restaurant......")
    contact = int(input("Enter your valid contact number : "))
    data_dictionary['your_contact']=contact
    email = input("Enter your valid email id : ")
    data_dictionary['your_email'] = email
    people_count = int(input("Enter number of peoples for booking table : "))
    data_dictionary['number_of_guest'] = people_count
    timing=input("For what timing you wish to book a table: ")
    data_dictionary['visiting_time'] = timing
    code="SALE"+str(list_of_code)
    ask=input("Do you want to proceed with booking 'yes' or 'no' : ")
    if ask=='yes' or ask=='Yes'or ask=='YES':
        send_mail(name,contact,email,people_count,timing,code)
        send_mail(name, contact, owner_mail_id, people_count, timing, code)
        print("\n Booking done!!!!!!")


def menu_selector(name):            #OPTION 2 FUNCTIONALITY

    menu=['Biryani', 'Paneer pulao', 'Fried Rice', 'Pineapple Raita', 'Murg Mussalam', 'Chicken Kadahi', 'Chicken Nawabi', 'Phirini', 'Chicken Tikka ', 'Mutton Curry', 'Kalmi kebabs', 'Tandoori Chicken', 'Haryali Chicken', 'Chicken kebabs', 'kebabs salad', 'salad', 'Sizzler', 'Butter Chicken', 'Kadhai Paneer', 'Noodles', 'Gobi Manchurian', 'Paneer Tikka Masala', 'Soup', 'Finger Chips', 'Choley Bhaturey', 'Aloo Gobi', 'Dal Tadka', 'Dal Makhani', 'Naan', 'Lachcha Paratha', 'Coffee', 'Lassi', 'Iced Coffee', 'Sundae']
    print(menu)

    print("Do you have any query like what is today's special....")
    menu_select=input("Then type 'a' for having a discount coupon and also for booking table in advance [NOTE: Booking can only be made 2 hours in advance.].")
    if menu_select=='a':
        print("Today's special is ",random.choice(menu))
    booking_table=input("Do you want to book or you had already booked (yes/no).... ")
    if booking_table=='yes' or booking_table=='Yes' or booking_table=='YES':
        take_user_data(name)


def about(name):                #OPTION 1 FUNCTIONALITY
    print(name ,", Restaurant Zaffran.... is situated near Akhlaq Apts., Opp. New I.G. Girls Hostel, Lal Diggi Road, Aligarh. \n Name of Owner is Mr.Usman Obaid and he is a fabulous chef......You will definitly love to be at his service. The opening and closing time of our restaurant is Monday to saturday from 9:00am to 9:00pm....And there are special discounts for our regular customers... So what are you waiting for have a visit.......I am waiting for you to visit :)")

def main_function():
        print("Hi !! this is your virtual waiter at your service.......")
        name = input("what is your name : ")
        print("What a pretty name :)  ", name)
        print(" How can I help you? ", name, " .....Ok let me provide you with some options :")
        while(True):
            print("\n Type 1 --- About my restaurant")
            print("Type 2 --- For Booking a table at restaurant")
            print("Type 3 --- Menu ")
            print("Type 4 --- Regarding some dishes or any current affair going on in this world")
            print("Type 5 --- If you wanna say bye or quit")
            option = input()
            if option == '1' or option.lower()=='about' or option.lower()=='about zafraan':
                about(name)

            elif option == '2' or option.lower()=='book table' or option.lower()=='book a table' or option.lower()=='for booking table':
                take_user_data(name)
                # send_info(name,contact,email,people_count)

            elif option == '3' or option.lower()=='menu' or option.lower()=='today special menu ':
                menu_selector(name)

            elif option=='5' or option.lower()=='bye' or option.lower()=='quit':
                print("Nice talking to you .....Bye")
                break

            else:
                try:
                    client = wolframalpha.Client("LR923L-K2AHW42J2L")  # Paste Your API Key Here....!!!
                    res = client.query(option)
                    ans = next(res.results).text
                    print(ans)

                except Exception:
                    try:
                        results = wikipedia.summary(option, sentences=2)
                        print(results)


                    except Exception:
                        try:
                            webbrowser.open('https://google.com/?#q=' + option)

                        except:
                            print("It is weird but I don't understand what are you asking for.....please type a valid input")




main_function()
