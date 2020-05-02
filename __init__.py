#tarea de Rolando Mamani Rocha
class Automovil:
    encendido_motor=False
    def __init__(self,marca, nro_serie, modelo,tipo, placa):
        self.marca=marca
        self.nro_serie=nro_serie
        self.modelo=modelo
        self.tipo=tipo
        self.placa=placa

    def getMarca(self):
        result = self.marca
        print("Marca: {}".format(result))
        return result

    def getNro_serie(self):
        result=self.nro_serie
        print("Nro de serie: {}".format(str(result)))
        return result

    def getModelo(self):
        result=self.modelo
        return "Modelo: {}".format(result)

    def getTipo(self):
        result=self.tipo
        print("Tipo: {}".format(str(result)))
        return result

    def getPlaca(self):
        result=self.placa
        print("Placa: {}".format(result))
        return result

    def car_data(self):
        result= self.getMarca() + str(self.getNro_serie()) + str(self.getModelo()) + self.getTipo() + self.getPlaca()
        return result

    def setPlaca(self,placa):
        self.placa=placa

    def encender_motor(self):
        encendido_motor=True
        print("Motor encendido")

    def apagar_motor(self):
        encendido_motor=False
        print("Motor Apagado")

my_auto=Automovil("Foton",98787, 2010,"taxi","123zxc")
my_auto.car_data()
print("--------------------------------------------")
my_auto.setPlaca("986klo")
my_auto.car_data()
my_auto.encender_motor()
my_auto.apagar_motor()

##########################################################################

class Student:
    def __init__(self, name, lastname, student_id, personal_id, average, enrollment_status=False):
        self.name=name
        self.lastname=lastname
        self.student_id=student_id
        self.personal_id=personal_id
        self.average=average
        self.enrollment_status=enrollment_status

    def __str__(self):
        return "nombre: {}\n" \
               "apellido: {}\n" \
               "Id de estudiante: {}\n" \
               "Nro de identidad: {}\n" \
               "promedio: {}\n" \
               "Estado de Inscripcion: {}".format(self.name,self.lastname,self.student_id,self.personal_id,self.average,self.enrollment_status)

    def setAverage(self,average):
        self.average=average

    def setEnrollment_status(self,status):
        self.enrollment_status=status

    def getAverage(self):
        return self.average

    def type_of_student(self):
        result=self.average
        if(result <= 100 and result >= 91):
            print("Estudiante Excelente")
        elif(result <= 90 and result >= 81):
            print("Estudiante Muy Bueno")
        elif(result <= 80 and result >= 51):
            print("Estudiante Satisfactorio")
        elif(result <= 50 and result >= 00):
            print("Estudiante Necesita apoyo")


"""
Calificación	Notas
100 -91	Excelente
90 - 81	Muy Bueno
80 - 51	Satisfactorio
50 - 00	Necesita apoyo
"""

student1=Student("Juan","Perez", 12345678, 876509, 45,enrollment_status=True)
print(student1)
student1.type_of_student()
print("--------------------------------------------")
student1.setAverage(70.9)
student1.setEnrollment_status(False)
print(student1)
student1.type_of_student()