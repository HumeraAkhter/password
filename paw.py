import re
import streamlit as st

# page styling
st.set_page_config(page_title="PASSWORD STRENGTH CHECKER BY HUMERA YAHYA" , page_icon ="㊪" , layout="centered")
#custom css
st.markdown("""
<style>
    .main { text-align :center; }
    .stTextInput { width: 60% !important; margin: auto; }
    .stButton button { width: 50%; background-color: blue;  color: white; font-size:18px; }
    .stButton button:hover { background-color: red; color: white; }
</style>      
""", unsafe_allow_html=True)      


# page title and description      

st.title(" ⌨Password Strength Generator")
st.write("Enter Your Password below to check its security level.✍️")

# funcyion to check your pasword strength
def Check_Password_strength(password):
    score = 0
    feedback = []
    if len (password)  >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("❌ Password should be **at least 8 charactor long**.") 

    if re.search(r"[A-Z]",password) and re.search(r"[a-z]", password):
        score += 1
    else :
        feedback.append("❌ Password should include **both uper case (A-Z) and lower case (a-z)letters**.") 
    if re.search(r"/d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.") 
    #speacial characters
    if re.search(r"[!@#$%^&*]", password) :
        score += 1
    else:
        feedback.append("❌Include ** at least one special character[!@#$%^&*]**.") 
     #display password strength results
    if score == 4:
        st.success("✔️ ** Strong Password** - your password is secure.") 
    elif score == 3:
        st.info("⚠️   **Moderate Password** - consider improving security by adding more feature")
    else:
        st.error("❌ **Weak Password** -Follow the suggestion below to strength it." )
    #feedback
    if feedback:
        with st.expander("♀️** Improve your Password**"):
          for item in feedback:
              st.write(item)
password = st.text_input("Enter your Password:" , type="password",help="Ensure your password is strong 🔐") 
 #Button working
if st.button("check strength"): 
      if password:
        Check_Password_strength(password) 
      else:
        st.info("   **Moderate Password** - consider improving security by adding more feature")
        
        
        st.warning("⚠️ Please enter a password first !") # show warning if password empty                






  