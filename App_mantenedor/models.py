from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    id_cli = models.IntegerField(primary_key=True)
    nom_cli = models.CharField(max_length=45)
    ap_cli = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.IntegerField()
    email = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    comuna_id_com = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='Comuna_id_com')  # Field name made lowercase.
    genero_id_gen = models.ForeignKey('Genero', models.DO_NOTHING, db_column='Genero_id_Gen')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class Comuna(models.Model):
    id_com = models.AutoField(primary_key=True)
    nom_com = models.CharField(max_length=45)

    def __str__(self):
        return self.nom_com
    class Meta:
        managed = False
        db_table = 'comuna'



class Empleado(models.Model):
    id_emp = models.IntegerField(primary_key=True)
    nom_emp = models.CharField(max_length=45)
    ap_emp = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.IntegerField()
    email = models.CharField(max_length=45)
    sueldo = models.IntegerField()
    genero_id_gen = models.ForeignKey('Genero', models.DO_NOTHING, db_column='Genero_id_Gen')  # Field name made lowercase.
    comuna_id_com = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='Comuna_id_com')  # Field name made lowercase.
    tipo_empleado_idtip_emp = models.ForeignKey('TipoEmpleado', models.DO_NOTHING, db_column='Tipo_Empleado_idTip_Emp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleado'


class EmpleadoEspecialidad(models.Model):
    empleado_id_emp = models.OneToOneField(Empleado, models.DO_NOTHING, db_column='Empleado_id_emp', primary_key=True)  # Field name made lowercase.
    especialidad_id_esp = models.ForeignKey('Especialidad', models.DO_NOTHING, db_column='Especialidad_id_Esp')  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_especialidad'
        unique_together = (('empleado_id_emp', 'especialidad_id_esp'),)


class Especialidad(models.Model):
    id_esp = models.AutoField(db_column='id_Esp', primary_key=True)  # Field name made lowercase.
    nom_espe = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'especialidad'


class Especie(models.Model):
    id_esp = models.AutoField(db_column='id_Esp', primary_key=True)  # Field name made lowercase.
    nom_esp = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'especie'


class Genero(models.Model):
    id_gen = models.AutoField(db_column='id_Gen', primary_key=True)  # Field name made lowercase.
    nom_gen = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'genero'


class Insumo(models.Model):
    id_insumo = models.AutoField(db_column='id_Insumo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    inventario = models.IntegerField()
    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False
        db_table = 'insumo'


class Paciente(models.Model):
    id_pac = models.AutoField(db_column='id_Pac', primary_key=True)  # Field name made lowercase.
    nom_pac = models.CharField(max_length=45)
    fec_nac = models.DateField(blank=True, null=True)
    raza = models.CharField(max_length=45)
    color = models.CharField(max_length=45)
    cliente_id_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_id_cli')  # Field name made lowercase.
    especie_id_esp = models.ForeignKey(Especie, models.DO_NOTHING, db_column='Especie_id_Esp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paciente'


class Pago(models.Model):
    idpago = models.AutoField(db_column='idPago', primary_key=True)  # Field name made lowercase.
    fec_pago = models.DateTimeField()
    detalle = models.CharField(max_length=45)
    total = models.IntegerField()
    tip_pago_id_tip_pago = models.ForeignKey('TipPago', models.DO_NOTHING, db_column='tip_pago_id_tip_pago')
    reserva_id_res = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='Reserva_id_Res')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pago'


class ProcedPacien(models.Model):
    idpro_pac = models.AutoField(db_column='idPro_Pac', primary_key=True)  # Field name made lowercase.
    paciente_id_pac = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='Paciente_id_Pac')  # Field name made lowercase.
    procedimiento_id_proc = models.ForeignKey('Procedimiento', models.DO_NOTHING, db_column='Procedimiento_id_Proc')  # Field name made lowercase.
    empleado_id_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='Empleado_id_emp')  # Field name made lowercase.
    descripcion = models.CharField(max_length=45)
    indicacion = models.CharField(max_length=45)
    fec_pro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'proced_pacien'


class Procedimiento(models.Model):
    id_proc = models.AutoField(db_column='id_Proc', primary_key=True)  # Field name made lowercase.
    nom_pro = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'procedimiento'


class Reserva(models.Model):
    id_res = models.AutoField(db_column='id_Res', primary_key=True)  # Field name made lowercase.
    fec_res = models.DateField()
    hora_res = models.TimeField()
    detalle = models.CharField(max_length=45)
    fec_creacion = models.DateTimeField()
    precio = models.IntegerField()
    empleado_id_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='Empleado_id_emp')  # Field name made lowercase.
    cliente_id_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_id_cli')  # Field name made lowercase.
    especialidad_id_esp = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='Especialidad_id_Esp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reserva'


class SolicitudInsumo(models.Model):
    id_sol_ins = models.AutoField(primary_key=True)
    empleado_id_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='Empleado_id_emp')  # Field name made lowercase.
    insumo_id_insumo = models.ForeignKey(Insumo, models.DO_NOTHING, db_column='Insumo_id_Insumo')  # Field name made lowercase.
    detalle = models.CharField(max_length=45)
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'solicitud_insumo'


class TipPago(models.Model):
    id_tip_pago = models.AutoField(primary_key=True)
    nom_tp_pago = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tip_pago'


class TipoEmpleado(models.Model):
    idtip_emp = models.AutoField(db_column='idTip_Emp', primary_key=True)  # Field name made lowercase.
    nom_tp_em = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_empleado'