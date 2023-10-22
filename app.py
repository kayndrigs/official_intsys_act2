# python web framework
import streamlit as st

# for scatterplot
import plotly.express as px

# pandas for csv file
import pandas as pd

# for avoiding sudden error 
import warnings
import base64

# to check the validity of the email entered
from email_validator import validate_email


import plotly.figure_factory as ff
from streamlit_option_menu import option_menu
import streamlit.components.v1 as com

# to simulate NLP for design
from annotated_text import annotated_text

# to prevent sudden shutdown of website
warnings.filterwarnings('ignore')
# to process and upload image for the website
import base64


# Adds Favicon of PLM Logo
from PIL import Image
img = Image.open('plm.ico')

# Page icons
st.set_page_config(page_title="PLM Dashboard", page_icon=img)


def main():
    
    # background of the website
    set_png_as_page_bg('background.png')

    selected = option_menu(
        menu_title=None,
        options=["Home","Project"],
        icons = ["house","book"],
        default_index=0,
        orientation="horizontal",
    )
    
    
    
    if selected == "Home":
        st.markdown('<div style="text-align: center;"><h1>Welcome to Our Project!</h1></div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: center;"><h4>A Simple Classification Model Project</h4><br></div>', unsafe_allow_html=True)
        com.iframe("https://lottie.host/?file=08b9a80a-7842-4c6c-9c37-db6b88c3cf2b/vKdx1qmMCH.json")
        st.markdown('<div><br><br></div>',unsafe_allow_html=True)
        st.divider()
        annotated_text(
            ("Good day!","Greetings"),
            " We are a group from   ",
            ("BSCS 3-1","Block in PLM"),
            "    presenting a ",
            ("Machine Learning","Data Science"),
            "Project, which utilizes a",
            ("Simple Classfication Model","Machine Learning"),
            "  for  ",
            ("Personally Identifiable Information (PII)","Data Class"), 
            " Sorter. It aims to classify each data point from a ",
            ("CSV Dataset","Data File"),
            "whether if it is from the category if PII, which involves a",
            ("name","PII"), 
            ("email address","PII"), 
            ("mobile number","PII"), 
            " and ",
            ("date of birth","PII"),
            " It may require users to prepare their existing",
            ("excel workbooks",'Excel File'),
            "    to be converted into ",
            ("CSV (Comma Separated Files)","Database"),
            "  or generate a new csv database instead.","."
        )
        st.divider()
        st.image('members.png')
        
        
    if selected == "Project":
        # Page Title
        st.title("Classification Model - Personal Identifiable Information Sorter")
        with open("plm_logo2.png", "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
            
            st.sidebar.markdown(
                f"""
                    <div style="display:table;margin-top:-15%;margin-left:0%;">
                        <img src="data:image/png;base64,{data}" width="425" height="100">
                    </div>
                """,
                unsafe_allow_html=True,
            )
        
        
        st.sidebar.header("Choose Data Source: ")
        
        menu = ["Existing CSV File","New CSV File"]
        choice = st.sidebar.selectbox("Menu",menu,label_visibility="hidden")
        
        if choice == "New CSV File":
            import csv
            with st.form(key='csv_form'):  
                st.subheader(":file_folder: Generate New CSV File")
                headerList = ['random_values'] 
                new_csv =  st.form_submit_button(label="Create Empty CSV")
                
                if new_csv:
                    with open("empty.csv", 'w') as file: 
                        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList) 
                        dw.writeheader() 
            fl = None
            
        elif choice == "Existing CSV File":
            fl = st.file_uploader(":file_folder: Upload a File",type=(["csv"]))
            empty_df = None
        
        try:
            empty_df = pd.read_csv("empty.csv",encoding="ISO-8859-1")
        except:
            empty_df = None
          
        # Will read the csv or similar dataset file
        if fl is not None:
            import csv
            filename = fl.name
            st.write(filename)
                                            
            with open(filename,'r',newline="") as file:
                reader= csv.reader(file)
                data_list = []
                for row in reader:
                    for value in row:
                        data_list.append(value)
                
            df = pd.DataFrame(data_list,columns=["random_values"])        
            with st.expander("Current Random Data Values"):
                st.dataframe(df.T)
                        
                
            st.subheader("Additional Input")
            st.caption("If dataset is empty, press submit button first before adding new datapoint.")
            with st.form(key='form1'):
                text = st.text_input("Enter Valid Name/ Email/ Phone Number/ Birth date (Note: this cannot be reversed)")
                submit_button = st.form_submit_button(label='Submit')
            
                if submit_button:
                    # fetching data from local directory
                    new_data = {"random_values":str(text)}
                    dataset_df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                    dataset_df.to_csv(filename, index=False)
                    st.dataframe(df.T)
                    
        elif empty_df is not None:
            df = pd.read_csv("empty.csv", encoding="ISO-8859-1")
            with st.expander("Current Random Data Values"):
                st.dataframe(df.T)
                
            st.subheader("Additional Input")
            st.caption("If dataset is empty, press submit button first before adding new datapoint.")
            with st.form(key='form1'):
                with st.expander("Updated Random Data Values"):
                    st.dataframe(df.T)
                text = st.text_input("Enter Valid Name/ Email/ Phone Number/ Birth date (Note this cannot be reversed)")
                submit_button = st.form_submit_button(label='Submit')
                
                if submit_button:
                    # fetching data from local directory
                    new_data = {"random_values":str(text)}
                    dataset_df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                    dataset_df.to_csv("empty.csv", index=False)
        else:
            # change the directory is none
            df = pd.read_csv("random_dataset4.csv", encoding="ISO-8859-1")
            with st.expander("Current Random Data Values"):
                st.dataframe(df.T)
                
            st.subheader("Additional Input")
            st.caption("If dataset is empty, press submit button first before adding new datapoint.")
            with st.form(key='form1'):
                with st.expander("Updated Random Data Values"):
                    st.dataframe(df.T)
                text = st.text_input("Enter Valid Name/ Email/ Phone Number/ Birth date (Note this cannot be reversed)")
                submit_button = st.form_submit_button(label='Submit')
                
                if submit_button:
                    # fetching data from local directory
                    new_data = {"random_values":str(text)}
                    dataset_df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                    dataset_df.to_csv("random_dataset4.csv", index=False)
                
        # Process
        phone_df = pd.read_excel('phonePrefix2.xlsx')
        dataset = []
        phonePrefix = []
        
        if any(df):
            for i in df.values:
                dataset.extend(i)
        else:
            dataset.extend("None")

        str_list = [str(j) for j in phone_df['phone_prefix']]
        phonePrefix = str_list
        
        #eliminates duplicates
        unique_dataset = list(dict.fromkeys(dataset))
        random_df = pd.DataFrame(unique_dataset)
        try:
            random_df.columns = ['temp_data']
        except:
            pass

        st.subheader("Sorted Dataset Result")  

        
        # block of code that will process the csv file
        with st.expander('Results'):

            sorted_data = classification(unique_dataset,phonePrefix)
            st.scatter_chart(sorted_data,width=250,height=400)
            fig = ff.create_table(sorted_data)

            st.plotly_chart(fig, use_container_width= True)
            
            csv = sorted_data.to_csv(index = False).encode('utf-8')
            st.download_button("Download Data",data=csv, file_name = "sorted_.csv", mime="text/csv",
                            help = 'Click here to download the data as a CSV file')
        
        
# renders background image        
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

     

def classification(dataset,phonePrefix):
 # initialize values
    name = []
    cellphoneNumber = []
    dateBirth = []
    emailAddress = []
    invalid_info = []
    
    #token for checking email strings
    emailChars = ['@','.']
    
    # processes the dataset
    for i in dataset:
        
        # initially scans for @ and . characters
        checkEmail = [char for char in emailChars if(char in i)]
        
        # checks validity of phone number based on philippine prefix system
        checkMobileNum = [char for char in phonePrefix if(char in i[0:5])]
        
        # re
        name_string = i.replace(" ","")
        
        # we can't accurately predict if a name is a valid name, therefore, we implement all alphabets as a name
        if name_string.isalpha():
            capitalize_name = i.title()
            name.append(capitalize_name)
        
        # validate and append email
        elif checkEmail:
            try:
                v = validate_email(i)
                if v:
                    emailAddress.append(i)
            except:
                invalid_info.append(i)
                
        # validate and append date
        elif '/' in i:
            check_date = i.split('/')
            if len(check_date[0]) >= 1 and len(check_date[0]) < 3  and len(check_date[1]) >= 1 and len(check_date[1]) < 3 and len(check_date[2]) == 4:
                dateBirth.append(i)
            else: 
                invalid_info.append(i)
            
        # validate and append date
        elif checkMobileNum:
            cellphoneNumber.append(i)
            
        else:
            invalid_info.append(i)
        

    data = {'name':name,'cellphone_no.':cellphoneNumber,'date_of_birth':dateBirth,'email_address':emailAddress, 'invalid_inputs':invalid_info}
    result = pd.DataFrame.from_dict(data,orient='index')
    result = result.transpose()
    return result

if __name__ == '__main__':
    main()
