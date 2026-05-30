import json as j
def respond(msg, data):
    msg= msg.lower().strip()
    students= data['students']
    tname= data['teacher_name']
    cname=data['class_name']
    total= len(students)
    print(msg)
    
    #basic stuff.
    if 'teacher' in msg:
        return f"its {tname}, Your Teacher"
    if 'how many students' in msg or 'total' in msg or 'strength' in msg or 'amount' in msg:
        return f"there are {total} students in {cname}"
    if 'class name' in msg or 'which class' in msg or 'class' in msg or 'standard' in msg or 'grade' in msg:
            return f"you are in {cname} student "

    
# i am thinkin of having a sync of my webclass track app
   
    if 'roll' in msg:
        for word in msg.split():
            if word.isdigit():
                rno  =int(word)
                for s in students:
                    if s['roll_no']==rno:
                        return f"roll {rno} is {s['name']}"
                return f"no one has roll {rno} pls.chec"

        return "give me another r.no fast"
        #gender
    if 'girls' in msg or 'female' in msg:
        cnt= len([s for s in students if s['gender'].lower()== 'female'])
        return f"{cnt} girls"
    if 'boys' in msg or 'male' in msg:
        cnt= len([s for s in students if s['gender'].lower()== 'male'])
        return f"{cnt} boys in class"

    #list(doing these comments so i dont lose track as i losed when i was in my previous project costing me hours so nvm
    if 'list' in msg or 'all' in msg or 'everyone' in msg:
        if total==0:
            return "no students added"
        names =  []
        for s in students:
            names.append(f"roll  {s['roll_no']} -{s['name']}")
        
        return "\n".join(names)

    #looping searches
    for s in students:
        if s['name'].lower() in msg:
            
            
            return f"{s['name']} - roll {s['roll_no']} - {s['gender']}"
    return "didn't get that, try -teacher /roll  5 / list / how many boy/girls"
            




        






