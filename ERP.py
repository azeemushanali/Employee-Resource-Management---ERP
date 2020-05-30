while 1:
    try:
        import random 
        class Employee:
            login_id = "azeem"
            login_pwd = '123'
            listEmp = []
            flag = 0
            def __init__(self):
                self.id = 0
                self.age = 0
                self.name = 0
                self.type = 0
            def getName(self):
                while(1):
                    name = input("Enter the name of the Employee- ")
                    if name.isalpha():
                        return name
                    else:
                        print("Enter the name in alphabets only ")
            def getAge(self):
                while(1):
                    age = input("Enter the age of the Employee- ")
                    if age.isnumeric():
                        if(int(age) >= 10 and int(age) <=110):
                            return age
                        else:
                            print("Enter the age in range from 10 to 110 ")
                    else:
                        print("Enter the age in numbers only ")
            
            def genID(self):
                while(1):
                    id = random.randint(1,999)
                    generated_id = self.name[:3] + str(id) +str(self.age)
                    #print("ID is",generated_id)
                    #return generated_id
                    for e in Employee.listEmp:
                            if (e.id == generated_id):
                                break
                    else:
                        print("ID is",generated_id)
                        return generated_id
        #                   
        #        id = random.randint(1,999)
        #        generated_id = self.name[:3] + str(id) +str(self.age)
        #        print("ID is",generated_id)
        #        return generated_id
        #            for e in Employee.listEmp:
        #                if (e.id == generated_id):
        #                    Employee.genID(self)
        #                else:
        #                    print("ID is",generated_id)
        #                    return generated_id
        #                    break
                            
            def addEmp(self):
                Employee.listEmp.append(self)
                
            def searchID(id= None, age = None, name = None):
                if name == None and age == None :
                    for e in Employee.listEmp:
                        if e.id == id:    
                            return e
                    else:
                        print(f"Employee with ID {id} not found in our Database")
                        return -1
                elif id  == None and age == None :
                    for e in Employee.listEmp:
                        if e.name == name:    
                            return e
                    else:
                        print(f"Employee with Name {name} not found in our Database")
                        return -1
                elif id  == None and name == None :
                    for e in Employee.listEmp:
                        if e.age == age:   
                            return e
                    else:
                        print(f"Employee with Age {age} not found in our Database")
                        return -1
                
                    #not found me kya condition lagegi
                    
            def searchAttribute(share = None, area = None , course = None):
                if share != None:
                    for e in Employee.listEmp:
                        if(e.type ==  "Director"):
                            if e.share == myshare:
                                return e
                    else:
                        print(f"Director with Share {share}% not found in our Database")
                        return -1
                elif area != None:
                    for e in Employee.listEmp:
                        if e.type == "Manager":
                            if e.area == myarea:
                                return e
                    else:
                        print(f"Manage with Area {area} not found in our Database")
                        return -1
                elif course != None:
                    for e in Employee.listEmp:
                        if e.type == "Trainer":
                            if e.course == mycourse:
                                return e
                    else:
                        print(f"Trainer with Course {course} not found in our Database")
                        return -1
               
            def del_ID(e):
                Employee.listEmp.remove(e)
                print("Employee deleted Successfully")
                        
                        
                        
                        
                        
                        
        class Director(Employee):
            def __init__(self):
                self.share = 0
            def getShare(self):
                self.share  = input("Enter the share of the Director- ")
        class Manager(Employee):
            def __init__(self):
                self.area = 0
            def getArea(self):
                self.area  = input("Enter the Area of the Manager ")
                    
        class Trainer(Employee):
            def __init__(self):
                self.course = 0
            def getCourse(self):
                self.course  = input("Enter the Course of the Trainer ")
                
                
                
                
                
        #PL v-0
        def showData(e):
            if(e == -1):
                pass
            else:
                if e.type == "Director":
                    print("ID- ",e.id,"Name- ",e.name ," ","Age- ", e.age," ","Post- ",e.type ," ", "Share-", e.share)
                elif e.type == "Trainer":
                    print("ID- ",e.id,"Name- ",e.name ," ","Age- ", e.age," ","Post- ",e.type ," ", "Course-", e.course)
                elif e.type == "Manager":
                    print("ID- ",e.id,"Name- ",e.name ," ","Age- ", e.age," ","Post- ",e.type ," ", "Area-", e.area)
                
            
            
                
                
        #PL
        if __name__ == '__main__':
            print("Welcome to my CMS Project,Be ready with your id and password!")
            print("Feel free to exit by pressing Enter key in id or password section")
            quit_program = 0
            while(1):
                if(Employee.flag<=3):
                    cms_id = input("Enter your CMS Login ID  ")
                    cms_pwd = input("Enter your CMS Login Password  ")
                    if(cms_id == Employee.login_id and Employee.login_pwd == cms_pwd):
                        print("You made it!!")
                        while(1):
                            ch = input('''Operations you can do in my CMS-
                              1- Add Customer
                              2- Modify Customer
                              3- Search Customer
                              4- Delete Customer
                              5- Display All
                              6- Exit
                              Enter your choice-->
                              ''')
                            if(ch.isnumeric()):
                                if(ch == '1'): #ADD Employee
                                    while(1):
                                        cht = input('''Enter the type of Employee
                                        1- Director
                                        2- Manager
                                        3- Trainer
                                        ''')
                                        if cht.isnumeric():
                                            if cht == '1': #ADDing Dir
                                                dir = Director()
                                                dir.name = dir.getName()
                                                dir.age = dir.getAge() 
                                                dir.getShare()  #dir.share = dir.getshare() me none aaraha tha
                                                dir.id = dir.genID()
                                                dir.type = "Director"
                                                dir.addEmp()
                                                break
                                            if cht == '2': #Adding Manager
                                                mgr = Manager()
                                                mgr.name = mgr.getName()
                                                mgr.age = mgr.getAge() 
                                                mgr.getArea()
                                                mgr.id = mgr.genID()
                                                mgr.type = "Manager"
                                                mgr.addEmp()
                                                break
                                            if cht == '3': #Adding Trainer
                                                trn = Trainer()
                                                trn.name = trn.getName()
                                                trn.age = trn.getAge() 
                                                trn.getCourse()
                                                trn.id = trn.genID()
                                                trn.type = "Trainer"
                                                trn.addEmp()
                                                break
                                            else:
                                                print("Enter Correct type")
                                                
                                        else:
                                            print("Enter the choice in numbers only")
                                            
                                elif ch == '2' :#modify
                                    cht = input('''Enter the entity through which you want to modify Employee
                                    1- By Id
                                    2- By Name
                                    3- By Age
                                    4- By Share
                                    5- By Area
                                    6- By Course
                                    ''')
                                    if cht == '1': #by id
                                        id = input("Enter the ID of the Employee  ")
                                        e = Employee.searchID(id = id)
                                        
                                        if e == -1:
                                            pass
                                        else:
                                            cht1  = input(f'''Enter the entity you want to modify-
                                            1- ID
                                            2- Name
                                            3-Age
                                                     ''')
                                            if cht1 == '1':
                                                print("New ",end = "")
                                                e.id = Employee.genID(e)
                                            elif cht1 == '2':
                                                e.name = Employee.getName(e)
                                                print("Name modified Successfully")
                                            elif cht1 == '3' :
                                                e.age = Employee.getAge(e)
                                                print("Age Modified successfully")
                                            
                                            else:
                                                print("Wrong Choice")
                                    elif cht == '2': #by name
                                        name = input("Enter the Name of the Employee  ")
                                        e = Employee.searchID(name = name)
                                        
                                        if e == -1:
                                            pass
                                        else:
                                            cht1  = input(f'''Enter the entity you want to modify-
                                            1- ID
                                            2- Name
                                            3-Age
                                            ''')
                                            if cht1 == '1':
                                                print("New ",end = "")
                                                e.id = Employee.genID(e)
                                            elif cht1 == '2':
                                                e.name = Employee.getName(e)
                                                print("Name modified Successfully")
                                            elif cht1 == '3' :
                                                e.age = Employee.getAge(e)
                                                print("Age Modified successfully")
                                            
                                            else:
                                                print("Wrong Choice")
                                        
                                    elif cht == '3': #by age
                                        age = input("Enter the Age of the Employee  ")
                                        e = Employee.searchID(age = age)
                                        
                                        if e == -1:
                                            pass
                                        else:
                                            cht1  = input(f'''Enter the entity you want to modify-
                                            1- ID
                                            2- Name
                                            3-Age
                                            ''')
                                            if cht1 == '1':
                                                print("New ",end = "")
                                                e.id = Employee.genID(e)
                                            elif cht1 == '2':
                                                e.name = Employee.getName(e)
                                                print("Name modified Successfully")
                                            elif cht1 == '3' :
                                                e.age = Employee.getAge(e)
                                                print("Age Modified successfully")
                                            
                                            else:
                                                print("Wrong Choice")
                                    elif cht == '4': #by share
                                        myshare = input("Enter the share of the Employee  ")
                                        e = Employee.searchAttribute(share = myshare)
                                        
                                        if e == -1:
                                            pass
                                        else:
                                            cht1  = input(f'''Enter the entity you want to modify-
                                            1- ID
                                            2- Name
                                            3-Age
                                            ''')
                                            if cht1 == '1':
                                                print("New ",end = "")
                                                e.id = Employee.genID(e)
                                            elif cht1 == '2':
                                                e.name = Employee.getName(e)
                                                print("Name modified Successfully")
                                            elif cht1 == '3' :
                                                e.age = Employee.getAge(e)
                                                print("Age Modified successfully")
                                            
                                            else:
                                                print("Wrong Choice")
                                    elif cht == '5': #by area
                                        myarea = input("Enter the area of the Employee  ")
                                        e = Employee.searchAttribute(area = myarea)
                                        
                                        if e == -1:
                                            pass
                                        else:
                                            cht1  = input(f'''Enter the entity you want to modify-
                                            1- ID
                                            2- Name
                                            3-Age
                                            ''')
                                            if cht1 == '1':
                                                print("New ",end = "")
                                                e.id = Employee.genID(e)
                                            elif cht1 == '2':
                                                e.name = Employee.getName(e)
                                                print("Name modified Successfully")
                                            elif cht1 == '3' :
                                                e.age = Employee.getAge(e)
                                                print("Age Modified successfully")
                                            
                                            else:
                                                print("Wrong Choice")
                                    elif cht == '6': #by Course
                                        mycourse = input("Enter the course of the Employee  ")
                                        e = Employee.searchAttribute(course = mycourse)
                                        
                                        if e == -1:
                                            pass
                                        else:
                                            cht1  = input(f'''Enter the entity you want to modify-
                                            1- ID
                                            2- Name
                                            3-Age
                                            ''')
                                            if cht1 == '1':
                                                print("New ",end = "")
                                                e.id = Employee.genID(e)
                                            elif cht1 == '2':
                                                e.name = Employee.getName(e)
                                                print("Name modified Successfully")
                                            elif cht1 == '3' :
                                                e.age = Employee.getAge(e)
                                                print("Age Modified successfully")
                                            
                                            else:
                                                print("Wrong Choice")
                                    else:
                                        print("Wrong Choice")
                                     
                                
                                
                                
                                elif ch == '3': #search
                                    cht = input('''Enter the entity through which you want to search Employee
                                    1- By Id
                                    2- By Name
                                    3- By Age
                                    4- By Share
                                    5- By Area
                                    6- By Course
                                    ''')
                                    if cht == '1':
                                        id = input("Enter the ID of the employee  ")
                                        e = Employee.searchID(id = id)
                                        showData(e)
                                        
                                    elif cht == '2':
                                        name = input("Enter the name of the Employee - ")
                                        e = Employee.searchID(name = name)
                                        showData(e)
                                    elif cht == '3':
                                        age = input("Enter the age of the Employee - ")
                                        e = Employee.searchID(age = age)
                                        showData(e)
                                    elif cht == '4':
                                        myshare = input("Enter the share of the Director")
                                        e = Employee.searchAttribute(share = myshare)
                                        showData(e)
                                    elif cht == '5':
                                        myarea = input("Enter the Area of the Manager")
                                        e = Employee.searchAttribute(area = myarea)
                                        showData(e)
                                    elif cht == '6':
                                        mycourse = input("Enter the course of the Trainer")
                                        e = Employee.searchAttribute(course = mycourse)
                                        showData(e)
                                    else:
                                        print("Wrong Choice")
                                        
                                elif ch == '4': # Delete
                                    cht = input('''Enter the entity through which you want to delete Employee
                                    1- By Id
                                    2- By Name
                                    3- By Age
                                    4- By Share
                                    5- By Area
                                    6- By Course
                                    ''')
                                    if cht == '1':
                                        id = input("Enter the id to delete the Employee- ")
                                        e = Employee.searchID(id = id)
                                        if e== -1:
                                            pass
                                        else:
                                            Employee.del_ID(e)
                                    elif cht == '2':
                                        name = input("Enter the name of the Employee to delete - ")
                                        e = Employee.searchID(name = name)
                                        if e== -1:
                                            pass
                                        else:
                                            Employee.del_ID(e)
                                    elif cht == '3':
                                        age = input("Enter the age to delete the Employee- ")
                                        e = Employee.searchID(age = age)
                                        if e== -1:
                                            pass
                                        else:
                                            Employee.del_ID(e)
                                    elif cht == '4':
                                        myshare = input("Enter the share of the Director to delete- ")
                                        e = Employee.searchAttribute(share = myshare)
                                        if e== -1:
                                            pass
                                        else:
                                            Employee.del_ID(e)
                                    elif cht == '5':
                                        myarea = input("Enter the Area of the Manager to delete- ")
                                        e = Employee.searchAttribute(area = myarea)
                                        if e== -1:
                                            pass
                                        else:
                                            Employee.del_ID(e)
                                    elif cht == '6':
                                        mycourse = input("Enter the course of the Trainer to delete - ")
                                        e = Employee.searchAttribute(course = mycourse)
                                        if e== -1:
                                            pass
                                        else:
                                            Employee.del_ID(e)
                                    else:
                                        print("Wrong Choice")
                                    
                                    
                                elif ch == '5': #display all
                                    if len(Employee.listEmp) == 0 :
                                        print("Add Employees First")
                                    else:
                                        for e in Employee.listEmp:
                                            showData(e)
                                        
                                            
                                elif ch == '6':  #Exit
                                    quit_program = 1
                                    print("Thank You for using my project")
                                    break
                                else:
                                    print("Wrong Choice!!")
                                    
                                    
                                    
                    elif(cms_id == '' or cms_pwd == ''):
                        print("You opted to exit by pressing enter key")
                        break
                    else:
                        print("Wrong ID or Password")
                        Employee.flag = Employee.flag + 1
                else:
                    print('''You exceeded the max limit-
                      Try again later''')
                    break
                if(quit_program >=1):
                    break
                
            break
    except Exception as err:
        print("Error : ",err)
        print("PLease try again")
