# Basic tkinter template
from tkinter import *
root=TK()

root.title ("Addition")
root.geometry("400x300")

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

# Create all the labels required to be displayed
label_id=lable(root)
label_name=lable(root)
label_dob=lable(root)
label_pin=lable(root)
label_address=lable(root)
label_vehicle_type=lable(root)


# Define the function

def add():
    result=
    label_id["ID :19827198349"]=result
    label_name["Name :Wnnie the pooh"]=result
    label_dob["Date of birth :21 August 1921"]=result
    label_pin["Pin no :451478"]=result
    label_address["Address :Disney land,Hong kong"]=result
    label_vehicle_type["Authorisation to drive the following vehicles"]=result  
# Create a button
btn =(Button root, text="Driving License" command=Driving License)
btn.pack()

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()

# tkinter basic template end statement

label_id.pack()
label_name.pack()
label_dob.pack()
label_pin.pack()
label_address.pack()
label_vehicle_type.pack()

root.mainloop()

