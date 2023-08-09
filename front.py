from flask import Flask, render_template, request
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
app = Flask(__name__,template_folder='template')

# Route for displaying the form page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling form submission
@app.route('/submit', methods=['POST'])

def submit_form():
    my_options=webdriver.ChromeOptions()
    service = Service(executable_path='C:/Users/syed abdul qayyum/Desktop/message/chromedriver.exe')
    
    browser=webdriver.Chrome(service=service,options=my_options)
    
   # file_path='C:/Users/syed abdul qayyum/Desktop/message/hello.txt'
    df=pd.read_excel('phone.xlsx')
    input1 = request.form['input1']
    input2 = request.form['input2']
    print(input2)
    for ind in df.index:
        contact=df['Phone'][ind]
        name=df['Name'][ind]
        browser.get(f"https://web.whatsapp.com/send?phone={contact}")
        time.sleep(5)
   

        while True:
            try:
       
              box_message=browser.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span')
              box_message.click()
              time.sleep(2)
              break
            
            except:
               pass

     
        image_box=browser.find_element("xpath","//input[@accept='*']")
        image_box.send_keys(input2)
        time.sleep(20)
        image_box=browser.find_element("xpath","//span[@data-testid='send']")
        image_box.click()
        time.sleep(10)
        box_message=browser.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        box_message.send_keys("ASSALAM-O-ALAIKUM   ",name, "    ",input1)  
        time.sleep(10)
        box_message=browser.find_element("xpath",'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
        box_message.click()
        time.sleep(10)   

    browser.close()
    # Process the inputs here (add your desired functionality)
    

    return "Message sent successfully"
if __name__ == '__main__':
    app.run(debug=True)