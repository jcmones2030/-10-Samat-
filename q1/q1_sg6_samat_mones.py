class Lab:
    def __init__(self, room_number):
        self.room_number = room_number
    
class Technician:
    def __init__(self, assigned_lab):
        self.assigned_lab = assigned_lab    
        assigned_lab = None
        
    def assign_lab(self, Lab_obj):
        self.assigned_lab = Lab_obj
        
chem_lab = Lab("302")
mr_cruz = Technician("Mr. Cruz")
mr_cruz.assign_lab(chem_lab)

print(mr_cruz.assigned_lab.room_number)
