# Import the Python SDK
import google.generativeai as genai
# Used to securely store your API key
#from google.colab import userdata

GOOGLE_API_KEY='AIzaSyDX6DZKq-_lKRBrWsOdHWCevnZEZ_8LRLE'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
y=0
while(y==0):
     x=str(input("entr the promt "))
     if(x=='exit'):
          y=1
     response = model.generate_content(x)
     print(response.text)


#api link : https://aistudio.google.com/app/apikey