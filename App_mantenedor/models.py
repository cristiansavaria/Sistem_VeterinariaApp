
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppClienteContacto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=254)
    tipo_consulta = models.IntegerField()
    mensaje = models.TextField()

    class Meta:
        managed = False
        db_table = 'app_cliente_contacto'



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cliente(models.Model):
    id_rut = models.CharField(primary_key=True, max_length=10)
    nom_cli = models.CharField(max_length=45)
    ap_cli = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.IntegerField()
    email = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    comuna_id_com = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='Comuna_id_com')  # Field name made lowercase.
    genero_id_gen = models.ForeignKey('Genero', models.DO_NOTHING, db_column='Genero_id_Gen')  # Field name made lowercase.
    activo = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.id_rut
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    id_emp = models.CharField(primary_key=True, max_length=10)
    nom_emp = models.CharField(max_length=45)
    ap_emp = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.IntegerField()
    email = models.CharField(max_length=45)
    sueldo = models.IntegerField()
    genero_id_gen = models.ForeignKey('Genero', models.DO_NOTHING, db_column='Genero_id_Gen')  # Field name made lowercase.
    comuna_id_com = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='Comuna_id_com')  # Field name made lowercase.
    tipo_empleado_idtip_emp = models.ForeignKey('TipoEmpleado', models.DO_NOTHING, db_column='tipo_empleado_idTip_Emp')  # Field name made lowercase.
    activo = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.nom_emp
    class Meta:
        managed = False
        db_table = 'empleado'


class Especie(models.Model):
    id_esp = models.AutoField(db_column='id_Esp', primary_key=True)  # Field name made lowercase.
    nom_esp = models.CharField(max_length=45)
    def __str__(self):
        return self.nom_esp
    class Meta:
        managed = False
        db_table = 'especie'


class Genero(models.Model):
    id_gen = models.AutoField(db_column='id_Gen', primary_key=True)  # Field name made lowercase.
    nom_gen = models.CharField(max_length=45)
    def __str__(self):
        return self.nom_gen
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
    especie_id_esp = models.ForeignKey(Especie, models.DO_NOTHING, db_column='Especie_id_Esp')  # Field name made lowercase.
    cliente_id_rut = models.ForeignKey(Cliente, on_delete= models.CASCADE, db_column='cliente_id_rut')
    activo = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.nom_pac
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
    def __str__(self):
        return self.tip_pago_id_tip_pago
    class Meta:
        managed = False
        db_table = 'pago'


class ProcedPacien(models.Model):
    idpro_pac = models.AutoField(db_column='idPro_Pac', primary_key=True)  # Field name made lowercase.
    paciente_id_pac = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='Paciente_id_Pac')  # Field name made lowercase.
    procedimiento_id_proc = models.ForeignKey('Procedimiento', models.DO_NOTHING, db_column='Procedimiento_id_Proc')  # Field name made lowercase.
    descripcion = models.CharField(max_length=45)
    indicacion = models.CharField(max_length=45)
    fec_pro = models.DateTimeField()
    empleado_id_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_emp', blank=True, null=True)
    def __str__(self):
        return self.descripcion
    class Meta:
        managed = False
        db_table = 'proced_pacien'


class Procedimiento(models.Model):
    id_proc = models.AutoField(db_column='id_Proc', primary_key=True)  # Field name made lowercase.
    nom_pro = models.CharField(max_length=45)
    def __str__(self):
        return self.nom_pro
    class Meta:
        managed = False
        db_table = 'procedimiento'


class Reserva(models.Model):
    id_res = models.AutoField(db_column='id_Res', primary_key=True)  # Field name made lowercase.
    fec_res = models.DateField()
    hora_res = models.TimeField()
    detalle = models.CharField(max_length=45)
    fec_creacion = models.DateTimeField()
    precio = models.IntegerField(blank=True, null=True)
    servicio_id_ser = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='servicio_id_ser')
    cliente_id_rut = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_rut', blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)
    empleado_id_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_emp', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserva'


class Servicio(models.Model):
    id_ser = models.AutoField(primary_key=True)
    nom_serv = models.CharField(max_length=45)
    precio = models.IntegerField(blank=True, null=True)
    detalle = models.CharField(max_length=300, blank=True, null=True)
    def __str__(self):
        return self.nom_serv
    class Meta:
        managed = False
        db_table = 'servicio'


class ServicioEmpleado(models.Model):
    idser_emp = models.AutoField(primary_key=True)
    servicio_id_ser = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='servicio_id_ser')
    detalle_ser = models.CharField(max_length=300, blank=True, null=True)
    empleado_id_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_emp')

    class Meta:
        managed = False
        db_table = 'servicio_empleado'


class SolicitudInsumo(models.Model):
    id_sol_ins = models.AutoField(primary_key=True)
    detalle = models.CharField(max_length=45)
    cantidad = models.IntegerField()
    fec_solici = models.DateTimeField()
    insumo_id_insumo = models.ForeignKey(Insumo, models.DO_NOTHING, db_column='Insumo_id_Insumo')  # Field name made lowercase.
    empleado_id_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_emp')

    class Meta:
        managed = False
        db_table = 'solicitud_insumo'


class TipPago(models.Model):
    id_tip_pago = models.AutoField(primary_key=True)
    nom_tp_pago = models.CharField(max_length=45)
    def __str__(self):
        return self.nom_tp_pago
    class Meta:
        managed = False
        db_table = 'tip_pago'


class TipoEmpleado(models.Model):
    idtip_emp = models.AutoField(db_column='idTip_Emp', primary_key=True)  # Field name made lowercase.
    nom_tp_em = models.CharField(max_length=45)
    def __str__(self):
        return self.nom_tp_em
    class Meta:
        managed = False
        db_table = 'tipo_empleado'


















