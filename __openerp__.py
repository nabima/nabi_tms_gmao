# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2010-2012 OpenERP s.a. (<http://openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'TMS GMAO',
    'sequence': 300,
    'version': '3.0.1',
    'category': 'Vertical functionality',
    'description': """
Maintenance for Transport Management System (TMS):
==================================================
    - Corrective maintenance
    - Sheets controls
    - Drain management
    - Parts Allocation
    - Assembly / disassembly tire
    - Technical visits
    - General Controls
    
Maintenance for Transport Management System (TMS):
==================================================
    - Maintenances correctives
    - Fiches de contrôles
    - Gestion de vidange
    - Affectation pièces détachées
    - Montage/démontage pneu
    - Visites techniques
    - Contrôles généraux
    - Alertes programmées
info@nextma.com
""",
    'author': 'NEXTMA',
    'maintainer': 'NEXTMA',
    'website': 'http://www.nextma.com',
    'icon': '/tms_gmao/static/src/img/icon.png',
    'depends': ["tms","mro"],
    'data': [
        'security/gmao_security.xml',
        'data/tms_gmao_data.xml',
        'tms_gmao_sequence.xml',
        'res_config_view.xml',
        'wizard/tms_gmao_pm_alert_process_view.xml',
        #'mro_workflow.xml',
        'fleet_view.xml',
        'mro_view.xml',
        'product_view.xml',
        'tms_gmao_view.xml',
        'tms_gmao_menu.xml',
        'security/ir.model.access.csv',
        'tms_gmao_report.xml'
    ],
    'demo': [
    ],
    'test': [
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'css': [
        #'static/src/css/modules.css'
    ],
    'js': [
        #'static/src/js/apps.js',
    ],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
