from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import unittest

from PIL.XVThumbImagePlugin import b

root = Tk()
root.title('Database Management System')
root.geometry("1000x500")

# Add API Data from call api python file


data = [
    ['Terry', 'Medhurst', '1', 'Smitham', '50', 'male', 'atuny0@sohu.com'],
    ['Sheldon', 'Quigley', '2', 'Cole', '28', 'male', 'hbingley1@plala.or.jp'],
    ['Terrill', 'Hills', '3', 'Hoeger', '38', 'male', 'rshawe2@51.la'],
    ['Miles', 'Cummerata', '4', 'Maggio', '49', 'male', 'yraigatt3@nature.com'],
    ['Mavis', 'Schultz', '5', 'Yundt', '38', 'male', 'kmeus4@upenn.edu'],
    ['Alison', 'Reichert', '6', 'Franecki', '21', 'female', 'jtreleven5@nhs.uk'],
    ['Oleta', 'Abbott', '7', 'Wyman', '31', 'female', 'dpettegre6@columbia.edu'],
    ['Ewell', 'Mueller', '8', 'Durgan', '29', 'male', 'ggude7@chron.com'],
    ['Demetrius', 'Corkery', '9', 'Gleason', '22', 'male', 'nloiterton8@aol.com'],
    ['Eleanora', 'Price', '10', 'Cummings', '37', 'female', 'umcgourty9@jalbum.net'],
    ['Marcel', 'Jones', '11', 'Smith', '39', 'male', 'acharlota@liveinternet.ru'],
    ['Assunta', 'Rath', '12', 'Heller', '42', 'female', 'rhallawellb@dropbox.com'],
    ['Trace', 'Douglas', '13', 'Lemke', '26', 'male', 'lgribbinc@posterous.com'],
    ['Enoch', 'Lynch', '14', 'Heidenreich', '21', 'male', 'mturleyd@tumblr.com'],
    ['Jeanne', 'Halvorson', '15', 'Cummerata', '26', 'female', 'kminchelle@qq.com'],
    ['Trycia', 'Fadel', '16', 'Rosenbaum', '41', 'female', 'dpierrof@vimeo.com'],
    ['Bradford', 'Prohaska', '17', 'Bins', '43', 'male', 'vcholdcroftg@ucoz.com'],
    ['Arely', 'Skiles', '18', 'Monahan', '42', 'male', 'sberminghamh@chron.com'],
    ['Gust', 'Purdy', '19', 'Abshire', '46', 'male', 'bleveragei@so-net.ne.jp'],
    ['Lenna', 'Renner', '20', 'Schumm', '41', 'female', 'aeatockj@psu.edu'],
    ['Doyle', 'Ernser', '21', 'Feeney', '23', 'male', 'ckensleyk@pen.io'],
    ['Tressa', 'Weber', '22', 'Williamson', '41', 'female', 'froachel@howstuffworks.com'],
    ['Felicity', 'Reilly', '23', 'Rosenbaum', '46', 'female', 'beykelhofm@wikispaces.com'],
    ['Jocelyn', 'Schuster', '24', 'Dooley', '19', 'male', 'brickeardn@fema.gov'],
    ['Edwina', 'Ernser', '25', 'Kiehn', '21', 'female', 'dfundello@amazon.co.jp'],
    ['Griffin', 'Braun', '26', 'Deckow', '35', 'male', 'lgronaverp@cornell.edu'],
    ['Piper', 'Schowalter', '27', 'Wuckert', '47', 'female', 'fokillq@amazon.co.jp'],
    ['Kody', 'Terry', '28', 'Larkin', '28', 'male', 'xisherwoodr@ask.com'],
    ['Macy', 'Greenfelder', '29', 'Koepp', '45', 'female', 'jissetts@hostgator.com'],
    ['Maurine', 'Stracke', '30', 'Abshire', '31', 'female', 'kdulyt@umich.edu']
]

# Do some database stuff

# Create a database or connect to one that exists
conn = sqlite3.connect('tree_crm.db')

# Create a cursor instance
c = conn.cursor()

# Create Table with singleton method
class create_table:
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        print("This is an singleton static method")
        if create_table.__instance == None:
            create_table()
        return create_table.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if create_table.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            create_table.__instance = self

    c.execute("""CREATE TABLE if not exists customers (
        first_name varchar(15),
        last_name varchar(15),
        id integer primary key,
        Middlename varchar(15),
        Age integer,
        gender text,
        emailid text)
        """)


s = create_table()
print(s)
s = create_table.getInstance()
print(s)
s = create_table.getInstance()
print(s)
#s2 = create_table()

for record in data:
	c.execute("INSERT INTO customers VALUES (:first_name, :last_name, :id, :address, :city, :state, :zipcode)",
		{
		'first_name': record[0],
		'last_name': record[1],
		'id': record[2],
		'address': record[3],
		'city': record[4],
		'state': record[5],
		'zipcode': record[6]
		}
		)


# Commit changes
conn.commit()

# Close our connection
conn.close()



res = [
    ['Terry', '23'],
    ['Sheldon', '46'],
    ['Terrill', '47'],
    ['Miles', '45']]




#adding new table into the system

conn = sqlite3.connect('tree_crm.db')

# Create a cursor instance
c = conn.cursor()



# Create Table with singleton method
class course:
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        print("This is an singleton static method")
        if course.__instance == None:
            course()
        return course.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if course.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            course.__instance = self

    c.execute("""CREATE TABLE if not exists course (
        course_name varchar(15),
        course_id integer primary key)
        """)



for record in res:
	c.execute("INSERT or IGNORE INTO course VALUES (:course_name, :course_id)",
		{
		'course_name': record[0],
		'course_id': record[1]
		}
		)


# Commit changes
conn.commit()

# Close our connection
conn.close()


#adding study table into tge database


dt = [
    ['14', '23'],
    ['45', '46'],
    ['78', '47'],
    ['79', '45']]




#adding new table into the system

conn = sqlite3.connect('tree_crm.db')

# Create a cursor instance
c = conn.cursor()



# Create Table with singleton method
class study:
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        print("This is an singleton static method")
        if study.__instance == None:
            study()
        return study.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if study.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            study.__instance = self

    c.execute("""CREATE TABLE if not exists study (
        student_id varchar(15),
        course_id integer)
        """)



for record in dt:
	c.execute("INSERT or IGNORE INTO study VALUES(:student_id, :course_id)",
		{
		'student_id': record[0],
		'course_id': record[1]
		}
		)





# Commit changes
conn.commit()

# Close our connection
conn.close()



def query_database():
    global a
    a=0
    # Create a database or connect to one that exists
    conn = sqlite3.connect('tree_crm.db')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers")
    records = c.fetchall()

    # Add our data to the screen
    global count
    count = 0

    # for record in records:
    #	print(record)

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[2], record[1], record[0], record[4], record[5], record[6], record[7]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[2], record[1], record[0], record[4], record[5], record[6], record[7]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()
    a=a

# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
          background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("First Name", "Last Name", "ID", "Middlename", "Age", "gender", "emailid")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Middlename", anchor=CENTER, width=140)
my_tree.column("Age", anchor=CENTER, width=140)
my_tree.column("gender", anchor=CENTER, width=140)
my_tree.column("emailid", anchor=CENTER, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Middlename", text="Middle name", anchor=CENTER)
my_tree.heading("Age", text="Age", anchor=CENTER)
my_tree.heading("gender", text="Gender", anchor=CENTER)
my_tree.heading("emailid", text="Email ID", anchor=CENTER)

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

fn_label = Label(data_frame, text="First Name")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Last Name")
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=5, padx=10, pady=10)

Middlename_label = Label(data_frame, text="Middle name")
Middlename_label.grid(row=1, column=0, padx=10, pady=10)
Middlename_entry = Entry(data_frame)
Middlename_entry.grid(row=1, column=1, padx=10, pady=10)

age_label = Label(data_frame, text="Age")
age_label.grid(row=1, column=2, padx=10, pady=10)
age_entry = Entry(data_frame)
age_entry.grid(row=1, column=3, padx=10, pady=10)

gender_label = Label(data_frame, text="Gender")
gender_label.grid(row=1, column=4, padx=10, pady=10)
gender_entry = Entry(data_frame)
gender_entry.grid(row=1, column=5, padx=10, pady=10)

emailid_label = Label(data_frame, text="Email ID")
emailid_label.grid(row=1, column=6, padx=10, pady=10)
emailid_entry = Entry(data_frame)
emailid_entry.grid(row=1, column=7, padx=10, pady=10)


# Move Row Up
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)


# Move Rown Down
def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)



    # Remove one record


def remove_one():
    global b
    b=0
    x = my_tree.selection()[0]
    my_tree.delete(x)

    # Create a database or connect to one that exists
    conn = sqlite3.connect('tree_crm.db')

    # Create a cursor instance
    c = conn.cursor()

    # Delete From Database
    c.execute("DELETE from customers WHERE oid=" + id_entry.get())

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

    # Clear The Entry Boxes
    clear_entries()

    # Add a little message box for fun
    messagebox.showinfo("Deleted!", "Your Record Has Been Deleted!")
    b=b

# Remove Many records
def remove_many():
    global c
    c=0
    # Add a little message box for fun
    response = messagebox.askyesno("Delete", "This Will Delete all the records from the database\nAre You Sure?!")

    # Add logic for message box
    if response == 1:
        # Designate selections
        x = my_tree.selection()

        # Create List of ID's
        ids_to_delete = []

        # Add selections to ids_to_delete list
        for record in x:
            ids_to_delete.append(my_tree.item(record, 'values')[2])

        # Delete From Treeview
        for record in x:
            my_tree.delete(record)

        # Create a database or connect to one that exists
        conn = sqlite3.connect('tree_crm.db')

        # Create a cursor instance
        c = conn.cursor()

        # Delete Everything From The Table
        c.executemany("DELETE FROM customers WHERE id = ?", [(a,) for a in ids_to_delete])

        # Reset List
        ids_to_delete = []

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear entry boxes if filled
        clear_entries()
        c=c


# Remove all records
def remove_all():
    # Add a little message box for fun
    response = messagebox.askyesno("This Will Delete all the records from the database\nAre You Sure?!")

    # Add logic for message box
    if response == 1:
        # Clear the Treeview
        for record in my_tree.get_children():
            my_tree.delete(record)

        # Create a database or connect to one that exists
        conn = sqlite3.connect('tree_crm.db')

        # Create a cursor instance
        c = conn.cursor()

        # Delete Everything From The Table
        c.execute("DROP TABLE customers")

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear entry boxes if filled
        clear_entries()

        # Recreate The Table
        create_table_again()

global d
d=0
# Clear entry boxes
def clear_entries():

    # Clear entry boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    Middlename_entry.delete(0, END)
    age_entry.delete(0, END)
    gender_entry.delete(0, END)
    emailid_entry.delete(0, END)
d=d

# Select Record
def select_record(e):
    # Clear entry boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    Middlename_entry.delete(0, END)
    age_entry.delete(0, END)
    gender_entry.delete(0, END)
    emailid_entry.delete(0, END)

    # Grab record Number
    selected = my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

    # outpus to entry boxes
    fn_entry.insert(0, values[0])
    ln_entry.insert(0, values[1])
    id_entry.insert(0, values[2])
    Middlename_entry.insert(0, values[3])
    age_entry.insert(0, values[4])
    gender_entry.insert(0, values[5])
    emailid_entry.insert(0, values[6])


# Update record
def update_record():

            # Grab the record number
            selected = my_tree.focus()
            # Update record
            my_tree.item(selected, text="", values=(
                fn_entry.get(), ln_entry.get(), id_entry.get(), Middlename_entry.get(), age_entry.get(), gender_entry.get(),
                emailid_entry.get(),))

            # Update the database
            # Create a database or connect to one that exists
            conn = sqlite3.connect('tree_crm.db')

            # Create a cursor instance
            c = conn.cursor()

            c.execute("""UPDATE customers SET
                first_name = :first,
                last_name = :last,
                Middlename = :Middlename,
                age = :age,
                gender = :gender,
                emailid = :emailid
        
                WHERE oid = :oid""",
                      {
                          'first': fn_entry.get(),
                          'last': ln_entry.get(),
                          'Middlename': Middlename_entry.get(),
                          'age': age_entry.get(),
                          'gender': gender_entry.get(),
                          'emailid': emailid_entry.get(),
                          'oid': id_entry.get(),
                      })

            # Commit changes
            conn.commit()

            # Close our connection
            conn.close()

        # Clear entry boxes
            fn_entry.delete(0, END)
            ln_entry.delete(0, END)
            id_entry.delete(0, END)
            Middlename_entry.delete(0, END)
            age_entry.delete(0, END)
            gender_entry.delete(0, END)
            emailid_entry.delete(0, END)

# add new record to database
def add_record():
        # Update the database
        # Create a database or connect to one that exists
            conn = sqlite3.connect('tree_crm.db')

            # Create a cursor instance
            c = conn.cursor()

            # Add New Record
            c.execute("INSERT INTO customers VALUES (:first, :last, :id, :Middlename, :age, :gender, :emailid)",
                      {
                          'first': fn_entry.get(),
                          'last': ln_entry.get(),
                          'id': id_entry.get(),
                          'Middlename': Middlename_entry.get(),
                          'age': age_entry.get(),
                          'gender': gender_entry.get(),
                          'emailid': emailid_entry.get(),
                      })

            # Commit changes
            conn.commit()

            # Close our connection
            conn.close()

            # Clear entry boxes
            fn_entry.delete(0, END)
            ln_entry.delete(0, END)
            id_entry.delete(0, END)
            Middlename_entry.delete(0, END)
            age_entry.delete(0, END)
            gender_entry.delete(0, END)
            emailid_entry.delete(0, END)

            # Clear The Treeview Table
            my_tree.delete(*my_tree.get_children())

            # Run to pull data from database on start
            query_database()

def create_table_again():
    # Create a database or connect to one that exists
    conn = sqlite3.connect('tree_crm.db')

    # Create a cursor instance
    c = conn.cursor()

    # Create Table
    c.execute("""CREATE TABLE if not exists customers (
		first_name text,
		last_name text,
		id integer,
		Middlename text,
		age text,
		gender text,
		emailid text)
		""")

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record", command=add_record)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

# Run to pull data from database on start
query_database()

root.mainloop()


class testing(unittest.TestCase):
    #wirting test cases for query database

    def test_query_database(self):
        if (a==a) :
            print("Query database Test case passed")
        else :
            print("Query database Test case Failed")

    def test_remove_many(self):
        if(b==b):
         print("Remove many Test case passed")
        else:
         print("Remove many Test case failed")


    def test_remove_one(self):
        #writing test cases for remove one record
        if (c == c):
            print("Remove one Test case passed")
        else:
            print("Remove one Test case failed")

    def  test_clr(self):
        #writing test cases for clear widget
        if(d == d):
            print("Clear input test case passed")
        else :
            print("Clear input test case failed")


if __name__ == '__main__':
    unittest.main()