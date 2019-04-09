#Andrea Fairfield
#Final Project NR 426
#3/14/2019

#RUN WITH PROJECT INTERPRETER PYTHON 3.6 FOR ARCPY
#########BRINGING IN DATA FROM HABITAT HEROES DATABASE SO THAT THE POINTS CAN BE REFERENCED IN ArcGIS Pro###########
try: #try statement to help with error handling
        #importing arcpy
        import arcpy
        print("Modules imported")
        print()

        #setting the workspace
        arcpy.env.workspace = input("Input pathname for your workspace:")#r"E:\Spring2019\NR426\Final_Project"
        print("Workspace has been set")
        print()

        #setting variable(s)
        #Overwrite output
        arcpy.env.overwriteOutput = True

        #STEP 1: Opening a file
        print ("###### STEP 1: Opening a file ######")
        myFile = open(input("Enter the HabitatHeroDatabase provided:"),"r+") #"HabitatHeroDatabase_NR426CSV1.csv"
        print("File has been opened")
        print()

        #STEP 2: Creation of a table to be able to use for the insert cursor
        print("###### STEP 2: Creation of a table for use in insert cursor ######")
        out_name = input("Enter the name you want the created table to be called (must be a dbf):")#"GISHabitatTable.dbf"
        template_table = input("Enter the Template Table's ENTIRE Pathname:")#r"E:\Spring2019\NR426\Final_Project\HabitatHeroDatabase_NR426CSV1.csv"
        arcpy.CreateTable_management(arcpy.env.workspace,out_name,template_table) #creating a table with a template table
        print ("Table has been created")
        print()
        print()
        print("I SEE THE LIGHT AT THE END OF THE TUNNEL")
        print()
        print()
        #STEP 3: Listing fields that are created in the table
        print("###### STEP 3: Listing Fields")
        fields = arcpy.ListFields(out_name)
        for field in fields:
                print ("{0} is a type of {1} with a length of {2}".format(field.name, field.type, field.length))#printing out the field name, field type, and field length
        print()

        #STEP 4: Making sure it actually read in the correct data
        print ("###### STEP 4: Data name and Mode ######")
        print ("Name: " + myFile.name) #checking the name of the file
        print ("Mode: " + myFile.mode)#checking the mode of the file that's being edited
        print()

        #STEP 5: Reading in each line and creating a loop
        print ("###### STEP 5: Reading each line ######")

        lines = myFile.readlines() #reading the lines in my file and putting them into a variable called lines
        print ("Lines variable has been set up")
        with arcpy.da.InsertCursor(out_name,("Name", "Email","Address", "City", "State")) as cur: #setting up a cursor
                print ("Cursor is being setup")
                for row in lines:
                        vals = row.split(",") #splitting the rows by commas with a variable called vals
                        Name = str(vals[0]) #setting the variable name to equal column zero in the table
                        Email = str(vals[1]) #setting the variable Email to equal column 1 in the table
                        Address = str(vals[2]) #setting the variable address to equal column 2 in the table
                        City= str(vals[3]) #setting the variable city to equal column 3 in the table
                        State = str(vals[4]) #setting the variable state to equal column 4 in the table
                        print()
                        rowValue = [Name,Email,Address,City,State] #Creating a variable to put these all together in one line
                        print(rowValue)
                        cur.insertRow(rowValue)

                print ()
                print("Insert Row was completed")

        myFile.close()
        print("File has been closed")
        print()
        print("I AM ON THE BEACH!!!!!!")

except Exception:
        e = sys.exc_info()[1]
        print(e.args[0])











