'''
step 1 -------> Greet User
step 2 -------> take users name
step 3 -------> Ask what user would prefer (About , Booking , Menu)
step 4 -------> According to the preference if they want to book a table than take details
step 5 ------->If user wants to choose about option then tell him/her about restaurant, menu , speciality, location , opening and closing time.
step 6 ------->If user chooses menu then tell them about the dishes that you provide and share some reviews


'''
import re
import random
import smtplib
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import pandas as pd
from openpyxl import load_workbook


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def save_data(name,email, contact):
    df = pd.DataFrame({'Name': [name],
                       'Email': [email],
                       'contact': [contact]})
    writer = pd.ExcelWriter('data.xlsx', engine='openpyxl')
    # try to open an existing workbook
    writer.book = load_workbook('data.xlsx')
    # copy existing sheets
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    reader = pd.read_excel(r'data.xlsx')
    # write out the new sheet
    df.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)

    writer.close()

def display_pdf():
    link_to_pdf = ''
    sleep(2)
    print("Star Waiter : So, This is Zaffran's exotic menu..... 🍝 🍲 🍛 🍸")
    sleep(2)
    print('''NAZARANA-E-TANDOOR(BREADS)------------------------------------
            * Tandoori Roti                 * Veg.Shezwan Chowmein
            * Plain Nan                     * Singapore Chowmein (Veg.)
            * Butter Nan                    * Singapore Chowmein (Non Veg.)
            * Butter Roti                   * Chinese Chopseuy (Non Veg.)
            * Akbari Nan                    * Veg.Chopseuy
            * Cheese Nan                    * America Chopseuy (Non Veg.)
            * Missi Roti                    * Gobi Manchurian
            * Lachcha Paratha               * Veg. Manchurian
            * Stuffed Paratha               * Chicken Manchurian
            * Chicken Paratha               * Chilli Paneer
            * Mughlai Paratha               * Chicken 65
            * Mint Paratha                  * Chicken Lollipop
            * Stuffed Nan                   * Drum of Heaven (4 pcs.)
                                            * Chicken Hong Kong (8 pcs.)
                                            
            EGG CURRIES ---                 SNACKS---
            * Egg Butter Masala             * Veg.Sandwich
            * Egg Bhurji                    * Cheese Sandwich
            * Egg Curry                     * Egg Sandwich
                                            * Chicken Sandwich
            SALAD & RAITA---                * Butter Toast
            * Special Green Salad           * Chicken Cutlet
            * Cucumber Salad                * Veg.Cutlet
            * Russian Salad                 * Paneer Pakoda
            * Pineapple Raita               * Chicken Pakoda
            * Plain Raita                   * Egg Pakoda
            * Boondi Raita                  * Veg.Pakoda
            * Plain Dahi                    * Finger Chips
            * Mint Raita                    * Choley Bhaturey
            * Fruit Raita
            * Mint Raita 
            
            CHINESE---
            * Chilli Chicken (Boneless)
            * Veg.Chowmein
            * Chicken Chowmein
            * Egg Chowmein
            * Mix Chowmein
    ''')
    sleep(4)
    print("There are many more left............")
    sleep(2)
    print("Star Waiter : You can download pdf from here :`https://zafraanrestaurant.com/pdf/our-full-menu.pdf`")
    #print("htmlfile,'<a href="%s">%s</a> (%s)''' % (link.encode('UTF8', 'replace'),title.encode('UTF8','replace'), description.encode('UTF8','replace')))

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def send_mail(name,contact,email,people_count,timing,code):
    # Send email to visitor as well as owner
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("mitchellanthony1999august@gmail.com", "xcamjbbnuebsfqiv")

    msg = MIMEMultipart()
    message_template = read_template('message.txt')
    message = message_template.substitute(PERSON_NAME=name.title(),COUPON_CODE=code,NUMBER_OF_PEOPLE=people_count,TIMING=timing,MOBILE_NUMBER=contact)
    msg['From'] = 'mitchellanthony1999august@gmail.com'
    msg['To'] = email
    msg['Subject'] = "CONFORMATION MAIL"
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
    sleep(2)
    contact = int(input("Star Waiter : Enter your valid contact number : "))
    sleep(2)
    email = input("Star Waiter : Enter your valid email id : ")

    if (re.search(regex, email)):

        people_count = int(input("Star Waiter : Enter number of peoples for booking table : "))
        timing = input("Star Waiter : For what timing you wish to book a table: ")
        data_dictionary['your_contact'] = contact
        data_dictionary['your_email'] = email
        data_dictionary['number_of_guest'] = people_count
        data_dictionary['visiting_time'] = timing
        code="SALE"+str(list_of_code)
        sleep(2)
        ask=input("Star Waiter : Do you want to proceed with booking 'yes' or 'no' : ")
        if ask=='yes' or ask=='Yes'or ask=='YES':
            send_mail(name,contact,email,people_count,timing,code)
            send_mail(name, contact, owner_mail_id, people_count, timing, code)
            save_data(name,email,contact)
            print("\n Booking Done  😀 👍 !!!!")
            sleep(2)
            print("Star Waiter : Thanks a lot for booking a table 🙂 ..... ", name)

        else :
            sleep(2)
            print("Star Waiter : No Problem ",name," you can book a table whenever you want to visit Zaffran 🙂 .......")

    else:
        sleep(2)
        print("Star Waiter : ",name ,"please enter a valid email and contact number......")
        take_user_data(name)

def menu_selector(name):            #For showing menu

    menu=['Biryani', 'Paneer pulao', 'Fried Rice', 'Pineapple Raita', 'Murg Mussalam', 'Chicken Kadahi', 'Chicken Nawabi', 'Phirini', 'Chicken Tikka ', 'Mutton Curry', 'Kalmi kebabs', 'Tandoori Chicken', 'Haryali Chicken', 'Chicken kebabs', 'kebabs salad', 'salad', 'Sizzler', 'Butter Chicken', 'Kadhai Paneer', 'Noodles', 'Gobi Manchurian', 'Paneer Tikka Masala', 'Soup', 'Finger Chips', 'Choley Bhaturey', 'Aloo Gobi', 'Dal Tadka', 'Dal Makhani', 'Naan', 'Lachcha Paratha', 'Coffee', 'Lassi', 'Iced Coffee', 'Sundae']
    print('''
    
    ''')
    sleep(2)
    print("Star Waiter : Today's special is",random.choice(menu)," and people love it 😃")
    display_pdf()


def about(name):                #About Restaurant Zaffran
    sleep(2)
    print("Star Waiter : In a land far, far away, a very creative food craft student dreamt about creating a place filled with taste, hospitality & the happiness and result is 'Zaffran' 👨‍🍳.")
    sleep(2)
    print("Star Waiter : Zaffran is fabulous restaurant situated near, Akhlaq Apts., Opp. New I.G. Girls Hostel, Lal Diggi Road, Aligarh.")
    sleep(2)
    print("Star Waiter : Following the principal of 'Progress in civilization has been accompanied by progress in cookery',")
    sleep(2)
    print("Star Waiter : ZAFRAAN is continuing to deliver the promise of healthy, homely, hygienic and tasty cuisine available with in affordable prices.")
    sleep(2)
    print("Star Waiter : For further more query you can contact us, Ph: 8810151147 / 9219455860 / 9719857950")


def main_function(name):

        while(True):
            sleep(2)
            print("Star Waiter : So with which option you wanna proceed.....🤔")
            sleep(2)
            print("1 ---> About my restaurant")
            sleep(2)
            print("2 ---> For Booking a table at restaurant")
            sleep(2)
            print("3 ---> Menu  😋 ")
            sleep(2)
            print("4 ---> If you wanna say bye or quit")
            option = input("Visitor : ")
            option = option.lower()
            if 'book table' in option or 'book a table' in option or 'for booking table' in option or 'booking' in option or 'book' in option:
                sleep(2)
                print(" Star Waiter : So it will our pleasure to have you as our guest ......")
                sleep(2)
                print("Star Waiter : please provide me with you contact number and your email address ")
                sleep(2)
                print("Star Waiter : So that we can send you a confirmation message after booking a table for you .... ")
                sleep(2)
                print("Star Waiter :And don't forget to tell us the number of beautiful peoples that are going to join you at our restaurant......")
                take_user_data(name)
                # send_info(name,contact,email,people_count)

            elif 'menu' in option or 'today special menu ' in option or 'dishes' in option:
                menu_selector(name)

            elif 'about' in option or 'about zafraan' in option:
                about(name)

            elif 'bye' in option or 'quit' in option:
                sleep(2)
                print("Star Waiter : It's ok. You can chat with me anytime. I'm always here to help you. 🙂")
                sleep(2)
                print("Star Waiter : Nice talking to you",name,".....Bye")
                break

            else:
                sleep(2)
                print("Star Waiter : Sorry 🥺, I am out of ideas right now. Please contact us at +91 - 881 015 1147 +91 - 921 945 5860 +91 - 971 985 7950")

def rest_of_the_option(name):
    sleep(2)
    print("Star Waiter : Other options on which I can help you are .......")
    while (True):
        sleep(2)
        print("Star Waiter : So with which option you wanna proceed.....🤔")
        sleep(2)
        print("1 ---> About my restaurant")
        sleep(2)
        print("2 ---> Menu  😋 ")
        sleep(2)
        print("3 ---> If you wanna exit then say bye or quit")
        option = input("Visitor : ")
        option = option.lower()
        if 'menu' in option or 'today special menu ' in option or 'dishes' in option:
            menu_selector(name)

        elif 'about' in option or 'about zafraan' in option:
            about(name)

        elif 'book table' in option or 'book a table' in option or 'for booking table' in option or 'booking' in option or 'book' in option:
            take_user_data(name)


        elif 'bye' in option or 'quit' in option or 'exit' in option:
            sleep(2)
            print("Star Waiter : It's ok. You can chat with me anytime. I'm always here to help you. 🙂")
            sleep(2)
            print("Star Waiter : Nice talking to you", name, ".....Bye")
            break

        else:
            sleep(2)
            print("Star Waiter : Sorry 🥺, I am out of ideas right now. Please contact us at +91 - 881 015 1147 , +91 - 921 945 5860 , +91 - 971 985 7950")



def start_function():
    print("Star Waiter : Hola !! this is your Star waiter at your service.......")
    sleep(2)
    print("Star Waiter : what is your name : ")
    name = input("Visitor : ")
    sleep(2)
    print("Star Waiter : Nice to meet you 😄! ", name)
    sleep(2)
    print("Star Waiter : Hey ",name," there is a surprise for you.....🤩 !!!!")
    sleep(2)
    print("Star Waiter : we have an awesome 10% off coupon 🥳 🎉,for a limited time. Would you like to have it ?")
    sleep(2)
    print("Star Waiter : Give your answer in (Yes or no) ")
    user_response = input("Visitor : ")

    if user_response.lower()=='yes':
            sleep(2)
            print("Star Waiter : For booking a table at Zaffran , please provide us with following details..........")
            take_user_data(name)
            rest_of_the_option(name)

    else:
        sleep(2)
        print("Star Waiter : No Problem ......", name)
        sleep(2)
        print("Star Waiter : So, these are the options on which I can assist you ...... now tell me with which option you want to proceed ....... 👇")
        main_function(name)

start_function()