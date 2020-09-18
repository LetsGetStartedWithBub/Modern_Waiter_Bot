<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>BotUI - Hello World</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <!--#1 CSS Files-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/botui/build/botui.min.css" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/botui/build/botui-theme-default.css" />
    <style>
      html, body {
        background-color: #ccbe41;
        background-image: linear-gradient(-90deg, #edba39, #f0e548);
      }
      .botui-container {
        background-color: inherit;
      }

      .botui-messages-container {
      }

      .botui-actions-container {
        padding: 0px 30px;
      }

      .botui-message {
      }

      .botui-message-content.text {
        background-color: #e1fafc;
        color: #404040;
      }

      .botui-message-content.human {
        background-color: #f7ff61;
        color: #404040;
      }

      .botui-message-content.embed {
      }

      .botui-message-content-link {
      }

      .botui-actions-text-input {
      }

      .botui-actions-text-submit {
      }

      button.botui-actions-buttons-button {
        margin-top: 0px;
      }
    </style>
  </head>
  <body>
    <!--#2 BotUI Tag-->
    <div class="botui-app-container" id="hello-world">
      <bot-ui></bot-ui>
    </div>
    <!--#3 Javascript Files-->
    <script src="https://cdn.jsdelivr.net/vue/latest/vue.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/botui/build/botui.js"></script>
    <script src="https://smtpjs.com/v3/smtp.js"></script>
    <script>
      const kara = new BotUI('hello-world')
      const fullNameCheck = name => /^[a-zA-Z]+ [a-zA-Z]+$/.test(name)
      const fullEmailCheck = email => /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)
      var name;

      const ask_menu= () =>{
        kara.message.add({
          delay:2000,
          loading: true,
          content: "So, This is Zaffran's exotic menu..... 🍝 🍲 🍛 🍸 "
        }).then(_=>{
          kara.message.add({
            type: 'html',
            content:`
            <img src = 'https://repl.it/@MDD4/starwaiter#Screenshot (192).png/' width="224" height="500">
            `
          }).then(_=>{
            kara.message.add({
            type: 'html',
            content:`
            <img src = 'https://repl.it/@MDD4/starwaiter#Screenshot (194).png/' width="224" height="500">
            `
          }).then(_=>{
            
            kara.action.button({
              action:[
                {
                  text : "About",
                  value : 0,
                },
                {
                  text : "Menu",
                  value: 1,
                },
                {
                  text : "Exit",
                  value: 2,
                }
              ]
            }).then(res5 =>{
              if(res5.value==0){
                ask_about()
              }
              else if(res5.value==1){
                ask_menu()
              }
              else exit()
            })
            
          })
          })
        })
      }

      const send_mail = (name,email) =>{
        Email.send({
          SecureToken :"Token",
          To: "Receiver_mail",
          From: "Sender_mail",
          Subject : "CONFIRMATION MAIL",
          Body: "Well that was easy",
        }).then(_=>{
          kara.message.add({
            delay:2000,
            loading: true,
            content:"Booking Done  😀 👍 !!!!"
          }).then(_=>{
            kara.action.button({
              action:[
                {
                  text : "About",
                  value : 0,
                },
                {
                  text : "Menu",
                  value: 1,
                },
                {
                  text : "Exit",
                  value: 2,
                }
              ]
            }).then(res5 =>{
              if(res5.value==0){
                ask_about()
              }
              else if(res5.value==1){
                ask_menu()
              }
              else exit()
            })
          })
        })
      }

      const ask_about = ()=>{
        kara.message.add({
          delay: 2000,
          loading: true,
          content: "In a land far, far away, a very creative food craft student dreamt about creating a place filled with taste, hospitality & the happiness and result is 'Zaffran' 👨‍🍳. Zaffran is fabulous restaurant situated near, Akhlaq Apts., Opp. New I.G. Girls Hostel, Lal Diggi Road, Aligarh."
        }).then(_=>{
          kara.message.add({
          delay: 3000,
          loading: true,
          content:"Following the principal of 'Progress in civilization has been accompanied by progress in cookery', ZAFRAAN is continuing to deliver the promise of healthy, homely, hygienic and tasty cuisine available with in affordable prices."
          }).then(_=>{
            kara.message.add({
            delay: 2000,
            loading: true,
            content: "For further more query you can contact us, Ph: 8810151147 / 9219455860 / 9719857950"
        }).then(_=>{
          ask_all_options()
        })

        })

        })
        
        
      }

      const ask_all_options = (name)=>{
        kara.message.add({
          delay: 2000,
          loading: true,
          content: "So, here are all the options with which I can help you out ...... then tell me with which you want to proceed ....... "
        }).then(_=>{
          kara.action.button({
            action:[
              {
                text: "About",
                value: 0
              },
              {
                text: "Menu",
                value: 1,
              },
              {
                text: "Booking",
                value: 2
              }
            ]
          }).then(res4=>{
            if(res4.value==0){
              ask_about()
            }
            else if(res4.value==1){
              ask_menu()
            }
            else{
              ask_booking(name)
            }
          })
        })
      }

      
      const ask_email = (name)=>{
          kara.action.text({
            action:[
            {
              placeholder:"Your Email"
            }]
          }).then(res4=>{
            email = res4.value
            if(fullEmailCheck(res4.value)){
              kara.action.button({
                action:[
                  {
                    text: "Booking Token",
                    value: 0,
                  },
                  {
                    text: "Back to main menu",
                    value: 1,
                  }
                ]
              }).then(res6=>{
                if(res6.value==0){
                  send_mail(name,email)
                }
              })
             
            }
            else {
              kara.message.add({
                delay:2000,
                loading:true,
                content:"Please enter a valid email id."
              }).then(_=>{
                ask_email(name)
              })
            }
          })
      }


      const ask_booking = (name) => {
        kara.message.add({
          delay:2000,
          loading: true,
          content: `${name} please enter your mail id...`
        }).then(_=>{
          ask_email(name)
        })
      }

      const ask_option = (name) => {
        kara.message.add({
              delay:2000,
              loading:true,
              content:`Hey ${name} we have an awesome 10% off couponfor a limited time. Would you like to have it ?`
        }).then(_=>
            kara.action.button({
              action:[
                {
                  text:'Yes',
                  value:true
                },
                {
                  text:'No',
                  value:false
                }
              ]
            }).then(res3=>{
              if(res3.value){
                  ask_booking(name)
                }
                else ask_all_options(name)
            })
          )
      }

      const ask_name = () =>{
        kara.action.text({
          action:[
          {
            placeholder:"Your Name"
          }]
        }).then(res=>{
          name = res.value
          if(fullNameCheck(res.value)){
            kara.message.add({
              delay:1500,
              loading:true,
              content:`Nice to meet you ${res.value}  😄!`
            }).then(_=>{
              kara.message.add({
                delay:2000,
                loading:true,
                content:` ${res.value} there is a surprise !!!!!!`
              }).then(_=>{
                ask_option(name)
              })
            })
          }
          else {
            kara.message.add({
              delay:2000,
              loading:true,
              content:"We encourage you to write your full name, like Albert Einstein. But it's ok if you don't want to mention it."
            }).then(_=>{
                kara.message.add({
              delay:3000,
              loading:true,
              content:`Are you sure you want to apply with this name, ${res.value}?`
            }).then(_=>{
                kara.action.button({
                action:[
                  {
                    text:'Yes',
                    value:true
                  },
                  {
                    text:'No',
                    value:false
                  }
                ]
              }).then(res2=>{
                if(res2.value){
                  kara.message.add({
                    delay:1500,
                    loading:true,
                    content:`Nice to meet you ${name}!`
                  }).then(_=>{
                    kara.message.add({
                      delay:2000,
                      loading:true,
                      content:`Hey ${name} there is a surprise`
                    }).then(_=>{
                      ask_option(name)
                    })
                  }) 
                }
                else {
                  kara.message.add({
                    delay:1500,
                    loading:true,
                    content:"We encourage you to write your full name, like Albert Einstein. But it's ok if you don't want to mention it."
                  }).then(_=>{
                    ask_name()
                  })  
                }
              })
            })
            })
            
          }
        })
      }

      const go_on = () =>{
        kara.message.add({
          delay:1500,
          loading:true,
          content:"Great then, let's get started!"
        }).then(_=>{
          kara.message.add({
            delay:2000,
            loading:true,
            content:"I will provide you with complete details but before that........"
          }).then(_=>{
            kara.message.add({
              delay:3000,
              loading:true,
              content:"First up, what's your full name?"
            }).then(_=>{
              ask_name()
            })
          })
        })
      }
      const exit = () =>{
        kara.message.add({
          delay:1000,
          loading:true,
          content:"It's ok. You can chat with me anytime. I'm always here to help you. 🙂"
        })
      }
      const greet = () => {
        kara.message.add({
        delay:3000,
        loading:true,
        content:"Hi there! I'm star waiter from Zaffran!"
        }).then(_=>{
        kara.message.add({
          type:'html',
          content: `
              <img src = 'https://s1.zerochan.net/Kara.%28Detroit%3A.Become.Human%29.600.2334931.jpg' width="224" height="224">
            `
        }).then(_=>{
          kara.message.add({
            delay:3000,
            loading:true,
            content:"Are you ready for this delicious tour 😋 ?"
          }).then(_=>{
            kara.action.button({
              action:[
                {
                  text:'Yes',
                  value:true
                },
                {
                  text:'No',
                  value:false
                }
              ]
            }).then(res=>{
                if(res.value){
                  go_on()
                }
                else exit()
            })
          })
        })
      })
      }
      greet();
    </script>
  </body>
</html>
