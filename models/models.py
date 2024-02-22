# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProyectoJavierEmpresasContratadoras(models.Model):    
    _name = 'proyecto_javier.empresas_contratadoras'
    _description = 'proyecto_javier.empresas_contratadoras'

    name = fields.Char(string="Nombre empresa")
    contact_name = fields.Char(string="Nombre del contacto")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Telefono")
    phone_code = fields.Char(string="Phone code", size=5, default=lambda self: self._get_phone_code() )
    address1 = fields.Char(string="Direccion 1")
    address2 = fields.Char(string="Direccion 2")
    employees_number = fields.Integer(string='Número de empleados')
    business_type = fields.Char(string="Tipo de empresa", compute='_compute_business_type')
    proyect_ids = fields.One2many('project.project', 'empresa_contratadora_id', string="Proyectos")   
    show_business_type = fields.Boolean(default=lambda self: self._get_show_business_type())

    @api.depends('employees_number')
    def _compute_business_type(self):
        for record in self:
            if record.employees_number:
                record.business_type = {
                    record.employees_number <= 10: 'Pequeña',
                    10 < record.employees_number <= 50: 'Mediana',
                    record.employees_number > 50: 'Grande'
                }.get(True, False)
            else:
                record.business_type = False

    def _get_show_business_type(self):
        param = self.env['ir.config_parameter'].sudo().get_param('proyecto_javier.show_business_type')

        return param.lower() == 'true' if param else False
    
    def _get_phone_code(self):
        param = self.env['ir.config_parameter'].sudo().get_param('employee_contract.phone_code')

        return param
    
    @api.model
    def create(self, values):
        res = super(ProyectoJavierEmpresasContratadoras, self).create(values)

        self.env['registro.empresa_contratadora'].create({
            'accion': 'creacion',
            'nombre_usuario': self.env.user.name,
            'nombre_empresa': res.name,
            'fecha_hora_creacion': fields.Datetime.now(),
            'empresa_contratadora_id': res.id,
        })

        return res

    def write(self, values):
        res = super(ProyectoJavierEmpresasContratadoras, self).write(values)

        for record in self:
            self.env['registro.empresa_contratadora'].create({
                'accion': 'modificacion',
                'fecha_hora_accion': fields.Datetime.now(),
                'nombre_usuario': self.env.user.name,
                'nombre_empresa': record.name,
                'empresa_contratadora_id': record.id,
            })

        return res

class ProjectProject(models.Model):
    _inherit = 'project.project'

    empresa_contratadora_id = fields.Many2one('proyecto_javier.empresas_contratadoras', string="Empresa Contratadora")
    tasks_ids = fields.One2many("project.task", "project_id", string="Tareas")

class ProjecTask(models.Model):
    _inherit = 'project.task'

    stage_id = fields.Many2one('project.task.type', string='Etapa')

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    phone_code = fields.Selection(
        [('+32', 'Bélgica'), ('+33', 'Francia'), ('+34', 'España')],
        string="Código telefónico",
        config_parameter='employee_contract.phone_code',
        help="Selecciona el código telefónico del país"
    )

    show_business_type = fields.Boolean(
        'Mostrar tipo de negocio',
        config_parameter='proyecto_javier.show_business_type',
        help="Casilla de verificación para mostrar/ocultar algunos campos en formularios y vistas"
    )
class RegistroEmpresaContratadora(models.Model):
    _name = 'registro.empresa_contratadora'
    _description = 'registro.empresa_contratadora'

    accion = fields.Selection(
        [('creacion', 'Creación'), ('modificacion', 'Modificación')], 
        string='Acción', 
        required=True
    )
    fecha_hora_accion = fields.Datetime(string='Fecha/hora de la acción')
    nombre_usuario = fields.Char(string='Nombre del usuario', required=True)
    nombre_empresa = fields.Char(string='Nombre de la empresa', required=True)
    fecha_hora_creacion = fields.Datetime(string='Fecha/hora de la creación',)
    empresa_contratadora_id = fields.Integer(string='ID Empresa Contratadora')
