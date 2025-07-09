from django.db import models

class Producto(models.Model):
    id_producto = models.BigAutoField(primary_key=True, db_column='ID_PRODUCTO')
    nombre_producto = models.CharField(max_length=50, db_column='NOMBRE_PRODUCTO', blank=True, null=True)
    descripcion_producto = models.CharField(max_length=100, db_column='DESCRIPCION_PRODUCTO', blank=True, null=True)
    stock = models.FloatField(db_column='STOCK', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PRODUCTO'


    
class Empleado(models.Model):
    id_empleado = models.BigAutoField(primary_key=True, db_column='ID_EMPLEADO')
    nombre_empleado = models.CharField(max_length=50, db_column='NOMBRE_EMPLEADO')
    telefono_empleado = models.BigIntegerField(db_column='TELEFONO_EMPLEADO')
    direccion_empleado = models.CharField(max_length=50, db_column='DIRECCION_EMPLEADO')
    edad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'EMPLEADOS'

    def __str__(self):
        return self.nombre_empleado


class Cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key=True, db_column='ID_CLIENTE')
    nombre_cliente = models.CharField(max_length=40, db_column="NOMBRE_CLIENTE")
    telefono = models.BigIntegerField(db_column='telefono')

    class Meta:
        managed = False
        db_table = 'CLIENTES'

    def __str__(self):
        return self.nombre_cliente


class Proveedor(models.Model):
    id_proveedor = models.BigAutoField(primary_key=True, db_column='ID_PROVEEDOR')
    nombre_proveedor = models.CharField(max_length=50, db_column='NOMBRE_PROVEEDOR')
    telefono = models.BigIntegerField(db_column='TELEFONO')

    class Meta:
        managed = False
        db_table = 'PROVEEDOR'

    def __str__(self):
        return self.nombre_proveedor


class Compra(models.Model):
    id_compra= models.BigAutoField(primary_key=True, db_column='ID_COMPRA')
    descripcion_compra = models.CharField(max_length=50, db_column='DESCRIPCION_COMPRA')
    fecha = models.DateField(db_column='FECHA')
    cantidad_compra = models.IntegerField(db_column='CANTIDAD_COMPRA')

    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, db_column='id_proveedor')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'COMPRAS'

    def __str__(self):
        return f"Compra {self.id} - {self.descripcion_compra}"


class Venta(models.Model):
    id_venta = models.BigAutoField(primary_key=True, db_column='ID_VENAT')
    descripcion_venta = models.CharField(max_length=60,db_column='DESCRIPCION_VENTA')
    fecha = models.DateField(db_column='FECHA')
    cantidad_venta = models.IntegerField(db_column='CANTIDAD_VENTA')

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'VENTAS'

    def __str__(self):
        return f"Venta {self.id} - {self.descripcion_venta}"
